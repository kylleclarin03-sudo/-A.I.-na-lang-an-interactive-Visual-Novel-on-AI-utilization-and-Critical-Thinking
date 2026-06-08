# Audio File Requirements — A.I. na lang!

All audio must be **.OGG** format, 44.1 kHz, stereo.
BGM: 96–128 kbps. SFX: 64–96 kbps.

---

## BGM Files (`game/audio/bgm/`)

| File                   | Scene Used In                | Mood               |
|------------------------|------------------------------|--------------------|
| bgm_menu.ogg           | Main menu                    | Lo-fi, hopeful     |
| bgm_campus.ogg         | Campus scenes, Ch.1          | Upbeat Pinoy indie |
| bgm_classroom.ogg      | Lecture scenes               | Light academic     |
| bgm_study.ogg          | Bedroom study scenes         | Lo-fi beats        |
| bgm_tension.ogg        | Exam / confrontation scenes  | Tense, minimal     |
| bgm_canteen.ogg        | Canteen social scenes        | Relaxed indie pop  |
| bgm_night.ogg          | Late-night gaming scenes     | Lo-fi, slight edge |
| bgm_sad.ogg            | Results / low-meter scenes   | Slow, subdued      |
| bgm_finals.ogg         | Finals exam sequence         | Cinematic, builds  |
| bgm_good_ending.ogg    | Good / Special good endings  | Warm, triumphant   |
| bgm_bad_ending.ogg     | Bad / Caught endings         | Sparse, fading     |

---

## SFX Files (`game/audio/sfx/`)

| File                  | Trigger                              |
|-----------------------|--------------------------------------|
| sfx_click.ogg         | Any choice button tap                |
| sfx_phone.ogg         | Phone notification / AI corner tap   |
| sfx_correct.ogg       | Correct minigame answer              |
| sfx_wrong.ogg         | Wrong minigame answer                |
| sfx_alarm.ogg         | Wake-up late scene                   |
| sfx_chime.ogg         | Character selection confirmation     |
| sfx_grade_reveal.ogg  | Grade results screen                 |
| sfx_chat.ogg          | Group chat message pop-up            |
| sfx_page_turn.ogg     | Scene transition                     |

---

> **Note:** Until real audio files are supplied, the game will silently skip
> music without crashing. The code uses `safe_play()` which checks file
> existence before calling `renpy.music.play()`.
