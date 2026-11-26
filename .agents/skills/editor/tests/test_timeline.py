#!/usr/bin/env python3
"""Executable metadata probes; no viewing, rendering or creative scoring."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_timeline import validate, mapped_position, rational  # noqa: E402


def fixture():
    return json.loads((ROOT / 'examples/silent-30s.timeline.json').read_text())


def one_clip(source_rate=25, source_count=100, record_count=96, speed=(1, 1), kind='video'):
    p = fixture()
    p['events'] = p['events'][:1]
    p['shots'] = p['shots'][:1]
    p['assets'] = p['assets'][:1]
    p['order_constraints'] = []
    p['sequence']['duration_frames'] = record_count
    a, e = p['assets'][0], p['events'][0]
    a['kind'] = p['tracks'][0]['kind'] = kind
    a['rate'] = {'num': source_rate, 'den': 1}
    a['available']['out'] = e['source']['out'] = source_count
    e['record']['out'] = record_count
    e['speed'] = {'num': speed[0], 'den': speed[1]}
    return p


class TimelineTests(unittest.TestCase):
    def test_estimated_paper_edit(self):
        result = validate(fixture())
        self.assertEqual((result['events'], result['duration_frames'], result['duration_seconds']),
                         (6, 720, '30'))

    def test_mixed_rate_and_reinterpretation(self):
        self.assertEqual(validate(one_clip())['duration_frames'], 96)
        self.assertEqual(validate(one_clip(record_count=100, speed=(24, 25)))['duration_frames'], 100)
        p = one_clip(source_rate=24, source_count=240, record_count=240)
        p['sequence']['rate'] = p['assets'][0]['rate'] = {'num': 24000, 'den': 1001}
        p['sequence']['timebase'] = {'num': 1001, 'den': 24000}
        self.assertEqual(validate(p)['duration_seconds'], '1001/100')

    def test_audio_sample_domain_and_sync(self):
        p = one_clip(source_rate=48000, source_count=192000, record_count=96, kind='audio')
        p['sync_anchors'] = [{'event_id': p['events'][0]['id'], 'source_position': 48000,
                              'record_position': 24, 'tolerance_frames': 0}]
        validate(p)
        self.assertEqual(mapped_position(p['events'][0], p['assets'][0],
                                        rational(p['sequence']['rate']), 48000), 24)
        p['sync_anchors'][0]['record_position'] = 25
        with self.assertRaisesRegex(ValueError, 'sync anchor mapping'):
            validate(p)

    def test_dissolve_handles_and_duration(self):
        p = fixture()
        first, second = p['events'][:2]
        for i in (0, 1):
            e, a = p['events'][i], p['assets'][i]
            e['source'] = {'in': 12, 'out': a['available']['out'] + 12}
            a['available']['out'] += 24
            e['handles'] = {'pre': 12, 'post': 12}
        second['transition'] = {'type': 'dissolve', 'before': 6, 'after': 6}
        self.assertEqual(validate(p)['duration_frames'], 720)
        first['handles']['post'] = 5
        with self.assertRaisesRegex(ValueError, 'transition handles'):
            validate(p)

    def test_explicit_gap_not_invented_media(self):
        p = one_clip()
        e = p['events'][0]
        e['kind'], e['asset_id'] = 'gap', None
        e['purpose'] = 'Labeled missing-footage slate in review assembly'
        self.assertEqual(validate(p)['duration_frames'], 96)

    def test_invalid_variants(self):
        # Each mutation targets a materially different handoff failure.
        variants = {
            'duplicate-event': lambda p: p['events'].append(copy.deepcopy(p['events'][0])),
            'duplicate-asset-version': lambda p: p['assets'].append(copy.deepcopy(p['assets'][0])),
            'unknown-asset-version': lambda p: p['events'][0].update(asset_version='missing'),
            'wrong-scene': lambda p: p['events'][0].update(scene_id='S999'),
            'wrong-beat-type': lambda p: p['events'][0].update(script_beat_ids=['NB01']),
            'wrong-shot-asset': lambda p: p['events'][0].update(asset_id=p['assets'][1]['id']),
            'zero-rate': lambda p: p['sequence']['rate'].update(num=0),
            'boolean-rate': lambda p: p['sequence']['rate'].update(num=True),
            'bad-timebase': lambda p: p['sequence']['timebase'].update(den=25),
            'unsupported-origin': lambda p: p['sequence'].update(record_origin=100),
            'invalid-DF-family': lambda p: p['sequence'].update(timecode_mode='DF'),
            'negative-source': lambda p: p['events'][0]['source'].update(**{'in': -1}),
            'reversed-range': lambda p: p['events'][0]['source'].update(out=0),
            'off-by-one-duration': lambda p: p['events'][0]['source'].update(out=121),
            'beyond-source': lambda p: p['assets'][0]['available'].update(out=119),
            'noninteger-frame': lambda p: p['events'][0]['record'].update(out=120.0),
            'unrepresented-rounding': lambda p: p['assets'][0]['rate'].update(num=25),
            'zero-speed': lambda p: p['events'][0]['speed'].update(num=0),
            'nonlinear-speed': lambda p: p['events'][0].update(mapping='optical-flow-ramp'),
            'VFR-without-map': lambda p: p['assets'][0].update(timing_mode='VFR'),
            'unknown-transition': lambda p: p['events'][0].update(transition={'type': 'wipe'}),
            'unsupported-effect': lambda p: p['events'][0].update(effects=['stabilize']),
            'false-observed-event': lambda p: p['events'][0].update(timing_basis='observed'),
            'false-observed-media': lambda p: p['assets'][0]['available'].update(basis='observed'),
            'false-handle': lambda p: p['events'][0]['handles'].update(pre=12),
            'unknown-handle-room': lambda p: (p['assets'][0].update(available=None),
                                               p['events'][0]['handles'].update(post=1)),
            'unlocated-render': lambda p: p['output'].update(state='rendered'),
            'unapproved-lock': lambda p: p['sequence'].update(lock_state='picture-locked'),
            'unknown-dependency': lambda p: p['events'][0].update(dependencies=['missing']),
            'dependency-cycle': lambda p: p['events'][0].update(dependencies=['ED-E006']),
            'wrong-constraint-namespace': lambda p: p['order_constraints'][0].update(namespace='shot'),
            'unknown-required-beat': lambda p: p['order_constraints'][0].update(before='SB99'),
            'sequence-truncated': lambda p: p['sequence'].update(duration_frames=719),
            'sequence-uncovered': lambda p: p['sequence'].update(duration_frames=721),
        }
        for label, mutate in variants.items():
            with self.subTest(label=label):
                p = fixture()
                mutate(p)
                with self.assertRaises((ValueError, KeyError)):
                    validate(p)

    def test_protected_disclosure_order(self):
        p = fixture()
        p['events'].reverse()
        cursor = 0
        for e in p['events']:
            count = e['record']['out'] - e['record']['in']
            e['record'] = {'in': cursor, 'out': cursor + count}
            cursor += count
        with self.assertRaisesRegex(ValueError, 'beat order'):
            validate(p)

    def test_claim_records_require_scoped_evidence(self):
        p = fixture()
        p['output'].update(state='verified', locator='claimed.mp4', sha256='claimed', render_log='claimed')
        with self.assertRaisesRegex(ValueError, 'scoped check'):
            validate(p)
        p['sequence'].update(lock_state='picture-locked',
            approval={'who': 'user', 'source': 'supplied note', 'scope': 'picture', 'version': 'old'})
        with self.assertRaisesRegex(ValueError, 'another cut'):
            validate(p)

    def test_accepted_output_requires_scoped_approval(self):
        p = fixture()
        approval = {'who': 'user', 'source': 'supplied acceptance note',
                    'date': '2026-11-26', 'version': p['version'], 'scope': 'technical delivery'}
        p['output'].update(
            state='accepted', locator='claimed.mp4', sha256='claimed', render_log='claimed',
            checks=[{'method': 'declared', 'range': 'all', 'result': 'pass', 'evidence': 'claimed'}],
            approval=approval,
        )
        self.assertEqual(validate(p)['duration_frames'], 720)
        for value in (True, False, 'approved', 1, None, [], {}):
            with self.subTest(approval=value):
                p['output']['approval'] = value
                with self.assertRaisesRegex(ValueError, 'acceptance lacks'):
                    validate(p)
        for key in approval:
            missing = approval.copy()
            del missing[key]
            for value in (missing, {**approval, key: ''}, {**approval, key: ' '},
                          {**approval, key: None}, {**approval, key: True},
                          {**approval, key: ['claimed']}):
                with self.subTest(field=key, approval=value):
                    p['output']['approval'] = value
                    with self.assertRaisesRegex(ValueError, 'acceptance lacks'):
                        validate(p)
        p['output']['approval'] = {**approval, 'version': 'old'}
        with self.assertRaisesRegex(ValueError, 'acceptance approval is for another cut'):
            validate(p)


def check_source(path):
    raw = path.read_bytes()
    source, packet = json.loads(raw), fixture()
    if hashlib.sha256(raw).hexdigest() != packet['upstream'][0]['sha256']:
        raise ValueError('authoring source changed; re-map rather than claim compatibility')
    assert packet['locked_facts'] == source['locked_facts']
    assert [e['shot_id'] for e in packet['events']] == source['proposed_sequence']
    assert packet['scenes'][0]['id'] == source['scene']['id']
    for event in packet['events']:
        shot = next(s for s in source['shots'] if s['id'] == event['shot_id'])
        assert event['record']['out']-event['record']['in'] == shot['duration_seconds']*24
        for key in ('narrative_beat_ids', 'script_beat_ids', 'scene_id'):
            assert event[key] == shot[key]
    print('Exact-source mapping checked:', packet['upstream'][0]['sha256'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path)
    args = parser.parse_args()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(TimelineTests))
    if args.source:
        check_source(args.source)
    raise SystemExit(not result.wasSuccessful())
