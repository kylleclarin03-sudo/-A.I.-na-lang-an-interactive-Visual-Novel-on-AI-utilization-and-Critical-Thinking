## game/screens.rpy
## All screen definitions for A.I. na lang!

################################################################################
## HUD, Persistent top bar shown during gameplay
################################################################################
screen hud():
    zorder 5
    style_prefix "hud"

    frame:
        xfill True
        ysize 90
        xalign 0.5
        yalign 0.0
        yoffset 0
        padding (30, 0)
        background Solid("#0d1117E0")
        hbox:
            xfill True
            yalign 0.5
            spacing 40

            ## Day / Time label
            vbox:
                yalign 0.5
                text "[day_label]" size 26 color "#8b949e"

            ## Grade display
            vbox:
                yalign 0.5
                hbox:
                    spacing 8
                    text "N:[letter_grade(networking_grade)]"  size 26 color "#e3b341"
                    text "P:[letter_grade(programming_grade)]" size 26 color "#ff7b72"
                    text "C:[letter_grade(cyber_grade)]"       size 26 color "#56d364"

            ## Critical Thinking Meter, segmented color zones
            vbox:
                yalign 0.5
                xminimum 500
                text "Critical Thinking" size 22 color "#8b949e" yoffset -4
                hbox:
                    spacing 3
                    for i in range(10):
                        python:
                            filled = (critical_thinking // 10) > i
                            if i < 2:
                                seg_color = "#b91c1c" if filled else "#30363d"
                            elif i < 4:
                                seg_color = "#b45309" if filled else "#30363d"
                            elif i < 6:
                                seg_color = "#854d0e" if filled else "#30363d"
                            elif i < 8:
                                seg_color = "#166534" if filled else "#30363d"
                            else:
                                seg_color = "#15803d" if filled else "#30363d"
                        frame:
                            xsize 46
                            ysize 18
                            background Solid(seg_color)

            ## Motivation, heart icon + bar
            vbox:
                yalign 0.5
                xminimum 220
                hbox:
                    spacing 8
                    text "♥" size 26 color "#f43f5e"
                    text "Motivation" size 22 color "#8b949e"
                bar:
                    value motivation
                    range 100
                    xsize 180
                    ysize 18
                    left_bar  Solid("#f43f5e")
                    right_bar Solid("#30363d")

## Attach HUD to the overlay layer so it persists across scenes.
init python:
    config.overlay_screens.append("hud")

################################################################################
## QUICK MENU, Bottom navigation bar
################################################################################
screen quick_menu():
    zorder 100
    style_prefix "quick"

    if renpy.variant("small"):
        frame:
            xfill True
            ysize 110
            yalign 1.0
            background Solid("#161b22E8")
            hbox:
                xalign 0.5
                yalign 0.5
                spacing 30
                textbutton _("Back")    action Rollback()                              text_size 34
                textbutton _("History") action ShowMenu('history')                     text_size 34
                textbutton _("Skip")    action Skip()                                  text_size 34
                textbutton _("Auto")    action Preference("auto-forward", "toggle")    text_size 34
                textbutton _("AI")      action Function(show_phone_ai)                 text_size 34 text_color "#58a6ff"
                textbutton _("Menu")    action ShowMenu()                              text_size 34
    else:
        frame:
            xfill True
            ysize 72
            yalign 1.0
            background Solid("#161b22E8")
            hbox:
                xalign 0.5
                yalign 0.5
                spacing 0

                hbox:
                    style_prefix "qbtn"
                    spacing 0
                    textbutton _("Back")    action Rollback()
                    textbutton _("History") action ShowMenu('history')
                    textbutton _("Skip")    action Skip()
                    textbutton _("Auto")    action Preference("auto-forward", "toggle")

                frame:
                    xsize 360
                    background Solid("#1f6feb30")
                    padding (10, 10)
                    textbutton _("Browse Social Media"):
                        action Function(show_phone_ai)
                        text_color "#58a6ff"
                        text_hover_color "#79c0ff"
                        text_size 28
                        xalign 0.5
                        yalign 0.5

                hbox:
                    style_prefix "qbtn"
                    spacing 0
                    textbutton _("Save")  action ShowMenu('save')
                    textbutton _("Load")  action ShowMenu('load')
                    textbutton _("Prefs") action ShowMenu('preferences')

style qbtn_button:
    xsize 130
    ysize 70
    background Solid("#21262D")
    hover_background Solid("#1f6feb")
    padding (8, 8)

style qbtn_button_text:
    size 26
    xalign 0.5
    yalign 0.5
    color "#8b949e"
    hover_color "#ffffff"

################################################################################
## PHONE AI OVERLAY, "Browse Social Media" / Ask AI mini-popup
################################################################################
init python:
    def show_phone_ai():
        renpy.show_screen("phone_ai_overlay")

screen phone_ai_overlay():
    modal True
    zorder 200

    frame:
        xsize 680
        ysize 480
        xalign 0.5
        yalign 0.4
        background Solid("#0d1117F0")
        padding (30, 30)

        vbox:
            spacing 20
            text "Phone ni [player_name]" size 34 color "#58a6ff" xalign 0.5
            text "Naka-open ang AI app..." size 28 color "#8b949e" xalign 0.5
            null height 10

            textbutton _("Itanong sa AI ang sagot"):
                action [
                    Function(ct_change, -10),
                    Function(mot_change, -3),
                    Hide("phone_ai_overlay"),
                    Jump("ai_used_result")
                ]
                xfill True
                ysize 80
                background Solid("#1f6feb")
                text_color "#ffffff"
                text_size 30
                text_xalign 0.5
                text_yalign 0.5

            textbutton _("Hindi na. Sariling utak na lang."):
                action [
                    Function(ct_change, +5),
                    Hide("phone_ai_overlay")
                ]
                xfill True
                ysize 80
                background Solid("#21262d")
                text_color "#7ee787"
                text_size 30
                text_xalign 0.5
                text_yalign 0.5

            text "CT: [critical_thinking]/100  |  AI uses: [ai_use_count]" size 24 color "#8b949e" xalign 0.5

################################################################################
## MAIN MENU
################################################################################
screen main_menu():
    tag menu
    style_prefix "main_menu"

    add gui.main_menu_background

    vbox:
        xalign 0.90
        yalign 0.60
        spacing 25

        textbutton _("Simulan")      action Start()
        textbutton _("Ipagpatuloy")  action ShowMenu("load")
        textbutton _("Mga Setting")  action ShowMenu("preferences")
        textbutton _("Credits")      action ShowMenu("about")

        ## Hide Quit on web, browsers block tab-close via JS.
        if not renpy.variant("web"):
            textbutton _("Umalis") action Quit(confirm=not main_menu)

    text "[config.name!t]  v[config.version]" xalign 0.98 yalign 0.98 size 22 color "#ffffff80"

style main_menu_button:
    xsize 350
    ysize 75
    xalign 1.0
    background Solid("#161b22E6")
    hover_background Solid("#1f6feb")
    padding (10, 10)

style main_menu_button_text:
    size 38
    xalign 0.5
    yalign 0.5
    color "#e6edf3"
    hover_color "#ffffff"

################################################################################
## CHAPTER TITLE CARD
################################################################################
screen chapter_title(chapter_num, chapter_name, subtitle):
    zorder 150

    frame:
        xfill True
        yfill True
        background Solid("#0d1117F8")

        vbox:
            xalign 0.5
            yalign 0.45
            spacing 18

            text "CHAPTER [chapter_num]" size 28 color "#8b949e" xalign 0.5
            text "[chapter_name]"        size 58 color "#f0f6fc" xalign 0.5 bold True
            text "[subtitle]"            size 30 color "#58a6ff" xalign 0.5 italic True

        text "[ i-tap o pindutin ang Space para magpatuloy ]" xalign 0.5 yalign 0.92 size 26 color "#8b949e"

    key "K_RETURN" action Hide("chapter_title")
    key "K_SPACE"  action Hide("chapter_title")
    button:
        xfill True
        yfill True
        action Hide("chapter_title")
        background None

################################################################################
## MINIGAME SCREEN, Used for all three subject minigames
################################################################################
screen minigame(title, question, options, correct_idx, subject, ct_reward=8, grade_reward=10, correct_label="minigame_correct", wrong_label="minigame_wrong"):
    modal True
    zorder 180

    frame:
        xsize 1400
        ysize 820
        xalign 0.5
        yalign 0.45
        background Solid("#0d1117F0")
        padding (36, 36)

        vbox:
            spacing 18

            ## Header
            frame:
                xfill True
                ysize 60
                background Solid("#161b22")
                padding (16, 0)
                hbox:
                    yalign 0.5
                    spacing 30
                    text title size 30 color "#58a6ff"
                    null width 30
                    text "CT: [critical_thinking] / 100" size 26 color "#8b949e" yalign 0.5

            ## Question
            frame:
                xfill True
                background Solid("#161b22")
                padding (16, 16)
                text question size 30 color "#c9d1d9"

            ## Answer buttons
            $ __minigame_correct = correct_idx
            for idx in range(len(options)):
                python:
                    _opt = options[idx]
                    _is_correct = (idx == __minigame_correct)
                    if _is_correct:
                        _jump = Jump(correct_label)
                    else:
                        _jump = Jump(wrong_label)
                textbutton _opt:
                    action [
                        Function(ct_change, ct_reward if _is_correct else -5),
                        Function(grade_change, subject, grade_reward if _is_correct else -5),
                        Hide("minigame"),
                        _jump
                    ]
                    xfill True
                    ysize 80
                    background Solid("#21262d")
                    hover_background Solid("#1f6feb40")
                    padding (16, 8)
                    text_color "#e6edf3"
                    text_hover_color "#79c0ff"
                    text_size 28
                    text_xalign 0.0
                    text_yalign 0.5

            ## AI corner option
            frame:
                xfill True
                background Solid("#1f6feb15")
                padding (12, 12)
                hbox:
                    spacing 16
                    vbox:
                        yalign 0.5
                        text "Itanong sa AI" size 28 color "#58a6ff" bold True
                        text "CT −10  |  Grade +" + str(grade_reward) + "  (pero walang naiintindihan)" size 22 color "#8b949e"
                    null width True
                    textbutton _("Gamitin"):
                        action [
                            Function(use_ai, subject, grade_reward),
                            Hide("minigame"),
                            Jump("ai_used_result")
                        ]
                        background Solid("#1f6feb")
                        hover_background Solid("#388bfd")
                        ysize 60
                        xsize 160
                        text_color "#fff"
                        text_size 28
                        text_xalign 0.5
                        text_yalign 0.5

################################################################################
## GRADE RESULTS SCREEN
################################################################################
screen grade_results():
    modal True
    zorder 170

    frame:
        xsize 900
        ysize 600
        xalign 0.5
        yalign 0.45
        background Solid("#0d1117F5")
        padding (40, 40)

        vbox:
            spacing 24
            text "RESULTA NG GRADES" size 38 color "#58a6ff" xalign 0.5 bold True
            null height 10

            hbox:
                xalign 0.5
                spacing 60
                vbox:
                    spacing 10
                    text "Networking"   size 28 color "#e3b341" xalign 0.5
                    text "[networking_grade]  ([letter_grade(networking_grade)])" size 34 color "#f0f6fc" xalign 0.5 bold True
                vbox:
                    spacing 10
                    text "Programming"  size 28 color "#ff7b72" xalign 0.5
                    text "[programming_grade]  ([letter_grade(programming_grade)])" size 34 color "#f0f6fc" xalign 0.5 bold True
                vbox:
                    spacing 10
                    text "Cybersecurity" size 28 color "#56d364" xalign 0.5
                    text "[cyber_grade]  ([letter_grade(cyber_grade)])" size 34 color "#f0f6fc" xalign 0.5 bold True

            null height 10
            text "Critical Thinking: [critical_thinking]/100" size 26 color "#8b949e" xalign 0.5
            text "Motivation: [motivation]/100"               size 26 color "#8b949e" xalign 0.5
            text "AI Uses: [ai_use_count]"                   size 26 color "#8b949e" xalign 0.5

            null height 10
            textbutton _("Magpatuloy"):
                action Hide("grade_results")
                xalign 0.5
                xsize 300
                ysize 70
                background Solid("#1f6feb")
                text_color "#fff"
                text_size 30
                text_xalign 0.5
                text_yalign 0.5
