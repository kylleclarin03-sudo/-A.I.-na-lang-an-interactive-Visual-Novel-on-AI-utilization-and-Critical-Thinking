## game/chapter1.rpy
## Chapter 1 — "Day One Vibes" (Week 1)

label chapter1:
    show screen hud
    call screen chapter_title("1", "Day One Vibes", "Week 1 — 'Sana ol, may motivation.'")
    $ day_label = "Day 1 — Umaga"
    $ current_week = 1

    ## ── SCENE 1-1: First Day, Classroom ──────────────────────────────────────
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_classroom.ogg", loop=True)

    narrator "Amoy floor wax at anxiety ang classroom. Humingi ka ng upuan sa gitna — hindi masyadong harapan, hindi obvious sa likod."

    if player_bestfriend == "carl":
        show carl normal at right with dissolve
        carl "Huy, nag-review ka ba ng syllabus?"
        if player_gender == "male":
            mc_m "Meron palang syllabus?"
        else:
            mc_f "Meron palang syllabus?"
        carl "Classic. Okay lang 'yan."
    else:
        show carly normal at right with dissolve
        carly "Huy, nag-review ka ba ng syllabus?"
        if player_gender == "male":
            mc_m "Meron palang syllabus?"
        else:
            mc_f "Meron palang syllabus?"
        carly "Classic. Okay lang 'yan, basta huwag lang iwanan ako sa lab activity."

    show kent normal at left with dissolve
    kent "Actually, reading the syllabus is a recommended practice. Nakakatanggal ng first-week anxiety ng approximately forty percent, according to a 2019 study on—"
    if player_bestfriend == "carl":
        carl "Kent."
    else:
        carly "Kent."
    kent "Opo?"
    if player_bestfriend == "carl":
        carl "Umupo ka na."
    else:
        carly "Salamat, umupo ka na."
    kent "...Valid lang naman ang concern ko."

    show gabby normal at center with dissolve
    gabby "Uy! Survive tayo ng another sem! Excited na ko sa breaks natin!"
    narrator "(Tinitingnan mo ang lahat habang nauupo ka. Para kang may nagsisimula — hindi lang isang semester, kundi isang bagay. Hindi mo sure kung ano.)"

    hide carl with dissolve
    hide carly with dissolve
    hide kent with dissolve
    hide gabby with dissolve

    ## Ms. Iva enters
    $ safe_stop("music")
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    show ms_iva normal at center with dissolve

    ms_iva "Good morning. Hindi ko sasayangin ang inyong oras sa mga introductions. Alam ninyo kung sino ako. Alam ninyo ang subject na ito."
    ms_iva "Ang gusto ko pag-usapan ngayon — isang bagay na ginagamit ninyo lahat simula pa noong high school."
    narrator "(Nagsulat siya sa board: ARTIFICIAL INTELLIGENCE.)"
    ms_iva "AI ay isang tool. Isang napakagandang tool. Ang tanong ko sa inyong lahat — at gusto ko itong seryosohin — ay ito:"
    ms_iva "Kailan nagiging crutch ang isang tool?"
    narrator "(Tahimik. May kumukuha sa'yo sa dibdib.)"

    show gabby normal at right with dissolve
    if player_bestfriend == "carl":
        show carl normal at left with dissolve
        gabby "(bumubulong) Yan na. Lecture agad. First day pa lang."
        carl "(bumubulong) Shh."
    else:
        show carly normal at left with dissolve
        gabby "(bumubulong) Yan na. Lecture agad. First day pa lang."
        carly "(bumubulong) Shh."

    ms_iva "Sa katapusan ng semester na ito, inaasahan ko na masasagot ninyo ang tanong na iyon. Hindi para sa akin. Para sa inyo."
    hide ms_iva with dissolve
    hide carl with dissolve
    hide carly with dissolve
    hide gabby with dissolve

    ## ── SCENE 1-2: Canteen after class ───────────────────────────────────────
    scene bg_canteen with dissolve
    $ safe_play("music", "audio/bgm/bgm_canteen.ogg", loop=True)
    $ day_label = "Day 1 — Hapon"

    narrator "Nahanap ng grupo ang mesa. Tray ng kanin, ulam, malamig na inumin. Ang universal na college meal."
    show gabby normal at left with dissolve
    if player_bestfriend == "carl":
        show carl normal at right with dissolve
    else:
        show carly normal at right with dissolve
    show kent normal at center with dissolve

    gabby "Hoy, 'yung sinabi ni Ms. Iva — 'when does a tool become a crutch' — grabe ang drama. Obvious naman kung sino ang tinutukoy nun."
    kent "Actually, tinutukoy niya ang isang documented na phenomenon sa cognitive science — skill atrophy. Kapag paulit-ulit mong inexternalize ang isang cognitive task sa isang tool, ang neural pathway na nag-ha-handle nun ay—"
    gabby "Kent, kumain ka muna."
    kent "...Valid lang ang concern ko."

    if player_bestfriend == "carl":
        carl "Anong meron sa'yo? Masyado kang tahimik kanina."
        if player_gender == "male":
            mc_m "Naiisip ko lang 'yung sinabi ni Ms. Iva. Alam mo naman 'yung nangyari, noong online classes."
        else:
            mc_f "Naiisip ko lang 'yung sinabi ni Ms. Iva. Alam mo naman 'yung nangyari, noong online classes."
        carl "(mas seryoso) Oo. Lahat tayo gumawa ng shortcuts noon. Walang choice."
    else:
        carly "Huy, anong meron? Masyado kang tahimik kanina."
        if player_gender == "male":
            mc_m "Naiisip ko lang 'yung sinabi ni Ms. Iva. Alam mo naman 'yung nangyari, noong online classes."
        else:
            mc_f "Naiisip ko lang 'yung sinabi ni Ms. Iva. Alam mo naman 'yung nangyari, noong online classes."
        carly "(mas seryoso) Oo. Lahat tayo gumawa. Pero iba na ngayon, 'di ba? Face-to-face na."

    if player_gender == "male":
        mc_m "Pero may choice. Hindi lang natin pinili 'yun noon."
    else:
        mc_f "Pero may choice tayo noon. Hindi lang natin pinili 'yun."

    narrator "(Tahimik ang mesa ng isang segundo. Tapos binasag ni Gabby.)"
    gabby "Uy, seryoso naman ang vibes! Kain na at mag-usap tayo ng masaya! May bagong season nga pala!"
    narrator "(Nagbago ang mood. Tawanan. Lumipas ang sandali. Pero hindi ka nito iniwan.)"
    hide gabby with dissolve
    hide carl with dissolve
    hide carly with dissolve
    hide kent with dissolve

    ## ── SCENE 1-3: First assignment dropped ─────────────────────────────────
    scene bg_hallway with dissolve
    $ safe_play("music", "audio/bgm/bgm_classroom.ogg", loop=True)
    $ day_label = "Day 2 — Hapon"

    show mr_kai normal at left with dissolve
    mr_kai "Class, naka-post na ang inyong unang programming activity. Basic Python — input/output, conditionals, loops. Due in three days. Independently, please."
    mr_kai "Gusto ko makita ang inyong sariling logic, hindi ang generated na sagot. Magiging malinaw kung alin ang alin."
    hide mr_kai with dissolve

    show gabby normal at right with dissolve
    gabby "(agad na tiningnan ang phone) Three days? Kukunin ko 'to later, sampung minuto, tapos na."
    show kent normal at center with dissolve
    kent "Gabby. Specifically sinabi ni Mr. Kai na independently—"
    gabby "Lahat naman gumagawa nun, Kent."

    if player_bestfriend == "carl":
        show carl normal at left with dissolve
        carl "Ikaw? Gagawin mo?"
    else:
        show carly normal at left with dissolve
        carly "Ikaw? Paano mo gagawin?"

    ## CHOICE NODE 1-A: How to handle first programming assignment
    menu:
        "Gagawin ko. Matututo naman tayo dito.":
            $ ct_change(8)
            $ mot_change(5)
            if player_gender == "male":
                mc_m "Gagawin ko. Para naman matuto."
            else:
                mc_f "Gagawin ko. Para matuto naman."
            if player_bestfriend == "carl":
                carl "Seryoso? Okay ka talaga eh."
            else:
                carly "Oo naman! Sama-sama tayo, I'll try din."
            narrator "(Pumunta ka sa library pagkatapos ng klase. Medyo matagal, pero natapos mo. Sa sarili mo.)"
            $ grade_change("programming", 5)

        "Depende. Subukan ko muna bago mag-AI.":
            $ ct_change(3)
            if player_gender == "male":
                mc_m "Tignan ko muna kung kaya ko."
            else:
                mc_f "Subukan ko muna. Kung talagang hindi ko kaya, saka lang."
            if player_bestfriend == "carl":
                carl "Fair enough. Text mo kung may tanong."
            else:
                carly "Sige, text mo ako kung may part na hindi mo gets."
            narrator "(Sinubukan mo. May mga parteng napagdaanan ng maayos. May ilang linya na nag-google ka. Pero ikaw pa rin ang nag-type ng logic.)"

        "I-AI ko na lang. Tatlong araw lang naman.":
            $ ct_change(-8)
            $ mot_change(-3)
            $ use_ai("programming", 8)
            if player_gender == "male":
                mc_m "(Sa isip mo) I-AI na lang siguro. Mabilis lang naman 'to."
            else:
                mc_f "(Sa isip mo) I-AI na lang siguro. Mas mabilis naman."
            narrator "(Pinindot mo ang app. Nag-generate. Kinopya mo ang sagot. Tapos na sa loob ng sampung minuto.)"
            narrator "(Nakita ng AI ang pattern. Sumugal ka. Pero may pumansin...)"
            call ai_used_result from _c1_ai_result

    hide gabby with dissolve
    hide kent with dissolve
    hide carl with dissolve
    hide carly with dissolve
    return
