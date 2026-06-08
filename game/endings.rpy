## game/endings.rpy
## All six endings for A.I. na lang!

label ending_sequence:
    ## Calculate and jump to the correct ending
    $ ending_target = determine_ending()
    jump expression ending_target

# ══════════════════════════════════════════════════════════════════════════════
# ENDING 1: SPECIAL GOOD, "The Real Deal"
# Condition: All ≥ 85, ai_use_count == 0, CT ≥ 75
# ══════════════════════════════════════════════════════════════════════════════
label ending_special_good:
    $ safe_play("music", "audio/bgm/bgm_good_ending.ogg", loop=True)
    scene black with dissolve

    narrator "TATLONG BUWAN PAGKATAPOS."
    pause 1.5
    scene bg_classroom with dissolve

    show ms_iva happy at left with dissolve
    ms_iva "Gusto kong ipakita sa klase ang isang bagay ngayon."
    narrator "(Binuhat niya ang isang papel mula sa kanyang mesa. Hindi mo ito inaasahan.)"
    ms_iva "Ang essay na ito tungkol sa cognitive debt. Binasa ko ito nang tatlong beses. Hindi dahil may mali, kundi dahil sa unang pagkakataon ngayong semester, may isang estudyante na hindi sumulat para sa grado."
    ms_iva "Sumulat siya dahil totoong may natutunan siya."
    narrator "(Naramdaman mo ang biglaang init sa iyong dibdib.)"
    ms_iva "May mga bahagi na hindi perpekto ang grammar. May isang transition na awkward. Pero alam mo kung ano ang naroon?"
    narrator "(Tumigil siya. Tumingin sa iyo nang diretso.)"
    ms_iva "Ang tunay na pag-unawa. Hindi perpekto. Pero totoo. At may lakas, may dating, na hindi kayang gayahin ng kahit anong language model."
    ms_iva "Ito ang tunay na estudyanteng na hindi kumuha ng shortcut. Hindi dahil bawal. Kundi dahil pinili niyang matuto."
    narrator "(Tahimik ang buong klase. Ilang segundo. Pakiramdam, mas matagal.)"
    ms_iva "Ipinagmamalaki ko kayo. And I'm sure kilala nyo na kung sino kayo :3."
    narrator "(Nakilala mo ang mga pangalan sa board. Hindi ka makapaniwala.)"
    narrator "(Tumingin ka sa papel. Binasa mo ang sarili mong mga salita.)"
    narrator "(At sa unang pagkakataon sa mahabang panahon, naniwala ka.)"

    if player_gender == "male":
        mc_m "Hindi ito yung papel na gustong isulat ng 'dating' na ako. Pero pinaka-totoo ito sa lahat ng aking sinulat."
    else:
        mc_f "Ito ang pinaka-totoo na sinulat ko. Walang AI na nag-generate nito. Bawat salita, galing sa akin."

    hide ms_iva with dissolve

    scene bg_canteen with dissolve
    $ safe_play("music", "audio/bgm/bgm_good_ending.ogg", loop=True)

    show carl happy at left with dissolve
    show gabby happy at right with dissolve
    show kent happy at center with dissolve
    show rey normal at right with dissolve

    narrator "(Grupo sa canteen. Extra rice para kay Carl. Tahimik na masaya si Kent. Si Gabby, nagnanakaw ng notes mo para sa susunod na semester.)"
    gabby "Pwede mo ba akong turuan? For real this time. 'Yung authentic na paraan."
    if player_gender == "male":
        mc_m "Oo. Pero i-review mo talaga. Sariling utak. Hindi AI."
    else:
        mc_f "Oo, pero sineseryoso ko. Sariling utak mo ang gamitin mo."
    gabby "Sige na, sige na!"
    kent "(bumubulong kay Rey) Miracle."
    rey "..."
    narrator "(Tahimik si Rey. Pero alam mo na, iyon ang kanyang paraan ng pagsabi na proud siya.)"

    hide carl with dissolve
    hide gabby with dissolve
    hide kent with dissolve
    hide rey with dissolve

    scene black with dissolve
    narrator "Hindi ka naging kung ano ang kinuha ng pandemic sa iyo."
    pause 1.0
    narrator "Naging isang bagay na hindi nito kayang kunin."
    pause 1.0
    narrator "Hindi shortcut. Ang mahabang daan. Ang landas mo."
    pause 1.5
    narrator "Graduated with honors apat na semester pagkatapos."
    narrator "Ang AI chat window, nakasara."
    narrator "Hindi dahil ipinagbawal."
    narrator "Kundi dahil hindi mo na kailangan ito para mag-isip para sa iyo."
    pause 2.0

    scene black
    narrator "✦ SPECIAL GOOD ENDING, 'The Real Deal' ✦"
    pause 1.5
    narrator "Networking: [letter_grade(networking_grade)] | Programming: [letter_grade(programming_grade)] | Cybersecurity: [letter_grade(cyber_grade)]"
    narrator "Critical Thinking: [critical_thinking] / 100 | AI Uses: [ai_use_count]"
    return

