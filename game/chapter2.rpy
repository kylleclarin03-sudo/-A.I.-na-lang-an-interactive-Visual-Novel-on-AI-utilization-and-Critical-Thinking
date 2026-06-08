## game/chapter2.rpy
## Chapter 2, "Laro Muna" (Week 2)

label chapter2:
    call screen chapter_title("2", "Laro Muna! Ano G?", "Week 2, 'Isa lang, tapos reply na sa group chat.'")
    $ day_label = "Week 2, Evening"
    $ current_week = 2

    ## ── SCENE 2-1: Group chat invite vs Packet Tracer assignment ─────────────
    scene bg_bedroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_night.ogg", loop=True)

    narrator "(Hapon ng Martes. Ang laptop mo ay nakabukas sa dalawang tab, Packet Tracer at YouTube. Isa sa kanila ang gumagana.)"
    narrator "(May Networking activity si Sir. Earns: i-configure ang isang basic VLAN topology. Due na bukas ng umaga.)"
    narrator "(Naka-overwhelm yung UI, pero kaya naman. Pwede mo namang i-search.)"


    groupchat "GABBY: uy laro na!! sabay tayo ranked tonight"
    groupchat "GABBY: game na guys please puro darksystem sa random e 😭😭"

    if player_bestfriend == "carl":
        groupchat "CARL: ano g! uy [player_name] ikaw boii?"
    else:
        groupchat "CARLY: in! uy [player_name] ikaw? 👀"

    groupchat "KENT: Nag-finish na ba lahat ng Packet Tracer activity? Mr. Earns checks the whole topology ahh."
    groupchat "GABBY: KENT STOP BEING THE CONSCIENCE OF THE GROUP"
    groupchat "REY: ... (online)"
    groupchat "(system) several people are typing..."


    narrator "(The notifications ay patuloy pa din na dumadating. Ang cursor mo ay naka-hover sa Packet Tracer.)"

    ## CHOICE NODE 2-A
    menu:
        "Tapusin muna ang Packet Tracer, tapos laro.":
            $ ct_change(10)
            $ mot_change(5)
            if player_gender == "male":
                mc_m "(I-type sa chat) Mamaya, may activity pa ako. GL sa ranked."
            else:
                mc_f "(I-type sa chat) Mamaya muna. Activity muna, saka laro."
            narrator "(Isinara mo ang chat. Binuksan mo ang Packet Tracer manual.)"
            jump chapter2_effort_route

        "Isang laro lang, pagkatapos Packet Tracer na.":
            $ ct_change(-5)
            $ mot_change(-3)
            if player_gender == "male":
                mc_m "(I-type sa chat) Okay, isa lang. Tapos serious mode na."
            else:
                mc_f "(I-type sa chat) Fine, isa lang. Promise."
            narrator "(Alas nwebe na ng gabi nang matapos ang 'isa lang.' Tatlong beses.)"
            narrator "(Ikinuskos mo ang mata. Binuksan mo ang Packet Tracer. Alas onse na.)"
            jump chapter2_ai_route

        "Maglaro na lang. Bukas na ang Packet Tracer.":
            $ ct_change(-12)
            $ mot_change(-8)
            $ use_ai("networking", 8)
            if player_gender == "male":
                mc_m "(I-type sa chat) In. Ano pa pang Packet Tracer."
            else:
                mc_f "(I-type sa chat) In! Bukas na 'yan."
            narrator "(Nagising ka nang alas singko ng umaga. Dalawang oras bago mag-submit.)"
            narrator "(Alam mo na ang susunod na gagawin mo.)"
            jump chapter2_ai_route

## ── ROUTE A: Effort Route (Networking minigame) ──────────────────────────────
label chapter2_effort_route:
    scene bg_bedroom with dissolve
    narrator "(Three hours in. You've understood the basic VLAN concept. Two switches are already configured.)"
    narrator "(But there's much more to configure. Time to test your networking knowledge.)"

    if player_bestfriend == "carl":
        show carl normal at right with dissolve
        carl "(text) hey done yet? txt me if u need help"
        hide carl with dissolve
    else:
        show carly normal at right with dissolve
        carly "(text) how's the activity going? msg me if you're stuck"
        hide carly with dissolve

    narrator "(You replied briefly. Now you need to prove you know what you're doing.)"
    narrator "(Several questions stand between you and a finished Packet Tracer topology.)"
    jump chapter2_effort_q1

