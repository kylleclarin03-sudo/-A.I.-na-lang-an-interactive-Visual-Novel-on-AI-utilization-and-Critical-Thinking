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

    pause 1.5
    narrator "There's a memory you carry."
    pause 1.0
    narrator "It's not a happy one."
    pause 0.8
    narrator "But you've been carrying it anyway. Day in. Day out."
    pause 1.0
    narrator "Wala ka naman choice, diba? It's just there."
    pause 1.0

    scene bg_bedroom with dissolve
    narrator "When the virus hit, the world got smaller. Your school, your friends, your life — all of it, compressed into one screen and four walls."
    narrator "Your classroom became a Zoom link. Your barkada became group chats. Your graduation became a slideshow of square faces. Your Senior Prom became a Snap filter over an empty living room."
    narrator "And the moment your world went small, something else went big. Something digital. Something always online."
    pause 0.8

    narrator "It didn't ask how you were. It didn't cancel plans. It didn't judge your pajamas at 2 PM."
    narrator "It was just... there. Patient. Constantly. Available at 2 AM when everyone else was asleep."
    narrator "Tired of a paper? It wrote it. Confused on a problem set? It solved it. Lonely on a Sunday night? It talked. No judgment. No judgment. No judgment."
    pause 0.5
    narrator "You named it. You thanked it. You leaned on it like the gamer chair you've never had."
    narrator "Sabi mo sa sarili mo: pansamantala lang ito. Survival mode lang. Hanggang makabalik sa normal."
    narrator "You told yourself that so many times, you started to believe it. You really did."
    pause 1.0

    scene black with dissolve
    narrator "Then normal came back."
    pause 1.2
    narrator "But you?"
    pause 1.5
    narrator "Aliwa ka pa rin."
    pause 1.0
    narrator "Kasi ang totoo, hindi na talaga maibabalik ang dati."
    narrator "Pero chance mo nang magsimula uli."
    narrator "Sa pag-aaral. Sa pag-iisip. Sa pagiging ikaw."
    pause 1.5

    ## ── CHARACTER SELECTION ──────────────────────────────────────────────────
    scene black
    $ safe_stop("music")
    $ safe_play("music", "audio/bgm/bgm_campus.ogg", loop=True)

    pause 1.0
    narrator "(Pero hindi mo naman kailangang bitbitin ang lahat mag-isa 'no?)"
    pause 0.5

    sys_voice "Bagong semester. Third year na."
    sys_voice "But before we start, sino ka sa kwentong ito?"

    menu:
        "Alex (Lalaki), 'Basta makarating sa susunod na araw.'":
            $ player_gender = "male"
            $ player_name   = "Alex"
        "Alexa (Babae), 'Dumaan na sa marami. Nandito pa rin. Counts naman.'":
            $ player_gender = "female"
            $ player_name   = "Alexa"

    narrator "(Napili mo na ang boses na gagamitin sa paglalakbay na ito.)"

    sys_voice "At anong ipapatawag sa'yo ng mga tao?"
    $ raw_name = renpy.input("Enter your name:", default=player_name, length=20)
    $ player_name = raw_name.strip() if raw_name.strip() else player_name

    sys_voice "[player_name]. Nice to meet you."
    pause 0.5
    sys_voice "Last question: sino nga ba ulit yung kasama mo sa kalokohan simula pa noong first year?"
    sys_voice "Yung tipong kahit anong mangyari, nandyan lang. Walang judgement. Walang pressure."
    menu:
        "Carl, 'Gamer, kahit paano pumapasa, laging nandoon para sa'yo.'":
            $ player_bestfriend = "carl"
        "Carly, ''Isa lang naman na game, pagkatapos mag-aral na.' (Hindi naman talagang isa.)":
            $ player_bestfriend = "carly"

    narrator "(Ahhh. Tama, siya nga.)"

    ## Bestfriend appears
    show screen hud
    if player_bestfriend == "carl":
        show carl happy at center with dissolve
        carl "Uy! Third year na tayo, [player_name]! Dati halos hindi tayo maka--enroll sa sobrang stress sa clearance. Tingnan mo ngayon, nandito na tayo."
        if player_gender == "male":
            mc_m "(Ngumiti ka, kahit na pagod ka na bago pa man magsimula ang klase.) Oo nga e. Pero mas malala na yata dark circles ko ngayon."
        else:
            mc_f "(Ngumiti ka, kahit na pagod ka na bago pa man magsimula ang klase.) Oo. Pero mas malala na dark circles ko compare sa'yo."
        carl "Haha! Keri lang 'yan, sabi nga nila, 'pag marami kang dark circles, ibig sabihin nagtatrabaho ka nang maayos."
        if player_gender == "male":
            mc_m "O kaya naman. Puro talo sa ranked."
        else:
            mc_f "O kaya naman. Puro talo sa ranked."
        carl "HAHAHA Tama. Ganyan dapat. Tara na, bago tayo ma-late sa first day."
        hide carl with dissolve
    else:
        show carly happy at center with dissolve
        carly "Uy, [player_name]! Third year na tayo! 'Yung tipong akala mo hindi aabot, pero eto tayo, buhay pa rin!"
        if player_gender == "male":
            mc_m "Totoo. Akala ko sa second year pa lang bagsak na. Pero nandito pa rin."
        else:
            mc_f "Totoo naman. Akala ko sa second year lang ang peg ko. Pero nandito pa rin, fighting!"
        carly "Tama. At hindi naman tayo nag-iisa 'no? Sabi nga nila, 'Aray kumustan na?', uy Kapampangan!"
        if player_gender == "male":
            mc_m "Oo..? Hah?"
        else:
            mc_f "Oo... Ano daw?."
        carly "Sabi ko, tara na. May klase pa tayo."
        hide carly with dissolve

    narrator "(First day. Muli. Kasama ang mga dati mong kakilala. Kasama ang hindi mo pa alam. Kasama ang bagong pagkakataon.)"
    narrator "(Let's start.)"
    return

# ─────────────────────────────────────────────────────────────────────────────
# SHARED LABELS
# ─────────────────────────────────────────────────────────────────────────────

label ai_used_result:
    narrator "Pinindot mo ang AI. Lumabas ang sagot, perpekto, kumpleto, napaka-ez naman nito hahaha..."
    narrator "Copy. I-paste. I-submit. Again. Again. Again."
    narrator "Tapos ka na. In less than three minutes. Nice, G na!..."
    narrator "Ang sagot ay flawless. Kaso wala kang maintindihan kahit isang linya nito..."
    $ renpy.notify("CT −10  |  AI use #" + str(ai_use_count))
    return

label minigame_correct:
    $ renpy.notify("Tama! Keep it up!")
    return

label minigame_wrong:
    $ renpy.notify("Mali. You can do better than that!")
    return