# ══════════════════════════════════════════════════════════════════════════════
# ENDING 2: GOOD WITH GUILT, "At What Cost?"
# Condition: All ≥ 75, ai_use_count > 3, CT < 55
# ══════════════════════════════════════════════════════════════════════════════
label ending_good_guilt:
    $ safe_play("music", "audio/bgm/bgm_good_ending.ogg", loop=True)
    scene bg_canteen with dissolve

    if player_bestfriend == "carl":
        show carl happy at right with dissolve
        carl "Uy! Lahat tayo nakapasa! Selebrasyon mamaya?"
    else:
        show carly happy at right with dissolve
        carly "Nakapasa tayo! Grabe, akala ko hindi na!"

    narrator "(Masarap ang pagkain. Tama ang grades. Nandoon ang mga numero sa report card.)"

    if player_gender == "male":
        mc_m "(Sa loob mo) Nakapasa ako. Tama ang resulta. Bakit parang walang masyadong nangyari?"
    else:
        mc_f "(Sa loob mo) Nakapasa. Lahat ng subjects. Tapos... ganito lang pala ang pakiramdam?"

    narrator "(Tinitingnan mo ang grade slip. Tapos ang bag mo. Tapos muli ang slip.)"

    if player_gender == "male":
        mc_m "(Sa loob mo) Anong matututunan ko sa susunod na semester? Kung paano gumawa ng mas magandang prompt?"
    else:
        mc_f "(Sa loob mo) Kung tatanungin ako bukas kung ano ang pinag-aralan ko, anong sasabihin ko?"

    hide carl with dissolve
    hide carly with dissolve

    scene black with dissolve
    narrator "Nakapasa ka."
    pause 1.2
    narrator "Ang tanong ni Ms. Iva sa una, kailan nga ba nagiging crutch ang isang tool? Hanggang ngayon, hindi mo pa nasasagot."
    pause 1.0
    narrator "Sa susunod na semester, hindi nawawala ang tanong. Mas humihirap lang pag-isipan."
    pause 1.5

    scene black
    narrator "✦ GOOD ENDING, 'But at What Cost?' ✦"
    pause 1.0
    narrator "Networking: [letter_grade(networking_grade)] | Programming: [letter_grade(programming_grade)] | Cybersecurity: [letter_grade(cyber_grade)]"
    narrator "Critical Thinking: [critical_thinking] / 100 | AI Uses: [ai_use_count]"
    narrator "(Pahiwatig: Subukan muli nang may mas mataas na CT at mas kaunting AI use para sa Special Good Ending.)"
    return

