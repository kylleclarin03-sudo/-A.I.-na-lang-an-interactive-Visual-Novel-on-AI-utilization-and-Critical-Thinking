## game/gui.rpy
## Authoritative GUI configuration. 1920x1080 desktop base.
## Mobile variant scales up for touch targets automatically.

init python:
    gui.init(1920, 1080)

# ── FONT CONFIGURATION ────────────────────────────────────────────────────────
## Place NotoSans-Regular.ttf in game/gui/fonts/ and update this path.
## Fallback: Ren'Py default font will be used if file is missing.
define gui.default_font       = "gui/fonts/NotoSans-Regular.ttf"
define gui.interface_font     = "gui/fonts/NotoSans-Regular.ttf"
define gui.glyph_font         = "gui/fonts/NotoSans-Regular.ttf"

# ── TEXT SIZES (desktop base 1920×1080) ──────────────────────────────────────
define gui.text_size              = 36
define gui.name_text_size         = 40
define gui.interface_text_size    = 33
define gui.button_text_size       = 36
define gui.label_text_size        = 36
define gui.choice_button_text_size= 36

# ── COLORS ────────────────────────────────────────────────────────────────────
define gui.accent_color       = "#1f6feb"
define gui.idle_color         = "#8b949e"
define gui.idle_small_color   = "#8b949e"
define gui.hover_color        = "#e6edf3"
define gui.selected_color     = "#58a6ff"
define gui.insensitive_color  = "#30363d"
define gui.text_color         = "#e6edf3"
define gui.interface_text_color = "#e6edf3"

# ── WINDOW LAYOUT ─────────────────────────────────────────────────────────────
define gui.textbox_height      = 278
define gui.textbox_yalign      = 1.0
define gui.name_xpos           = 360
define gui.name_ypos           = 0
define gui.name_xalign         = 0.0
define gui.dialogue_xpos       = 402
define gui.dialogue_ypos       = 75
define gui.dialogue_width      = 1116
define gui.dialogue_text_xalign= 0.0

# ── CHOICE BUTTONS ────────────────────────────────────────────────────────────
define gui.choice_button_width  = 1185
define gui.choice_button_height = 100    ## Tall for touch targets
define gui.choice_button_tile   = False

# ── BARS & SLIDERS ────────────────────────────────────────────────────────────
define gui.bar_size        = 38
define gui.slider_size     = 44
define gui.scrollbar_size  = 18
define gui.vscrollbar_size = 18

# ── DIALOGUE WINDOW ───────────────────────────────────────────────────────────
define gui.dialogue_window_xalign = 0.5
define gui.pref_text_size         = 45

# ── MOBILE VARIANT (small = phones & tablets) ─────────────────────────────────
init python:
    if renpy.variant("small"):
        gui.text_size               = 44
        gui.name_text_size          = 48
        gui.interface_text_size     = 40
        gui.button_text_size        = 44
        gui.choice_button_text_size = 42
        gui.choice_button_height    = 120
        gui.bar_size                = 54
        gui.slider_size             = 60
        gui.navigation_spacing      = 36

# ── WEB VARIANT TRANSITION OVERRIDE ──────────────────────────────────────────
## Lightweight transitions on web prevent frame drops on mid-range phones.
init python:
    if renpy.variant("web"):
        config.enter_transition = dissolve
        config.exit_transition  = dissolve
