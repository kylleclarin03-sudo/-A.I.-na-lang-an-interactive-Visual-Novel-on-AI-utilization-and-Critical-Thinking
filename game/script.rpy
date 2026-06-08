## game/script.rpy
## Entry point, init, and Prologue sequence for A.I. na lang!

label start:
    $ safe_play("music", "audio/bgm/bgm_menu.ogg", loop=True)
    call prologue from _call_prologue
    call chapter1  from _call_chapter1
    call chapter2  from _call_chapter2
    call chapter3  from _call_chapter3
    call chapter4  from _call_chapter4
    call chapter5  from _call_chapter5
    call chapter6  from _call_chapter6
    call chapter7  from _call_chapter7
    call chapter8  from _call_chapter8
    call ending_sequence from _call_ending
    return

# ─────────────────────────────────────────────────────────────────────────────
# PROLOGUE
# ─────────────────────────────────────────────────────────────────────────────
label prologue:
    hide screen hud
    scene black with fade
    $ safe_stop("music")
    $ safe_play("music", "audio/bgm/bgm_sad.ogg", loop=True)

    narrator "Mayroon kang naaalala."
    pause 1.0
    narrator "Hindi ito isang masayang alaala."
    pause 0.8
    narrator "Pero kasama ka nito hanggang ngayon."

    scene bg_bedroom with dissolve
    narrator "Noong panahon ng virus, ang school mo ay naging isang laptop at apat na pader."
    narrator "Ang graduation mo ay Zoom call. Ang Senior Prom mo ay filter sa mukha mo."
    narrator "At doon, sa loob ng lahat ng isolation na 'yon — may dumating."

    narrator "Hindi ito nagtatanong kung kumusta ka. Hindi ito nagkakancel ng plano."
    narrator "Nandoon lang ito. At kaya nitong gawin ang lahat."
    narrator "Mga assignments: tapos na. Mga report: tapos na."
    narrator "Mga sanaysay na mas magaling pa sa lahat ng magsusulat ka ng 2AM: tapos na."
    narrator "Sinabi mo sa sarili mo — pangsurvive lang ito. Pansamantala. Hanggang lumabas sa normal."

    scene black with dissolve
    narrator "Naging normal na."
    pause 1.2
    narrator "Ikaw?"

    ## ── CHARACTER SELECTION ──────────────────────────────────────────────────
    scene black
    $ safe_stop("music")
    $ safe_play("music", "audio/bgm/bgm_campus.ogg", loop=True)

    sys_voice "Bagong semester. Ikatlong taon. Subukan nating muli."
    sys_voice "Una sa lahat — sino ka?"

    menu:
        "Alex (Lalaki) — 'Basta makarating sa susunod na araw.'":
            $ player_gender = "male"
            $ player_name   = "Alex"
        "Alexa (Babae) — 'Dumaan na sa marami. Nandito pa rin. Counts naman.'":
            $ player_gender = "female"
            $ player_name   = "Alexa"

    sys_voice "At anong pangalan nila sa'yo?"
    $ raw_name = renpy.input("Pangalan:", default=player_name, length=20)
    $ player_name = raw_name.strip() if raw_name.strip() else player_name

    sys_voice "Maganda. Sino ang iyong tao sa group? Ang isa mong pinaka-kinukutext simula nung first year?"

    menu:
        "Carl — 'Gamer, kahit paano pumapasa, laging nandoon para sa'yo.'":
            $ player_bestfriend = "carl"
        "Carly — ''Isa lang naman na game, pagkatapos mag-aral na.' (Hindi naman talagang isa.)":
            $ player_bestfriend = "carly"

    ## Bestfriend appears
    show screen hud
    if player_bestfriend == "carl":
        show carl happy at center with dissolve
        carl "Uy! Ikatlong taon na natin! Parang kahapon lang noh?"
        if player_gender == "male":
            mc_m "(Ngumiti ka kahit pagod na pagod.) Oo nga. Pero mas malala na ang dark circles."
        else:
            mc_f "(Ngumiti ka kahit pagod na pagod.) Oo nga. Pero mas malala na ang dark circles."
        carl "Haha! Tara na, late na tayo."
        hide carl with dissolve
    else:
        show carly happy at center with dissolve
        carly "Uy! Third year na tayo! Nakakatawa, dati palagi kang nahihirapan sa enrollment."
        if player_gender == "male":
            mc_m "(Totoo naman.) Tapos ngayon nandito na tayo."
        else:
            mc_f "(Totoo naman.) Tapos ngayon nandito na tayo."
        carly "Sige na, tara na. May 8AM pa tayo."
        hide carly with dissolve

    return

# ─────────────────────────────────────────────────────────────────────────────
# SHARED LABELS
# ─────────────────────────────────────────────────────────────────────────────

label ai_used_result:
    narrator "Pinindot mo ang AI. Lumabas ang sagot — perpekto, kumpleto, walang kahirap-hirap."
    narrator "Kinopya mo. I-paste. I-submit."
    narrator "Tapos ka na. In under three minutes."
    narrator "Ang sagot ay perpekto. Hindi mo maintindihan kahit isang linya nito."
    $ renpy.notify("CT −10  |  AI use #" + str(ai_use_count))
    return

label minigame_correct:
    $ renpy.notify("Tama! CT +8")
    return

label minigame_wrong:
    $ renpy.notify("Mali. Subukan ulit. CT −5")
    return
