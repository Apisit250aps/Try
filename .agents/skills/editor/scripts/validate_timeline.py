#!/usr/bin/env python3
"""Validate the documented editor-timeline/0.1 linear subset; never reads media."""
import argparse
import json
from fractions import Fraction
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, label, minimum=0):
    require(type(value) is int and value >= minimum, f"{label}: invalid integer")
    return value


def rational(value):
    return Fraction(integer(value['num'], 'numerator', 1),
                    integer(value['den'], 'denominator', 1))


def interval(value):
    start = integer(value['in'], 'range in')
    end = integer(value['out'], 'range out')
    require(end > start, 'empty or reversed range')
    return start, end


def index(items, key):
    result = {}
    for item in items:
        item_key = key(item)
        require(item_key not in result, f'duplicate identity: {item_key}')
        result[item_key] = item
    return result


def mapped_position(event, asset, record_rate, source_position):
    return (Fraction(event['record']['in']) +
            Fraction(source_position - event['source']['in']) /
            rational(asset['rate']) / rational(event['speed']) * record_rate)


def validate(packet):
    require(packet['contract'] == 'editor-timeline/0.1', 'unsupported contract')
    seq = packet['sequence']
    rate = rational(seq['rate'])
    require(rate * rational(seq['timebase']) == 1, 'timebase is not reciprocal fps')
    duration = integer(seq['duration_frames'], 'sequence duration', 1)
    require(type(seq['record_origin']) is int and seq['record_origin'] == 0,
            'linear subset requires record origin zero')
    require(seq['timecode_mode'] in ('NDF', 'DF', 'unknown'), 'invalid counting mode')
    if seq['timecode_mode'] == 'DF':
        require(rate in (Fraction(30000, 1001), Fraction(60000, 1001)),
                'DF unsupported at this rate')
    require(seq['lock_state'] in ('unlocked', 'picture-locked'), 'invalid lock state')
    if seq['lock_state'] == 'picture-locked':
        approval = seq['approval']
        require(approval and all(approval.get(k) for k in ('source', 'scope', 'who', 'version')),
                'picture lock lacks authority record')
        require(approval['version'] == packet['version'], 'lock approval is for another cut')

    beats = packet['beats']
    for kind in ('narrative', 'script'):
        require(len(beats[kind]) == len(set(beats[kind])), 'duplicate typed beat')
    scenes = index(packet['scenes'], lambda x: x['id'])
    shots = index(packet['shots'], lambda x: x['id'])
    assets = index(packet['assets'], lambda x: (x['id'], x['version']))
    tracks = index(packet['tracks'], lambda x: x['id'])
    events = index(packet['events'], lambda x: x['id'])
    require(events and tracks, 'empty timeline')
    for scene in scenes.values():
        for kind in ('narrative', 'script'):
            require(set(scene[kind + '_beat_ids']) <= set(beats[kind]), 'dangling scene beat')
    for shot in shots.values():
        scene = scenes[shot['scene_id']]
        for kind in ('narrative', 'script'):
            require(set(shot[kind + '_beat_ids']) <= set(scene[kind + '_beat_ids']),
                    'shot beat not in scene namespace')
    for asset in assets.values():
        require(asset['shot_id'] in shots, 'dangling asset shot')
        rational(asset['rate'])
        require(asset['timing_mode'] == 'CFR', 'unsupported VFR/unknown timing mapping')
        available = asset['available']
        if available is not None:
            interval(available)
            require(available['basis'] in ('estimated', 'observed'), 'invalid availability basis')
            if available['basis'] == 'observed':
                require(available.get('evidence'), 'observed availability needs evidence locator')

    for event in events.values():
        track = tracks[event['track_id']]
        require(track['kind'] in ('video', 'audio'), 'unsupported caption/other track')
        start, end = interval(event['record'])
        require(end <= duration, 'event exceeds sequence')
        require(event['purpose'].strip(), 'event needs narrative purpose')
        require(event['lock_state'] in ('unlocked', 'locked'), 'invalid event lock')
        require(set(event['dependencies']) <= events.keys(), 'dangling event dependency')
        require(event['id'] not in event['dependencies'], 'self dependency')
        require(not event.get('effects'), 'effects unsupported by linear validator')
        if event['kind'] == 'gap':
            require(track['kind'] == 'video' and event.get('asset_id') is None,
                    'invalid video gap')
            continue
        require(event['kind'] == 'clip', 'unsupported event kind')
        shot = shots[event['shot_id']]
        require(event['scene_id'] == shot['scene_id'], 'event/shot scene mismatch')
        for kind in ('narrative', 'script'):
            require(event[kind + '_beat_ids'] and
                    set(event[kind + '_beat_ids']) <= set(shot[kind + '_beat_ids']),
                    'event/shot typed beat mismatch')
        asset = assets[(event['asset_id'], event['asset_version'])]
        require(asset['shot_id'] == event['shot_id'], 'asset/shot mismatch')
        require(asset['kind'] == track['kind'], 'asset/track kind mismatch')
        source_in, source_out = interval(event['source'])
        speed = rational(event['speed'])
        require(event['mapping'] == 'linear', 'unsupported speed mapping')
        require(Fraction(source_out-source_in) / rational(asset['rate']) / speed ==
                Fraction(end-start) / rate, 'source/record duration mismatch')
        require(event['timing_basis'] in ('estimated', 'observed'), 'invalid event timing basis')
        available = asset['available']
        if event['timing_basis'] == 'observed':
            require(available and available['basis'] == 'observed',
                    'observed event needs observed source availability')
        if available:
            lo, hi = interval(available)
            require(lo <= source_in < source_out <= hi, 'source range outside availability')
        for side, room in (('pre', source_in - available['in'] if available else None),
                           ('post', available['out'] - source_out if available else None)):
            handle = event['handles'][side]
            if handle is not None:
                integer(handle, 'handle')
                require(room is not None and handle <= room, 'handle exceeds known media')

    # Reject cycles while allowing forward references used for nonchronological dependencies.
    visited, active = set(), set()
    def visit(event_id):
        require(event_id not in active, 'cyclic event dependency')
        if event_id in visited:
            return
        active.add(event_id)
        for dep in events[event_id]['dependencies']:
            visit(dep)
        active.remove(event_id)
        visited.add(event_id)
    for event_id in events:
        visit(event_id)

    for track in tracks.values():
        require(track['kind'] in ('video', 'audio'), 'unsupported track')
        ordered = sorted((e for e in events.values() if e['track_id'] == track['id']),
                         key=lambda e: e['record']['in'])
        cursor, previous = 0, None
        for event in ordered:
            start, end = interval(event['record'])
            require(start >= cursor, 'same-track nominal overlap')
            if track['kind'] == 'video':
                require(start == cursor, 'video gap must be explicit')
            trans = event['transition']
            require(trans['type'] in ('cut', 'dissolve'), 'unsupported transition')
            if trans['type'] == 'dissolve':
                require(track['kind'] == 'video' and previous and
                        event['kind'] == previous['kind'] == 'clip', 'invalid dissolve pair')
                before = integer(trans['before'], 'transition before')
                after = integer(trans['after'], 'transition after')
                require(before + after > 0 and before <= previous['record']['out']-previous['record']['in']
                        and after <= end-start, 'invalid transition offsets')
                for clip, side, need in ((event, 'pre', before), (previous, 'post', after)):
                    asset = assets[(clip['asset_id'], clip['asset_version'])]
                    handle = clip['handles'][side]
                    required = Fraction(need) / rate * rational(asset['rate']) * rational(clip['speed'])
                    require(handle is not None and handle >= required,
                            'insufficient transition handles')
                previous_incoming = previous['transition']
                used = previous_incoming.get('after', 0) if previous_incoming['type'] == 'dissolve' else 0
                require(used + before <= previous['record']['out']-previous['record']['in'],
                        'transitions overlap within clip')
            cursor, previous = end, event
        if track['kind'] == 'video':
            require(cursor == duration, 'video track does not cover sequence')

    for constraint in packet['order_constraints']:
        kind = constraint['namespace']
        require(kind in ('narrative', 'script'), 'unknown beat namespace')
        starts = []
        for beat in (constraint['before'], constraint['after']):
            require(beat in beats[kind], 'order constraint has unknown beat')
            matches = [e['record']['in'] for e in events.values()
                       if beat in e.get(kind + '_beat_ids', [])]
            require(matches, 'required beat absent from timeline')
            starts.append(min(matches))
        require(starts[0] < starts[1], 'protected beat order violated')
    for anchor in packet['sync_anchors']:
        event = events[anchor['event_id']]
        asset = assets[(event['asset_id'], event['asset_version'])]
        source = integer(anchor['source_position'], 'sync source')
        record = integer(anchor['record_position'], 'sync record')
        tolerance = integer(anchor['tolerance_frames'], 'sync tolerance')
        require(event['source']['in'] <= source < event['source']['out'] and
                event['record']['in'] <= record < event['record']['out'], 'sync anchor outside event')
        require(abs(mapped_position(event, asset, rate, source) - record) <= tolerance,
                'sync anchor mapping mismatch')
    output = packet['output']
    require(output['state'] in ('planned', 'rendered', 'verified', 'accepted'), 'invalid output state')
    if output['state'] != 'planned':
        require(all(output.get(k) for k in ('locator', 'sha256', 'render_log')),
                'render claim lacks artifact evidence')
    if output['state'] in ('verified', 'accepted'):
        require(output['checks'] and all(all(c.get(k) for k in ('method', 'range', 'result', 'evidence'))
                for c in output['checks']), 'verification claim lacks scoped check evidence')
    if output['state'] == 'accepted':
        approval = output.get('approval')
        require(isinstance(approval, dict) and
                all(isinstance(approval.get(k), str) and approval[k].strip()
                    for k in ('who', 'source', 'date', 'version', 'scope')),
                'acceptance lacks scoped approval record')
        require(approval['version'] == packet['version'],
                'acceptance approval is for another cut')
    return {'events': len(events), 'assets': len(assets), 'duration_frames': duration,
            'duration_seconds': str(Fraction(duration) / rate), 'scope': 'linear metadata only'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('timeline', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(validate(json.loads(args.timeline.read_text())), indent=2))
    except (ValueError, KeyError, TypeError, AttributeError, OSError, RecursionError) as exc:
        parser.exit(1, f'Invalid/unsupported timeline: {exc}\n')


if __name__ == '__main__':
    main()
