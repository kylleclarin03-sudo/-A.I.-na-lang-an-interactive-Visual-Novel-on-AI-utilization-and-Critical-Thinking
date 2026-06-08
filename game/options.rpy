## game/options.rpy
## Core game configuration for A.I. na lang!

define config.name = _("A.I. na lang!")
define config.version = "1.0.0"
define config.window_title = "A.I. na lang! — A Visual Novel"

## 1920x1080 canonical authoring resolution.
define gui.init(1920, 1080)

define config.has_music = True
define config.has_sound = True
define config.has_voice = False
define config.main_menu_music = "audio/bgm/bgm_menu.ogg"

## Persistent saves survive cache clears on IndexedDB (web).
define config.save_directory = "ai_na_lang-1.0.0"

## Taglish — no separate translation layer needed.
define config.language = None

## Hide developer console in production.
define config.developer = False

## Scene transitions.
define config.enter_transition = dissolve
define config.exit_transition  = dissolve

define config.window = "auto"

init python:
    ## Safe music play helper — silently skips if file is missing.
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
