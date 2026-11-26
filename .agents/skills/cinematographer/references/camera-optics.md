# Camera, optics and motion decisions

Use for physical capture, a virtual camera or a model-agnostic shot specification.
P = physical/technical fact; C = convention; H = craft heuristic; I = contextual
interpretation; S = local system choice. Claim IDs resolve in
[notes](../research/notes.md). Numbers in examples are proposed settings, not
measurements of footage or guarantees of model compliance.

## Choose viewpoint before a lens label

For a rectilinear ideal camera, horizontal angle of view is approximately
`2 atan(sensor_width / (2 focal_length))`. Use the active recorded gate, not the
camera's marketing sensor size. State width/height, crop and orientation; a focal
length alone cannot specify the frame. Real distortion, close focus and lens
design can depart from this approximation. [P07: P]

Perspective depends on viewpoint relative to the scene. Focal length changes
framing at that viewpoint; stepping back to preserve subject size changes relative
near/far scale. A smaller sensor crops the image; it does not lengthen the lens.
“Long lens compression” often bundles the lens with a more distant camera. Record
both to avoid giving an impossible instruction. [P07/P08: P; pinhole deduction]

**Worked distinction (ideal pinhole):** a face at 2 m and equal-height background
mark at 6 m have a background/face image-size ratio of 2/6 = .333. Changing 35 mm
to 70 mm at the same station enlarges both equally: ratio stays .333. Moving the
camera 1 m forward changes distances to 1 m and 5 m: ratio becomes .2. That is a
perspective change. A crop/digital push also preserves perspective while losing
image area/resolution; it does not produce dolly parallax. [H analytical example]

| Need | How / why (H) | Trade-off, counterexample and remedy |
| --- | --- | --- |
| Show hand, face and room | Set camera distance/height for their relationship, then choose FOV. | Close wide views may enlarge the hand relative to face. If identity looks wrong, move back and reframe; distinguish projection from lens distortion. |
| Isolate without losing context | Compare separation by blocking/light against shallow DOF. | A long focal length may require an unavailable wall position. Widen gate/FOV or revise staging, with approval if action changes. |
| Match cameras / virtual views | Match gate, viewpoint, orientation, focus and framing; record lens assumptions. | Same millimeters on different gates do not match. Use a known FOV or field dimensions at subject plane. |

## Aperture, focus and exposure

DOF is an acceptable-sharpness range, dependent on aperture, distance,
magnification and the sharpness criterion/output. It is not the same as the
focus plane or image-side depth of focus. Stopping down generally extends useful
depth but excessive stopping can lose fine detail to diffraction. [P09: P]

Choose what must remain legible across the action first, then test aperture and
focus marks. For a two-person handoff, fully open shallow focus may lose the hand
at the critical contact. Stop down/add light, change depth staging, or plan a
focus pull. Do not say “more light creates DOF” without noting the aperture change.
For a virtual camera, DOF can be disabled if the approved medium calls for graphic
clarity. [H]

Exposure at capture depends on scene light, aperture/transmission and exposure
time. One stop doubles/halves light; f/2.8 → f/4 is about one stop less. F-number
describes geometry, T-stop transmission; label which. ISO/gain affects camera
signal handling/noise and may redistribute usable latitude; raising it does not
deliver more photons. Consult the specific camera's mode and test. [P10/P11: P]

| Symptom | Diagnose / remedy (H) | What the fix costs |
| --- | --- | --- |
| Hand sharp, face soft | Check focus marks and depth path, not only prompt adjectives. Stop down or restage plane. | More light / changed background rendering; avoid removing essential action. |
| Highlights clip, face reads | Check acquisition clipping with the right scopes/false color and monitor transform. Reduce source contrast or practical intensity. | Darkening everything can bury the face; a display LUT cannot recover clipped capture. |
| Low light looks muddy | Inspect source separation and actual noise; add a motivated source/bounce or simplify movement. | Opening aperture narrows DOF; longer exposure smears motion. Record the chosen priority. |
| Unwanted color shift between shots | Compare WB/tint, source spectrum, exposure and viewing transform. | WB is a global interpretation; it cannot independently neutralize all mixed sources. |

