## game/gui.rpy
## Authoritative GUI configuration. 1920x1080 desktop base.
## Mobile variant scales up for touch targets automatically.

init python:
    gui.init(1920, 1080)

# ── FONT CONFIGURATION ────────────────────────────────────────────────────────
## Place NotoSans-Regular.ttf in game/gui/fonts/ and update this path.
## Fallback: Ren'Py default font will be used if file is missing.
define gui.default_font    = "gui/fonts/IndieFlower-Regular.ttf" # For dialogue
define gui.interface_font  = "gui/fonts/Marmelad-Regular.ttf" # For menus/buttons
define gui.name_text_size  = 44
define gui.text_size       = 34

# ── TEXT SIZES (desktop base 1920×1080) ──────────────────────────────────────
define gui.text_size              = 34
define gui.name_text_size         = 38
define gui.interface_text_size    = 30
define gui.button_text_size       = 34
define gui.label_text_size        = 36
define gui.choice_button_text_size = 30
define gui.choice_button_height   = 88
define gui.textbox_height         = 270
define gui.main_menu_background = "images/backgrounds/bg_campus.webp"


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
define gui.textbox_background = Frame(
    Window(
        background=Solid("#0d1117E6"), # Dark hex with 90% opacity (E6)
        top_border=Solid("#1f6feb"),   # Blue accent line on top
        top_padding=4
    )
)

# ── CHOICE BUTTONS (App Aesthetic) ────────────────────────────────────────────
define gui.choice_button_width  = 1100
define gui.choice_button_height = 85
define gui.choice_button_tile   = False

# Make choices look like dark mode app buttons
define gui.choice_button_idle_background = Solid("#21262d")
define gui.choice_button_hover_background = Solid("#30363d")

# The text turns your Ocean Blue when hovered
define gui.choice_button_text_idle_color = "#c9d1d9"
define gui.choice_button_text_hover_color = "#58a6ff"

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

# ── DISABLE DEFAULT TEXTBOX BACKGROUND ────────────────────────────────────────
## Our custom say screen draws its own background, so we clear the default.
define gui.textbox_background = Solid("#00000000")

# ── WEB VARIANT TRANSITION OVERRIDE ──────────────────────────────────────────
## Lightweight transitions on web prevent frame drops on mid-range phones.
init python:
    if renpy.variant("web"):
        config.enter_transition = dissolve
        config.exit_transition  = dissolve


################################################################################
## FILE SLOTS (shared by save and load)
################################################################################
screen file_slots(title):

    frame:
        xfill True
        yfill True
        background Solid("#0d1117")

        vbox:
            xalign 0.5
            yalign 0.1
            spacing 10
            text title xalign 0.5 size 44 color "#58a6ff" bold True

        vpgrid:
            cols 2
            xalign 0.5
            yalign 0.5
            xspacing 20
            yspacing 20

            for i in range(1, 9):
                # Inside screen file_slots(title):
                button:
                    xsize 700
                    ysize 120
                    # Standard dark box, but turns solid blue on hover
                    background Solid("#21262d")
                    hover_background Solid("#1f6feb")
                    action FileAction(i)

                    hbox:
                        xalign 0.0
                        yalign 0.5
                        xoffset 30
                        spacing 20

                        vbox:
                            yalign 0.5
                            # Text stays white on hover for readability
                            text "Save Slot [i]" size 28 color "#8b949e" hover_color "#ffffff"
                            text "[FileTime(i, empty=_('Walang save'))]" size 24 color "#c9d1d9" hover_color "#ffffff"

        textbutton "Bumalik":
            action Return()
            xalign 0.5
            yalign 0.95
            xsize 300
            ysize 70
            background Solid("#1f6feb")
            hover_background Solid("#388bfd")
            text_color "#fff"
            text_size 30
            text_xalign 0.5
            text_yalign 0.5