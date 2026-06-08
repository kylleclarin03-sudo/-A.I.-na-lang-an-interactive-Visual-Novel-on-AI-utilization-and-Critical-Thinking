# Audio File Inventory — A.I. na lang!

This is the **complete manifest** of every audio file referenced anywhere in the game's code. Drop the matching `.ogg` files into the `bgm/` and `sfx/` folders and the game will pick them up automatically (the `safe_play()` helper silently skips missing files, so the game won't crash without them).

**Format required:** `.ogg`, 44.1 kHz, stereo
**BGM bitrate:** 96–128 kbps
**SFX bitrate:** 64–96 kbps

---

## BGM Files (`game/audio/bgm/`)

| # | File | Used In | Mood / Genre | Notes |
|---|------|---------|--------------|-------|
| 1 | ok`bgm_menu.ogg` | Main menu, opening | Lo-fi, hopeful | The first thing the player hears |
| 2 | `bgm_campus.ogg` | Campus scenes, Ch. 1 opening, Ch. 8 after-finals | Upbeat Pinoy indie | Light and bouncy |
| 3 | `bgm_classroom.ogg` | Lecture scenes (Ch. 1, Ch. 3, Ch. 5) | Light academic | Subtle background |
| 4 | `bgm_study.ogg` | Bedroom study scenes (Ch. 4 eve, Ch. 6 redo) | Lo-fi beats | Concentration |
| 5 | ok`bgm_tension.ogg` | Exam scenes, Ms. Iva confrontation (Ch. 2, 4, 6) | Tense, minimal | Building dread |
| 6 | ok`bgm_canteen.ogg` | Canteen social scenes (Ch. 1, 3, 7) | Relaxed indie pop | Friendly chatter vibe |
| 7 | ok`bgm_night.ogg` | Late-night gaming scenes (Ch. 2, Ch. 4 night) | Lo-fi with slight edge | Bedroom-at-2AM |
| 8 | ok`bgm_sad.ogg` | Results, INC reveal, bad outcomes (Ch. 5, 6, 7) | Slow, subdued | Emotional weight |
| 9 | ok`bgm_finals.ogg` | Finals exam morning (Ch. 8) | Cinematic, builds | Pressure and momentum |
| 10 | ok`bgm_good_ending.ogg` | Good, Special Good, Solid Enough endings | Warm, triumphant | Hopeful resolution |
| 11 | ok`bgm_bad_ending.ogg` | Bad, Caught endings | Sparse, fading | Quiet closure |

---

## SFX Files (`game/audio/sfx/`)

| # | File | Trigger | Notes |
|---|------|---------|-------|
| 1 | `sfx_click.ogg` | Any choice button tap | Short, soft click |
| 2 | `sfx_phone.ogg` | Phone notification, AI corner tap | Digital notification sound |
| 3 | `sfx_correct.ogg` | Correct minigame answer | Cheerful chime |
| 4 | `sfx_wrong.ogg` | Wrong minigame answer | Soft buzz or low tone |
| 5 | `sfx_alarm.ogg` | Wake-up late scene (Ch. 4) | Alarm clock ringing |
| 6 | `sfx_chime.ogg` | Character selection confirmation | Soft bell / ding |
| 7 | `sfx_grade_reveal.ogg` | Grade results screen | Drumroll or reveal hit |
| 8 | `sfx_chat.ogg` | Group chat message pop-up | Pop notification |
| 9 | `sfx_page_turn.ogg` | Scene transition | Subtle paper/page sound |

---

## How the Code Handles Missing Audio

Every audio call uses `safe_play()` and `safe_stop()` (defined in `options.rpy`). These check if the file exists before calling `renpy.music.play()`. If a file is missing:

- The game continues normally
- No crash, no warning popup
- The scene just plays silently

So you can build, test, and play the game **right now** without any audio files. Drop them in later when ready.

---

## Free / CC0 Audio Sources

If you need royalty-free OGG music for this project, these are good starting points:

- **OpenGameArt.org** — full music and SFX packs, CC0 / CC-BY
- **Free Music Archive (freemusicarchive.org)** — royalty-free tracks
- **Freesound.org** — SFX and ambient sounds, CC0 / CC-BY
- **Pixabay Music** — no attribution required
- **YouTube Audio Library** — free with optional attribution

For OGG conversion, use **Audacity** (free, open-source) — File → Export as OGG.