## ROUTE A, Question 1: Access Port VLAN Assignment
## Reference: Cisco CCNA 200-301, Configuring VLAN Access Ports
label chapter2_effort_q1:
    show screen minigame(
        "Networking, VLAN Configuration (1/5)",
        "Which two IOS commands must be executed in interface configuration mode\nto assign an access port to VLAN 10 on a Cisco switch?",
        [
            "A. switchport mode access\n    switchport access vlan 10",
            "B. switchport access vlan 10\n    switchport trunk encap dot1q",
            "C. set port vlan 10\n    set port mode access",
            "D. vlan 10\n    switchport mode access"
        ],
        0,
        "networking",
        8,
        5,
        correct_label="chapter2_effort_q1_correct",
        wrong_label="chapter2_effort_q1_wrong"
    )
    return

label chapter2_effort_q1_correct:
    narrator "(Correct! First step done. Next: trunk port configuration between switches.)"
    jump chapter2_effort_q2

label chapter2_effort_q1_wrong:
    narrator "(Wrong syntax. In interface config mode on a Cisco switch, you must first set the port to access mode, then assign it to the specific VLAN.)"
    jump chapter2_effort_q1

## ── ROUTE A, Question 2: Trunk Port Configuration ──────────────────────────
## Reference: Cisco CCNA 200-301, Configuring VLAN Trunks
label chapter2_effort_q2:
    show screen minigame(
        "Networking, VLAN Configuration (2/5)",
        "A network administrator needs to configure a GigabitEthernet port as a trunk\nand allow VLANs 10, 20, and 30. Which command set accomplishes this?",
        [
            "A. switchport mode trunk\n    switchport trunk allowed vlan 10,20,30",
            "B. switchport mode trunk\n    switchport trunk vlan add 10,20,30",
            "C. interface trunk\n    allow vlan 10,20,30",
            "D. set trunk enable\n    trunk vlan 10,20,30"
        ],
        0,
        "networking",
        8,
        5,
        correct_label="chapter2_effort_q2_correct",
        wrong_label="chapter2_effort_q2_wrong"
    )
    return

label chapter2_effort_q2_correct:
    narrator "(Nice work! The trunk link between switches is now carrying VLANs 10, 20, and 30.)"
    jump chapter2_effort_q3

label chapter2_effort_q2_wrong:
    narrator "(That's not right. On a Cisco switch, setting a port to trunk mode is done with 'switchport mode trunk', then you specify which VLANs are allowed across it.)"
    jump chapter2_effort_q2

## ── ROUTE A, Question 3: Creating a VLAN ────────────────────────────────────
## Reference: Cisco CCNA 200-301, Creating and Naming VLANs
label chapter2_effort_q3:
    show screen minigame(
        "Networking, VLAN Configuration (3/5)",
        "Which sequence of IOS commands correctly creates VLAN 10\nand assigns it the name Engineering?",
        [
            "A. configure terminal\n    vlan 10\n    name Engineering",
            "B. create vlan 10\n    set name Engineering",
            "C. vlan database\n    vlan 10 name Engineering",
            "D. configure terminal\n    interface vlan 10\n    description Engineering"
        ],
        0,
        "networking",
        8,
        5,
        correct_label="chapter2_effort_q3_correct",
        wrong_label="chapter2_effort_q3_wrong"
    )
    return

label chapter2_effort_q3_correct:
    narrator "(Great! VLAN 10 'Engineering' now exists in the VLAN database. Next: verification.)"
    jump chapter2_effort_q4

label chapter2_effort_q3_wrong:
    narrator "(Not quite. On a Cisco switch, VLANs are created in global configuration mode. First enter 'configure terminal', then the 'vlan' command followed by the VLAN number, then 'name' to label it.)"
    jump chapter2_effort_q3

