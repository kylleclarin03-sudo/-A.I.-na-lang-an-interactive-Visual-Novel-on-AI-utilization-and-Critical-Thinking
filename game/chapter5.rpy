## game/chapter5.rpy
## Chapter 5, "Incomplete?" (Week 5, Midterm Results)

label chapter5:
    call screen chapter_title("5", "Incomplete?", "Week 5, 'Kahit ano nalang grade, basta meron.'")
    $ day_label = "Week 5, Afternoon"
    $ current_week = 5

    ## ── SCENE 5-1: Midterm results posted ───────────────────────────────────
    scene bg_hallway with dissolve
    $ safe_play("music", "audio/bgm/bgm_sad.ogg", loop=True)

    narrator "(The midterm grades are posted on the portal.)"
    narrator "(You don't rush to check. You already have a feeling.)"

    ## Grade reveal based on current stats
    python:
        ng_letter = letter_grade(networking_grade)
        pg_letter = letter_grade(programming_grade)
        cg_letter = letter_grade(cyber_grade)
        any_inc   = any_incomplete()

    if any_inc:
        narrator "(Your name on the list. Networking: [ng_letter]. Programming: [pg_letter]. Cybersecurity: [cg_letter].)"
        narrator "(One or more are marked in red. INC in the midterm component.)"
        narrator "(You stare at the screen. The hallway noise fades into nothing.)"
        narrator "(You knew. You always knew. But seeing it in black and white, that's different.)"
        $ mot_change(-15)
    else:
        narrator "(Your name on the list. Networking: [ng_letter]. Programming: [pg_letter]. Cybersecurity: [cg_letter].)"
        narrator "(You made it through. Not always pretty, but you made it through.)"
        narrator "(You let out a big sigh you didn't realize you were holding.)"
        $ mot_change(5)

    show gabby normal at right with dissolve
    if player_bestfriend == "carl":
        show carl normal at left with dissolve
    else:
        show carly normal at left with dissolve

    if any_inc:
        gabby "Huy, okay ka lang ba? Medyo tahimik ka ahh..."
        if player_gender == "male":
            mc_m "(Tahimik lang...)"
        else:
            mc_f "(Habang tinitingnan mo ang papel. Lumuluha ka nang hindi mo namamalayan.)"
        if player_bestfriend == "carl":
            carl "(mababa) Uy. Kaya pa ba."
        else:
            carly "(mababa) Hey. Huwag muna mag-isip ng masama."
        narrator "(You nod without meaning it. You know you're not okay. But saying it out loud would make it real.)"
    else:
        gabby "Ay, okay naman! Ako rin, okay rin!"
        if player_bestfriend == "carl":
            carl "Oo naman. Kaya pa natin."
        else:
            carly "Maganda ang midterm scores! Next step, finals."
        narrator "(There's relief. But also a quiet voice in your head asking if you actually learned anything. The grades are fine, but what about the knowledge?)"

    show kent normal at center with dissolve
    kent "Before anyone celebrates or drowns in silence, I just want to say the midterm was designed to filter. The finals will be designed to challenge what you actually learned and retained."
    kent "If you got through by copying configurations or debugging without understanding, the finals won't be as forgiving."
    narrator "(Kent's words hang in the air. He's not looking at anyone in particular. But everyone feels seen.)"

    hide gabby with dissolve
    hide carl with dissolve
    hide carly with dissolve
    hide kent with dissolve

    ## ── SCENE 5-2: Kent speaks up in canteen ────────────────────────────────
    scene bg_canteen with dissolve
    $ safe_play("music", "audio/bgm/bgm_canteen.ogg", loop=True)
    $ day_label = "Week 5, Hapon"

    narrator "(The canteen is unusually quiet for a Friday afternoon. Your group sits at the usual table, but no one touches their food.)"

    show rey normal at left with dissolve
    show kent normal at center with dissolve

    if player_bestfriend == "carl":
        show carl normal at right with dissolve
    else:
        show carly normal at right with dissolve

    rey "So. We all saw the list."
    kent "Yes. And I have something to say. Something that might make some of you uncomfortable."
    rey "Go ahead, Kent."
    kent "I looked at the department-wide grade distribution. Three patterns stood out. First, the top ten scores all came from students who rarely use the AI tools in their submissions. Second, the middle cluster, that's most of us, had mixed results. Third, the bottom fifteen all had very low critical thinking metrics on their assessments."
    kent "I'm not here to expose anyone. I'm here because we still have finals. And completion exams for those who need them."

    if player_bestfriend == "carl":
        carl "Kent, personal 'yung grades,"
    else:
        carly "Kent, personal 'yung grades,"

    kent "I know. I'm not asking anyone to share their scores. I'm asking if we can study together. I have compiled notes across all three subjects. We can review. We can test each other. No AI, just discussion."
    narrator "(Silence. You can hear the ice clinking in someone's glass from three tables away.)"
    rey "Kent has a point. Study session? This weekend. Library. No games. No phones."
    kent "I'll bring my Cisco Packet Tracer lab notes, the ones I annotated by hand. And my Python debugging cheat sheet. And the RA 10173 summary I made."
    narrator "(He's prepared. He's always prepared. The question is: are you?)"

    ## CRITICAL CHOICE 5-A: Sets the direction toward ending
    menu:
        "Oo, gusto ko ng tulong. Sineseryoso ko ang finals.":
            $ ct_change(12)
            $ mot_change(15)
            if player_gender == "male":
                mc_m "Oo. Kailangan ko ng tulong. Sineseryoso ko 'to."
            else:
                mc_f "Sige. Oo. Kailangan ko ng help, at aaminin ko 'yun."
            kent "(ngumiti nang bihira) Good. Saturday, 9 AM. Library. I'll save you a seat."
            narrator "(Something shifts at the table. It's small. But you feel it.)"
            narrator "(Admitting you need help, that's not weakness. That's the first real step you've taken all semester.)"
            $ grade_change("networking", 5)
            $ grade_change("programming", 5)
            $ grade_change("cyber", 5)

        "Mag-AI study session na lang, mas mabilis.":
            $ ct_change(-10)
            $ mot_change(-5)
            if player_gender == "male":
                mc_m "Sige... oo. Pero may paraan naman ako. AI-generated reviewers, mas efficient."
            else:
                mc_f "...May paraan naman ako. Mag-o-organize ng AI reviewer."
            kent "(naging seryoso) The AI reviewer isn't the problem. The problem is if you can't read its answers with understanding. I've seen AI-generated notes that sounded correct but missed entire concepts."
            $ use_ai(None, 0)
            narrator "(You know he's right. But the habit is already there, comfortable, easy. And habits are hard to break.)"

        "Kaya ko pa 'to mag-isa. Hindi ko kailangan ng group study.":
            $ ct_change(-5)
            $ mot_change(-10)
            if player_gender == "male":
                mc_m "Kaya ko 'to. Mag-isa lang ako nag-aral noon, kaya pa 'yun."
            else:
                mc_f "Okay na ako. Kaya ko 'to."
            kent "(bumubulong) That's not apathy. That's fear."
            narrator "(You heard him. Even under his breath. You felt the words settle in your chest like a stone.)"
            narrator "(You didn't answer. Because what could you say? He's right.)"
            narrator "(The conversation moves on without you. And you let it.)"

    show gabby normal at right with dissolve
    gabby "Okay, whatever we decide, the finals are two weeks away. Let's not pretend we have forever."
    rey "Gabby's right. The deadline doesn't wait for anyone to catch up."
    hide gabby with dissolve
    hide rey with dissolve
    hide kent with dissolve
    hide carl with dissolve
    hide carly with dissolve

    narrator "(You leave the canteen with more questions than answers. But at least one thing is clear: something has to change.)"

    ## ── SCENE 5-3: Ms. Iva's reminder ───────────────────────────────────────
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 5, Huling Klase"

    narrator "(The final class of the week. Ms. Iva stands at the podium, a stack of papers in her hand. She doesn't look happy.)"

    show ms_iva normal at center with dissolve
    ms_iva "Before you leave, one more thing. The final paper I'll be assigning has an essay component."
    ms_iva "The prompt: explain cognitive debt in the context of AI use in education. Then provide one concrete step an IT student can take to use AI ethically."
    ms_iva "You may cite RA 10173 or RA 10175. But cite them correctly. Citations that cannot be verified in the actual text of the law will be flagged. I've already caught three students doing that in the midterm essay."
    narrator "(She lets that sink in. A few students shift in their seats.)"
    ms_iva "Let me be clear. I can tell when someone read the actual text of a law. The wording is different. The logic flows differently. AI-generated citations sound clean, but they lack the texture of human comprehension."
    narrator "(She picks up a paper from the stack.)"
    ms_iva "This student cited RA 10173 Section 4 and quoted a definition that doesn't exist in the actual law. The AI made it up. And the student submitted it without checking."
    narrator "(She puts the paper down. Looks at the class. One by one.)"
    ms_iva "Sleep well. Study well. Wake up your own brain before you ask a machine to think for you."
    narrator "(The room is silent as she walks out. You're left with your notes, your conscience, and two weeks until finals.)"
    hide ms_iva with dissolve
return