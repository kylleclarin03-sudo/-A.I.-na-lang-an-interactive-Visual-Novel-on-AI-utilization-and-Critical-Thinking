## game/screens.rpy
## A.I. na lang!  —  Complete UI/UX Overhaul v2.0
## Aesthetic: Dark Academic Terminal (GitHub palette + neon-blue accents)
## Web-safe: no image files required. Pure Ren'Py displayables.

################################################################################
## UTILITY: CARD BACKGROUND BUILDER
## Produces a two-tone card: 3-px blue stripe on top, dark content area below.
## Used by dialogue box, chapter title, minigame, and grade results.
################################################################################
init python:
    def card_bg(stripe_color="#1f6feb", body_color="#0d1117F4",
                stripe_h=3, xpad=0, ypad=0):
        """
        Returns a LiveComposite that draws a colored stripe + dark body.
        NOT used directly in screens — the screens build this structure
        using screen-language vbox/frame stacks for layout flexibility.
        This function is here as a reference for any init python usage.
        """
        return Fixed(
            Frame(Solid(stripe_color), 0, 0),
            Frame(Solid(body_color), 0, stripe_h)
        )

################################################################################
## CHOICE SCREEN
## Changes from v1: left-aligned text, left accent bar, dimmed overlay,
## "Piliin mo ang iyong landas" header, wider hover background.
################################################################################
screen choice(items):
    zorder 150

    ## Subtle full-scene dim so choices read over bright backgrounds
    frame:
        xfill True
        yfill True
        background Solid("#0d111748")

    ## Choices column
    vbox:
        xalign 0.5
        yalign 0.73
        xsize 1100
        spacing 0

        ## Header label
        frame:
            xfill True
            ysize 38
            background Solid("#1f6feb18")
            padding (24, 0, 24, 0)
            hbox:
                yalign 0.5
                spacing 10
                frame:
                    xsize 3
                    ysize 22
                    yalign 0.5
                    background Solid("#1f6feb")
                text "PILIIN MO ANG IYONG LANDAS":
                    color "#58a6ff60"
                    size 20
                    yalign 0.5

        null height 8

        for i in items:
            button:
                action i.action
                xfill True
                ysize 0
                yminimum 88
                background Solid("#161b22EE")
                hover_background Solid("#1f6feb22")
                insensitive_background Solid("#0d111788")
                bottom_margin 6
                padding (0, 0, 0, 0)

                hbox:
                    xfill True
                    yminimum 88
                    spacing 0

                    ## Left accent bar
                    frame:
                        xsize 4
                        yminimum 88
                        background Solid("#1f6feb90")

                    ## Text content
                    frame:
                        xfill True
                        yminimum 88
                        background Solid("#00000000")
                        padding (22, 14, 22, 14)

                        text i.caption:
                            style "choice_caption_text"
                            yalign 0.5

style choice_caption_text:
    size 30
    color "#c9d1d9"
    hover_color "#79c0ff"
    insensitive_color "#8b949e"
    text_align 0.0
    layout "subtitle"

init python:
    if renpy.variant("small"):
        ## Mobile: wider and taller touch targets
        pass  ## vbox xsize is proportional; button yminimum handles height


