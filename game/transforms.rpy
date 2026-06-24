## game/transforms.rpy
## ATL Animation and Transformation Library for A.I. na lang!
## All sprite animations, entry/exit moves, and idle loops live here.
## Web-safe: all transforms use linear/ease only (no cubic-bezier).
## "repeat" transforms are O(1) per frame — safe for web builds.

## ── NAMED POSITIONS (replaces at left / at right / at center) ───────────────
## Use these instead of raw at positions for consistency.

transform pos_far_left:
    xalign 0.05
    yalign 1.0

transform pos_left:
    xalign 0.20
    yalign 1.0

transform pos_center:
    xalign 0.50
    yalign 1.0

transform pos_right:
    xalign 0.80
    yalign 1.0

transform pos_far_right:
    xalign 0.95
    yalign 1.0

## ── IDLE BREATHING (loop forever, very subtle) ──────────────────────────────

transform breathing:
    ## Default idle for all student sprites.
    subpixel True
    yalign 1.0
    yoffset 0
    linear 2.0 yoffset -7
    linear 2.0 yoffset 0
    repeat

transform breathing_tense:
    ## Faster, shallower — for high-stakes scenes.
    subpixel True
    yalign 1.0
    yoffset 0
    linear 1.1 yoffset -5
    linear 1.1 yoffset 0
    repeat

transform breathing_slow:
    ## Calm/tired characters.
    subpixel True
    yalign 1.0
    yoffset 0
    linear 3.0 yoffset -5
    linear 3.0 yoffset 0
    repeat

transform idle_sway:
    ## Energetic characters (Gabby). Subtle side-to-side.
    subpixel True
    yalign 1.0
    xoffset 0
    linear 1.4 xoffset 5
    linear 1.4 xoffset -5
    linear 1.4 xoffset 0
    repeat

transform thinking_float:
    ## Professor/contemplative float. Use with thinking sprite.
    subpixel True
    yalign 1.0
    yoffset 0
    linear 2.2 yoffset -9
    linear 2.2 yoffset 0
    repeat

## ── COMBINED POSITION + IDLE (most common usage pattern) ────────────────────
## These are the transforms you will use most in chapter files.
## Example: show carl normal at left_idle

transform left_idle:
    subpixel True
    xalign 0.20
    yalign 1.0
    yoffset 0
    linear 2.0 yoffset -7
    linear 2.0 yoffset 0
    repeat

transform center_idle:
    subpixel True
    xalign 0.50
    yalign 1.0
    yoffset 0
    linear 2.0 yoffset -7
    linear 2.0 yoffset 0
    repeat

transform right_idle:
    subpixel True
    xalign 0.80
    yalign 1.0
    yoffset 0
    linear 2.0 yoffset -7
    linear 2.0 yoffset 0
    repeat

transform far_left_idle:
    subpixel True
    xalign 0.08
    yalign 1.0
    yoffset 0
    linear 2.0 yoffset -6
    linear 2.0 yoffset 0
    repeat

transform far_right_idle:
    subpixel True
    xalign 0.92
    yalign 1.0
    yoffset 0
    linear 2.0 yoffset -6
    linear 2.0 yoffset 0
    repeat

transform center_idle_tense:
    subpixel True
    xalign 0.50
    yalign 1.0
    yoffset 0
    linear 1.1 yoffset -5
    linear 1.1 yoffset 0
    repeat

## ── ENTRY TRANSFORMS ────────────────────────────────────────────────────────
## Use WITH dissolve or on their own:
##   show carl normal at enter_from_left
##   show carl normal at enter_from_left with dissolve

transform enter_from_left:
    subpixel True
    yalign 1.0
    xalign -0.25
    alpha 0.0
    ease 0.45 xalign 0.20 alpha 1.0

transform enter_from_right:
    subpixel True
    yalign 1.0
    xalign 1.25
    alpha 0.0
    ease 0.45 xalign 0.80 alpha 1.0

transform enter_center_rise:
    ## Professors entering from center (authoritative).
    subpixel True
    xalign 0.50
    yalign 1.0
    yoffset 25
    alpha 0.0
    ease 0.40 yoffset 0 alpha 1.0

