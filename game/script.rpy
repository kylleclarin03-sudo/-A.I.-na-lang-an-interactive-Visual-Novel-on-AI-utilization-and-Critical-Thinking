## game/script.rpy
## Entry point, init, and Prologue sequence for A.I. na lang!

label splashscreen:
    $ renpy.music.stop(fadeout=0.0)
    scene black
    pause 0.5

    ## Studio card
    play sound "audio/sfx/sfx_phone.ogg"
    show text "{color=#8b949e}{size=22}Mabalacat City College\nInstitute of Computing Studies, 2026{/size}{/color}" at truecenter with dissolve
    pause 3.2
    hide text with dissolve
    pause 1.4

    ## Terminal boot - sfx_click.ogg as stand-in typing sound
    play sound "audio/sfx/sfx_click.ogg"
    show text "{color=#1f6feb}{size=26}{cps=30}> a.i.na.lang.exe  v1.0.0  loading...{/cps}{/color}" at truecenter with dissolve
    pause 1.8
    hide text

    play sound "audio/sfx/sfx_click.ogg"
    show text "{color=#56d364}{size=26}{cps=40}> OK. All modules initialized.{/cps}{/color}" at truecenter with dissolve
    pause 1.4
    hide text

    ## Thematic sting - sfx_chime.ogg as stand-in notification sound
    stop sound
    play sound "audio/sfx/sfx_grade_reveal.ogg"
    show text "{color=#e3b341}{size=32}[ ADVISORY ]{/color}\n\n{color=#c9d1d9}{size=26}AI dependency level in previous session: HIGH.{/size}{/color}\n{color=#8b949e}{size=22}Proceed with caution.{/size}{/color}" at truecenter with dissolve
    pause 2.8

    ## TODO: uncomment when sfx_hum.ogg is ready:
    ## play ambient "audio/sfx/sfx_hum.ogg" fadein 0.8
    hide text with dissolve
    pause 0.5
    return

label start:
    $ safe_play("music", "audio/bgm/bgm_menu.ogg", loop=True)
    call prologue from _call_prologue
    call chapter1  from _call_chapter1
    call chapter2  from _call_chapter2
    call chapter3  from _call_chapter3
    call chapter4  from _call_chapter4
    call chapter5  from _call_chapter5
    call chapter6  from _call_chapter6
    call chapter7  from _call_chapter7
    call chapter8  from _call_chapter8
    call ending_sequence from _call_ending
    return
