# Consulted source registry

Access date for every entry: **2026-11-25 (Asia/Bangkok)**. “Read” means the
identified web text/PDF sections returned by the web tool, not video playback,
course attendance, a purchased standard or a test of a provider. No source assets
are copied. Local synthesis uses P IDs in [notes](notes.md); gaps are in
[audit](audit.md). Refresh changing provider/delivery claims before actual use.

| ID | Source / URL and inspected portion | Supported claim | Limits |
| --- | --- | --- | --- |
| S01 | Randy Thom, 1999, [Designing a Movie for Sound](https://filmsound.org/articles/designing_for_sound.htm): opening, pre-production/POV, acoustic place, ambiguity sections | Sound can shape film decisions early; perspective and acoustic space serve narrative. | Practitioner argument hosted by FilmSound, not controlled audience research; film examples were not played. |
| S02 | Yale Film Analysis, [Part 5: Sound](https://filmanalysis.yale.edu/sound/): bridges, source/diegesis, offscreen, postsynchronization, perspective, synchrony | Distinguishes source/world, frame visibility and temporal/spatial relationships. | Educational definitions and written examples; embedded clips not played. |
| S03 | Berklee Online, [Professional Film Scoring Skills 1](https://online.berklee.edu/courses/professional-film-scoring-skills-1-collaboration-and-communication): public syllabus lessons 4–11 | Spotting/cue matrix, dialogue/SFX collaboration, conform, stems and delivery belong in training. | Course outline only; not full lessons or empirical proof of this workflow. |
| S04 | Adobe, [Noise reduction and restoration](https://helpx.adobe.com/audition/desktop/effects-reference/noise-reduction-restoration-effects.html): restoration overview, noise reduction controls/artifacts | Excessive restoration can damage wanted sound; preview removed content. | Product-specific explanation; no Audition execution or claim its suggested settings generalize. |
| S05 | ITU, [BS.1770 index](https://www.itu.int/rec/R-REC-BS.1770/en), [version record](https://www.itu.int/rec/R-REC-BS.1770-5-202311-I/en) and [English PDF](https://www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.1770-5-202311-I!!PDF-E.pdf), printed pp. 1–3, 18–19: scope/recommendations, Annex 1 overview, Annex 2 | Loudness is an objective estimate with listener/material uncertainty; true peaks can exceed sample peaks. | Web PDF timed out twice; later system curl download and pypdf text extraction succeeded. Selected sections only, not all annexes or meter-conformance testing. |
| S06 | EBU, [R128 v5 PDF](https://tech.ebu.ch/files/live/sites/tech/files/shared/r/r128.pdf), printed pp. 2–4, especially clauses h–m | Programme −23 LUFS; linear −1 dBTP; current exception/QC tolerances and whole-programme measurement. | Broadcast recommendation, not every platform's contract; distribution can impose other ceilings. |
| S07 | Microsoft, [SSML pronunciation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-pronunciation): phoneme and custom lexicon sections | Pronunciation controls depend on supported locale/phone set. | Documentation text was returned despite an authorization banner; no account access or synthesis; verify selected voice support. |
| S08 | Microsoft, [Custom voice overview](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/custom-neural-voice): professional voice steps | Provider requires recorded talent consent before professional fine-tuning. | Provider workflow, not universal legal sufficiency or evidence any speaker consented. |
| S09 | Microsoft, [Viseme guide](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-speech-synthesis-viseme): overview, IDs, offsets, locale notes | Offsets use 100 ns ticks; phoneme/viseme mapping is not one-to-one; features vary by locale. | Text returned with authorization banner; no SDK or animation test; guide events do not prove lip sync. |
| S10 | W3C WAI, [Making Audio and Video Media Accessible](https://www.w3.org/WAI/media/av/): planning and component guidance, updated 2024-09-17 | Access planning includes captions, transcripts, visual description and player support. | General guidance, not a compliance audit of this package or a film. |
| S11 | W3C WAI, [Captions/Subtitles](https://www.w3.org/WAI/media/av/captions/): definitions, automatic captions, formats | Captions convey meaningful speech/non-speech audio; automatic captions need accuracy checking. | No timed caption file/player evaluated; actual obligations depend on medium and requirements. |
| S12 | AES, [TD1008 landing](https://aes.org/community/technical-council/technical-document-aestd1008/) and [linked PDF](https://aes.org/wp-content/uploads/2026/10/20210924_TD1008_v3.13.pdf), introduction, tables 1–2, peak-control and downmix sections | Audio-only distribution scope explicitly excludes sound-with-picture; codec/downmix paths affect peak/balance judgments. | Landing identifies 2021 document despite a 2026 hosting path; tables are not OTT delivery rules. No AES77 full standard read. |
| S13 | YouTube Help, [Recommended upload encoding settings](https://support.google.com/youtube/answer/1722171?hl=en): audio codec/channels/rate | Official upload encoding recommendations include 48 kHz. | No universal −14 LUFS requirement in opened page; no upload/playback or normalization test. Recheck actual delivery path. |
| S14 | FFmpeg, [Filters manual](https://ffmpeg.org/ffmpeg-filters.html#loudnorm): loudnorm options and [ebur128](https://ffmpeg.org/ffmpeg-filters.html#ebur128) scanner/peak modes | Documents measurement/normalization controls and fallback behavior. | Living documentation; installed build may differ. FFmpeg was not found on this session's PATH. |
| S15 | U.S. Copyright Office, [How Songwriters, Composers, and Performers Get Paid](https://www.copyright.gov/music-modernization/educational-materials/musicians-income.pdf), printed p. 12, synchronization note | Distinguishes composition synchronization and recording master-use licensing in audiovisual uses. | U.S.-specific educational guidance; no project clearance, Thai-law determination or AI-rights conclusion. |
| S16 | ElevenLabs, [Sound effects](https://elevenlabs.io/docs/overview/capabilities/sound-effects): usage, prompting, model limitations and key facts | Requests for exact repetitions may fail; provider settings/output capabilities require checking. | Provider claims, not an independent quality study; page is changeable, no generation or API run. |
| S17 | Adobe Learn, [Use the Phase Analysis panel](https://www.adobe.com/learn/audition/web/audition-phase-analysis-cc), text transcript on timing/inversion and mono | Channel timing/inversion issues warrant mono inspection. | Read transcript, did not watch/listen. Do not generalize every simplified physical explanation in tutorial. |

## Other consultations and failed access

- [Berklee Composer (Film)](https://www.berklee.edu/careers/roles/composer-film):
  read role/collaboration description only; no additional technical rule derived.
- [Berklee Sound Designer](https://www.berklee.edu/careers/roles/sound-designer)
  failed; the attempted film-role variant redirected to sign-in. No craft claims
  attributed to either inaccessible page; used the accessible syllabus instead.
- ITU PDF recovery: 32-page file, SHA-256
  `eefb926f72f72a96b96f251067bfee0650a0f29a26f60661d354162038b041ad`.
  Read PDF pages 1–5 and 20–21 (title/front matter and selected technical text),
  not a full-standard review. No videos, books or papers referenced by the
  opened pages are silently counted as read.
- Separate HTTP reachability attempts are retained in
  [link evidence](../tests/http-links.json); successful HEAD is not body reading.
