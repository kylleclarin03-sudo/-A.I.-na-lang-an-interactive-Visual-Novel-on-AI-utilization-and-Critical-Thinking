## game/chapter3.rpy
## Chapter 3 — "Submit Mo Na Lang" (Week 3)

label chapter3:
    call screen chapter_title("3", "Submit Mo Na Lang", "Week 3 — 'Kahit paano, may nasubmit.'")
    $ day_label = "Week 3 — Umaga"
    $ current_week = 3

    ## ── SCENE 3-1: Mr. Kai's Python debug activity ───────────────────────────
    scene bg_lab with dissolve
    $ safe_play("music", "audio/bgm/bgm_classroom.ogg", loop=True)

    show mr_kai normal at left with dissolve
    mr_kai "Good morning! Okay, para ngayon — debugging activity. May code kayo sa harap ninyo. Broken. I-fix ninyo."
    mr_kai "Twenty minutes. Walang phone, walang AI, walang Google. Sariling utak lang. Go."
    hide mr_kai with dissolve

    narrator "(Tiningnan mo ang code sa screen. Tatlong bugs. Alam mo ang isa.)"

    ## Programming minigame — Debug
    show screen minigame(
        "Programming — Python Debug Challenge",
        "Bakit mag-e-error ang code na ito?\n\ndef greet(name):\n    print('Hello, ' + name)\n\ngreet(123)",
        [
            "A. Hindi valid ang function name na 'greet'",
            "B. TypeError: hindi pwedeng i-concatenate ang str at int",
            "C. Walang error, tatakbo nang maayos",
            "D. IndentationError sa loob ng function"
        ],
        1,
        "programming",
        8,
        10
    )

    scene bg_lab with dissolve
    $ safe_play("music", "audio/bgm/bgm_classroom.ogg", loop=True)

    show mr_kai normal at left with dissolve
    mr_kai "Okay, time. Tingnan natin ang scoreboard."
    narrator "(Lumabas ang mga pangalan. Ang sa'yo — nasa gitna. Hindi pinakamataas. Hindi pinakamababa.)"
    mr_kai "Maganda ang progress. Pero gusto ko pa rin makita ang inyong indibidwal na approach. Hindi lahat ng sagot ay oo o hindi — minsan ang proseso ang mas mahalaga."
    hide mr_kai with dissolve

    ## ── SCENE 3-2: Canteen halftime check-in ────────────────────────────────
    scene bg_canteen with dissolve
    $ safe_play("music", "audio/bgm/bgm_canteen.ogg", loop=True)
    $ day_label = "Week 3 — Tanghali"

    narrator "(Hapon. Grupo sa canteen. Si Rey ay hindi karaniwan na nagsasalita — ngayon ay may sinasabi siya.)"

    show rey normal at left with dissolve
    show kent normal at center with dissolve
    show gabby normal at right with dissolve

    rey "...Nakita ko yung submission ni Gabby."
    narrator "(Tahimik. Lahat ay tumingin kay Rey.)"
    rey "Pareho ng sagot namin sa debugging activity. Word for word. Pero hindi tayo nag-usap."
    gabby "Coincidence. Pare-pareho naman ang bugs, pare-pareho ang solusyon."
    rey "Hindi ko sinasabi na copied. Sinasabi ko lang na... parehong solusyon. Ganoon naman talaga kung AI ang nagbibigay ng sagot."
    kent "Urm, technically that is a valid observation regarding AI output homogeneity—"
    gabby "Okay na, pakitaan mo ko ng proof."

    if player_bestfriend == "carl":
        show carl normal at right with dissolve
    else:
        show carly normal at right with dissolve

    narrator "(Tinitingnan kita ni [player_bestfriend].)"

    if player_bestfriend == "carl":
        carl "(mababa) Ikaw... sarili mo ba ang ginawa mo?"
    else:
        carly "(mababa) Ano sa tingin mo, tama si Rey?"

    ## CHOICE NODE 3-A
    menu:
        "Oo, sarili ko. Kahit na medyo mahirap.":
            $ ct_change(5)
            if player_gender == "male":
                mc_m "Sarili ko. Bagal ko nga ng kalahati ng klase, pero sarili ko."
            else:
                mc_f "Sarili ko. May mga parts na kinailangan ko ng tulong mula sa notes, pero sarili ko."
            if player_bestfriend == "carl":
                carl "(huminga ng malalim) Okay. Good."
            else:
                carly "(ngumiti) Sige. Ganoon talaga."
            narrator "(Nag-move on ang grupo. Pero sa isip mo — sigurado ka ba?)"

        "...Mostly. May AI-assisted na parts.":
            $ ct_change(-3)
            if player_gender == "male":
                mc_m "Mostly sarili ko. May isang part na kinonsulta ko sa AI."
            else:
                mc_f "Mostly. May napagod ako at pinag-AI ang isang section."
            if player_bestfriend == "carl":
                carl "Basta wag maging habit, okay? Mapapansin ni Sir 'yan."
            else:
                carly "Ingat ka lang. Mr. Kai ay matalino. Mapapansin niya."
            narrator "(Tama sila. At alam mo iyon.)"

        "Huwag mong alamin.":
            $ ct_change(-8)
            if player_gender == "male":
                mc_m "Huwag mong alamin."
            else:
                mc_f "Huwag mong alamin."
            if player_bestfriend == "carl":
                carl "...Sige."
            else:
                carly "...Okay."
            narrator "(Binabalewala mo siya. Pero hindi siya tumitigil sa pagmasid sa'yo.)"
            $ mot_change(-5)

    hide rey with dissolve
    hide kent with dissolve
    hide gabby with dissolve
    hide carl with dissolve
    hide carly with dissolve

    ## ── SCENE 3-3: Rey's warning ─────────────────────────────────────────────
    scene bg_hallway with dissolve
    $ day_label = "Week 3 — Hapon"

    show rey normal at center with dissolve
    narrator "(Naabutan ka ni Rey sa hallway pagkatapos ng klase.)"
    rey "Hindi kita kinokontra. Alam ko kung bakit ginagawa ng mga tao 'yun."
    rey "Pero may napansin ako — kapag puro AI na ang nagsasagot, hindi ka na nagtatanong ng sarili mong mga tanong."
    rey "At 'yung mga sariling tanong — 'yun ang hindi mabibigyan ng AI ng sagot."

    narrator "(Lumakad na siya bago ka pa makasagot.)"
    hide rey with dissolve
    return
