## game/chapter6.rpy
## Chapter 6, "Busted" (Week 6, Confrontation)

label chapter6:
    call screen chapter_title("6", "Busted", "Week 6, 'Ma'am, may explanation po ako...'")
    $ day_label = "Week 6, Umaga"
    $ current_week = 6

    ## ── SCENE 6-1: Ms. Iva pulls player aside ───────────────────────────────
    scene bg_hallway with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)

    narrator "(Bago magsimula ang klase. Tinatawag ka ni Ms. Iva.)"
    narrator "(Lahat ay nakapansin. Nagtataka. Ikaw lang ang hindi nagtataka, alam mo na kung bakit.)"

    show ms_iva normal at enter_center_rise
    ms_iva "Ang essay mo sa cybersecurity paper, may nahanap akong citation. RA 10173, Section 4, Subsection g, Paragraph 3."
    ms_iva "Binuksan ko ang textbook. Walang ganoon na provision."
    narrator "(Tahimik bigla ang hallway.)"
    ms_iva "Hindi ito ang unang pagkakataon na nakakita ako ng ganito. Ang AI ay madalas gumawa ng citations na mukhang totoo, exact section numbers, exact titles. Pero hindi totoo."
    ms_iva "(mababa) Tanong ko lang sa iyo, ikaw mismo ba ang sumulat ng citation na iyon, o kinopya mo ang output ng AI nang hindi bina-verify?"

    ## CRITICAL CHOICE 6-A: Determines got_caught variable
    menu:
        "Totoo po, Ma'am. Hindi ko nabasa ang aktwal na batas. Kinopya ko ang AI output.":
            $ got_caught = False
            $ ct_change(15)
            $ mot_change(5)
            if player_gender == "male":
                mc_m "Totoo po, Ma'am. Hindi ko bina-verify ang citation. Kinopya ko ang sagot ng AI. Pasensya na po."
            else:
                mc_f "Hindi ko po bina-verify. Kinopya ko ang output ng AI nang hindi nag-check. Mali ko po, Ma'am."
            show ms_iva thinking at center with dissolve
            ms_iva "..."
            ms_iva "Salamat sa katapatan. Hindi ko ito basta-basta babalewalain, mayroon itong epekto sa iyong grade. Pero bibigyan kita ng pagkakataon na mag-resubmit ng tamang papel sa loob ng isang linggo."
            ms_iva "At ang conditions: sarili mong salita. Actual citations mula sa RA 10173 at RA 10175. At isang talata tungkol sa kung ano ang natutunan mo mula sa pagkakamaling ito."
            if player_gender == "male":
                mc_m "Opo, Ma'am. Salamat po."
            else:
                mc_f "Opo. Salamat po, Ma'am. Gagawin ko."
            narrator "(Lumakad siya. Nanatili kang nakatanga sa hallway, nang halos isang minuto.)"
            $ grade_change("cyber", -10)

        "N-Nabasa ko po, Ma'am. Baka nagkamali lang ng pag-cite.":
            $ got_caught = True
            $ ct_change(-20)
            $ mot_change(-15)
            if player_gender == "male":
                mc_m "N-Nabasa ko po 'yun, Ma'am. Baka nagkamali lang po ako ng pag-cite ng section number."
            else:
                mc_f "N-Nabasa ko po siya, Ma'am. Siguro nagkamali lang ako ng format ng citation."
            show ms_iva disappointed at enter_center_rise
            ms_iva "..."
            ms_iva "Sineseryoso ko ang academic integrity sa aking klase. At sineseryoso ko rin ang bawat estudyante."
            ms_iva "Ibig sabihin: alam ko kung kailan nagsisinungaling ang isang estudyante sa harap ko."
            narrator "(Bumagsak ang mundo nang kaunti.)"
            ms_iva "Huwag kang pumasok sa aking klase ng walang resubmission bukas, at ng kumpletong explanation kung paano mo gagawin ito nang tama."
            ms_iva "At gagawin nating opisyal ang pangyayaring ito sa department."
            narrator "(Lumakad na siya. Nanatili ka sa hallway.)"
            narrator "(Hindi ka sumasagot. Wala ka nang maisasagot.)"
            $ grade_change("cyber", -20)

    hide ms_iva with dissolve

    ## ── SCENE 6-2: After the confrontation ──────────────────────────────────
    scene bg_canteen with dissolve
    $ safe_play("music", "audio/bgm/bgm_sad.ogg", loop=True)
    $ day_label = "Week 6, Hapon"

    if player_bestfriend == "carl":
        show carl stressed at center with dissolve
        carl "Huy. Narinig ko. Okay ka lang ba?"
        if player_gender == "male":
            mc_m "Hindi ko inexpect na ganoon ka-strict si Ms. Iva."
        else:
            mc_f "Hindi ko inexpect na... ganoon pala talaga 'yun. Na mapapansin."
        carl "Lagi naman sinasabi ni Kent, 'verify your citations.' Ngayon alam mo na kung bakit."
        hide carl with dissolve
    else:
        show carly stressed at center with dissolve
        carly "Narinig ko kung ano ang nangyari sa hallway. Okay ka ba?"
        if player_gender == "male":
            mc_m "Okay lang. Medyo napahiya ako, pero... kailangan ko nang harapin ito."
        else:
            mc_f "Hindi okay, pero... kailangan ko nang gawin ng tama."
        carly "Tama 'yun. Nandito ako kung kailangan mo ng help sa resubmission."
        hide carly with dissolve

    ## ── SCENE 6-3: Cybersecurity redo activity ───────────────────────────────
    if not got_caught:
        scene bg_lab with dissolve
        $ safe_play("music", "audio/bgm/bgm_study.ogg", loop=True)
        $ day_label = "Week 6, Resubmission Prep"

        narrator "(Library. Ang laptop mo ay nakabukas sa dalawang tab: ang Official Gazette ng Pilipinas at ang blank na document.)"
        narrator "(Binabasa mo nang maingat, ang tunay na RA 10173. Section 3. Section 4. Section 16.)"
        narrator "(Iba ang pakiramdam kapag ang sarili mong mata ang nagbabasa. Mabagal. Pero totoo.)"

        show screen minigame(
            "Cybersecurity, RA 10173 (Data Privacy Act)",
            "Alin sa mga sumusunod ang isang karapatan ng data subject sa ilalim ng RA 10173 (Data Privacy Act of 2012)?",
            [
                "A. Karapatang mag-access ng personal data na hawak ng isang organization",
                "B. Karapatang tanggapin ang suweldo ng data controller",
                "C. Karapatang mag-imbak ng datos sa ibang tao nang walang pahintulot",
                "D. Karapatang baguhin ang privacy policy ng isang kumpanya"
            ],
            0,
            "cyber",
            12,
            15
        )

        scene bg_lab with dissolve
        narrator "(Natapos mo ang resubmission paper. Bawat citation ay may totoong section number.)"
        narrator "(Matagal. Pero tunay na iyo.)"
        $ grade_change("cyber", 10)

    return
