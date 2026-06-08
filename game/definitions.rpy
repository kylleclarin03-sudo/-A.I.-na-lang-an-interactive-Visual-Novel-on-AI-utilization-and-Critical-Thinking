## game/definitions.rpy
## All character definitions, persistent variables, and image declarations.

# ── GLOBAL GAME VARIABLES ────────────────────────────────────────────────────
default critical_thinking    = 50   # 0–100. Drops with AI, rises with effort.
default motivation           = 50   # 0–100. Drops with failure/shame, rises with wins.
default networking_grade     = 65   # Subject grade 0–100. INC if below 60 at finals.
default programming_grade    = 65
default cyber_grade          = 65
default ai_use_count         = 0    # Times player chose "Ask AI" during minigames.
default got_caught           = False  # True if Ms. Iva catches hallucinated citation.
default player_gender        = "male"   # Set in prologue character selection.
default player_bestfriend    = "carl"   # "carl" or "carly", set in prologue.
default player_name          = "Alex"   # Overwritten by name input in prologue.
default current_week         = 1        # Narrative week tracker (1–8).
default day_label            = "Day 1, Umaga"

# ── HELPER FUNCTIONS ─────────────────────────────────────────────────────────
init python:

    def ct_change(delta):
        store.critical_thinking = max(0, min(100, store.critical_thinking + delta))

    def mot_change(delta):
        store.motivation = max(0, min(100, store.motivation + delta))

    def grade_change(subject, delta):
        if subject == "networking":
            store.networking_grade = max(0, min(100, store.networking_grade + delta))
        elif subject == "programming":
            store.programming_grade = max(0, min(100, store.programming_grade + delta))
        elif subject == "cyber":
            store.cyber_grade = max(0, min(100, store.cyber_grade + delta))

    def use_ai(subject=None, grade_boost=8):
        store.ai_use_count += 1
        ct_change(-10)
        if subject:
            grade_change(subject, grade_boost)

    def letter_grade(score):
        if score >= 90: return "A"
        elif score >= 80: return "B"
        elif score >= 70: return "C"
        elif score >= 60: return "D"
        else: return "INC"

    def any_incomplete():
        return (store.networking_grade < 60 or
                store.programming_grade < 60 or
                store.cyber_grade < 60)

    def determine_ending():
        ng     = store.networking_grade
        pg     = store.programming_grade
        cg     = store.cyber_grade
        ct     = store.critical_thinking
        mot    = store.motivation
        ai     = store.ai_use_count
        caught = store.got_caught

        all_pass = (ng >= 60 and pg >= 60 and cg >= 60)
        all_high = (ng >= 85 and pg >= 85 and cg >= 85)

        if caught:
            return "ending_caught"
        if any_incomplete():
            if ct >= 45 and mot >= 45:
                return "ending_redemption"
            else:
                return "ending_bad"
        if all_high and ai == 0 and ct >= 75:
            return "ending_special_good"
        if all_pass and ai > 3 and ct < 55:
            return "ending_good_guilt"
        if all_pass:
            return "ending_good_solid"
        return "ending_bad"

# ── CHARACTER DEFINITIONS ────────────────────────────────────────────────────

define mc_m = Character("[player_name]",
    color="#79c0ff", what_color="#e6edf3",
    window_background=Solid("#161b22CC"))

define mc_f = Character("[player_name]",
    color="#a5d6ff", what_color="#e6edf3",
    window_background=Solid("#161b22CC"))

define carl = Character("Carl",
    color="#7ee787", what_color="#e6edf3",
    window_background=Solid("#161b22CC"))

define carly = Character("Carly",
    color="#a5d6ff", what_color="#e6edf3",
    window_background=Solid("#161b22CC"))

define gabby = Character("Gabby",
    color="#f78166", what_color="#e6edf3",
    window_background=Solid("#161b22CC"))

define kent = Character("Kent",
    color="#d2a8ff", what_color="#e6edf3",
    window_background=Solid("#161b22CC"))

define rey = Character("Rey",
    color="#ffa657", what_color="#e6edf3",
    window_background=Solid("#161b22CC"))

define mr_earns = Character("Mr. Earns",
    color="#e3b341", what_color="#e6edf3",
    window_background=Solid("#1a1a22CC"))

define mr_kai = Character("Mr. Kai",
    color="#ff7b72", what_color="#e6edf3",
    window_background=Solid("#1a1a22CC"))

define ms_iva = Character("Ms. Iva",
    color="#56d364", what_color="#e6edf3",
    window_background=Solid("#1a1a22CC"))