transform enter_from_far_left:
    subpixel True
    yalign 1.0
    xalign -0.25
    alpha 0.0
    ease 0.45 xalign 0.08 alpha 1.0

transform enter_from_far_right:
    subpixel True
    yalign 1.0
    xalign 1.25
    alpha 0.0
    ease 0.45 xalign 0.92 alpha 1.0

## ── EXIT TRANSFORMS ─────────────────────────────────────────────────────────
## Apply BEFORE hide:
##   show carl normal at exit_to_left
##   pause 0.5
##   hide carl

transform exit_to_left:
    subpixel True
    ease 0.35 xalign -0.25 alpha 0.0

transform exit_to_right:
    subpixel True
    ease 0.35 xalign 1.25 alpha 0.0

transform exit_down:
    subpixel True
    ease 0.35 yoffset 30 alpha 0.0

transform fade_out:
    linear 0.30 alpha 0.0

## ── EMOTIONAL / REACTION TRANSFORMS ─────────────────────────────────────────
## These play ONCE and stop. Apply to the sprite to trigger the animation.
## After applying, the sprite needs a base transform or it will hold the
## end position. Use:  show carl happy at right_idle
## immediately after the reaction scene if you want idle to resume.

transform bounce_once:
    ## Excited jump. Use for: good news, winning, "TARA NA!" moments.
    subpixel True
    yalign 1.0
    yoffset 0
    ease 0.13 yoffset -32
    ease 0.10 yoffset 0
    ease 0.07 yoffset -16
    ease 0.07 yoffset 0
    ease 0.05 yoffset -7
    ease 0.05 yoffset 0

transform shake_once:
    ## Stress shake. Use for: caught, wrong answer, alam na niya.
    subpixel True
    xoffset 0
    linear 0.05 xoffset -9
    linear 0.04 xoffset 9
    linear 0.04 xoffset -7
    linear 0.04 xoffset 7
    linear 0.04 xoffset -4
    linear 0.04 xoffset 4
    linear 0.04 xoffset 0

transform nod_once:
    ## Agreement/acknowledgement nod.
    subpixel True
    yoffset 0
    linear 0.08 yoffset 13
    linear 0.08 yoffset 0
    linear 0.06 yoffset 8
    linear 0.06 yoffset 0

transform flinch_once:
    ## Shock/surprise backward flinch.
    subpixel True
    xoffset 0 yoffset 0
    linear 0.06 xoffset -14 yoffset -6
    ease 0.14 xoffset 0 yoffset 0

transform step_forward:
    ## Character steps toward center (emphasis).
    subpixel True
    yalign 1.0
    zoom 1.0
    ease 0.30 zoom 1.06

transform step_back:
    subpixel True
    yalign 1.0
    zoom 1.06
    ease 0.30 zoom 1.0

## ── BACKGROUND OVERLAYS (for AI/phone UI moments) ──────────────────────────

transform scanline_pulse:
    ## Subtle pulse for the AI overlay. Apply to the overlay frame.
    alpha 0.85
    linear 1.2 alpha 1.0
    linear 1.2 alpha 0.85
    repeat

## ── CHAPTER TITLE CARD ANIMATIONS ──────────────────────────────────────────

transform title_enter:
    ## Used internally by chapter_title screen.
    yoffset -20 alpha 0.0
    ease 0.50 yoffset 0 alpha 1.0

transform subtitle_enter:
    yoffset 10 alpha 0.0
    ease 0.55 yoffset 0 alpha 1.0

## ── WEB PERFORMANCE NOTES ───────────────────────────────────────────────────
## - All transforms use only linear/ease (not complex easing functions).
## - "repeat" transforms schedule themselves: zero frame-budget overhead.
## - Each active "at transform" costs ~1ms CPU per frame on mid-range phones.
## - Limit active repeat transforms to 4 simultaneous sprites maximum.
## - Use pause 0.0 after reaction transforms to let them complete before
##   showing the next dialogue line.

## ── END OF transforms.rpy ───────────────────────────────────────────────────
