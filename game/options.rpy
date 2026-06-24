## game/options.rpy
## Core game configuration for A.I. na lang!

define config.name = _("A.I. na lang!")
define config.version = "1.0.0"
define config.window_title = "A.I. na lang!, A Visual Novel"

## 1920x1080 canonical authoring resolution.
init -1 python:
    # Set the default resolution; this informs the GUI layout.
    config.physical_width = 1920
    config.physical_height = 1080

define config.has_music = True
define config.has_sound = True
define config.has_voice = False
define config.main_menu_music = "audio/bgm/bgm_menu.ogg"

## Persistent saves survive cache clears on IndexedDB (web).
define config.save_directory = "ai_na_lang-1.0.0"

## Keep up to 250 dialogue lines in the history screen.
define config.history_length = 250

## Taglish, no separate translation layer needed.
define config.language = None

## Hide developer console in production.
define config.developer = False

## Scene transitions.
define config.enter_transition = dissolve
define config.exit_transition  = dissolve

define config.window = "auto"

init python:
    ## Safe music play helper, silently skips if file is missing.
    def safe_play(channel, filename, loop=True):
        import os
        path = os.path.join(config.gamedir, filename)
        if not os.path.exists(path):
            return
        try:
            if loop:
                renpy.music.play(filename, channel=channel, loop=True)
            else:
                renpy.music.play(filename, channel=channel, loop=False)
        except Exception:
            pass

    def safe_stop(channel="music"):
        try:
            renpy.music.stop(channel=channel, fadeout=1.0)
        except Exception:
            pass

    ## ── WEB MEMORY OPTIMISATION ────────────────────────────────────────────
    ## Limit rollback history to reduce IndexedDB / WASM heap pressure.
    ## 120 steps ≈ about 1 full chapter's worth of undo.
    config.rollback_length = 120

    ## Disable Ren'Py's automatic thumbnail generation for save slots.
    ## Thumbnails cost ~2 MB each; with 80 slots that's 160 MB wasted.
    ## We use text-only slot display (already done in slot_grid screen).
    config.thumbnail_width  = 1
    config.thumbnail_height = 1

    ## Cap the per-channel audio cache.
    ## Default is unlimited; 32 MB covers all OGG files for the chapter.
    ## Lower if web build crashes on mid-range phones.
    config.audio_cache_size = 32 * 1024 * 1024  # 32 MB

    ## Prefer smaller image surfaces on web — Ren'Py will downscale if needed.
    ## Only enable if the build is crashing; comment out otherwise.
    ## config.image_cache_size = 64 * 1024 * 1024  # 64 MB — adjust as needed

    ## Web: disable voice channel to reclaim one audio context.
    if renpy.variant("web"):
        config.has_voice = False
