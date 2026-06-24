## game/chapter4.rpy
## Chapter 4, "May Test Bukas" (Week 4, Midterms Approaching)

label chapter4:
    call screen chapter_title("4", "May Test Bukas", "Week 4, 'Kailangan mag-review.'")
    $ day_label = "Week 4, Gabi"
    $ current_week = 4

    ## ── SCENE 4-1: Night before the exam ─────────────────────────────────────
    scene bg_bedroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_night.ogg", loop=True)

    narrator "(Gabi bago ang Networking midterm. Ang notes mo ay nakabukas sa laptop. Ang phone mo ay nakapatay, naka-charge lang.)"
    narrator "(Alas nwebe pa lang. Maaga ka. Para sa iyo, kahit paano.)"

    groupchat "GABBY: huy last game na please!! ranked!! isa lang HAHA"
    groupchat "GABBY: wag ka magtampo pag hindi ka sumama"

    if player_bestfriend == "carl":
        groupchat "CARL: huy matulog na kayo. test bukas."
        groupchat "GABBY: luhh yoko nga 😤"
    else:
        groupchat "CARLY: seryoso 'to, matulog na kayo. review muna kayo."
        groupchat "GABBY: ayy pabibo"

    groupchat "KENT: The recommended pre-exam sleep duration is 7-9 hours. REM sleep is critical for memory consolidation of newly acquired,"
    groupchat "GABBY: KENT HINDI KO NEED ANG SCIENCE"
    groupchat "REY: zzz"

    narrator "(Ang phone mo ay naka-mute. Ang notes mo ay nakabukas. Ngunit ang kamay mo ay kating-kati na mag-laro.)"

    ## CHOICE NODE 4-A
    menu:
        "Matulog na. Review na lang sana sa umaga.":
            $ ct_change(8)
            $ mot_change(5)
            if player_gender == "male":
                mc_m "(I-type sa chat) Matulog na ako. GL sa ranked mga baliw."
            else:
                mc_f "(I-type sa chat) Matutulog na ko. GL sa ranked mga baliw."
            narrator "(Nagising ka nang may oras pa. Nag-review ng isang oras. Kumain ng almusal. Nakarating sa klase nang maaga.)"
            $ grade_change("networking", 8)

        "Isa lang na laro, tapos matutulog na talaga.":
            $ ct_change(-5)
            $ mot_change(-5)
            if player_gender == "male":
                mc_m "(I-type sa chat) Fine. Isa lang. ISA."
            else:
                mc_f "(I-type sa chat) Okay FINE. Isa lang ha."
            narrator "(Tatlong laro pagkatapos, alas dose na ng hatinggabi. Natulog ka nang walang review.)"
            narrator "(Nagising ka nang late. PATAY. Alarm ay hindi narinig.)"
            $ mot_change(-3)
            jump chapter4_late_scene

        "Mag-aral pa ng konti, kahit pagod na.":
            $ ct_change(5)
            if player_gender == "male":
                mc_m "(I-type sa chat) Mag-aral muna ko mga boss. Kayo na muna."
            else:
                mc_f "(I-type sa chat) Nah, mag-aral muna ko mga boss. Kayo na lang."
            narrator "(Pinagpatuloy mo ang review. Dalawang oras. Pagod pero may natandaan ka.)"
            narrator "(Natulog ka nang alas onse. Nagising ka nang may oras pa. At nakarating ka pa sa klase nang maaga.)"
            $ grade_change("networking", 5)

    ## ── SCENE 4-2: Running late ───────────────────────────────────────────────
    scene bg_hallway with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 4, Exam Day"
    narrator "(Nakarating ka sa klase. Nakarating, iyon ang mahalaga.)"
    jump chapter4_exam

label chapter4_late_scene:
    scene bg_hallway with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 4, Exam Day (Late)"

    show mr_earns normal at enter_center_rise
    mr_earns "Twelve minutes late."
    narrator "(Wala siyang ibang sinabi. Pinagmasdan ka niya habang umuupo ka.)"
    mr_earns "Exam na. Walang phone."
    hide mr_earns with dissolve
    $ grade_change("networking", -8)
    narrator "(Ang mga tanong sa exam, nakita mo na ang ilan sa kanila sa notes mo. Kahapon. Bago ka natulog nang maaga.)"

## ── SCENE 4-3: Networking Long Test ──────────────────────────────────────────
label chapter4_exam:
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)

    show mr_earns normal at enter_center_rise
    mr_earns "Phones in your bags. Bags in front. Begin."
    hide mr_earns with dissolve

    narrator "(First question, subnetting. You know the formula. Or so you think.)"
    narrator "(Five questions in total. Your phone is locked away. No shortcuts this time.)"
    jump chapter4_subnet_q1

## ── Chapter 4: Subnetting Exam (5 questions) ─────────────────────────────────
## Reference: Cisco CCNA 200-301, Subnetting fundamentals

label chapter4_subnet_q1:
    show screen minigame(
        "Midterm Exam, Subnetting (1/5), Phone Locked!",
        "Given the network address 192.168.10.0/26,\nwhat is the maximum number of usable hosts per subnet?",
        [
            "A. 30",
            "B. 62",
            "C. 126",
            "D. 14"
        ],
        1,
        "networking",
        12,
        5,
        correct_label="chapter4_subnet_q1_correct",
        wrong_label="chapter4_subnet_q1_wrong"
    )
    return

label chapter4_subnet_q1_correct:
    narrator "(Correct! /26 means 6 bits for hosts. 2^6 = 64, minus network and broadcast = 62 usable.)"
    jump chapter4_subnet_q2

