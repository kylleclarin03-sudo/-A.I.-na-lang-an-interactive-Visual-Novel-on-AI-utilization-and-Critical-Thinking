## game/build.rpy
## Registers the web distribution package for Ren'Py's distribute command.

init python:
    build.name = "AInaLang"
    build.executable_name = "AInaLang"

    ## Clear default packages (we only want web)
    build.packages = []

    ## Register the web package using the correct API
    build.package("web", "web", "")