## game/chapter8.rpy
## Chapter 8 — "Finals" (Week 8 — Grand Finale)

label chapter8:
    call screen chapter_title("8", "Finals", "Week 8 — 'Ito na. Walang balik.'")
    $ day_label = "Week 8 — Finals Day"
    $ current_week = 8

    ## ── SCENE 8-1: Morning of finals — Carl/Carly with coffee at the gate ───
    scene bg_campus with dissolve
    $ safe_play("music", "audio/bgm/bgm_finals.ogg", loop=True)

    narrator "(Alas siyete ng umaga. Ang campus ay maliwanag at maingay — lahat ay may dala-dalang reviewer, may pantalon na halos hindi natulog, may kape.)"

    if player_bestfriend == "carl":
        show carl happy at center with dissolve
        carl "Uy! Heto ka na. Akala ko late ka na naman."
        if player_gender == "male":
            mc_m "Nagbago na 'ko. Maaga na 'ko ngayon."
        else:
            mc_f "Maaga na 'ko ngayon. Bago na akong tao."
        carl "Haha! Here — kape. Walang tulog kaya ito ang fuel."
        if player_gender == "male":
            mc_m "(Tinanggap mo ang kape. Mainit. Tama.)"
        else:
            mc_f "(Tinanggap mo ang kape. Sinimsim mo. Buo ang pakiramdam.)"
    else:
        show carly happy at center with dissolve
        carly "Nandito na! Alam ko na maaga ka na ngayon."
        if player_gender == "male":
            mc_m "Oo, nagbago na 'ko. Sineseryoso ko na ito."
        else:
            mc_f "Oo. Sineseryoso ko na. Huli na para mag-back down."
        carly "Heto — dalawa kang kape. Isa para ngayon, isa para in between exams."
        if player_gender == "male":
            mc_m "(Tumawa ka. Ang kape ay mainit at tama.)"
        else:
            mc_f "(Tumawa ka. Mainit ang kape at buo ang pakiramdam.)"

    show kent normal at left with dissolve
    kent "Nasa schedule: Networking una, Programming pagkatapos ng break, Cybersecurity last. I-pace ninyo ang sarili ninyo."
    show rey normal at right with dissolve
    rey "Kaya natin 'to."
    narrator "(Bihirang marinig 'yan kay Rey. Lingon ka sa kanya.)"
    rey "...Kaya natin."

    hide carl with dissolve
    hide carly with dissolve
    hide kent with dissolve
    hide rey with dissolve

    ## ── SCENE 8-2: Finals Exam 1 — Networking (Mr. Earns) ───────────────────
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 8 — Networking Finals"

    show mr_earns normal at center with dissolve
    mr_earns "Magsimula na. Dalawang oras. Walang phone. Walang kahit ano."
    narrator "(Binaliktad mo ang papel. Ang unang tanong — subnetting. Alam mo ito.)"
    narrator "(Hindi dahil kinopya mo mula sa AI. Kundi dahil ginawa mo sa sarili mo, nang paulit-ulit, hanggang sumama sa iyo.)"
    hide mr_earns with dissolve

    ## Networking Finals Minigame
    show screen minigame(
        "Networking Finals — Routing Protocol",
        "Alin sa mga sumusunod ang tamang katangian ng OSPF kumpara sa RIP?",
        [
            "A. Gumagamit ng hop count bilang metric; maximum 15 hops",
            "B. Link-state protocol; gumagamit ng Dijkstra's algorithm para sa routing",
            "C. Distance-vector protocol; nagse-send ng buong routing table tuwing 30 segundo",
            "D. Hindi sumusuporta sa VLSM at CIDR"
        ],
        1,
        "networking",
        15,
        18
    )

    scene bg_hallway with dissolve
    narrator "(Natapos ang Networking exam. Lumabas ka nang tahimik. Hindi ka nagre-react.)"
    narrator "(Sa loob mo lang — 'Kaya ko 'yun.')"

    ## ── SCENE 8-3: Finals Exam 2 — Programming (Mr. Kai) ────────────────────
    scene bg_lab with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 8 — Programming Finals"

    show mr_kai normal at center with dissolve
    mr_kai "Okay! Finals na. May coding output kayo — i-type ninyo ang inyong solusyon sa editor. Walang AI tools open. Siniseryoso ko ito."
    mr_kai "At para sa lahat — ang code na masyadong perpekto para sa lalim ng topic ay mapapansin ko."
    mr_kai "Good luck. Kaya ninyo."
    hide mr_kai with dissolve

    ## Programming Finals Minigame
    show screen minigame(
        "Programming Finals — Python Functions",
        "Ano ang output ng sumusunod na Python code?\n\ndef square(n):\n    return n * n\n\nresult = square(4) + square(3)\nprint(result)",
        [
            "A. 49",
            "B. 25",
            "C. 7",
            "D. 12"
        ],
        1,
        "programming",
        15,
        18
    )

    scene bg_hallway with dissolve
    narrator "(Programming exam — tapos. Ang code mo ay hindi perpekto. May isang function na medyo awkward.)"
    narrator "(Pero ikaw ang nag-isip nito. Bawat linya — ikaw.)"

    ## ── SCENE 8-4: Finals Exam 3 — Cybersecurity (Ms. Iva) ─────────────────
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 8 — Cybersecurity Finals"

    show ms_iva normal at center with dissolve
    ms_iva "Ang huling exam. May MCQ portion at may essay."
    ms_iva "Ang essay prompt, tandaan ninyo: ipaliwanag ang cognitive debt sa konteksto ng AI use sa edukasyon. At isang hakbang para gamitin ang AI nang etikal."
    ms_iva "Actual citations kung may ci-cite — verified mula sa tunay na batas. Wala akong tinatanggap na AI-generated references."
    ms_iva "(huminto) Kaya ninyo."
    hide ms_iva with dissolve

    ## Cybersecurity Finals Minigame
    show screen minigame(
        "Cybersecurity Finals — RA 10175",
        "Sa ilalim ng RA 10175 (Cybercrime Prevention Act of 2012), alin ang nakalista bilang cybercrime offense?",
        [
            "A. Paggamit ng social media para mag-post ng personal na larawan",
            "B. Illegal access sa isang computer system nang walang pahintulot",
            "C. Pag-download ng libre at legal na open-source software",
            "D. Pagtanggap ng email mula sa hindi kilalang sender"
        ],
        1,
        "cyber",
        15,
        18
    )

    ## Essay prompt scene
    scene bg_classroom with dissolve
    narrator "(Ang essay prompt ay nakaharap sa iyo. Puti ang papel. Blangko pa.)"
    narrator "'Ipaliwanag ang cognitive debt sa konteksto ng AI use sa edukasyon, at isang hakbang na magagawa ng isang IT student para gamitin ang AI nang etikal.'"
    narrator "(Naisip mo ang lahat ng nangyari nitong walong linggo. Ang mga aral, ang mga pagkakamali, ang mga pagpipilian.)"

    if player_gender == "male":
        mc_m "(Sa isip mo) Hindi ito ang papel na gusto ko isulat. Pero ito ang pinakatotoo.)"
    else:
        mc_f "(Sa isip mo) Hindi ko ito maisusulat para sa grado. Isusulat ko ito dahil totoo ito.)"

    narrator "(Simula ka ng magsulat. Hindi mabilis. Hindi perpekto. Pero bawat salita ay iyong sarili.)"
    narrator "(RA 10173 — Section 3, ang kahulugan ng personal information. Tama ang section number. Bina-verify mo.)"
    narrator "(Natapos ka. Hindi ka siguradong mataas ang grado. Pero sigurado kang totoo ang sinulat mo.)"
    $ grade_change("cyber", 12)

    ## ── SCENE 8-5: After last exam ───────────────────────────────────────────
    scene bg_campus with dissolve
    $ safe_play("music", "audio/bgm/bgm_campus.ogg", loop=True)
    $ day_label = "Week 8 — Pagkatapos ng Finals"

    narrator "(Hapon na. Ang campus ay maliwanag at maingay — ngayon, iba ang ingay. Mas magaan.)"
    narrator "(Nakarating kayo sa canteen entrance. Lahat ng grupo.)"

    show gabby happy at right with dissolve
    show kent happy at left with dissolve
    show rey normal at center with dissolve

    gabby "TAPOS NA! LAHAT TAPOS NA! PAGKAIN TAYO!"
    kent "Technically, may grade pa lang kailangang lumabas—"
    gabby "KENT."
    kent "...Okay. Pagkain tayo."
    rey "..."
    narrator "(Tumingin ka kay Rey.)"
    rey "Maayos."
    narrator "(Dalawang salita. Mula kay Rey — iyon ang sapat na.)"

    if player_bestfriend == "carl":
        show carl happy at center with dissolve
        carl "Uy! Kumusta ang essay ni Ms. Iva?"
        if player_gender == "male":
            mc_m "Sarili ko ang sinulat. Hindi AI."
        else:
            mc_f "Sarili ko. Verified citations at lahat."
        carl "(ngumiti) Seryoso? Ikaw talaga."
        hide carl with dissolve
    else:
        show carly happy at center with dissolve
        carly "Kumusta ang essay? Tinupad mo ang promise mo?"
        if player_gender == "male":
            mc_m "Oo. Sarili ko. Bini-verify ko pa ang bawat citation."
        else:
            mc_f "Oo. Sarili kong salita. Lahat bina-verify ko."
        carly "(ngumiti) Proud ako. Seryoso."
        hide carly with dissolve

    hide gabby with dissolve
    hide kent with dissolve
    hide rey with dissolve

    scene black with dissolve
    narrator "(Ilang linggo pagkatapos, lalabas ang mga grades.)"
    narrator "(Ngayon — kumain muna kayo. Grupo. Maingay. Buhay.)"
    narrator "(At ikaw — nandoon ka. Presente. Tunay.)"

    ## Trigger ending calculation
    return
