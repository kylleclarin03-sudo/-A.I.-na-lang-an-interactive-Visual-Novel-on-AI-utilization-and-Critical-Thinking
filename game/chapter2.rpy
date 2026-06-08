## game/chapter2.rpy
## Chapter 2 — "Laro Muna" (Week 2)

label chapter2:
    call screen chapter_title("2", "Laro Muna", "Week 2 — 'Isa lang, tapos tutugon na sa group chat.'")
    $ day_label = "Week 2 — Gabi"
    $ current_week = 2

    ## ── SCENE 2-1: Group chat invite vs Packet Tracer assignment ─────────────
    scene bg_bedroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_night.ogg", loop=True)

    narrator "(Hapon ng Martes. Ang laptop mo ay nakabukas sa dalawang tab — Packet Tracer at YouTube. Isa sa kanila ang gumagana.)"
    narrator "(Ang Networking activity ni Mr. Earns: i-configure ang isang basic VLAN topology. Due bukas ng umaga.)"

    groupchat "GABBY: uy laro na!! sabay tayo ranked tonight"
    groupchat "GABBY: game na please 😭😭"

    if player_bestfriend == "carl":
        groupchat "CARL: in! uy [player_name] ikaw?"
    else:
        groupchat "CARLY: in! uy [player_name] ikaw? 👀"

    groupchat "KENT: Nag-finish na ba lahat ng Packet Tracer activity? Mr. Earns checks syntax pati topology."
    groupchat "GABBY: KENT STOP BEING THE CONSCIENCE OF THE GROUP"
    groupchat "REY: ... (online)"

    narrator "(Ang notipikasyon ay patuloy na dumadating. Ang cursor mo ay naka-hover sa Packet Tracer.)"

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
                mc_m "(I-type sa chat) Okay, isa lang. Tapos serious na."
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
    narrator "(Tatlong oras na. Naiintindihan mo na ang basic na konsepto ng VLAN. Naka-configure na ang dalawang switch.)"
    narrator "(May isang tanong: paano ang trunk port syntax?)"

    if player_bestfriend == "carl":
        show carl normal at right with dissolve
        carl "(text) uy natapos mo na? pag may tanong txt mo"
        hide carl with dissolve
    else:
        show carly normal at right with dissolve
        carly "(text) kumusta ang activity? text mo kung may hindi gets"
        hide carly with dissolve

    narrator "(Sinagot mo. Pinagpatuloy ang trabaho. Natapos ka bago mag-hatinggabi.)"

    ## Networking minigame — VLAN
    show screen minigame(
        "Networking — VLAN Configuration",
        "Alin ang tamang IOS command para mag-assign ng access port sa VLAN 10 sa isang Cisco switch?",
        [
            "A. switchport mode access\n    switchport access vlan 10",
            "B. vlan 10 access switchport",
            "C. set port vlan 10 access mode",
            "D. enable vlan 10 access"
        ],
        0,
        "networking",
        8,
        10
    )
    return

## ── ROUTE B: AI Route ────────────────────────────────────────────────────────
label chapter2_ai_route:
    scene bg_bedroom with dissolve
    narrator "(Alas singko ng umaga. Ang Packet Tracer ay nakabukas. Ang mata mo ay nakasara nang halos.)"
    narrator "(I-open mo ang AI app. I-type mo ang buong instructions ng activity.)"
    narrator "(Nag-generate. Kumpleto. Perpekto ang topology. Hindi mo maintindihan kahit isang hakbang nito.)"
    narrator "(Kinopya mo ang configuration. I-save. I-submit. Tapos.)"
    call ai_used_result from _c2_ai_result

    ## ── SCENE 2-3: Submission Day — Mr. Earns ────────────────────────────────
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 2 — Submission"

    show mr_earns normal at center with dissolve
    mr_earns "VLAN activity. Checked."
    narrator "(Nagtayo siya sa harap ng klase, hawak ang listahan.)"
    mr_earns "May dalawang topology na may parehong interface numbering error. Alam ninyo kung sino kayo."
    narrator "(Hindi siya tumingin sa iyo. Pero naramdaman mo.)"
    mr_earns "Next topic. Subnetting. Walang shortcuts doon."
    hide mr_earns with dissolve

    if player_bestfriend == "carl":
        show carl stressed at right with dissolve
        carl "(bulong) Uy, okay ka lang? Mukha kang aswang."
        if player_gender == "male":
            mc_m "Okay lang. Natapos ko naman."
        else:
            mc_f "Okay lang. Natapos naman."
        carl "(bulong) Natanggap naman ang submission mo?"
        if player_gender == "male":
            mc_m "Oo. Sige na, pakinggan na natin si Sir."
        else:
            mc_f "Oo naman. Tayo na, pakinggan na natin."
        hide carl with dissolve
    else:
        show carly stressed at right with dissolve
        carly "(bulong) Huy, okay ka? Namumutla ka."
        if player_gender == "male":
            mc_m "Okay lang. Natapos ko naman."
        else:
            mc_f "Okay lang. Natapos naman."
        carly "(bulong) Sige, pakinggan na natin. Subnetting daw susunod."
        hide carly with dissolve

    return