# ─────────────────────────────────────────────────────────────────────────────
# PROLOGUE
# ─────────────────────────────────────────────────────────────────────────────
label prologue:
    $ show_hud = False
    hide screen hud
    scene black with fade
    $ safe_stop("music")
    $ safe_play("music", "audio/bgm/bgm_sad.ogg", loop=True)

    ## ═══════════════════════════════════════════════════════════════════════
    ## BEAT 1: THE HOOK
    ## Pure black. Pure narrator. Three lines. Then the gut-punch.
    ## ═══════════════════════════════════════════════════════════════════════

    pause 2.0
    narrator "Alam mo kung paano nagsimula ito?"
    pause 0.8
    narrator "Hindi sa isang malaking desisyon."
    pause 0.5
    narrator "Hindi sa isang masama o tamad na gabi."
    pause 1.2
    narrator "Sa isang linya lang ng code na hindi mo maintindihan."
    pause 2.0

    ## ═══════════════════════════════════════════════════════════════════════
    ## BEAT 2: THE NIGHT
    ## 3AM. Deadline. No solutions. Then the app.
    ##
    ## STAND-IN: bg_bedroom.webp
    ## REPLACE WITH: bg_bedroom_night.webp when ready
    ## Art direction: same room, ONLY laptop screen glow from the left edge.
    ## No overhead light. Half-empty 3-in-1 cup on desk. Phone face-down.
    ## Sticky note: "DEADLINE 8AM" in messy ballpen. Window: total darkness.
    ## ═══════════════════════════════════════════════════════════════════════

    scene bg_bedroom with dissolve
    pause 1.2

    narrator "Mag-aalas tres na ng umaga."
    narrator "Python program. Due ng alas otso. Object-oriented design."
    pause 0.8
    narrator "Hindi mo maintindihan. {w=0.6}Kahit isang linya."
    pause 1.0
    narrator "Nag-Google ka. {w=0.4}Nag-YouTube ka. {w=0.4}Nag-scroll ng Reddit hanggang hindi mo na alam kung bakit ka nagbu-browse."
    pause 0.5
    narrator "Walang nakakatulong."
    pause 2.0

    narrator "Tapos... {w=1.2}nakita mo siya."
    pause 0.8
    narrator "Hindi siya tao."
    pause 0.5
    narrator "Isang app lang. {w=0.4}Isang kahon na naghihintay ng tanong."
    pause 0.8
    narrator "Pero nandoon siya. {w=0.5}Gising. {w=0.5}Handa. {w=0.5}Walang pagod. Walang judgement."
    pause 1.8

    ## ═══════════════════════════════════════════════════════════════════════
    ## BEAT 3: THE FIRST USE
    ## ai_voice appears for the first time. Cold. Too clean. Too fast.
    ## The contrast with the tired narrator should feel wrong immediately.
    ## ═══════════════════════════════════════════════════════════════════════

    play sound "audio/sfx/sfx_phone.ogg"
    pause 0.8
    ai_voice "I can help with that."
    pause 1.2
    ai_voice "Complete solution generated. All edge cases handled."
    pause 1.5

    narrator "Sampung segundo."
    pause 0.8
    narrator "Kumpleto ang sagot. {w=0.4}Tama lahat. {w=0.4}Mas maganda pa sa kahit anong isusulat mo kahit may isang linggong oras ka pa."
    pause 1.0
    narrator "Kinopya mo. {w=0.5}I-paste. {w=0.5}I-submit."
    pause 1.0
    narrator "Tapos natulog ka."
    pause 1.8
    narrator "{cps=15}Para sa unang beses sa napakatagal na panahon, natulog ka ng walang kasabay na guilt.{/cps}"
    pause 2.0

    narrator "Naisip mo nang gumising ka:"
    pause 0.8
    narrator "{cps=18}Isa lang naman ito.{/cps}"
    pause 0.8
    narrator "Hindi naman mauulit."
    pause 2.0

    ## ═══════════════════════════════════════════════════════════════════════
    ## BEAT 4: THE PANDEMIC YEARS
    ## The specificity is the point. Zoom boxes. Cameras off. The counting
    ## that eventually stops. Let each beat land before moving on.
    ##
    ## OPTIONAL FUTURE ASSET: bg_zoom.webp
    ## Art: dark bedroom, laptop screen showing 16 black Zoom grid squares.
    ## Name labels only. No cameras on. One green mic icon. Screen = only light.
    ## ═══════════════════════════════════════════════════════════════════════

    scene black with dissolve
    pause 1.5

    narrator "Pero hindi lang iyon ang nangyari."
    pause 1.0
    narrator "Noong una, excited ka pa."
    narrator "'{cps=20}Dalawang linggo lang daw. Parang vacation ata ito.{/cps}'"
    pause 1.5

    narrator "Sa ikalawang buwan, nag-aayos ka pa rin ng background sa Zoom."
    pause 0.5
    narrator "Sa ikaapat na buwan, tinanggal mo na ang camera."
    pause 0.5
    narrator "'{cps=18}Hindi naman nila papansinin. Lahat naman ganoon na.{/cps}'"
    pause 1.8

    narrator "Sa ika-anim na buwan..."
    pause 1.8
    narrator "{cps=11}...hihinto ka na sa pagbibilang.{/cps}"
    pause 2.5

    narrator "Dalawang taon."
    pause 0.8
    narrator "Paper? {w=0.3}Naisulat na niya."
    narrator "Program? {w=0.3}Natapos na niya."
    narrator "Modules na hindi mo gets? {w=0.5}Naipaliwanag na niya. {w=0.3}Nang sampung beses. {w=0.3}Walang reklamo."
    pause 1.0
    narrator "At ikaw? {w=1.0}Natutulog ka na."
    pause 1.5

    narrator "Sabi mo sa sarili mo:"
    pause 0.5
    narrator "'{cps=16}Pansamantala lang ito. Survival mode. Hanggang matapos ang lahat.{/cps}'"
    pause 1.2
    narrator "{cps=14}Sinabi mo iyon nang paulit-ulit, hanggang sa naniniwala ka na.{/cps}"
    pause 2.5

    ## ═══════════════════════════════════════════════════════════════════════
    ## BEAT 5: THE COST
    ## Music stops completely. The question lands in silence.
    ## Do not rush the pauses here. This is the gut-punch of the whole prologue.
    ## ═══════════════════════════════════════════════════════════════════════

    $ safe_stop("music")
    pause 2.0

    narrator "Tapos natapos na ang lahat."
    pause 1.5
    narrator "Bumalik ang klase. {w=0.5}Bumalik ang campus. {w=0.5}Bumalik ang 'normal.'"
    pause 2.0
    narrator "Pero may isang tanong na lagi kang tinatambad nito sa gitna ng gabi:"
    pause 1.5
    narrator "{cps=16}Kung tatanungin ka nila bukas ng kahit anong malalim tungkol sa kurso mo...{/cps}"
    pause 1.2
    narrator "{cps=16}Maari mo bang sagutin nang sarili mong utak?{/cps}"
    pause 3.0

    ## Silence. The worst part is knowing the answer.
    narrator "{cps=10}...{/cps}"
    pause 3.5

    $ safe_play("music", "audio/bgm/bgm_sad.ogg", loop=True)
    pause 0.8

    narrator "Kasi ang totoo:"
    pause 0.8
    narrator "Hindi mo alam kung ilan sa mga 'natutunan' mo ang tunay mong sarili."
    pause 0.8
    narrator "At hindi mo alam kung paano na mabuhay nang walang AI na nag-iisip para sa'yo."
    pause 2.5

    ## ═══════════════════════════════════════════════════════════════════════
    ## BEAT 6: THE SILVER LINING
    ## A breath after all that dark. Someone was always there.
    ## This beat EARNS the bestfriend reveal in Beat 8.
    ## ═══════════════════════════════════════════════════════════════════════

    narrator "Pero..."
    pause 1.5
    narrator "Hindi ka ganap na nag-iisa sa lahat ng iyon."
    pause 1.0
    narrator "May isang tao."
    pause 0.8
    narrator "Hindi niya palaging naiintindihan ang lahat ng pinagdadaanan mo."
    narrator "Pero nandoon lang siya. Tapat. Consistent."
    pause 0.8
    narrator "Sa chat kahit gabing gabi. {w=0.4}Sa calls kahit walang masyadong masabi. {w=0.5}Sa mga araw na parang lahat ay suko na."
    pause 1.2
    narrator "{cps=16}Yung tipong kahit anong mangyari, present siya.{/cps}"
    pause 2.5

    ## ═══════════════════════════════════════════════════════════════════════
    ## BEAT 7: CHARACTER SELECTION
    ## No terminal boot. No system menus. The player claims the story.
    ## The narrator asks softly. The player answers.
    ## ═══════════════════════════════════════════════════════════════════════

    narrator "(Pero bago tayo magsimula... sino ka sa kwentong ito?)"
    pause 0.8

    menu:
        "Alex. Lalaki. 'Basta nandito. Gumagawa ng paraan.'":
            $ player_gender = "male"
            $ player_name   = "Alex"
        "Alexa. Babae. 'Dumaan na sa marami. Nandito pa rin.'":
            $ player_gender = "female"
            $ player_name   = "Alexa"

    narrator "(Ano ang ipapatawag sa'yo ng mga tao?)"
    pause 0.3

    menu:
        "Ibang pangalan ang gusto ko":
            $ raw_name = renpy.input("Pangalan:", default=player_name, length=20)
            $ player_name = raw_name.strip() if raw_name.strip() else player_name
        "[player_name] na lang":
            $ player_name = player_name

    pause 0.8

    ## ═══════════════════════════════════════════════════════════════════════
    ## BEAT 8: THE BESTFRIEND REVEAL
    ## The player is at the gate. The person from Beat 6 is there.
    ## The choice is framed as recognition, not configuration.
    ##
    ## STAND-IN: bg_campus.webp
    ## REPLACE WITH: bg_campus_gate.webp when ready
    ## Art: school entrance from outside, facing in. Early morning pale light.
    ## Two or three blurred students in the background. Gate is open.
    ## Feels like a threshold you are not sure you are ready to cross.
    ## ═══════════════════════════════════════════════════════════════════════

    scene bg_campus with dissolve
    $ safe_stop("music")
    $ safe_play("music", "audio/bgm/bgm_campus.ogg", loop=True)
    pause 1.5

    narrator "Third year. Unang araw. Nakatayo ka sa labas ng gate."
    pause 0.8
    narrator "Alam mo kung paano ito gumagana sa teorya."
    narrator "Pumasok. {w=0.3}Umupo. {w=0.3}Matuto."
    pause 1.0
    narrator "Pero ngayon, sa harapan ng aktwal na pintuan, may bahagi ng utak mo na nagsasabi:"
    pause 0.5
    narrator "'{cps=16}Kung lumabas ang totoo, hindi ka siguradong kayang-kaya mo 'to.{/cps}'"
    pause 1.5

    narrator "Ilang segundo kang nakatayo doon, nag-aalangan."
    pause 1.0
    narrator "Tapos may kumakatok sa iyong balikat."
    pause 2.0

    ## Framed as recognition, not a menu prompt.
    ## The player already knows this person from Beat 6. Now they name them.
    menu:
        "Carl. Nag-aabang sa gate. Kamay sa bulsa. Mukha siyang dalawang oras lang natulog.":
            $ player_bestfriend = "carl"
        "Carly. Nag-aabang sa gate. Nakangiti na bago ka pa lumingon.":
            $ player_bestfriend = "carly"

    if player_bestfriend == "carl":
        show carl happy at center with dissolve
        pause 0.8
        carl "Huy. {w=0.8}Nandito ka na rin."
        pause 0.8
        if player_gender == "male":
            mc_m "(Napatingin ka sa kanya. Ganoon pa rin siya. {w=0.4}Parang hindi nagbago.)"
        else:
            mc_f "(Napatingin ka sa kanya. Para kang nakahinga ng malalim nang hindi mo namamalayan.)"
        pause 0.5
        carl "Mukha kang kasing-antok ko. {w=0.5}Malaking bagay iyon, believe me."
        if player_gender == "male":
            mc_m "{cps=22}Salamat?{/cps} {w=0.5}Sigata?"
        else:
            mc_f "Salamat ata sa... compliment na iyon."
        carl "{cps=17}Tara na. Baka ma-late pa tayo sa first day nang pinagsusumakitan nating huwag dumating.{/cps}"
        pause 0.8
        narrator "(Lumakad siya nang walang atubili.)"
        pause 0.5
        narrator "(At ikaw, sinundan mo siya. {w=0.5}Ganoon palagi.)"
        pause 0.5
        narrator "(Siya ang nagsisimula. {w=0.5}Ikaw ang sumusunod.)"
        pause 0.5
        narrator "(Ngayon lang, gusto mong matiyak na ikaw mismo ang magde-desisyon kung saan ka talaga patungo.)"
        hide carl with dissolve

    else:
        show carly happy at center with dissolve
        pause 0.8
        carly "Uy! {w=0.6}Nandito ka na!"
        pause 0.8
        if player_gender == "male":
            mc_m "(Bigla kang naging medyo mas okay.)"
        else:
            mc_f "(Nakita mo ang mukha niya at parang kaya mo pala 'to.)"
        pause 0.5
        carly "Mukhang hindi ka natulog. {w=0.5}Okay ka lang ba?"
        if player_gender == "male":
            mc_m "Okay naman. {w=0.5}Medyo."
        else:
            mc_f "Oo. {w=0.5}I think so. {cps=15}Basta, nandito na ko.{/cps}"
        carly "{cps=18}Okay. {w=0.3}Sapat na iyon ngayon.{/cps} Tara na."
        pause 0.8
        narrator "(Lumakad kayo nang magkasabay.)"
        pause 0.5
        narrator "(At sa unang pagkakataon ngayong umaga, hindi ka nag-iisa.)"
        pause 0.5
        narrator "(May paraan siya ng paggawa ng lahat na parang 'kaya pa.' {w=0.5}Kahit na hindi mo pa sigurado.)"
        pause 0.5
        narrator "(Ngayon lang, gusto mong maging sigurado para sa sarili mo.)"
        hide carly with dissolve

    pause 1.2
    narrator "(First day. Muli.)"
    pause 0.5
    narrator "(Pero ngayon, may isang bagay na gusto mong sagutin nang tama.)"
    pause 0.5
    narrator "(Hindi para sa grado.)"
    pause 0.5
    narrator "{cps=14}Para sa sarili mo.{/cps}"
    pause 2.0
    $ show_hud = False
    return

