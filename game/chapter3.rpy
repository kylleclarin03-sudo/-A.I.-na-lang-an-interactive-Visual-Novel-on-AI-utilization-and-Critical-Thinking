## game/chapter3.rpy
## Chapter 3, "Submit Mo Na Lang" (Week 3)

label chapter3:
    call screen chapter_title("3", "Submit Mo Na Lang", "Week 3, 'Basta may nasubmit...'")
    $ day_label = "Week 3, Umaga"
    $ current_week = 3

    ## ── SCENE 3-1: Mr. Kai's Python debug activity ───────────────────────────
    scene bg_lab with dissolve
    $ safe_play("music", "audio/bgm/bgm_classroom.ogg", loop=True)

    show mr_kai normal at left with dissolve
    mr_kai "Good morning! Okay, for today's debugging activity. May code kayo sa harap ninyo. Broken. I-fix ninyo."
    mr_kai "Twenty minutes. Walang phone, walang AI, walang Google. Sariling utak lang. Go."
    hide mr_kai with dissolve

    narrator "(You look at the pseudo-code on screen. Multiple bugs hidden. You do recognize some of them. Right?)"
    narrator "(Mr. Kai expects you to find them all. Let's see if you can debug each one.)"
    jump chapter3_debug_q1

## ── ROUTE A: Programming Debug Minigame (5 questions) ────────────────────────
## Reference: Python 3 common errors, Python official documentation

label chapter3_debug_q1:
    show screen minigame(
        "Programming, Python Debug Challenge (1/5)",
        "What error will this code produce?\n\ndef greet(name):\n    print('Hello, ' + name)\n\ngreet(123)",
        [
            "A. The function name 'greet' is invalid",
            "B. TypeError: cannot concatenate str and int",
            "C. No error, it will run fine",
            "D. IndentationError inside the function"
        ],
        1,
        "programming",
        8,
        5,
        correct_label="chapter3_debug_q1_correct",
        wrong_label="chapter3_debug_q1_wrong"
    )
    return

label chapter3_debug_q1_correct:
    narrator "(Right! You cannot concatenate a string and an integer in Python without explicit conversion.)"
    jump chapter3_debug_q2

label chapter3_debug_q1_wrong:
    narrator "(Not quite. Python is strict about mixing data types with the + operator. Strings and integers don't mix.)"
    jump chapter3_debug_q1

## ── Question 2: IndentationError ─────────────────────────────────────────────
## Reference: Python 3, PEP 8 indentation rules
label chapter3_debug_q2:
    show screen minigame(
        "Programming, Python Debug Challenge (2/5)",
        "What error will this code produce?\n\ndef check_number(x):\n    if x > 0:\n    print('Positive')\n    else:\n        print('Not positive')",
        [
            "A. SyntaxError: invalid syntax",
            "B. IndentationError: expected an indented block",
            "C. NameError: x is not defined",
            "D. ZeroDivisionError: division by zero"
        ],
        1,
        "programming",
        8,
        5,
        correct_label="chapter3_debug_q2_correct",
        wrong_label="chapter3_debug_q2_wrong"
    )
    return

label chapter3_debug_q2_correct:
    narrator "(Correct! The 'print' statement after 'if' must be indented. Python uses indentation to define code blocks.)"
    jump chapter3_debug_q3

label chapter3_debug_q2_wrong:
    narrator "(That's not it. Look at the line after 'if x > 0:', it should be indented but it isn't. Python cares about whitespace.)"
    jump chapter3_debug_q2

## ── Question 3: NameError (undefined variable) ───────────────────────────────
## Reference: Python 3, NameError and variable scope
label chapter3_debug_q3:
    show screen minigame(
        "Programming, Python Debug Challenge (3/5)",
        "What error will this code produce?\n\ndef calculate():\n    result = a + b\n    return result\n\nprint(calculate())",
        [
            "A. SyntaxError: invalid syntax",
            "B. NameError: name 'a' is not defined",
            "C. TypeError: unsupported operand type",
            "D. ValueError: not enough values to unpack"
        ],
        1,
        "programming",
        8,
        5,
        correct_label="chapter3_debug_q3_correct",
        wrong_label="chapter3_debug_q3_wrong"
    )
    return