################################################################################
## HUD — top stats bar (show_hud flag controls visibility)
## Changes from v1: cleaner grade display, better separator, tighter layout.
################################################################################
screen hud():
    zorder 5

    if show_hud:
        if renpy.variant("small"):
            ## ── Mobile HUD ───────────────────────────────────────────────────
            frame:
                xfill True
                ysize 96
                yalign 0.0
                background Solid("#0d1117EE")
                padding (12, 0, 12, 0)

                vbox:
                    xfill True
                    yalign 0.5
                    spacing 3

                    ## Row 1
                    hbox:
                        xfill True
                        yalign 0.5
                        spacing 0
                        text "[day_label]":
                            size 20
                            color "#8b949e"
                            xalign 0.0
                            yalign 0.5
                        null width True
                        hbox:
                            spacing 12
                            text "N [letter_grade(networking_grade)]":
                                size 20
                                color "#e3b341"
                            text "P [letter_grade(programming_grade)]":
                                size 20
                                color "#ff7b72"
                            text "C [letter_grade(cyber_grade)]":
                                size 20
                                color "#56d364"

                    ## Row 2 — CT + Motivation
                    hbox:
                        xfill True
                        yalign 0.5
                        spacing 14

                        ## CT segmented bar
                        hbox:
                            spacing 2
                            yalign 0.5
                            text "CT":
                                size 18
                                color "#8b949e"
                                yalign 0.5
                            null width 4
                            for i in range(10):
                                python:
                                    _filled = (critical_thinking // 10) > i
                                    if   i < 2: _sc = "#b91c1c" if _filled else "#21262d"
                                    elif i < 4: _sc = "#b45309" if _filled else "#21262d"
                                    elif i < 6: _sc = "#854d0e" if _filled else "#21262d"
                                    elif i < 8: _sc = "#166534" if _filled else "#21262d"
                                    else:       _sc = "#15803d" if _filled else "#21262d"
                                frame:
                                    xsize 22
                                    ysize 12
                                    yalign 0.5
                                    background Solid(_sc)

                        ## Motivation bar
                        hbox:
                            spacing 6
                            yalign 0.5
                            text "♥":
                                size 20
                                color "#f43f5e"
                                yalign 0.5
                            bar:
                                value motivation
                                range 100
                                xsize 100
                                ysize 12
                                yalign 0.5
                                left_bar Solid("#f43f5e")
                                right_bar Solid("#30363d")

        else:
            ## ── Desktop HUD ──────────────────────────────────────────────────
            frame:
                xfill True
                ysize 0
                yminimum 3
                yalign 0.0
                background Solid("#1f6feb")

            frame:
                xfill True
                ysize 80
                yalign 0.0
                yoffset 3
                background Solid("#0d1117F2")
                padding (30, 0, 30, 0)

                hbox:
                    xfill True
                    yalign 0.5
                    spacing 36

                    ## Day label
                    vbox:
                        yalign 0.5
                        xminimum 280
                        text "[day_label]":
                            size 24
                            color "#8b949e"

                    ## Blue separator
                    frame:
                        xsize 1
                        ysize 40
                        yalign 0.5
                        background Solid("#1f6feb40")

                    ## Subject grades
                    hbox:
                        yalign 0.5
                        spacing 20
                        text "NET  [letter_grade(networking_grade)]":
                            size 24
                            color "#e3b341"
                        text "PROG [letter_grade(programming_grade)]":
                            size 24
                            color "#ff7b72"
                        text "CYB  [letter_grade(cyber_grade)]":
                            size 24
                            color "#56d364"

                    ## Blue separator
                    frame:
                        xsize 1
                        ysize 40
                        yalign 0.5
                        background Solid("#1f6feb40")

                    ## CT segmented bar
                    vbox:
                        yalign 0.5
                        xminimum 300
                        spacing 5
                        text "Critical Thinking":
                            size 19
                            color "#8b949e"
                        hbox:
                            spacing 3
                            for i in range(10):
                                python:
                                    _filled = (critical_thinking // 10) > i
                                    if   i < 2: _sc = "#b91c1c" if _filled else "#30363d"
                                    elif i < 4: _sc = "#b45309" if _filled else "#30363d"
                                    elif i < 6: _sc = "#854d0e" if _filled else "#30363d"
                                    elif i < 8: _sc = "#166534" if _filled else "#30363d"
                                    else:       _sc = "#15803d" if _filled else "#30363d"
                                frame:
                                    xsize 24
                                    ysize 16
                                    background Solid(_sc)

                    ## Blue separator
                    frame:
                        xsize 1
                        ysize 40
                        yalign 0.5
                        background Solid("#1f6feb40")

                    ## Motivation
                    vbox:
                        yalign 0.5
                        xminimum 180
                        spacing 5
                        hbox:
                            spacing 6
                            text "♥":
                                size 22
                                color "#f43f5e"
                            text "Motivation":
                                size 19
                                color "#8b949e"
                        bar:
                            value motivation
                            range 100
                            xsize 160
                            ysize 16
                            left_bar Solid("#f43f5e")
                            right_bar Solid("#30363d")

init python:
    config.overlay_screens.append("hud")


################################################################################
## QUICK MENU — bottom navigation bar
## Changes from v1: mobile uses larger icons, desktop uses pill-style layout.
################################################################################
screen quick_menu():
    zorder 100

    if renpy.variant("small"):
        frame:
            xfill True
            ysize 110
            yalign 1.0
            background Solid("#161b22F2")

            ## Top edge line
            frame:
                xfill True
                ysize 1
                yalign 0.0
                background Solid("#1f6feb40")

            hbox:
                xalign 0.5
                yalign 0.5
                spacing 10

                for lbl, act in [
                    ("◀",    Rollback()),
                    ("Log",  ShowMenu('history')),
                    ("Skip", Skip()),
                    ("Auto", Preference("auto-forward","toggle")),
                    ("Menu", ShowMenu()),
                ]:
                    textbutton lbl:
                        action act
                        text_size 28
                        xsize 100
                        ysize 88
                        background Solid("#21262d")
                        hover_background Solid("#1f6feb")
                        text_xalign 0.5
                        text_yalign 0.5
                        text_color "#8b949e"
                        text_hover_color "#ffffff"

                ## AI Phone button — visually distinct
                textbutton "AI📱":
                    action Function(show_phone_ai)
                    text_size 26
                    xsize 120
                    ysize 88
                    background Solid("#1f6feb30")
                    hover_background Solid("#1f6feb")
                    text_xalign 0.5
                    text_yalign 0.5
                    text_color "#58a6ff"
                    text_hover_color "#ffffff"

    else:
        frame:
            xfill True
            ysize 68
            yalign 1.0
            background Solid("#161b22F0")

            ## Top accent line
            frame:
                xfill True
                ysize 1
                yalign 0.0
                background Solid("#1f6feb35")

            hbox:
                xalign 0.5
                yalign 0.5
                spacing 2

                ## Left cluster
                for lbl, act in [
                    ("Back",    Rollback()),
                    ("History", ShowMenu('history')),
                    ("Skip",    Skip()),
                    ("Auto",    Preference("auto-forward","toggle")),
                ]:
                    textbutton lbl:
                        action act
                        xsize 118
                        ysize 66
                        background Solid("#21262d")
                        hover_background Solid("#30363d")
                        text_size 24
                        text_xalign 0.5
                        text_yalign 0.5
                        text_color "#8b949e"
                        text_hover_color "#e6edf3"

                ## Browse Social Media — center pill
                frame:
                    xsize 300
                    ysize 66
                    yalign 0.5
                    background Solid("#1f6feb20")
                    padding (8, 0)
                    textbutton "Browse Social Media":
                        action Function(show_phone_ai)
                        xfill True
                        ysize 66
                        background Solid("#00000000")
                        hover_background Solid("#1f6feb18")
                        text_size 24
                        text_xalign 0.5
                        text_yalign 0.5
                        text_color "#58a6ff"
                        text_hover_color "#79c0ff"

                ## Right cluster
                for lbl, act in [
                    ("Save",  ShowMenu('save')),
                    ("Load",  ShowMenu('load')),
                    ("Prefs", ShowMenu('preferences')),
                    ("Menu",  ShowMenu()),
                ]:
                    textbutton lbl:
                        action act
                        xsize 108
                        ysize 66
                        background Solid("#21262d")
                        hover_background Solid("#30363d")
                        text_size 24
                        text_xalign 0.5
                        text_yalign 0.5
                        text_color "#8b949e"
                        text_hover_color "#e6edf3"


################################################################################
## PHONE AI OVERLAY
################################################################################
init python:
    def show_phone_ai():
        renpy.show_screen("phone_ai_overlay")

screen phone_ai_overlay():
    modal True
    zorder 200
    on "show" action Play("sound", "audio/sfx/sfx_phone.ogg")

    ## Background dim
    frame:
        xfill True
        yfill True
        background Solid("#0d111780")

    ## Modal card
    frame:
        xsize 700
        ysize 0
        yminimum 480
        xalign 0.5
        yalign 0.42
        background Solid("#0d1117")
        padding (0, 0, 0, 0)

        vbox:
            xfill True
            spacing 0

            ## Blue top stripe
            frame:
                xfill True
                ysize 3
                background Solid("#1f6feb")

            ## Header
            frame:
                xfill True
                background Solid("#161b22")
                padding (28, 16, 28, 16)
                vbox:
                    spacing 4
                    text "📱  [player_name]'s Phone":
                        size 30
                        color "#58a6ff"
                        bold True
                    text "AI App naka-bukas...":
                        size 22
                        color "#8b949e"

            ## Divider
            frame:
                xfill True
                ysize 1
                background Solid("#30363d")

            ## Buttons
            frame:
                xfill True
                background Solid("#0d1117")
                padding (28, 20, 28, 20)

                vbox:
                    xfill True
                    spacing 12

                    textbutton "Itanong sa AI ang sagot":
                        action [
                            Function(ct_change, -10),
                            Function(mot_change, -3),
                            Hide("phone_ai_overlay"),
                            Jump("ai_used_result")
                        ]
                        xfill True
                        ysize 80
                        background Solid("#1f6feb")
                        hover_background Solid("#388bfd")
                        text_color "#ffffff"
                        text_size 28
                        text_xalign 0.5
                        text_yalign 0.5

                    textbutton "Hindi na. Sariling utak na lang.":
                        action [
                            Function(ct_change, +5),
                            Hide("phone_ai_overlay")
                        ]
                        xfill True
                        ysize 80
                        background Solid("#21262d")
                        hover_background Solid("#30363d")
                        text_color "#7ee787"
                        text_hover_color "#56d364"
                        text_size 28
                        text_xalign 0.5
                        text_yalign 0.5

                    frame:
                        xfill True
                        background Solid("#161b2260")
                        padding (16, 10)
                        text "CT: [critical_thinking]/100  ·  AI uses: [ai_use_count]":
                            color "#8b949e"
                            size 22
                            xalign 0.5


################################################################################
## MAIN MENU
## Changes from v1: animated digital dust retained, better button polish.
################################################################################
## ATL transforms moved to game/transforms.rpy
## (title_pulse, menu_slide_in, digital_dust)

image digital_dust = SnowBlossom(
    Solid("#58a6ff", xysize=(3, 3)),
    count=60,
    border=50,
    xspeed=(-12, 12),
    yspeed=(-8, 20),
    start=2.5,
    fast=True
)

screen main_menu():
    tag menu
    style_prefix "main_menu"

    add Solid("#0d1117")
    add "digital_dust"

    ## Title block (right-aligned, pulsing)
    vbox at title_pulse:
        xalign 0.88
        yalign 0.22
        spacing 6
        text "A.I. NA LANG!":
            font "gui/fonts/Marmelad-Regular.ttf"
            size 100
            color "#ffffff"
            bold True
            outlines [(3, "#1f6feb", 0, 0)]
            xalign 1.0
        text "A Web-Based Interactive Visual Novel":
            size 26
            color "#c9d1d9"
            xalign 1.0
            outlines [(2, "#000000", 1, 1)]
        text "Mabalacat City College  ·  ICS 2026":
            size 20
            color "#8b949e"
            xalign 1.0

    ## Navigation buttons
    vbox:
        xalign if renpy.variant("small") then 0.5 else 0.88
        yalign if renpy.variant("small") then 0.72 else 0.58
        spacing 14

        textbutton "Simulan"       action Start()                 at menu_slide_in(0.10)
        textbutton "Ipagpatuloy"   action ShowMenu("load")        at menu_slide_in(0.20)
        textbutton "Mga Setting"   action ShowMenu("preferences") at menu_slide_in(0.30)
        textbutton "Credits"       action ShowMenu("about")       at menu_slide_in(0.40)

        if not renpy.variant("web"):
            textbutton "Umalis" action Quit(confirm=not main_menu) at menu_slide_in(0.50)

    text "[config.name!t]  v[config.version]":
        xalign 0.98
        yalign 0.98
        size 20
        color "#ffffff60"

style main_menu_button:
    xsize 340
    ysize 72
    xalign 1.0
    background Solid("#161b22CC")
    hover_background Solid("#1f6feb")
    padding (14, 10)

style main_menu_button_text:
    size 36
    xalign 0.5
    yalign 0.5
    color "#e6edf3"
    hover_color "#ffffff"
    bold True


################################################################################
## CHAPTER TITLE CARD
## Changes from v1: animated entry (title_enter / subtitle_enter ATL),
## scanline decoration, chapter number badge.
################################################################################
screen chapter_title(chapter_num, chapter_name, subtitle):
    zorder 150
    on "show" action Play("sound", "audio/sfx/sfx_page_turn.ogg")

    frame:
        xfill True
        yfill True
        background Solid("#0d1117FC")

        ## Center content
        vbox:
            xalign 0.5
            yalign 0.44
            spacing 14

            ## Chapter number badge
            frame at title_enter:
                xalign 0.5
                background Solid("#1f6feb")
                padding (20, 6)
                text "CHAPTER [chapter_num]":
                    size 22
                    color "#ffffff"
                    xalign 0.5
                    bold True
                    letter_spacing 3

            ## Chapter name
            text "[chapter_name]" at title_enter:
                size 56
                color "#f0f6fc"
                xalign 0.5
                bold True
                outlines [(2, "#1f6feb20", 0, 2)]

            ## Decorative divider
            frame at subtitle_enter:
                xalign 0.5
                xsize 420
                ysize 1
                background Solid("#1f6feb50")

            ## Subtitle / week label
            text "[subtitle]" at subtitle_enter:
                size 28
                color "#58a6ff"
                xalign 0.5
                italic True

        ## Continue hint
        text "[ i-tap o pindutin ang Space para magpatuloy ]":
            xalign 0.5
            yalign 0.92
            size 24
            color "#8b949e60"

    key "K_RETURN" action Return()
    key "K_SPACE"  action Return()
    button:
        xfill True
        yfill True
        action Return()
        background None


################################################################################
## MINIGAME SCREEN
## Function signature MUST remain identical.
## Changes from v1: better header, cleaner option buttons, fixed viewport issue.
################################################################################
screen minigame(title, question, options, correct_idx, subject,
                ct_reward=8, grade_reward=10,
                correct_label="minigame_correct",
                wrong_label="minigame_wrong"):
    modal True
    zorder 180

    ## Full-screen backdrop
    frame:
        xfill True
        yfill True
        background Solid("#0d1117F4")

    ## Content card
    frame:
        xsize 1380
        yminimum 600
        ymaximum 900
        xalign 0.5
        yalign 0.48
        background Solid("#161b22")
        padding (0, 0)

        vbox:
            xfill True
            spacing 0

            ## ── Blue top stripe ───────────────────────────────────────────
            frame:
                xfill True
                ysize 3
                background Solid("#1f6feb")

            ## ── Header bar ────────────────────────────────────────────────
            frame:
                xfill True
                background Solid("#0d1117")
                padding (24, 14, 24, 14)
                hbox:
                    xfill True
                    yalign 0.5
                    spacing 0
                    text "[title]":
                        size 28
                        color "#58a6ff"
                        bold True
                        yalign 0.5
                    null width True
                    frame:
                        background Solid("#1f6feb20")
                        padding (14, 6)
                        text "CT: [critical_thinking] / 100":
                            size 24
                            color "#8b949e"
                            yalign 0.5

            ## ── Question block ────────────────────────────────────────────
            frame:
                xfill True
                background Solid("#161b22")
                padding (24, 18, 24, 18)
                text "[question]":
                    size 29
                    color "#c9d1d9"
                    line_leading 6

            ## ── Divider ───────────────────────────────────────────────────
            frame:
                xfill True
                ysize 1
                background Solid("#30363d")

            ## ── Answer options ────────────────────────────────────────────
            frame:
                xfill True
                background Solid("#0d1117")
                padding (20, 14, 20, 10)

                vbox:
                    xfill True
                    spacing 8

                    $ __correct = correct_idx
                    for idx in range(len(options)):
                        python:
                            _opt       = options[idx]
                            _is_right  = (idx == __correct)
                            _jump_lbl  = correct_label if _is_right else wrong_label
                            _ct_delta  = ct_reward if _is_right else -5
                            _gr_delta  = grade_reward if _is_right else -5

                        button:
                            action [
                                Function(ct_change,    _ct_delta),
                                Function(grade_change, subject, _gr_delta),
                                Hide("minigame"),
                                Jump(_jump_lbl)
                            ]
                            xfill True
                            yminimum 70
                            background Solid("#161b22")
                            hover_background Solid("#1f6feb1A")
                            padding (0, 0)

                            hbox:
                                xfill True
                                yminimum 70
                                spacing 0
                                frame:
                                    xsize 4
                                    yminimum 70
                                    background Solid("#30363d")
                                frame:
                                    xfill True
                                    yminimum 70
                                    background Solid("#00000000")
                                    padding (18, 12)
                                    text _opt:
                                        size 27
                                        color "#c9d1d9"
                                        hover_color "#79c0ff"
                                        yalign 0.5
                                        layout "subtitle"

            ## ── AI shortcut footer ────────────────────────────────────────
            frame:
                xfill True
                background Solid("#1f6feb0C")
                padding (20, 12, 20, 12)

                hbox:
                    xfill True
                    yalign 0.5
                    spacing 16

                    vbox:
                        yalign 0.5
                        text "Itanong sa AI":
                            size 26
                            color "#58a6ff"
                            bold True
                        text "CT −10  ·  Grade +" + str(grade_reward) + "  (walang naiintindihan)":
                            size 20
                            color "#8b949e"

                    null width True

                    textbutton "Gamitin":
                        action [
                            Function(use_ai, subject, grade_reward),
                            Hide("minigame"),
                            Jump("ai_used_result")
                        ]
                        xsize 140
                        ysize 56
                        background Solid("#1f6feb")
                        hover_background Solid("#388bfd")
                        text_color "#fff"
                        text_size 26
                        text_xalign 0.5
                        text_yalign 0.5


################################################################################
## GRADE RESULTS SCREEN
################################################################################
screen grade_results():
    modal True
    zorder 170

    frame:
        xfill True
        yfill True
        background Solid("#0d111780")

    frame:
        xsize 900
        yminimum 560
        xalign 0.5
        yalign 0.45
        background Solid("#161b22")
        padding (0, 0)

        vbox:
            xfill True
            spacing 0

            frame:
                xfill True
                ysize 3
                background Solid("#1f6feb")

            frame:
                xfill True
                background Solid("#0d1117")
                padding (36, 24, 36, 24)

                vbox:
                    xfill True
                    spacing 24

                    text "RESULTA NG GRADES":
                        size 36
                        color "#58a6ff"
                        xalign 0.5
                        bold True
                        letter_spacing 2

                    frame:
                        xfill True
                        ysize 1
                        background Solid("#30363d")

                    hbox:
                        xalign 0.5
                        spacing 50

                        for subj, grade_var, col in [
                            ("Networking",    "networking_grade",   "#e3b341"),
                            ("Programming",   "programming_grade",  "#ff7b72"),
                            ("Cybersecurity", "cyber_grade",        "#56d364"),
                        ]:
                            vbox:
                                spacing 8
                                text subj:
                                    size 24
                                    color col
                                    xalign 0.5
                                text "[letter_grade([grade_var])]":
                                    size 48
                                    color "#f0f6fc"
                                    xalign 0.5
                                    bold True

                    frame:
                        xfill True
                        ysize 1
                        background Solid("#30363d")

                    hbox:
                        xalign 0.5
                        spacing 40
                        text "CT: [critical_thinking]/100":
                            size 24
                            color "#8b949e"
                        text "Mot: [motivation]/100":
                            size 24
                            color "#f43f5e"
                        text "AI: [ai_use_count]x":
                            size 24
                            color "#58a6ff"

                    textbutton "Magpatuloy":
                        action Hide("grade_results")
                        xalign 0.5
                        xsize 280
                        ysize 66
                        background Solid("#1f6feb")
                        hover_background Solid("#388bfd")
                        text_color "#fff"
                        text_size 28
                        text_xalign 0.5
                        text_yalign 0.5


################################################################################
## SAY SCREEN (DIALOGUE BOX)
## Changes from v1: blue top stripe, name badge with background,
## better readable layout, narrator uses narrower italic style.
################################################################################
screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        xfill True
        yalign 1.0
        background Solid("#00000000")
        padding (0, 0)
        yminimum 230

        vbox:
            xfill True
            spacing 0

            ## ── 3px blue accent stripe ─────────────────────────────────────
            frame:
                xfill True
                ysize 3
                background Solid("#1f6feb")

            ## ── Name badge (hidden when narrator speaks) ───────────────────
            if who:
                frame:
                    xfill True
                    background Solid("#161b22F8")
                    padding (30, 0, 30, 0)
                    ysize 48
                    hbox:
                        yalign 0.5
                        spacing 10
                        ## Small colour dot matching character colour
                        ## (We can't read the Character's color dynamically here,
                        ##  so just use the accent blue as a universal badge dot.)
                        frame:
                            xsize 6
                            ysize 22
                            yalign 0.5
                            background Solid("#1f6feb")
                        text who:
                            id "who"
                            size 30
                            bold True
                            yalign 0.5

            ## ── Dialogue text area ────────────────────────────────────────
            frame:
                xfill True
                yfill True
                background Solid("#0d1117F0")
                padding (30, 14, 30, 16)
                yminimum 160

                text what:
                    id "what"
                    size 30
                    color "#e6edf3"
                    line_leading 5

style say_window:
    xfill True

style say_label:
    color "#58a6ff"
    size 30
    bold True

style say_dialogue:
    size 30
    color "#e6edf3"
    line_leading 5


################################################################################
## GAME MENU SHELL (save/load/prefs/about/return)
################################################################################
screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    tag menu

    frame:
        xfill True
        yfill True
        background Solid("#0d1117F4")

        vbox:
            xfill True
            yfill True
            spacing 0

            ## Header
            frame:
                xfill True
                ysize 3
                background Solid("#1f6feb")

            frame:
                xfill True
                ysize 82
                background Solid("#161b22")
                padding (30, 0)
                hbox:
                    xfill True
                    yalign 0.5
                    spacing 20
                    text title:
                        size 34
                        color "#f0f6fc"
                        bold True
                        yalign 0.5
                    null width True
                    textbutton "Bumalik":
                        action Return()
                        yalign 0.5
                        xsize 180
                        ysize 60
                        background Solid("#21262d")
                        hover_background Solid("#1f6feb")
                        text_color "#e6edf3"
                        text_hover_color "#fff"
                        text_size 26
                        text_xalign 0.5
                        text_yalign 0.5

            if scroll == "viewport":
                viewport:
                    id "viewport"
                    xfill True
                    yfill True
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    transclude

            elif scroll == "vpgrid":
                vpgrid:
                    id "viewport"
                    cols 1
                    xfill True
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    transclude

            else:
                transclude

style game_menu_frame:
    background Solid("#0d1117F4")


################################################################################
## SAVE / LOAD
################################################################################
screen save():
    tag menu
    use game_menu("I-save", scroll="vpgrid"):
        use slot_grid(True)

screen load():
    tag menu
    use game_menu("Mag-load", scroll="vpgrid"):
        use slot_grid(False)

screen slot_grid(saving):
    style_prefix "slot"
    $ _SLOTS_PER_PAGE = 10

    for page in ["auto", "quick"] + [str(i) for i in range(1, 9)]:
        vbox:
            xfill True
            spacing 0

            frame:
                xfill True
                ysize 44
                background Solid("#161b22")
                padding (20, 0)
                text (
                    "Auto" if page == "auto" else
                    "Quick" if page == "quick" else
                    "Page " + page
                ):
                    size 24
                    color "#8b949e"
                    yalign 0.5

            python:
                if page in ("auto", "quick"):
                    _slot_list = [page + "-1"]
                else:
                    _slot_list = [
                        "{}-{}".format(page, i)
                        for i in range(1, _SLOTS_PER_PAGE + 1)
                    ]

            for _slot_name in _slot_list:
                python:
                    _exists   = renpy.can_load(_slot_name)
                    _time_str = ""
                    if _exists:
                        try:
                            import datetime
                            _mt = renpy.slot_mtime(_slot_name)
                            if _mt:
                                _time_str = datetime.datetime.fromtimestamp(
                                    _mt).strftime("%b %d  %H:%M")
                        except Exception:
                            _time_str = ""
                    if saving:
                        _slot_action = FileSave(_slot_name, confirm=True)
                    elif _exists:
                        _slot_action = FileLoad(_slot_name)
                    else:
                        _slot_action = NullAction()

                button:
                    action _slot_action
                    xfill True
                    ysize 100
                    background Solid("#161b22")
                    hover_background Solid("#21262d")
                    padding (18, 8)

                    hbox:
                        spacing 18
                        yalign 0.5
                        frame:
                            xsize 130
                            ysize 74
                            background Solid("#21262d")
                            text ("📁" if _exists else "—"):
                                size 28
                                color "#30363d"
                                xalign 0.5
                                yalign 0.5
                        vbox:
                            yalign 0.5
                            spacing 4
                            if _exists:
                                text _slot_name:
                                    size 24
                                    color "#e6edf3"
                                text _time_str:
                                    size 20
                                    color "#8b949e"
                            else:
                                text "— walang naka-save —":
                                    size 24
                                    color "#30363d"


################################################################################
## PREFERENCES SCREEN
################################################################################
screen preferences():
    tag menu
    use game_menu("Mga Setting", scroll="viewport"):
        vbox:
            xfill True
            spacing 28
            xalign 0.5
            xmaximum 820

            if not renpy.variant("web") and not renpy.variant("small"):
                use pref_section("Display"):
                    hbox:
                        spacing 10
                        textbutton "Fullscreen":
                            action Preference("display", "fullscreen")
                            xsize 220
                            ysize 66
                            background Solid("#21262d")
                            hover_background Solid("#1f6feb")
                            text_color "#e6edf3"
                            text_hover_color "#fff"
                            text_size 26
                            text_xalign 0.5
                            text_yalign 0.5
                        textbutton "Window":
                            action Preference("display", "window")
                            xsize 220
                            ysize 66
                            background Solid("#21262d")
                            hover_background Solid("#1f6feb")
                            text_color "#e6edf3"
                            text_hover_color "#fff"
                            text_size 26
                            text_xalign 0.5
                            text_yalign 0.5

            use pref_section("Bilis ng Teksto"):
                bar:
                    value Preference("text speed")
                    xfill True
                    ysize 44
                    left_bar Solid("#1f6feb")
                    right_bar Solid("#30363d")

            use pref_section("Auto-Forward"):
                bar:
                    value Preference("auto-forward time")
                    xfill True
                    ysize 44
                    left_bar Solid("#1f6feb")
                    right_bar Solid("#30363d")

            use pref_section("Musika"):
                bar:
                    value Preference("music volume")
                    xfill True
                    ysize 44
                    left_bar Solid("#56d364")
                    right_bar Solid("#30363d")

            use pref_section("Tunog"):
                bar:
                    value Preference("sound volume")
                    xfill True
                    ysize 44
                    left_bar Solid("#e3b341")
                    right_bar Solid("#30363d")

            use pref_section("Boses"):
                bar:
                    value Preference("voice volume")
                    xfill True
                    ysize 44
                    left_bar Solid("#ff7b72")
                    right_bar Solid("#30363d")

screen pref_section(label):
    vbox:
        spacing 10
        xfill True
        frame:
            xfill True
            ysize 1
            background Solid("#30363d")
        text label:
            size 26
            color "#8b949e"
        transclude


################################################################################
## INPUT
################################################################################
screen input(prompt):
    style_prefix "input"
    frame:
        xfill True
        yfill True
        background Solid("#0d111790")
        frame:
            xalign 0.5
            yalign 0.5
            background Solid("#161b22")
            padding (50, 40)
            vbox:
                xalign 0.5
                spacing 20
                text prompt:
                    xalign 0.5
                    size 36
                    color "#e6edf3"
                frame:
                    xfill True
                    ysize 1
                    background Solid("#1f6feb")
                input id "input":
                    xalign 0.5
                    size 36
                    color "#79c0ff"


################################################################################
## HISTORY
################################################################################
screen history():
    tag menu
    use game_menu("Kasaysayan", scroll="viewport"):
        vbox:
            xfill True
            spacing 4

            python:
                _hist = list(reversed(_history_list)) if _history_list else []

            if not _hist:
                text "Walang kasaysayan pa.":
                    size 28
                    color "#8b949e"
                    xalign 0.5

            for h in _hist:
                python:
                    _who_text  = h.who  if h.who  else None
                    _what_text = h.what if h.what else ""
                frame:
                    xfill True
                    background Solid("#161b22")
                    padding (20, 12)
                    bottom_margin 4
                    vbox:
                        spacing 6
                        if _who_text:
                            text _who_text:
                                size 24
                                color "#58a6ff"
                                bold True
                        text _what_text:
                            size 26
                            color "#c9d1d9"


################################################################################
## ABOUT / CREDITS
################################################################################
screen about():
    tag menu
    use game_menu("Credits", scroll="viewport"):
        vbox:
            xalign 0.5
            spacing 18
            xmaximum 720

            text "[config.name!t]":
                size 40
                color "#f0f6fc"
                bold True
                xalign 0.5
            text "Bersyon [config.version]":
                size 26
                color "#8b949e"
                xalign 0.5

            frame:
                xfill True
                ysize 1
                background Solid("#1f6feb40")

            null height 8
            text "Ginawa ng Team:":
                size 28
                color "#58a6ff"
                xalign 0.5
            for name in [
                "Cecilio, Neil Ayangel C.",
                "Clarin, Kylle Benedict",
                "Morgan, Christian David F.",
            ]:
                text name:
                    size 26
                    color "#c9d1d9"
                    xalign 0.5

            frame:
                xfill True
                ysize 1
                background Solid("#30363d")

            text "Technical Adviser: Ernie Lee Pineda":
                size 24
                color "#8b949e"
                xalign 0.5
            null height 6
            text "Mabalacat City College":
                size 24
                color "#8b949e"
                xalign 0.5
            text "Institute of Computing Studies, 2026":
                size 22
                color "#8b949e"
                xalign 0.5


################################################################################
## CONFIRM DIALOG
################################################################################
screen confirm(message, yes_action, no_action=Return()):
    modal True
    zorder 300

    frame:
        xfill True
        yfill True
        background Solid("#0d111780")

    frame:
        xsize 640
        xalign 0.5
        yalign 0.45
        background Solid("#161b22")
        padding (0, 0)

        vbox:
            xfill True
            spacing 0

            frame:
                xfill True
                ysize 3
                background Solid("#e3b341")

            frame:
                xfill True
                background Solid("#0d1117")
                padding (36, 28)

                vbox:
                    xfill True
                    spacing 28

                    text message:
                        size 28
                        color "#e6edf3"
                        xalign 0.5
                        text_align 0.5

                    hbox:
                        xalign 0.5
                        spacing 20

                        textbutton "Oo":
                            action yes_action
                            xsize 200
                            ysize 68
                            background Solid("#b91c1c")
                            hover_background Solid("#dc2626")
                            text_color "#fff"
                            text_size 28
                            text_xalign 0.5
                            text_yalign 0.5

                        textbutton "Hindi":
                            action no_action
                            xsize 200
                            ysize 68
                            background Solid("#21262d")
                            hover_background Solid("#30363d")
                            text_color "#e6edf3"
                            text_size 28
                            text_xalign 0.5
                            text_yalign 0.5


################################################################################
## NOTIFY
################################################################################
screen notify(message):
    zorder 250
    frame:
        xalign 0.5
        yalign 0.07
        background Solid("#161b22EE")
        padding (20, 12)
        hbox:
            spacing 10
            frame:
                xsize 3
                ysize 28
                yalign 0.5
                background Solid("#1f6feb")
            text message:
                size 26
                color "#58a6ff"
    timer 3.0 action Hide("notify")


################################################################################
## SKIP INDICATOR
################################################################################
screen skip_indicator():
    zorder 100
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -10
        yoffset 86
        background Solid("#161b22CC")
        padding (14, 8)
        text ">> Nilalaktawan...":
            size 22
            color "#8b949e"


################################################################################
## GLOBAL BUTTON SOUND
################################################################################
style button:
    activate_sound "audio/sfx/sfx_click.ogg"


################################################################################
## SHARED GAME LABELS (keep here, remove duplicates from script.rpy)
################################################################################

label ai_used_result:
    play sound "audio/sfx/sfx_phone.ogg"
    narrator "Pinindot mo ang AI app."
    ai_voice "Output generated. Syntax and logical structures have been optimized."
    narrator "Copy. {w=0.4}Paste. {w=0.4}Submit."
    narrator "Tapos ka na. Sa loob ng tatlong minuto."
    narrator "(Wala kang maintindihan kahit isang linya nito.)"
    $ renpy.notify("CT −10  ·  AI use #" + str(ai_use_count))
    return

label minigame_correct:
    play sound "audio/sfx/sfx_correct.ogg"
    $ renpy.notify("✓  Tama!  CT +" + str(8))
    return

label minigame_wrong:
    play sound "audio/sfx/sfx_wrong.ogg"
    $ renpy.notify("✗  Mali.  CT −5")
    return

## ── END OF screens.rpy ──────────────────────────────────────────────────────