define narrator = Character(None,
    what_italic=True, what_color="#c9d1d9",
    window_background=Solid("#0d1117CC"))

define sys_voice = Character(None,
    what_color="#8b949e", what_italic=True)

define groupchat = Character("GROUP CHAT",
    color="#8b949e", what_color="#c9d1d9",
    what_italic=True, window_background=Solid("#21262DCC"))

# ── IMAGE DECLARATIONS ───────────────────────────────────────────────────────

## Sprites, students (normal / happy / stressed)
image alex normal    = "images/sprites/alex_normal.webp"
image alex happy     = "images/sprites/alex_happy.webp"
image alex stressed  = "images/sprites/alex_stressed.webp"
image alexa normal   = "images/sprites/alexa_normal.webp"
image alexa happy    = "images/sprites/alexa_happy.webp"
image alexa stressed = "images/sprites/alexa_stressed.webp"
image carl normal    = "images/sprites/carl_normal.webp"
image carl happy     = "images/sprites/carl_happy.webp"
image carl stressed  = "images/sprites/carl_stressed.webp"
image carly normal   = "images/sprites/carly_normal.webp"
image carly happy    = "images/sprites/carly_happy.webp"
image carly stressed = "images/sprites/carly_stressed.webp"
image gabby normal   = "images/sprites/gabby_normal.webp"
image gabby happy    = "images/sprites/gabby_happy.webp"
image gabby stressed = "images/sprites/gabby_stressed.webp"
image kent normal    = "images/sprites/kent_normal.webp"
image kent happy     = "images/sprites/kent_happy.webp"
image kent stressed  = "images/sprites/kent_stressed.webp"
image rey normal     = "images/sprites/rey_normal.webp"
image rey happy      = "images/sprites/rey_happy.webp"
image rey stressed   = "images/sprites/rey_stressed.webp"

## Sprites, professors (normal / thinking / disappointed)
image mr_earns normal       = "images/sprites/mr_earns_normal.webp"
image mr_earns thinking     = "images/sprites/mr_earns_thinking.webp"
image mr_earns disappointed = "images/sprites/mr_earns_disappointed.webp"
image mr_kai normal         = "images/sprites/mr_kai_normal.webp"
image mr_kai thinking       = "images/sprites/mr_kai_thinking.webp"
image mr_kai disappointed   = "images/sprites/mr_kai_disappointed.webp"
image ms_iva normal         = "images/sprites/ms_iva_normal.webp"
image ms_iva thinking       = "images/sprites/ms_iva_thinking.webp"
image ms_iva disappointed   = "images/sprites/ms_iva_disappointed.webp"

## Backgrounds
image bg_classroom = "images/backgrounds/bg_classroom.webp"
image bg_canteen   = "images/backgrounds/bg_canteen.webp"
image bg_hallway   = "images/backgrounds/bg_hallway.webp"
image bg_bedroom   = "images/backgrounds/bg_bedroom.webp"
image bg_lab       = "images/backgrounds/bg_lab.webp"
image bg_campus    = "images/backgrounds/bg_campus.webp"

## Dynamic MC sprite (resolves male or female based on player_gender)
## Dynamic best friend sprite (resolves Carl or Carly based on player_bestfriend)
## Using renpy.image() in an init python block to avoid ATL parser confusion
## with multi-line ConditionSwitch indentation.
init python:
    renpy.image("mc normal", ConditionSwitch(
        "player_gender == 'male'", "images/sprites/alex_normal.webp",
        "True", "images/sprites/alexa_normal.webp"
    ))
    renpy.image("mc happy", ConditionSwitch(
        "player_gender == 'male'", "images/sprites/alex_happy.webp",
        "True", "images/sprites/alexa_happy.webp"
    ))
    renpy.image("mc stressed", ConditionSwitch(
        "player_gender == 'male'", "images/sprites/alex_stressed.webp",
        "True", "images/sprites/alexa_stressed.webp"
    ))
    renpy.image("bestfriend normal", ConditionSwitch(
        "player_bestfriend == 'carl'", "images/sprites/carl_normal.webp",
        "True", "images/sprites/carly_normal.webp"
    ))
    renpy.image("bestfriend happy", ConditionSwitch(
        "player_bestfriend == 'carl'", "images/sprites/carl_happy.webp",
        "True", "images/sprites/carly_happy.webp"
    ))
    renpy.image("bestfriend stressed", ConditionSwitch(
        "player_bestfriend == 'carl'", "images/sprites/carl_stressed.webp",
        "True", "images/sprites/carly_stressed.webp"
    ))