label chapter3_debug_q3_correct:
    narrator "(Exactly! Variables 'a' and 'b' were never defined before being used. Python raises a NameError.)"
    jump chapter3_debug_q4

label chapter3_debug_q3_wrong:
    narrator "(Not quite. The variables 'a' and 'b' are being used without ever being assigned a value. Python doesn't know what they refer to.)"
    jump chapter3_debug_q3

## ── Question 4: IndexError (list out of range) ───────────────────────────────
## Reference: Python 3, IndexError and list indexing
label chapter3_debug_q4:
    show screen minigame(
        "Programming, Python Debug Challenge (4/5)",
        "What error will this code produce?\n\nnumbers = [[10, 20, 30]]\nprint(numbers[[3]])",
        [
            "A. IndexError: list index out of range",
            "B. KeyError: key not found",
            "C. TypeError: list indices must be integers",
            "D. ZeroDivisionError: division by zero"
        ],
        0,
        "programming",
        8,
        5,
        correct_label="chapter3_debug_q4_correct",
        wrong_label="chapter3_debug_q4_wrong"
    )
    return

label chapter3_debug_q4_correct:
    narrator "(Correct! The list has indices 0, 1, and 2. Index 3 does not exist, so Python raises an IndexError.)"
    jump chapter3_debug_q5

label chapter3_debug_q4_wrong:
    narrator "(Think again. Lists in Python are zero-indexed. A list of three elements has indices 0, 1, and 2. What happens when you try index 3?)"
    jump chapter3_debug_q4

## ── Question 5: SyntaxError (missing colon) ──────────────────────────────────
## Reference: Python 3, SyntaxError and compound statements
label chapter3_debug_q5:
    show screen minigame(
        "Programming, Python Debug Challenge (5/5)",
        "What error will this code produce?\n\nscore = 85\nif score >= 75\n    print('Passing')",
        [
            "A. SyntaxError: expected ':' after 'if' condition",
            "B. NameError: score is not defined",
            "C. IndentationError: unexpected indent",
            "D. TypeError: '>=' not supported"
        ],
        0,
        "programming",
        8,
        5,
        correct_label="chapter3_debug_q5_correct",
        wrong_label="chapter3_debug_q5_wrong"
    )
    return

label chapter3_debug_q5_correct:
    narrator "(Perfect! In Python, every compound statement like 'if', 'for', 'while' needs a colon at the end of the condition line.)"
    narrator "(You've identified all five bugs. Mr. Kai would be proud of your debugging skills.)"
    jump chapter3_post_minigame

label chapter3_debug_q5_wrong:
    narrator "(Not quite. Look at the 'if' line, something is missing at the end. Python expects a colon after the condition in compound statements.)"
    jump chapter3_debug_q5

