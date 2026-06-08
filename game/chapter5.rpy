## game/chapter5.rpy
## Chapter 5 — "Incomplete?" (Week 5 — Midterm Results)

label chapter5:
    call screen chapter_title("5", "Incomplete?", "Week 5 — 'Kahit ano nang grade, basta may grade.'")
    $ day_label = "Week 5 — Tanghali"
    $ current_week = 5

    ## ── SCENE 5-1: Midterm results posted ───────────────────────────────────
    scene bg_hallway with dissolve
    $ safe_play("music", "audio/bgm/bgm_sad.ogg", loop=True)

    narrator "(Naka-post na ang midterm grades sa portal. Lahat ay nakapaligid sa bulletin board ng department.)"
    narrator "(Hindi ka nagmamadali. Alam mo na ang magiging resulta, kahit paano.)"

    ## Grade reveal based on current stats
    python:
        ng_letter = letter_grade(networking_grade)
        pg_letter = letter_grade(programming_grade)
        cg_letter = letter_grade(cyber_grade)
        any_inc   = any_incomplete()

    if any_inc:
        narrator "(Ang iyong pangalan sa listahan. Networking: [ng_letter]. Programming: [pg_letter]. Cybersecurity: [cg_letter].)"
        narrator "(May isa o higit pa na kulay pula. INC sa midterm component.)"
        $ mot_change(-15)
        $ renpy.notify("Midterm: Networking=[ng_letter] | Prog=[pg_letter] | Cyber=[cg_letter]")
    else:
        narrator "(Ang iyong pangalan sa listahan. Networking: [ng_letter]. Programming: [pg_letter]. Cybersecurity: [cg_letter].)"
        narrator "(Nakalusot. Hindi palaging maganda, pero nakalusot.)"
        $ mot_change(5)
        $ renpy.notify("Midterm: Networking=[ng_letter] | Prog=[pg_letter] | Cyber=[cg_letter]")

    show gabby normal at right with dissolve
    if player_bestfriend == "carl":
        show carl normal at left with dissolve
    else:
        show carly normal at left with dissolve
    show kent normal at center with dissolve

    if any_inc:
        gabby "Huy, okay ka lang ba? Medyo..."
        if player_gender == "male":
            mc_m "(Tahimik lang.)"
        else:
            mc_f "(Tinitingnan mo ang papel. Lumuluha ka nang hindi mo namamalayan.)"
        if player_bestfriend == "carl":
            carl "(mababa) Uy. Kaya pa 'to."
        else:
            carly "(mababa) Hey. Huwag muna mag-isip ng masama."
    else:
        gabby "Ay, okay naman! Ako rin, okay rin!"
        if player_bestfriend == "carl":
            carl "Oo naman. Kaya pa natin."
        else:
            carly "Maganda ang midterm scores! Next step, finals."

    hide gabby with dissolve
    hide carl with dissolve
    hide carly with dissolve

    ## ── SCENE 5-2: Kent speaks up in canteen ────────────────────────────────
    scene bg_canteen with dissolve
    $ safe_play("music", "audio/bgm/bgm_canteen.ogg", loop=True)
    $ day_label = "Week 5 — Hapon"

    show kent normal at center with dissolve
    show rey normal at left with dissolve

    kent "Urm. Pwede ba akong magsabi ng isang bagay na baka hindi magustuhan ng ilan?"
    rey "Go lang, Kent."
    kent "Nakita ko 'yung grades ng lahat sa department listahan. Hindi ko gustong maging masyadong direkta pero... may mga tao sa grupong ito na mas mababang midterm score kaysa sa inaasahan ko."

    if player_bestfriend == "carl":
        show carl normal at right with dissolve
        carl "Kent, hindi 'yun—"
    else:
        show carly normal at right with dissolve
        carly "Kent, personal 'yung grades—"

    kent "Hindi ko ibinubuka para mapahiya ang sinuman. Ibinubuka ko dahil may finals pa. At may completion exam pa kung kailangan. At ang grupo — kaya nating mag-tulong-tulong."
    narrator "(Sandali. Tahimik ang mesa.)"
    rey "Kent has a point. Study session? This weekend. Library. No games."
    kent "Mayroon akong mga notes mula sa lahat ng tatlong subjects. Pwede kong i-share."

    ## CRITICAL CHOICE 5-A: Sets the direction toward ending
    menu:
        "Oo, gusto ko ng tulong. Sineseryoso ko ang finals.":
            $ ct_change(12)
            $ mot_change(15)
            if player_gender == "male":
                mc_m "Oo. Kailangan ko ng tulong. Sineseryoso ko 'to."
            else:
                mc_f "Sige. Oo. Kailangan ko ng help, at aaminin ko 'yun."
            kent "(ngumiti nang bihira) Good. Saturday. Inaabangan kita."
            narrator "(Isang bagay ang nagbago sa mesa — hindi malaki, pero naramdaman mo.)"
            $ grade_change("networking", 5)
            $ grade_change("programming", 5)
            $ grade_change("cyber", 5)

        "Mag-AI study session na lang, mas mabilis.":
            $ ct_change(-10)
            $ mot_change(-5)
            if player_gender == "male":
                mc_m "Sige... oo. Pero may paraan naman ako. AI-generated reviewers — mas efficient."
            else:
                mc_f "...May paraan naman ako. Mag-o-organize ng AI reviewer."
            kent "(naging seryoso) 'Yung AI reviewer — hindi 'yun ang problema. Ang problema ay kung hindi mo mabasa nang may pag-unawa ang sagot nito."
            $ use_ai(None, 0)
            narrator "(Tama si Kent. Pero hindi mo pa maintindihan kung bakit.)"

        "Kaya ko pa 'to mag-isa. Hindi ko kailangan ng group study.":
            $ ct_change(-5)
            $ mot_change(-10)
            if player_gender == "male":
                mc_m "Kaya ko 'to. Mag-isa lang ako nag-aral noon, kaya pa 'yun."
            else:
                mc_f "Okay na ako. Kaya ko 'to."
            kent "(bumubulong) That's not apathy. That's fear."
            narrator "(Narinig mo siya. Kahit mababa ang boses niya.)"
            narrator "(Hindi ka sumagot.)"

    hide kent with dissolve
    hide rey with dissolve
    hide carl with dissolve
    hide carly with dissolve

    ## ── SCENE 5-3: Ms. Iva's reminder ───────────────────────────────────────
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 5 — Huling Klase"

    show ms_iva normal at center with dissolve
    ms_iva "Bago kayo umalis — isang bagay lang. Ang finals paper na ibibigay ko sa inyo ay may essay component."
    ms_iva "Ang prompt: ipaliwanag ang cognitive debt sa konteksto ng AI use sa edukasyon. At isang konkretong hakbang ng isang IT student para gamitin ang AI nang etikal."
    ms_iva "Pwedeng mag-cite ng batas — RA 10173 o RA 10175. Pero i-cite ninyo nang tama. Ang mga citations na hindi mahanap sa aktwal na batas ay magiging isang seryosong problema."
    narrator "(Tumingin siya sa klase. Isa-isa.)"
    ms_iva "Matulog nang maayos. Mag-aral nang maayos. Gisingin ninyo ang inyong sariling utak."
    hide ms_iva with dissolve
    return
