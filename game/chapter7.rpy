## game/chapter7.rpy
## Chapter 7, "Last Chance Na" (Week 7, Finals Prep)

label chapter7:
    call screen chapter_title("7", "Last Chance Na", "Week 7, 'Ito na 'yung laban.'")
    $ day_label = "Week 7, Sabado"
    $ current_week = 7

    ## ── SCENE 7-1: Study session in front of classroom ──────────────────────
    scene bg_campus with dissolve
    $ safe_play("music", "audio/bgm/bgm_study.ogg", loop=True)

    narrator "(Sabado ng umaga. Ang campus ay tahimik maliban sa ilang grupo na nag-aaral sa labas ng mga silid-aralan.)"
    narrator "(May naghihintay sa iyo sa harap ng IT building.)"

    show kent happy at left with dissolve
    show rey normal at center with dissolve

    kent "Nandito na lahat. O halos lahat."
    narrator "(Si Kent ay may dalang malaking notebook at tatlong kulay ng highlighter. Si Rey ay may dalang dalawang cups ng instant coffee.)"

    if player_bestfriend == "carl":
        show carl happy at right with dissolve
        carl "Uy! Nag-aalala na ako. Tara na, malamig sa labas."
    else:
        show carly happy at right with dissolve
        carly "Nandito ka! Tara na, naghintay na kaming matagal."

    narrator "(Pumunta kayo sa loob. Ang study room ay malinis, tahimik, walang distraksiyon, walang game console, walang ranked queue.)"

    ## Study montage
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_study.ogg", loop=True)

    narrator "(Nagsimula si Kent sa Networking. VLAN, subnetting, routing protocols.)"
    narrator "(Hindi siya nagtuturo nang parang guro, nagtatanong siya. Binibigyan kayo ng pagkakataon na sumagot.)"

    show kent normal at center with dissolve
    kent "Okay. Simpleng tanong. Ano ang pagkakaiba ng VLAN at physical LAN segment?"
    narrator "(Nag-isip ka. Totoong nag-isip, hindi nag-phone, hindi nag-AI.)"

    if player_gender == "male":
        mc_m "Sa physical LAN, ang segmentasyon ay base sa hardware. Sa VLAN, logical, kahit nasa parehong switch, maaaring magkaibang broadcast domain."
    else:
        mc_f "Sa physical LAN, segmented by hardware. Sa VLAN, software-defined ang segmentation, kahit physically connected, logically separated ang broadcast domain."

    show kent happy at center with dissolve
    kent "Tama. Exactly. Yan ang klase ng sagot na gusto ko."

    show rey normal at left with dissolve
    rey "..."
    narrator "(Tiningnan ka ni Rey. May bahagyang ngiti, rare para sa kanya.)"
    rey "Hindi ka ganito dati. Sa lab activities noon."
    if player_gender == "male":
        mc_m "Tinatamad lang ako dati."
    else:
        mc_f "...Oo. Tinatamad lang talaga."
    rey "Hindi tinatamad. Takot. May pagkakaiba."
    narrator "(Tumingin ka sa kanya. Hindi ka nagtanggol.)"

    hide kent with dissolve
    hide rey with dissolve
    hide carl with dissolve
    hide carly with dissolve

    ## Gabby arrives late
    show gabby normal at right with dissolve
    gabby "Uy! Nandito na! Sorry late, nalaro ko ng konti,"
    kent "(bumabalik) Gabby. Sit down. Cybersecurity na tayo."
    gabby "(tahimik na umupo) Sige na, sige na."

    ## ── SCENE 7-2: Evening, Programming review ──────────────────────────────
    scene bg_canteen with dissolve
    $ day_label = "Week 7, Gabi"
    $ safe_play("music", "audio/bgm/bgm_canteen.ogg", loop=True)

    narrator "(Pagkatapos ng anim na oras. Gutom na kayo. Kumain sa canteen bago umuwi.)"

    show gabby normal at right with dissolve
    if player_bestfriend == "carl":
        show carl normal at left with dissolve
        carl "Hoy, nagpapasalamat ako kay Kent. Pero ang utak ko ay kapasidad na."
    else:
        show carly normal at left with dissolve
        carly "Nag-aral tayo nang matagal ngayon. Feels different 'no? 'Yung naiintindihan mo talaga."

    show kent normal at center with dissolve
    show rey normal at left with dissolve

    kent "Bukas, Programming review. Mr. Kai's finals ay may coding output required. Walang AI."
    gabby "Alam ko na 'yun, Kent."
    kent "Sinasabi ko para sa lahat."
    rey "...Kasama ka ba bukas?"

    ## CHOICE 7-A: Finals eve decision
    menu:
        "Oo, nandito ako bukas. Finals na 'to, sineseryoso ko.":
            $ ct_change(10)
            $ mot_change(10)
            if player_gender == "male":
                mc_m "Nandito. Promise. Sineseryoso ko na 'to."
            else:
                mc_f "Nandito. Wala na akong excuse. Sineseryoso ko ito."
            narrator "(Ngumiti si Kent nang bihira. Nod ni Rey.)"
            $ grade_change("programming", 8)
            $ grade_change("networking", 5)

        "Baka maaga kayo, matutulog pa ako.":
            $ ct_change(-3)
            if player_gender == "male":
                mc_m "Depende kung anong oras kayo magsisimula."
            else:
                mc_f "Anong oras? Baka medyo late ako."
            if player_bestfriend == "carl":
                carl "Alas nwebe. Wag kang mag-late."
            else:
                carly "Alas nwebe. Hintayin kita."
            narrator "(Pumangako ka. Sana sundin mo.)"

    hide gabby with dissolve
    hide kent with dissolve
    hide rey with dissolve
    hide carl with dissolve
    hide carly with dissolve

    ## ── SCENE 7-3: Night before finals, phone face-down ────────────────────
    scene bg_bedroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_study.ogg", loop=True)
    $ day_label = "Week 7, Gabi (Finals Eve)"

    narrator "(Gabi na. Ang phone mo ay nakahiga nang pababa sa mesa.)"
    narrator "(Ang notes mo, mga sariling notes, hindi AI-generated, ay nakaladlad sa harapan mo.)"
    narrator "(Mabagal ka. Pero nandoon ka.)"
    narrator "(Binabasa mo ang iyong sariling sulat. May mga mali. May mga hindi kumpleto. Pero ikaw ang nagsulat.)"

    if player_gender == "male":
        mc_m "(Sa isip mo) Ganito pala 'yung pakiramdam ng mag-aral. Hindi yung magbasa ng AI output. Magbasa ng sariling notes."
    else:
        mc_f "(Sa isip mo) Ganito pala 'to. Hindi rush. Hindi shortcut. Sariling mga salita, sariling mga tanong."

    narrator "(Isinara mo ang laptop. Natulog ka nang may maliwanag na konsiyensya, hindi perpekto, pero mas maliwanag kaysa noong mga nakaraang linggo.)"
    narrator "(Bukas na ang finals.)"
    return