## ── Return point after all 5 questions ───────────────────────────────────────
label chapter3_post_minigame:
    scene bg_lab with dissolve
    $ safe_play("music", "audio/bgm/bgm_classroom.ogg", loop=True)

    show mr_kai normal at left with dissolve
    mr_kai "Okay, time. Let's check the scoreboard."
    narrator "(Names appear on screen. Yours lands somewhere in the middle. Not the highest. Not the lowest.)"
    mr_kai "Good progress everyone. But I still want to see your individual approaches. Not every answer is yes or no, sometimes the process matters more."
    hide mr_kai with dissolve

    ## ── SCENE 3-2: Canteen halftime check-in ────────────────────────────────
    scene bg_canteen with dissolve
    $ safe_play("music", "audio/bgm/bgm_canteen.ogg", loop=True)
    $ day_label = "Week 3, Tanghali"

    narrator "(Hapon. Grupo sa canteen. Si Rey ay hindi karaniwan na nagsasalita, ngayon ay may sinasabi siya.)"

    show rey normal at left with dissolve
    show kent normal at center with dissolve
    show gabby normal at right with dissolve

    rey "...Nakita ko yung submission ni Gabby."
    narrator "(Tahimik. Lahat ay tumingin kay Rey.)"
    rey "Pareho ng sagot namin sa debugging activity. Word for word. Pero hindi tayo nag-usap."
    gabby "Coincidence. Pare-pareho naman ang bugs, pare-pareho ang solusyon."
    rey "Hindi ko sinasabi na copied. Sinasabi ko lang na... parehong solusyon. Ganoon naman talaga kung AI ang nagbibigay ng sagot."
    kent "Urm, technically that is a valid observation regarding AI output homogeneity,"
    gabby "Okay, sige nga, pakitaan mo ko ng proof."

    if player_bestfriend == "carl":
        show carl normal at right with dissolve
    else:
        show carly normal at right with dissolve

    narrator "(Tinitingnan kita ni [player_bestfriend].)"

    if player_bestfriend == "carl":
        carl "(mababa) Ikaw... sarili mo ba ang ginawa mo?"
    else:
        carly "(mababa) Ano sa tingin mo, tama ba si Rey?"

    ## CHOICE NODE 3-A
    menu:
        "Oo, sarili ko. Kahit na medyo mahirap.":
            $ ct_change(5)
            if player_gender == "male":
                mc_m "Sarili ko. Bagal ko nga ng kalahati ng klase, pero sarili ko."
            else:
                mc_f "Sarili ko. May mga parts na kinailangan ko ng tulong mula sa notes, pero sarili ko."
            if player_bestfriend == "carl":
                carl "(huminga ng malalim) Okay. Good."
            else:
                carly "(ngumiti) Sige. Ganoon talaga."
            narrator "(Nag-move on ang grupo. Pero sa isip mo, sigurado ka ba?)"

        "...Mostly. May AI-assisted na parts.":
            $ ct_change(-3)
            if player_gender == "male":
                mc_m "Mostly sarili ko. May isang part na kinonsulta ko sa AI."
            else:
                mc_f "Mostly. May napagod ako at pinag-AI ang isang section."
            if player_bestfriend == "carl":
                carl "Basta wag maging habit, okay? Mapapansin ni Sir 'yan."
            else:
                carly "Ingat ka lang. Mr. Kai ay matalino. Mapapansin niya."
            narrator "(Tama sila. At alam mo iyon.)"

        "Huwag mong alamin.":
            $ ct_change(-8)
            if player_gender == "male":
                mc_m "Huwag mong alamin."
            else:
                mc_f "Huwag mong alamin."
            if player_bestfriend == "carl":
                carl "...Sige."
            else:
                carly "...Okay."
            narrator "(Binabalewala mo siya. Pero hindi siya tumitigil sa pagmasid sa'yo.)"
            $ mot_change(-5)

    hide rey with dissolve
    hide kent with dissolve
    hide gabby with dissolve
    hide carl with dissolve
    hide carly with dissolve

    ## ── SCENE 3-3: Rey's warning ─────────────────────────────────────────────
    scene bg_hallway with dissolve
    $ day_label = "Week 3, Hapon"

    show rey normal at center with dissolve
    narrator "(Naabutan ka ni Rey sa hallway pagkatapos ng klase.)"
    rey "Hindi kita kinokontra. Alam ko kung bakit ginagawa ng mga tao 'yun."
    rey "Pero may napansin ako, kapag puro AI na ang nagsasagot, hindi ka na nagtatanong ng sarili mong mga tanong."
    rey "At 'yung mga sariling tanong, 'yun ang hindi mabibigyan ng AI ng sagot."

    narrator "(Lumakad na siya bago ka pa makasagot.)"
    hide rey with dissolve
    return