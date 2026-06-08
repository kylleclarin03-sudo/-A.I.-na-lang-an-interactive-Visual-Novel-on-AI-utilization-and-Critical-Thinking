## game/chapter4.rpy
## Chapter 4 — "May Test Bukas" (Week 4 — Midterms Approaching)

label chapter4:
    call screen chapter_title("4", "May Test Bukas", "Week 4 — 'Sige na, isa pa lang, tapos tutulog na.'")
    $ day_label = "Week 4 — Gabi"
    $ current_week = 4

    ## ── SCENE 4-1: Night before the exam ─────────────────────────────────────
    scene bg_bedroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_night.ogg", loop=True)

    narrator "(Gabi bago ang Networking midterm. Ang notes mo ay nakabukas sa laptop. Ang phone mo ay nakapatay — na-charge lang.)"
    narrator "(Alas nwebe pa lang. Maaga ka. Para sa iyo, kahit paano.)"

    groupchat "GABBY: huy last game na please!! ranked!! isa lang HAHA"
    groupchat "GABBY: wag ka magtampo pag hindi ka sumama"

    if player_bestfriend == "carl":
        groupchat "CARL: huy matulog na kayo. test bukas."
        groupchat "GABBY: kupal 😤"
    else:
        groupchat "CARLY: seryoso 'to, matulog na kayo. review muna kayo."
        groupchat "GABBY: ayy pabibo"

    groupchat "KENT: The recommended pre-exam sleep duration is 7-9 hours. REM sleep is critical for memory consolidation of newly acquired—"
    groupchat "GABBY: KENT HINDI KO NEED ANG SCIENCE"
    groupchat "REY: zzz"

    narrator "(Ang phone mo ay naka-mute. Ang notes mo ay nakabukas. Ang mata mo ay nagsisimulang mabigat.)"

    ## CHOICE NODE 4-A
    menu:
        "Matulog na. Review na sana sa umaga.":
            $ ct_change(8)
            $ mot_change(5)
            if player_gender == "male":
                mc_m "(I-type sa chat) Matulog na ako. GL sa ranked, Gabs."
            else:
                mc_f "(I-type sa chat) Matutulog na ko. Kaya ninyo."
            narrator "(Nagising ka nang may oras pa. Nag-review ng isang oras. Kumain ng almusal. Nakarating sa klase nang maaga.)"
            $ grade_change("networking", 8)

        "Isa lang na laro, tapos tutulog na talaga.":
            $ ct_change(-5)
            $ mot_change(-5)
            if player_gender == "male":
                mc_m "(I-type sa chat) Fine. Isa lang. ISA."
            else:
                mc_f "(I-type sa chat) Okay FINE. Isa lang ha."
            narrator "(Tatlong laro pagkatapos, alas dose na ng hatinggabi. Natulog ka nang walang review.)"
            narrator "(Nagising ka nang late. Alarma hindi narinig. O baka hindi sinundan.)"
            $ mot_change(-3)
            jump chapter4_late_scene

        "Mag-aral pa ng konti, kahit pagod na.":
            $ ct_change(5)
            if player_gender == "male":
                mc_m "(I-type sa chat) Mag-aral muna ako. Kayo na laro."
            else:
                mc_f "(I-type sa chat) Nah, mag-aral muna. Kayo na."
            narrator "(Pinagpatuloy mo ang review. Dalawang oras. Pagod pero may natandaan ka.)"
            narrator "(Natulog ka nang alas onse. Nag-alarma nang alas siyete. Maayos.)"
            $ grade_change("networking", 5)

    ## ── SCENE 4-2: Running late ───────────────────────────────────────────────
    scene bg_hallway with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 4 — Exam Day"
    narrator "(Nakarating ka sa klase. Nakarating — iyon ang mahalaga.)"
    jump chapter4_exam

label chapter4_late_scene:
    scene bg_hallway with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 4 — Exam Day (Late)"

    show mr_earns normal at center with dissolve
    mr_earns "Twelve minutes late."
    narrator "(Wala siyang ibang sinabi. Pinagmasdan ka niya habang umuupo ka.)"
    mr_earns "Exam na. Walang phone."
    hide mr_earns with dissolve
    $ grade_change("networking", -8)
    narrator "(Ang mga tanong sa exam — nakita mo na ang ilan sa kanila sa notes mo. Kahapon. Bago ka natulog nang maaga.)"

## ── SCENE 4-3: Networking Long Test ──────────────────────────────────────────
label chapter4_exam:
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)

    show mr_earns normal at center with dissolve
    mr_earns "Ang phone ay nasa bag. Bag ay sa harap. Magsimula na."
    hide mr_earns with dissolve

    narrator "(Ang unang tanong — subnetting. Alam mo ang formula. O akala mo.)"

    ## Networking minigame — Subnetting (LOCKED — no phone option)
    show screen minigame(
        "Midterm Exam — Subnetting (Phone Locked!)",
        "Ang network address ay 192.168.10.0/26. Ilan ang maximum na bilang ng usable hosts?",
        [
            "A. 30",
            "B. 62",
            "C. 126",
            "D. 14"
        ],
        1,
        "networking",
        12,
        15
    )

    scene bg_classroom with dissolve
    narrator "(Natapos ang exam. Binaliktad mo ang papel. Huminga ng malalim.)"
    narrator "(Hindi mo sure sa lahat ng sagot mo. Pero nasubukan mo. Wala kang pinag-AI. Ngayon, wala.)"

    if player_bestfriend == "carl":
        show carl normal at right with dissolve
        carl "Kumusta? Mahirap ba?"
        if player_gender == "male":
            mc_m "Okay lang. 'Yung subnetting... hindi ko sure."
        else:
            mc_f "Ewan. Sagot ko sa subnetting — 62. Tama ba?"
        carl "Ako rin. Tama 'yun. Sixty-two."
        hide carl with dissolve
    else:
        show carly normal at right with dissolve
        carly "Kumusta ang exam? Kayanin mo?"
        if player_gender == "male":
            mc_m "Siguro. Yung isa o dalawa hindi ko sure."
        else:
            mc_f "Ewan, pero yung subnetting sagot ko ay sixty-two. Tama?"
        carly "Sixty-two rin sagot ko! Sana tama."
        hide carly with dissolve

    return
