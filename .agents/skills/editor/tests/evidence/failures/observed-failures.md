# Observed failures and retests

These are actual development observations, retained rather than rewritten as an
all-pass history. No neighboring source or shared file was edited to repair them.

1. First local link validation: 42 links scanned; one failure because the registry
   linked to `tests/http-links.json` before the HTTP log existed. After creating
   the actual log, the same scan passed. This was construction state, not a source
   quality result.
2. OTIO 0.18.1 / Python 3.14: constructing Clip with explicit dictionary metadata
   raised `RuntimeError: bad any cast`, even for an empty dict. Named/default Clip
   and scalar metadata assignment worked. The harness switched to a scalar JSON
   custom field preserving the event rather than declaring fields native OTIO.
3. A second Python 3.14 OTIO attempt reached `adapters.write_to_file` but failed
   loading the built-in plugin manifest with the same `bad any cast` error.
   No successful `.otio` round trip is claimed for that environment. This does
   not establish the underlying library cause or all Python 3.14 compatibility.
4. Python 3.9.6 with OTIO 0.18.1 successfully constructed/serialized a nested test
   record. Its environment's FFmpeg 7.1 then exposed a different harness error:
   mixed-rate output without explicit output `-r` inherited 25 fps, decoded 199
   frames rather than expected 192, and failed the count assertion. The actual
   [decode log](ffmpeg7-mixed-rate-199-frames.log) is retained. FFmpeg 9.0 had
   selected 24 fps on that earlier command, so its pass did not prove portability.
5. Added explicit `-r 24 -fps_mode cfr` after the normalized concat. Full harness
   rerun under Python 3.9.6 with FFmpeg 7.1 **and** 9.0 passed all assertions,
   including core OTIO read-back with the same OTIO 0.18.1. Logs/results retain
   actual versions, commands, hashes, counts and unassessed areas. See
   [final media results](../media/results.json) and
   [second-build results](../ffmpeg7-retest-results.json).

6. A final-report construction scan similarly found the newly linked
   `static-checks.json` before the command-capture process had written that file.
   The [failed command record](static-link-construction.json) is retained; the
   completed record exists before the final rerun and isolated-copy check.

Media intermediates from unsuccessful runs stayed in temporary test directories;
only the failed diagnostic log and final successful media are packaged. No
production render was overwritten. A codec/process pass does not close perceptual
or downstream acceptance checks.