## ── ROUTE A, Question 4: Verifying VLAN Configuration ──────────────────────
## Reference: Cisco CCNA 200-301, Verifying VLAN Configuration
label chapter2_effort_q4:
    show screen minigame(
        "Networking, VLAN Configuration (4/5)",
        "Which Cisco IOS command displays a summary of all VLANs\nand shows which switch ports belong to each VLAN?",
        [
            "A. show vlan brief",
            "B. show running-config",
            "C. display vlan all",
            "D. show interfaces vlan"
        ],
        0,
        "networking",
        8,
        5,
        correct_label="chapter2_effort_q4_correct",
        wrong_label="chapter2_effort_q4_wrong"
    )
    return

label chapter2_effort_q4_correct:
    narrator "(You've confirmed your configuration is correct. All ports are in their assigned VLANs. One question remaining.)"
    jump chapter2_effort_q5

label chapter2_effort_q4_wrong:
    narrator "(There's a specific 'show' command that provides a concise summary of VLANs and their port assignments. Hint: it's one of the most common CCNA verification commands.)"
    jump chapter2_effort_q4

## ── ROUTE A, Question 5: Native VLAN ────────────────────────────────────────
## Reference: Cisco CCNA 200-301, Native VLAN Security Best Practice
## Source: ITExams / Cisco NetAcad, VLAN Security
label chapter2_effort_q5:
    show screen minigame(
        "Networking, VLAN Configuration (5/5)",
        "What is the default Native VLAN on a Cisco switch,\nand what is the security best practice concerning it?",
        [
            "A. VLAN 1, it should be changed to an unused VLAN for security",
            "B. VLAN 100, it is automatically assigned to voice VLAN",
            "C. VLAN 0, it is used for management traffic only",
            "D. VLAN 999, it is the default for all trunk ports"
        ],
        0,
        "networking",
        8,
        5,
        correct_label="chapter2_effort_q5_correct",
        wrong_label="chapter2_effort_q5_wrong"
    )
    return

label chapter2_effort_q5_correct:
    narrator "(You've completed all configurations! Every switch, every VLAN, every trunk link, set up properly.)"
    narrator "(You close the terminal. The topology is saved. All configurations are in place.)"
    narrator "(You finished before midnight. There's a strange satisfaction, one that came from your own understanding.)"
    narrator "(You didn't need AI for this. You did it yourself.)"
    return

label chapter2_effort_q5_wrong:
    narrator "(Think about the default VLAN that exists on every Cisco switch. Leaving it as-is on trunk ports is a well-known security risk in CCNA.)"
    jump chapter2_effort_q5

