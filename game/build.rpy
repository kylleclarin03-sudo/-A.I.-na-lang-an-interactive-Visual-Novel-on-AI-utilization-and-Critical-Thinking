## game/build.rpy
## Build configuration for A.I. na lang!
##
## FIX: Removed build.package("web", "web", "") — "web" is NOT a valid
## format string for build.package(). The web format is registered internally
## by the Ren'Py Launcher at distribute-time. Calling it here caused:
## Exception: Format web not known.
##
## The --package web flag in the CI workflow handles the web build.

init python:
    build.name = "AInaLang"
    build.executable_name = "AInaLang"