Dynamic range is the usable span between dark and bright recorded detail, not
“flat contrast” or a guarantee that any highlight can be graded back. A log encoding
and display LUT serve different functions. Record recording format/transfer,
working/view/output interpretation when relevant; judge look with the intended
viewing transform. Numeric skin targets need the camera/transform and subject,
not a universal IRE for all skin. [P11: P; H application]

## Time, shutter and focus animation

Exposure time in seconds = `shutter_angle / (360 * capture_fps)`: 24 fps at 180°
gives 1/48 s; 90° gives 1/96 s. Shorter exposures reduce motion blur but may feel
more staccato; longer ones trade detail for smear. Near 180° is a convention, not
a requirement, and is unrelated to the spatial 180-degree axis. [P12: P/C]

Capture and playback rates must both be stated: 48 captured frames played at
24 fps take twice their capture time. Animation on twos does not mean a 12 fps
delivery file. Avoid prescribing high frame rate merely to mean “cinematic”.
Lighting/display flicker and rolling-shutter behavior require device/mode tests;
no mains-frequency formula guarantees every LED is flicker-free. [P13: P; H]

A focus pull changes the plane of attention; a camera move changes viewpoint;
a zoom changes focal length. Specify focus start/end target, trigger and duration
separately from camera path. Focus breathing may alter framing in a real lens;
do not promise a perfectly invariant frame without testing. [P01/P11: P; H]

## Movement: describe the path and its purpose

These are operational distinctions (C/P); the choices and diagnostics are H.
“Tracking” can mean several paths: specify coordinates/landmarks rather than
relying on the word. Yale supplies general movement vocabulary; the motion
specification format here is local. [P01/S02]

| Choice | When / how | Trade-off or failure → remedy |
| --- | --- | --- |
| Static / locked | Let blocking or changing information carry the shot. State fixed station and orientation. | Subject exits useful framing → allow deliberate reframe or redesign blocking. A locked frame can contain intense action. |
| Pan / tilt | Rotate horizontally / vertically at a station to follow or reveal. Give start/end view and trigger. | Rotation may expose a withheld subject; constrain reveal timing. Fast detailed pans can judder; test motion, shutter and playback. |
| Dolly in/out | Translate toward/away from subject; set distance/path and focus follow. | Parallax may expose an unwanted object or change face projection. Check intermediate views, not just endpoints. |
| Truck | Translate laterally; state direction in world and resulting screen motion. | Foreground occlusion or speed mismatch → move obstructions or simplify path. |
| Pedestal | Translate vertically with orientation defined. | It is not a tilt. If horizon/eye relation shifts undesirably, revise height and aim together. |
| Crane / boom | Translate on a rising/sweeping path; identify what new geography becomes visible. | Real reach/rig clearance or virtual intersections → reduce height/path or use another shot. |
| Orbit / arc | Move around a subject with radius, extent and facing target. | Can cross axis, reveal new sides/assets and demand refocusing. Use only when those changes do narrative work. |
| Handheld | Specify restrained drift vs energetic response, subject relation and amplitude. | Random shake obscures information or disrupts identity in generation → stabilize/simplify. Handheld need not be frantic. |
| Zoom | Change focal length at a fixed viewpoint; state range and subject-size change. | It magnifies without dolly parallax. Do not ask it to reveal behind an occluder. Digital crop also spends resolution. |
| Dolly zoom | Couple translation and focal change to roughly retain subject scale while background relation changes. | Complex focus/path/scale coordination; choose a simple push if the background effect is unnecessary. |
| Focus pull | Keep path/orientation fixed if intended; transfer focus A → B at a specified event. | Missed target or conspicuous breathing → restage depth or use an insert, subject to reveal constraints. |

RED's pan guidance treats its seven-second screen-transit starting point as
conditional on 24 fps/180° and viewing/content, not a hard speed limit. Test at
delivery playback, especially high-contrast edges; do not apply a landscape pan
rule blindly to a whip pan or portrait crop. [P14: C/H]

For any move, ask: what changes in information that a static frame, actor movement
or a cut cannot achieve as economically? Budget the path, action and focus
together. A “camera locked, orbiting around the actor” spec is contradictory;
resolve it before handing off. See [AI constraints](animation-ai.md).