# ══════════════════════════════════════════════════════════════════════════════
# ENDING 3: GOOD SOLID, "Solid Enough"
# Condition: All ≥ 75, ai_use_count ≤ 1, CT ≥ 60
# ══════════════════════════════════════════════════════════════════════════════
label ending_good_solid:
    $ safe_play("music", "audio/bgm/bgm_good_ending.ogg", loop=True)
    scene bg_canteen with dissolve

    if player_bestfriend == "carl":
        show carl happy at right with dissolve
    else:
        show carly happy at right with dissolve

    narrator "(Nakalusot. Hindi lahat perpekto, may ilang grade na medyo mababa.)"
    narrator "(Pero nakalusot. At alam mo kung saan nanggaling ang bawat puntos.)"

    show mr_kai happy at left with dissolve
    mr_kai "Ang coding output mo, may ilang inefficiency, pero sarili mo ang logic. 'Yan ang pinakamahalaga."
    hide mr_kai with dissolve

    if player_gender == "male":
        mc_m "Hindi perpekto ang grades ko. Pero 'yung linya na sinulat ko sa essay ni Ms. Iva, 'yun talaga galing sa akin."
    else:
        mc_f "Hindi perpekto ang lahat. Pero lahat ay earned. Lahat, sarili ko."

    hide carl with dissolve
    hide carly with dissolve

    scene black with dissolve
    narrator "Hindi perpekto. Pero earned."
    pause 1.0
    narrator "Bawat grade na nakusurot ay paalala na nandoon ka, presente, nagsisikap, paminsan-minsang nagkamali sa paraan na nagtuturo ng isang bagay."
    pause 1.5
    narrator "Kita kita sa susunod na semester."
    pause 2.0

    scene black
    narrator "✦ GOOD ENDING, 'Solid Enough' ✦"
    pause 1.0
    narrator "Networking: [letter_grade(networking_grade)] | Programming: [letter_grade(programming_grade)] | Cybersecurity: [letter_grade(cyber_grade)]"
    narrator "Critical Thinking: [critical_thinking] / 100 | AI Uses: [ai_use_count]"
    return

# ══════════════════════════════════════════════════════════════════════════════
# ENDING 4: REDEMPTION, "Not Yet, But Getting There"
# Condition: Any INC, CT ≥ 45 and motivation ≥ 45
# ══════════════════════════════════════════════════════════════════════════════
label ending_redemption:
    $ safe_play("music", "audio/bgm/bgm_sad.ogg", loop=True)
    scene bg_hallway with dissolve

    narrator "(Lumabas ang grades. Isa o dalawang INC.)"
    narrator "(Nakatayo ka sa harapan ng bulletin board. Hindi ka umiiyak. Pero hindi ka rin nagsasalita.)"

    if player_gender == "male":
        mc_m "INC."
    else:
        mc_f "INC."

    if player_bestfriend == "carl":
        show carl normal at right with dissolve
        carl "Okay ka lang ba?"
        if player_gender == "male":
            mc_m "...Okay lang. Alam ko na kung bakit. Yun na ang difference."
        else:
            mc_f "Alam ko kung bakit nangyari ito. Yun ang mahalaga ngayon."
        carl "(mababa) May completion exam. Kent ang nagsabi."
        hide carl with dissolve
    else:
        show carly normal at right with dissolve
        carly "Huy. Okay ka lang ba?"
        if player_gender == "male":
            mc_m "...Okay lang. Alam ko na kung bakit. Yun na ang difference."
        else:
            mc_f "Hindi okay, pero alam ko kung saan nagkamali. At yun na ang simula ng pagbabago."
        carly "May completion exam. Handa ka ba?"
        hide carly with dissolve

    show kent happy at left with dissolve
    kent "May completion exam. Chineck ko na ang schedule. Pwede nating i-prepare."
    hide kent with dissolve

    scene bg_canteen with dissolve
    $ safe_play("music", "audio/bgm/bgm_campus.ogg", loop=True)

    narrator "(Completion exam montage.)"
    narrator "(This time: notes by hand. No AI on the syntax drills.)"
    narrator "(Si Kent, nagtu-tutor sa canteen. Si Rey, tahimik na nanonood, paminsan-minsang nagko-correct ng isang mali.)"
    narrator "(Dumating ang araw ng completion exam.)"
    narrator "(Pumasok ka nang may kumpiyansa na hindi nanggaling sa shortcuts.)"

    scene black with dissolve
    narrator "(Lumabas ang revised grade. INC, removed. Passing mark.)"
    pause 1.5
    narrator "Mas matagal. Pero ngayon, kapag may nagtatanong tungkol sa VLAN configuration o Python scope errors o RA 10173,"
    pause 1.0
    narrator "alam mo na ang sagot."
    pause 1.0
    narrator "Alam mo dahil ikaw mismo ang naglagay nito doon."
    pause 2.0

    scene black
    narrator "✦ REDEMPTION ENDING, 'Not Yet, But Getting There' ✦"
    pause 1.0
    narrator "Critical Thinking: [critical_thinking] / 100 | Motivation: [motivation] / 100"
    narrator "(Nagsimula sa INC. Natapos nang wala. Ganoon ang redemption.)"
    return

