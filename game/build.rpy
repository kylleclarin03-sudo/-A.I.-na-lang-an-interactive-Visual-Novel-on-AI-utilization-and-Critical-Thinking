## game/build.rpy
## Tells Ren'Py what packages to build for distribution.

init python:
    build.name = "AInaLang"
    build.executable_name = "AInaLang"

    build.include_old_themes = False
    build.classify_renpy("**", None)

    ## Web (HTML5/WebAssembly) — the only package we need
    build.web("web", "A.I. na lang!")
