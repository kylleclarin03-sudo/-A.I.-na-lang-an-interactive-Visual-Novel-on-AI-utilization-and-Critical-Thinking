## game/chapter1.rpy
## Chapter 1, "Day One Vibes" (Week 1)

label chapter1:
    call screen chapter_title("1", "Day One na?", "Week 1, 'Sana ol, may motivation.'")
    $ day_label = "Day 1, Morning"
    $ current_week = 1

## ── SCENE 1-1: First Day, Classroom ──────────────────────────────────────
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_campus.ogg", loop=True)
    $ show_hud = False


    narrator "First day of the semester. You know the drill: walk in, find a seat that's not sa harap, but not masyado sa likod (nobody wants to be the taga-sagot ng katok sa pinto)."
    narrator "You settle somewhere in the middle. The sweet spot. The 'pwede na' zone."
    narrator "Amoy cables, at yung specific na brand of panic na alam mong tatagal ng isang semester."

    show gabby normal at center with dissolve
    gabby "UY! Guys! tayo na naman magkakaklase!"
    gabby "Sabog na naman tayo this sem! WOOOO!"
    narrator "(Pumalakpak siya nang isang beses. Malakas. May energy na nakakahawa.)"

    show kent normal at left with dissolve
    kent "Technically, we're not a group. We're a cluster of individuals who happened to share the same enrollment block. But yes, emotionally speaking, group tayo."
    gabby "Kent."
    gabby "Minsan gusto kita sapakin."
    kent "That would be an inefficient use of your kinetic energy, but I appreciate the sentiment po."

    if player_bestfriend == "carl":
        show carl normal at right with dissolve
        carl "(sabay upo sa tabi mo) Huy. Nag-review ka ba ng syllabus?"
        if player_gender == "male":
            mc_m "Meron na palang syllabus?"
        else:
            mc_f "Meron na palang syllabus?"
        carl "(tawa) Classic. Ayos lang 'yan. Basta magkaklase tayo, keri."
        carl "Saka sabi ni Gabby, madami daw 'yung breaks this sem. Parang nag-design si Ms. Iva ng calendar para sa mga gusto matulog."
        kent "Actually, I already computed the break distribution. May total of 14 non-instructional days across the semester, excluding holidays. That's above the national average for IT programs."
        gabby "See! Sinabi ko sa inyo! Break tayo nang break!"
        carl "(sa iyo, mababa) Si Kent, ginawang research paper ang enrollment."
        hide carl with dissolve
    else:
        show carly normal at right with dissolve
        carly "(sabay upo sa tabi mo) Huy! Same block tayo! Sabi ko na eh. Magkaklase tayo ulit."
        if player_gender == "male":
            mc_m "Buti na lang. Kung hindi, wala akong kausap."
        else:
            mc_f "Buti na lang. Kung hindi, wala akong karamay."
        carly "Totoo!"
        carly "Sabi ni Gabby, maraming breaks daw this sem. Baka mag-enjoy na ako sa IT."
        kent "Actually, I already computed the break distribution. May total of 14 non-instructional days across the semester, excluding holidays. That's above the national average for IT programs."
        gabby "See! Panalo tayo!"
        carly "(sa iyo, mababa) Ginawa ni Kent Excel sheet ang semester natin."
        hide carly with dissolve

    show kent normal at left with dissolve
    kent "Anyway. May nilista akong mga tips para sa first day. Isang page lang naman. In 8-point font."
    gabby "Isang PAGE? Kent, first day pa lang. Relax."
    kent "I also made a pie chart. For motivation."
    gabby "...Sige, send mo sa GC."
    kent "Na-send ko na noong 6:47 AM."
    narrator "(Tiningnan mo ang phone. May notification ka nga mula sa group chat, isang PDF na may title na 'SEMESTER OPTIMIZATION GUIDE v1.3'.)"
    narrator "(v1.3. Ibig sabihin, dalawang beses niya itong in-update bago pa man magsimula ang klase.)"

    show rey normal at right with dissolve
    narrator "(Pumasok si Rey. Walang maingay na pagbati. Umupo sya sa tabi ng bintana. Kinuha ang notebook. At nagbasa.)"
    narrator "(Ilan sa inyo, kasama si Kent, ay napatingin sa kanya.)"
    gabby "(bulong) Si Rey, seryoso agad. First day pa lang, ang tense na."
    kent "(bulong) Actually, I admire the preparedness. Yannn that's what I call a pro-gamer move."
    rey "Guys... Naririnig ko kayo."
    gabby "Sorry sorry."
    kent "No regrets. Angas mo men *thumbs up*"

    narrator "(Tumawa ka nang tahimik. Ganito pala ulit: yung energy na sabay-sabay kang napapagod at napapasaya.)"

    hide gabby with dissolve
    hide kent with dissolve
    hide rey with dissolve

    ## Ms. Iva enters
    $ safe_stop("music")
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    show ms_iva normal at center with dissolve

    ms_iva "Good morning everyone. I am Ms. Iva, your instructor for this semester. I hope you are all as excited as I am to start this journey together."
    ms_iva "Hindi na tayo mag-sasayang nang oras sa mga introductions. Alam ko na magkakakilala na kayo."
    ms_iva "At sawang sawa na kayo sa isa't isa. Kaya let's get down to business."
    ms_iva "Ang gusto ko pag-usapan ngayon, isang bagay na ginagamit ninyo lahat simula pa noong high school."
    narrator "(Nagsulat siya sa board: ARTIFICIAL INTELLIGENCE.)"
    ms_iva "Ang AI ay isang tool. I am sure alam na ninyong lahat kung ano ito."
    ms_iva "Ang tanong ko sa inyong lahat, at gusto ko itong seryosohin nyo to:"
    ms_iva "Kailan nagiging crutch ang isang tool?"
    narrator "(Ang tahimik... You felt something rising from within.)"

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
    if player_bestfriend == "carl":
        hide carl with dissolve
    else:
        hide carly with dissolve
    hide gabby with dissolve
    narrator "Class continues, pero hindi mo na masyadong naririnig. Paulit-ulit ang tanong ni Ms. Iva sa isip mo. What does it mean? 'Kailan nagiging crutch ang isang tool?'"


    ## ── SCENE 1-2: Canteen after class ───────────────────────────────────────
    scene bg_canteen with dissolve
    $ safe_play("music", "audio/bgm/bgm_canteen.ogg", loop=True)
    $ day_label = "Day 1, Hapon"

    narrator "Nahanap ng grupo ang mesa. Tray ng kanin, ulam, malamig na inumin. Ang universal na college meal."
    show gabby normal at enter_from_left
    if player_bestfriend == "carl":
        show carl normal at right_idle
    else:
        show carly normal at right_idle
    show kent normal at center_idle

    gabby "Hoy, 'yung sinabi ni Ms. Iva, grabe ang O.A. Obvious naman kung sino ang tinutukoy nun."
    kent "Actually, tinutukoy niya ang isang documented na phenomenon sa cognitive science, skill atrophy. Kapag paulit-ulit mong inexternalize ang isang cognitive task sa isang tool, ang neural pathway na nag-ha-handle nun ay,"
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
    gabby "Uy, ang seryoso naman ang aura nyo! Kain na at mag-usap tayo ng masaya! May bagong season nga pala! G na!"
    narrator "(Nagbago ang mood. Tawanan. Lumipas ang sandali. Pero hindi ka nito iniwan.)"
    hide gabby with dissolve
    if player_bestfriend == "carl":
        hide carl with dissolve
    else:
        hide carly with dissolve
    hide kent with dissolve

    ## ── SCENE 1-3: First assignment dropped ─────────────────────────────────
    scene bg_hallway with dissolve
    $ safe_play("music", "audio/bgm/bgm_classroom.ogg", loop=True)
    $ day_label = "Day 2, Hapon"

    show mr_kai normal at left with dissolve
    mr_kai "Class, naka-post na ang inyong unang programming activity. Basic Python, input/output, conditionals, loops. Due in three days. Independently po, please."
    mr_kai "Gusto ko makita ang inyong sariling logic, hindi ang generated na sagot. Magiging malinaw kung alin ang alin."
    hide mr_kai with dissolve

    show gabby normal at right with dissolve
    gabby "(agad na tiningnan ang phone) Three days? Kukunin ko 'to later, sampung minuto, tapos na."
    show kent normal at center with dissolve
    kent "Gabby. Specifically sinabi ni Mr. Kai na independently,"
    gabby "Lahat naman ata gumagawa nun, Kent."

    if player_bestfriend == "carl":
        show carl normal at left with dissolve
        carl "Ikaw? Gagawin mo?"
    else:
        show carly normal at left with dissolve
        carly "Ikaw? Paano mo gagawin?"

    ## CHOICE NODE 1-A: How to handle first programming assignment
    $ show_hud = True
    menu:
        "Gagawin ko. Matututo naman tayo dito.":
            $ ct_change(8)
            $ mot_change(5)
            if player_gender == "male":
                mc_m "Gagawin ko. Para naman matuto."
            else:
                mc_f "Gagawin ko. Para matuto naman."
            if player_bestfriend == "carl":
                carl "Seryoso yan? Sige na nga."
            else:
                carly "Oo naman! Sama-sama tayo, I'll try din."
            narrator "(Pumunta ka sa library pagkatapos ng klase. Nag-open ka ng IDE. Nagsimula kang mag-code. May mga parteng na-stuck ka, pero nag-research ka, nag-google, nag-YouTube. Pero natapos mo rin sa huli.)"
            narrator "(Medyo matagal, pero natapos mo. Sa sarili mo.)"
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
                mc_f "(Sa isip mo) I-AI na lang siguro. Para mabilis."
            narrator "(Pinindot mo ang app. Nag-generate. Kinopya mo ang sagot. Tapos na sa loob ng sampung segundo.)"
            narrator "(Hmm... Hindi mo maintindihan kahit isang linya nito. Pero ang importante..)"
            narrator "(Matapos na agad.)"
            call ai_used_result from _c1_ai_result

    hide gabby with dissolve
    hide kent with dissolve
    if player_bestfriend == "carl":
        hide carl with dissolve
    else:
        hide carly with dissolve
    return