# ══════════════════════════════════════════════════════════════════════════════
# ENDING 5: BAD, "Try Again Next Year"
# Condition: Any INC, CT < 30, motivation < 30
# ══════════════════════════════════════════════════════════════════════════════
label ending_bad:
    $ safe_play("music", "audio/bgm/bgm_bad_ending.ogg", loop=True)
    scene bg_hallway with dissolve

    narrator "(Ang grades screen. Tatlong incomplete. Naka-flag ang enrollment system.)"
    if player_gender == "male":
        mc_m "..."
    else:
        mc_f "..."

    scene bg_canteen with dissolve
    narrator "(Nandoon ang grupo pero parang malayo ang usapan.)"
    narrator "(Tumatawa si Gabby sa isang bagay. Nag-check ng phone si Carl. Nagdi-discuss sina Kent at Rey.)"
    narrator "(Umupo ka sa mesa pero hindi ka nagsalita.)"
    narrator "(Wala kang nasabi sa buong tanghalian.)"

    if player_gender == "male":
        mc_m "(Sa loob mo) Alam ko naman ang magiging mangyayari. Alam ko naman iyon. Alam ko na noong simula pa lang."
    else:
        mc_f "(Sa loob mo) Alam ko naman. Alam ko na habang ginagawa ko ang bawat shortcut. Alam ko."

    scene black with dissolve
    narrator "\"See you next year.\""
    pause 2.0
    narrator "Sapat na ang kinuha ng pandemic sa iyo."
    pause 1.0
    narrator "Huwag mong hayaang umulitin ang nangyari."
    pause 1.5

    scene black
    narrator "✦ BAD ENDING, 'See you Next Year' ✦"
    pause 1.0
    narrator "Critical Thinking: [critical_thinking] / 100 | AI Uses: [ai_use_count]"

    menu:
        "Try again (Go back to Chapter 5, make different choices to avoid INCs)":
            jump chapter5
        "Finish the game. (Accept this ending)":
            return
    return

# ══════════════════════════════════════════════════════════════════════════════
# ENDING 6: CAUGHT, "Academic Integrity Issue"
# Condition: got_caught == True and player lied to Ms. Iva
# ══════════════════════════════════════════════════════════════════════════════
label ending_caught:
    $ safe_play("music", "audio/bgm/bgm_bad_ending.ogg", loop=True)
    scene bg_classroom with dissolve

    show ms_iva disappointed at center with dissolve
    ms_iva "Ang academic integrity ay hindi lang isang patakaran. Ito ay isang kasunduan, sa institusyon, sa iyong mga kaklase, at sa iyong sarili."
    ms_iva "Binigyan kita ng pagkakataon na maging tapat. Pero pinili mong hindi eh."
    hide ms_iva with dissolve

    scene bg_hallway with dissolve
    narrator "(Mas mabigat ang pakiramdam ng hallway habang lumalabas ka.)"
    narrator "(Hindi nagtatanong si Carl. Alam na niya kung may nangyari.)"
    narrator "(Mabilis lumayo si Gabby. Si Kent, tinitingnan ka, pero hindi nagsasalita.)"
    narrator "(Si Rey, lumakad palayo nang walang kibo.)"

    if player_gender == "male":
        mc_m "(Sa loob mo) Hindi naman kita nalinlang, Ms. Iva. Niloko ko lang sarili ko."
    else:
        mc_f "(Sa loob mo) Hindi kita nalinlang, Ma'am. Niloko ko ang sarili ko. Matagal na."

    scene black with dissolve
    narrator "\"Kailan nagiging crutch ang isang tool?\""
    pause 1.5
    narrator "Mayroon ka na palaging sagot."
    pause 1.0
    narrator "Ang problema, hindi mo ito inamin sa tamang oras."
    pause 2.0

    scene black
    narrator "✦ CAUGHT ENDING, 'Academic Integrity Issue' ✦"
    pause 1.0
    narrator "got_caught: True | Critical Thinking: [critical_thinking] / 100"

    menu:
        "Try again. (Return to Chapter 6, sagutin nang tapat si Ms. Iva)":
            jump chapter6
        "Finish the game. (Accept the ending)":
            return
    return