## ── ROUTE B: AI Route ────────────────────────────────────────────────────────
label chapter2_ai_route:
    scene bg_bedroom with dissolve
    narrator "(Alas singko ng umaga. Ang mata mo ay tila dinikdik sa asin at pinirito sa mantika, ganun kasara.)"
    narrator "(Ang Packet Tracer ay nakabukas. Ang mukha mo ay sumasalamin sa screen: isang tunay na IT student na hindi naka-kuha ng tamang tulog.)"
    narrator "(I-open mo ang AI app. I-type mo ang buong instructions ng activity. Parang may binibigyan ng utos na intern.)"
    narrator "AI: 'Here is the complete configuration for your VLAN topology.'"
    narrator "(Tumingin ka. Kumpleto. Perpekto. Maganda pa sa pagkakagawa ng iyong magiging thesis, kung gagawin mo man 'yun.)"
    narrator "(Isang problema lang: wala kang maintindihan kahit isang hakbang nito.)"
    narrator "(Siya nga pala: Tatlong minuto lang ginugol mo dito. Tatlo.)"
    narrator "(Isasara mo na ang AI app. Ngunit bago mo pa magawa...)"
    narrator "AI: 'Would you like me to explain how this configuration works step by step?'"
    narrator "(Titig ka sa screen.)"
    if player_gender == "male":
        mc_m "(Sa isip) Gusto ko ba? Oo. Pero kung ie-explain pa, baka abutin ng isang oras 'to."
    else:
        mc_f "(Sa isip) Gusto ko. Pero alam ko na i-click ko ang 'No' at magpanggap na naintindihan ko na lang."
    narrator "(Kinumpleto mo ang copy-paste. Isinara ang laptop. Nahiga. Hindi makatulog. Hindi dahil sa caffeine.)"
    narrator "(Kinopya mo ang configuration. I-save. I-submit. Tapos.)"
    call ai_used_result from _c2_ai_result

    ## ── SCENE 2-3: Submission Day, Mr. Earns ────────────────────────────────
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 2, Submission"

    show mr_earns normal at center with dissolve
    mr_earns "VLAN activity. Checked."
    narrator "(Tumayo siya sa harap ng klase, hawak ang isang printout — parang may dalang death note.)"
    mr_earns "May dalawang topology na may parehong interface numbering error. Pareho. Hindi nagkataon."
    narrator "(Ramdam mo ang biglaang init sa leeg. Hindi ka tumingin sa kahit kanino.)"
    mr_earns "Alam ko kung sino kayo. At alam ko kung bakit. Huwag ninyo na lang ulitin."
    narrator "(Hindi siya tumingin sa iyo. Pero naramdaman mo. Lahat ay naramdaman.)"
    narrator "(May bumubulong sa likod. Hindi mo sure kung si Gabby o si Kent o ang konsensya mo.)"
    mr_earns "Next topic. Subnetting."
    narrator "(Huminto siya. Tumingin sa klase. Sa paraang hindi biro.)"
    mr_earns "Walang shortcuts doon."
    hide mr_earns with dissolve

    narrator "(Natapos ang klase. Lumapit sa iyo ang [player_bestfriend] sa hallway. Mukhang concerned. O baka curious lang.)"

    if player_bestfriend == "carl":
        show carl stressed at right with dissolve
        carl "(bulong, papalapit) Uy. Okay ka lang? Mukha kang character sa horror game na hindi nakaligtas sa unang chapter."
        if player_gender == "male":
            mc_m "(tawa, pilit) Grabe naman. Okay lang. Natapos ko naman ang activity."
        else:
            mc_f "(pilit na ngiti) Grabe ka naman. Okay lang. Natapos ko."
        carl "(hindi kumbinsido) Oo... 'Yung topology mo, pumasok naman?"
        if player_gender == "male":
            mc_m "Oo naman. Bakit hindi?"
        else:
            mc_f "Oo. Bakit?"
        carl "(kibit balikat) Kasi pareho kayo ng error ng isa pa. Sabi ni Kent, hindi raw kayo magkaklase noong isang section. Interesting daw."
        if player_gender == "male":
            mc_m "(Nawala ang ngiti.) Ano? Sinabi ni Kent 'yun?"
        else:
            mc_f "(Napahinto.) Sinabi ni Kent 'yun?"
        carl "Hindi sa akin. Kay Gabby. Pero narinig ko."
        if player_gender == "male":
            mc_m "...Sige na. Subnetting pa."
        else:
            mc_f "...Next topic na lang. Subnetting."
        carl "(tapik sa balikat) Oo. Sige. Text mo ko kung gusto mo ng tulong. TOTOONG tulong."
        hide carl with dissolve
    else:
        show carly stressed at right with dissolve
        carly "(bulong, papalapit) Huy. Okay ka? Namumutla ka. As in. Napansin ni Gabby."
        if player_gender == "male":
            mc_m "Okay lang 'to. Kulang lang sa tulog."
        else:
            mc_f "Okay lang. Baka kulang lang sa tulog."
        carly "Uh-huh. At yung topology mo?"
        if player_gender == "male":
            mc_m "Ano roon?"
        else:
            mc_f "Ano roon?"
        carly "Wala. Sinabi lang ni Kent na pareho raw ng interface numbering error 'yung sa'yo at sa isa pang submission mula sa kabilang section. Sabi niya statistically improbable daw."
        if player_gender == "male":
            mc_m "...Gusto mo bang sabihin kay Kent na mag-focus na lang sa sarili niyang grades?"
        else:
            mc_f "...Pwedeng sabihin kay Kent na mag-aral na lang siya ng sarili niya?"
        carly "(tawa) Oo nga 'no. Sige, subnetting na tayo. Pero totoo — kung kailangan mo ng tulong, nandito lang ako. Yung totoong tulong ha."
        hide carly with dissolve

    narrator "(Tumalikod ka. Onwards sa next class session. Bitbit ang pakiramdam na hindi mo maintindihan: nakapasa ka. Pero bakit ang bigat pa rin?)"
    return
