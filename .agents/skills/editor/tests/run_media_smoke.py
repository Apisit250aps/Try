#!/usr/bin/env python3
"""Optional synthetic timing/OTIO probes; requires explicitly installed test tools.

Produces timing diagrams, not a dramatic film or a general timeline renderer.
Never downloads tools/media. Writes only to a new user-selected output directory.
"""
import argparse
import hashlib
import json
from pathlib import Path
import struct
import subprocess
import sys
import wave


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command, output, name):
    result = subprocess.run(command, capture_output=True, check=False)
    (output / (name + '.log')).write_bytes(result.stderr)
    if result.returncode:
        raise RuntimeError(f'{name}: exit {result.returncode}; inspect log')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--ffmpeg', required=True, help='Actual FFmpeg executable, no shell command')
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    ff = args.ffmpeg
    version = subprocess.run([ff, '-version'], capture_output=True, check=True).stdout.decode().splitlines()[0]
    commands = []
    def execute(name, options):
        command = [ff, '-hide_banner', '-nostdin', '-n'] + options
        commands.append({'name': name, 'argv': command})
        return run(command, output, name)

    packet = json.loads((Path(__file__).resolve().parents[1] / 'examples/silent-30s.timeline.json').read_text())
    # Six geometric timing panels. Motion only represents state transitions;
    # it does not depict or verify upstream character appearance/performance.
    w, h = 320, 180
    video = output / 'silent-30s-schematic.mp4'
    command = [ff, '-hide_banner', '-nostdin', '-n', '-f', 'rawvideo', '-pixel_format', 'rgb24',
               '-video_size', f'{w}x{h}', '-framerate', '24', '-i', 'pipe:0', '-an',
               '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', str(video)]
    commands.append({'name': 'schematic-render', 'argv': command})
    with (output / 'schematic-render.log').open('wb') as log:
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=log, stdout=subprocess.DEVNULL)
        for frame in range(720):
            event_index = next(i for i,e in enumerate(packet['events']) if e['record']['in'] <= frame < e['record']['out'])
            event = packet['events'][event_index]
            progress = (frame - event['record']['in']) / (event['record']['out'] - event['record']['in'])
            pixels = bytearray(bytes((24, 30, 40)) * (w*h))
            def box(x, y, bw, bh, rgb):
                for row in range(max(0,y), min(h,y+bh)):
                    left, right = max(0,x), min(w,x+bw)
                    if right > left:
                        pixels[(row*w+left)*3:(row*w+right)*3] = bytes(rgb)*(right-left)
            box(0,150,320,30,(55,65,75))
            box(170,100,115,6,(160,120,80))
            box(195,106,8,44,(160,120,80))
            box(270,106,8,44,(160,120,80))
            person_x = int(30+70*progress) if event_index==0 else 100
            box(person_x,65,22,58,(100,180,220))
            bird_y = 138 if event_index==0 else int(138-55*progress) if event_index==1 else 83
            bird_x = int(215+25*progress) if event_index==5 else 215
            box(bird_x,bird_y,22,16,(240,205,90))
            if event_index >= 2:
                box(bird_x+22,bird_y+5,12,4,(230,130,110))
            if event_index==3:
                box(237,72+int(progress*8),4,10,(230,130,110))
            # Panel identity and elapsed-frame bars allow cut/timing inspection.
            for n in range(event_index+1):
                box(8+n*14,8,10,8,(120,210,150))
            box(8,168,int(304*frame/719),4,(170,170,220))
            process.stdin.write(pixels)
        process.stdin.close()
        if process.wait():
            raise RuntimeError('schematic render failed; inspect log')

    # Decode every frame as raw RGB; the byte count is an exact decoded count.
    decoded = execute('schematic-full-decode', ['-i',str(video),'-map','0:v:0','-fps_mode','passthrough',
                      '-f','rawvideo','-pix_fmt','rgb24','pipe:1']).stdout
    count = len(decoded)//(w*h*3)
    assert len(decoded) == 720*w*h*3, count
    assert 'Audio:' not in (output/'schematic-full-decode.log').read_text()
    execute('contact-sheet', ['-i',str(video),'-vf','fps=2/5,tile=4x3','-frames:v','1',str(output/'contact-sheet.png')])

    # Actual mixed-rate sources with nonzero source trim; zero timestamps before concat.
    for label, rate, color in [('25',25,'red'),('24',24,'blue')]:
        execute('source-'+label,['-f','lavfi','-i',f'color=c={color}:s=160x90:r={rate}:d=6',
                                '-an','-c:v','libx264','-pix_fmt','yuv420p',str(output/f'source-{label}.mp4')])
    mixed=output/'mixed-rate-8s.mp4'
    execute('mixed-rate-conform',['-i',str(output/'source-25.mp4'),'-i',str(output/'source-24.mp4'),
        '-filter_complex','[0:v]trim=start_frame=25:end_frame=125,setpts=PTS-STARTPTS,fps=24[a];'
                          '[1:v]trim=start_frame=24:end_frame=120,setpts=PTS-STARTPTS[b];'
                          '[a][b]concat=n=2:v=1:a=0[v]',
        '-map','[v]','-an','-c:v','libx264','-pix_fmt','yuv420p','-r','24','-fps_mode','cfr',str(mixed)])
    raw = execute('mixed-full-decode',['-i',str(mixed),'-map','0:v:0','-fps_mode','passthrough',
                                     '-f','rawvideo','-pix_fmt','rgb24','pipe:1']).stdout
    assert len(raw) == 192*160*90*3
    assert raw[0] > raw[2] and raw[96*160*90*3+2] > raw[96*160*90*3]

    # Separate PCM layers establish J/L ranges and an exact synthetic sync pulse.
    samples = [0] * (6*48000)
    samples[192000:192480] = [12000]*480  # pulse at record frame 96 = 4 seconds
    incoming = [0 if not 168000 <= i < 264000 else (2000 if i%100<50 else -2000)
                for i in range(6*48000)]
    outgoing = [(1000 if i%200<100 else -1000) if i<216000 else 0
                for i in range(6*48000)]
    for name, values in [('pulse',samples),('B-J',incoming),('A-L',outgoing)]:
        path=output/(name+'.wav')
        with wave.open(str(path),'wb') as stream:
            stream.setparams((1,2,48000,len(values),'NONE','not compressed'))
            stream.writeframes(struct.pack('<'+'h'*len(values),*values))
    sync=output/'sync-pulse.mkv'
    execute('sync-render',['-f','lavfi','-i','color=c=black:s=160x90:r=24:d=6',
        '-i',str(output/'pulse.wav'),'-vf',"drawbox=x=0:y=0:w=iw:h=ih:color=white:t=fill:enable='eq(n,96)'",
        '-map','0:v:0','-map','1:a:0','-c:v','ffv1','-c:a','pcm_s16le',str(sync)])
    sync_raw=execute('sync-picture-decode',['-i',str(sync),'-map','0:v:0','-fps_mode','passthrough',
                     '-f','rawvideo','-pix_fmt','rgb24','pipe:1']).stdout
    audio_raw=execute('sync-audio-decode',['-i',str(sync),'-map','0:a:0','-f','s16le','pipe:1']).stdout
    pulse=next(i for i,(v,) in enumerate(struct.iter_unpack('<h',audio_raw)) if v)
    frame_size=160*90*3
    flash=next(i for i in range(144) if sync_raw[i*frame_size]>200)
    assert pulse==192000 and flash==96 and len(sync_raw)==144*frame_size

    jl=output/'jl-overlap.mkv'
    execute('jl-render',['-f','lavfi','-i','color=c=black:s=160x90:r=24:d=6',
        '-i',str(output/'B-J.wav'),'-i',str(output/'A-L.wav'),
        '-vf',"drawbox=x=0:y=0:w=iw:h=ih:color=white:t=fill:enable='gte(n,96)'",
        '-map','0:v:0','-map','1:a:0','-map','2:a:0','-c:v','ffv1','-c:a','pcm_s16le',str(jl)])
    bounds=[]
    for stream in range(2):
        decoded_audio=execute('jl-audio-'+str(stream),['-i',str(jl),'-map',f'0:a:{stream}',
            '-f','s16le','pipe:1']).stdout
        nonzero=[i for i,(v,) in enumerate(struct.iter_unpack('<h',decoded_audio)) if v]
        bounds.append((nonzero[0],nonzero[-1]+1))
    assert bounds==[(168000,264000),(0,216000)]
    jl_picture=execute('jl-picture-decode',['-i',str(jl),'-map','0:v:0','-fps_mode','passthrough',
        '-f','rawvideo','-pix_fmt','rgb24','pipe:1']).stdout
    assert len(jl_picture)==144*frame_size
    assert jl_picture[95*frame_size]<20 and jl_picture[96*frame_size]>200

    # Core OTIO-only serialization test, explicitly excludes plugin/NLE formats.
    import opentimelineio as otio
    timeline=otio.schema.Timeline(name='Editor paper edit')
    track=otio.schema.Track(kind=otio.schema.TrackKind.Video)
    timeline.tracks.append(track)
    for e in packet['events']:
        clip=otio.schema.Clip(name=e['id'],media_reference=otio.schema.MissingReference(),
            source_range=otio.opentime.TimeRange(
                otio.opentime.RationalTime(e['source']['in'],24),
                otio.opentime.RationalTime(e['source']['out']-e['source']['in'],24)))
        # Tested 0.18.1 rejected a nested dict in constructor metadata. A JSON
        # scalar preserves the local packet without implying native OTIO fields.
        clip.metadata['editor_event_json']=json.dumps(e,sort_keys=True)
        track.append(clip)
    otio_path=output/'silent-paper-edit.otio'
    otio.adapters.write_to_file(timeline,str(otio_path))
    restored=otio.adapters.read_from_file(str(otio_path))
    assert restored.duration().value==720 and restored.duration().rate==24
    assert [c.name for c in restored.tracks[0]] == [e['id'] for e in packet['events']]
    for clip,event in zip(restored.tracks[0],packet['events']):
        assert clip.source_range.start_time.value==event['source']['in']
        assert json.loads(clip.metadata['editor_event_json'])==event
        assert clip.range_in_parent().start_time.value==event['record']['in']
    files={p.name:{'bytes':p.stat().st_size,'sha256':digest(p)}
           for p in output.iterdir() if p.is_file()}
    report={'python_version':sys.version,'ffmpeg':version,'otio_version':otio.__version__,
        'fixture_sha256':digest(Path(__file__).resolve().parents[1]/'examples/silent-30s.timeline.json'),
        'commands':commands,'files':files,
        'measurements':{'schematic_frames':count,'schematic_audio_stream':'absent',
          'mixed_rate_output_frames':192,'mixed_rate_output_fps':24,'mixed_rate_join_frame':96,
          'sync_flash_frame':flash,'sync_pulse_sample_48000Hz':pulse,'sync_offset_frames':0,
          'J_start_record_frame':84,'L_end_record_frame':108,
          'JL_decoded_nonzero_sample_ranges_48000Hz':bounds,
          'JL_evidence':'two separate PCM streams; measured boundaries around frame-96 picture change; no dialogue/mix evaluation',
          'otio_core_roundtrip':'6 clips, source ranges, parent starts, asset version metadata; 720 frames at 24'},
        'not_assessed':['full perceptual playback/listening','lip sync or J/L dramatic quality',
          'upstream character/prop continuity','calibrated color','captions/player',
          'actual NLE/CMX EDL/FCPXML import','audience response','real generated footage']}
    (output/'results.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'output':str(output),'measurements':report['measurements'],'ffmpeg':version,
                      'otio_version':otio.__version__},indent=2))


if __name__=='__main__':
    main()