label chapter4_subnet_q1_wrong:
    narrator "(Not quite. A /26 prefix leaves 6 host bits. Calculate 2^6 then subtract 2 for network and broadcast addresses.)"
    jump chapter4_subnet_q1

## ── Question 2: Subnet Mask ──────────────────────────────────────────────────
## Reference: Cisco CCNA 200-301, Subnet mask calculation
label chapter4_subnet_q2:
    show screen minigame(
        "Midterm Exam, Subnetting (2/5), Phone Locked!",
        "What is the subnet mask equivalent of the /28 prefix length?",
        [
            "A. 255.255.255.192",
            "B. 255.255.255.224",
            "C. 255.255.255.240",
            "D. 255.255.255.248"
        ],
        2,
        "networking",
        12,
        5,
        correct_label="chapter4_subnet_q2_correct",
        wrong_label="chapter4_subnet_q2_wrong"
    )
    return

label chapter4_subnet_q2_correct:
    narrator "(That's right! /28 = 255.255.255.240. 28 bits = 255.255.255.240, which leaves 4 host bits.)"
    jump chapter4_subnet_q3

label chapter4_subnet_q2_wrong:
    narrator "(Think about it in binary. A /28 means the first 28 bits are network bits. 24 bits = 255.255.255, then 4 more bits = 240.)"
    jump chapter4_subnet_q2

## ── Question 3: Number of Subnets ────────────────────────────────────────────
## Reference: Cisco CCNA 200-301, Subnet creation
label chapter4_subnet_q3:
    show screen minigame(
        "Midterm Exam, Subnetting (3/5), Phone Locked!",
        "You are given 192.168.1.0/24. You need 4 subnets with equal hosts.\nWhat subnet mask should you use and how many hosts per subnet?",
        [
            "A. /25, 126 hosts per subnet",
            "B. /26, 62 hosts per subnet",
            "C. /27, 30 hosts per subnet",
            "D. /28, 14 hosts per subnet"
        ],
        1,
        "networking",
        12,
        5,
        correct_label="chapter4_subnet_q3_correct",
        wrong_label="chapter4_subnet_q3_wrong"
    )
    return

label chapter4_subnet_q3_correct:
    narrator "(Correct! Borrowing 2 bits from /24 gives /26, creating 4 subnets (2^2) with 62 usable hosts each.)"
    jump chapter4_subnet_q4

label chapter4_subnet_q3_wrong:
    narrator "(To create 4 subnets, you need to borrow enough bits. 2 bits = 4 subnets. Starting from /24, borrowing 2 gives /26.)"
    jump chapter4_subnet_q3

## ── Question 4: Broadcast Address ────────────────────────────────────────────
## Reference: Cisco CCNA 200-301, Identifying broadcast addresses
label chapter4_subnet_q4:
    show screen minigame(
        "Midterm Exam, Subnetting (4/5), Phone Locked!",
        "The network 172.16.0.0 is subnetted with a /20 mask.\nWhat is the broadcast address of the third subnet (subnet 3)?",
        [
            "A. 172.16.31.255",
            "B. 172.16.47.255",
            "C. 172.16.63.255",
            "D. 172.16.15.255"
        ],
        1,
        "networking",
        12,
        5,
        correct_label="chapter4_subnet_q4_correct",
        wrong_label="chapter4_subnet_q4_wrong"
    )
    return

label chapter4_subnet_q4_correct:
    narrator "(Right! /20 = 255.255.240.0. Each subnet has 16 hops. Subnet 3 starts at 172.16.32.0, so broadcast is 172.16.47.255.)"
    jump chapter4_subnet_q5

label chapter4_subnet_q4_wrong:
    narrator "(With a /20 mask, the block size is 16 in the third octet. Subnet 0 = 172.16.0.0, Subnet 1 = .16.0, Subnet 2 = .32.0. The broadcast is the next subnet minus 1.)"
    jump chapter4_subnet_q4

## ── Question 5: Wildcard Mask ────────────────────────────────────────────────
## Reference: Cisco CCNA 200-301, ACL and wildcard masks
label chapter4_subnet_q5:
    show screen minigame(
        "Midterm Exam, Subnetting (5/5), Phone Locked!",
        "What wildcard mask matches all hosts in the 192.168.1.0/27 network?",
        [
            "A. 0.0.0.31",
            "B. 0.0.0.63",
            "C. 0.0.0.15",
            "D. 0.0.0.7"
        ],
        0,
        "networking",
        12,
        5,
        correct_label="chapter4_subnet_q5_correct",
        wrong_label="chapter4_subnet_q5_wrong"
    )
    return

label chapter4_subnet_q5_correct:
    narrator "(Perfect! /27 = 255.255.255.224. Wildcard = inverse of mask = 0.0.0.31. You aced the subnetting portion!)"
    narrator "(You finish and flip the paper over. Deep breath. Then another.)"
    narrator "(You're not sure about every answer. But you tried. No AI. No phone. Just you and your knowledge.)"
    jump chapter4_exam_done

label chapter4_subnet_q5_wrong:
    narrator "(Wildcard mask is the inverse of the subnet mask. For /27 = 255.255.255.224. Subtract each octet from 255.)"
    jump chapter4_subnet_q5

## ── Exam completion ──────────────────────────────────────────────────────────
label chapter4_exam_done:
    scene bg_classroom with dissolve
    narrator "(Natapos ang exam. Binaliktad mo ang papel. Huminga ng malalim.)"
    if player_bestfriend == "carl":
        show carl normal at right with dissolve
        carl "Kumusta? Mahirap ba?"
        if player_gender == "male":
            mc_m "Okay lang. 'Yung subnetting... hindi ko sure."
        else:
            mc_f "Ewan. Sagot ko sa subnetting, 62. Tama ba?"
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