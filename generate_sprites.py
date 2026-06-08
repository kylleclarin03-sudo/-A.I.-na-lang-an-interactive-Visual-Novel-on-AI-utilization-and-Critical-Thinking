# generate_sprites.py
# Run: python generate_sprites.py
# Generates all 30 placeholder sprites + 6 background WebP files.

from PIL import Image, ImageDraw, ImageFont
import os, sys

SPRITE_W, SPRITE_H = 400, 700

CHARACTERS = {
    "alex":     {"base": (61, 110, 180),  "label": "Alex (M) MC",          "type": "student"},
    "alexa":    {"base": (120, 80, 170),  "label": "Alexa (F) MC",         "type": "student"},
    "carl":     {"base": (30, 130, 80),   "label": "Carl (Best Friend M)",  "type": "student"},
    "carly":    {"base": (20, 160, 140),  "label": "Carly (Best Friend F)", "type": "student"},
    "gabby":    {"base": (200, 100, 30),  "label": "Gabby (Bad Influence)", "type": "student"},
    "kent":     {"base": (160, 140, 20),  "label": "Kent (Nerdy 1)",        "type": "student"},
    "rey":      {"base": (90, 90, 110),   "label": "Rey (Nerdy 2)",         "type": "student"},
    "mr_earns": {"base": (160, 30, 30),   "label": "Mr. Earns (Networking)","type": "prof"},
    "mr_kai":   {"base": (20, 110, 50),   "label": "Mr. Kai (Programming)", "type": "prof"},
    "ms_iva":   {"base": (110, 40, 160),  "label": "Ms. Iva (Cybersecurity)","type": "prof"},
}

STUDENT_EXPRS = {
    "normal":   (0, 0, 0),
    "happy":    (40, 40, 20),
    "stressed": (-30, -20, -20),
}
PROF_EXPRS = {
    "normal":       (0, 0, 0),
    "thinking":     (-10, -10, 30),
    "disappointed": (-30, -30, -30),
}

def tint(base, delta):
    return tuple(max(0, min(255, b + d)) for b, d in zip(base, delta))

def get_font(size, bold=False):
    """Try several font paths for cross-platform support."""
    candidates = [
        # Windows
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf",
        # Linux
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default()

def make_sprite(char_key, char_info, expr_name, expr_delta, out_dir):
    r, g, b = tint(char_info["base"], expr_delta)
    img = Image.new("RGBA", (SPRITE_W, SPRITE_H), (r, g, b, 220))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle(
        [20, 20, SPRITE_W - 20, SPRITE_H - 20],
        radius=24, outline=(255, 255, 255, 80), width=3
    )
    cx = SPRITE_W // 2
    draw.ellipse([cx - 60, 60, cx + 60, 180],
                 fill=(255, 255, 255, 40), outline=(255, 255, 255, 80), width=2)

    font_big = get_font(22, bold=True)
    font_sm  = get_font(17)

    draw.text((SPRITE_W // 2, SPRITE_H // 2 - 30), char_info["label"],
              fill=(255, 255, 255, 230), font=font_big, anchor="mm")
    draw.text((SPRITE_W // 2, SPRITE_H // 2 + 20), f"[ {expr_name.upper()} ]",
              fill=(255, 255, 255, 180), font=font_sm, anchor="mm")
    draw.text((SPRITE_W // 2, SPRITE_H - 40), "PLACEHOLDER — Replace with final art",
              fill=(255, 255, 255, 100), font=font_sm, anchor="mm")

    fname = f"{char_key}_{expr_name}.webp"
    img.save(os.path.join(out_dir, fname), "webp", quality=85)
    print(f"  Created sprite: {fname}")

def make_backgrounds(bg_dir):
    os.makedirs(bg_dir, exist_ok=True)
    BACKGROUNDS = {
        "bg_classroom": (45, 50, 65),
        "bg_canteen":   (55, 45, 35),
        "bg_hallway":   (50, 55, 60),
        "bg_bedroom":   (30, 30, 45),
        "bg_lab":       (35, 45, 55),
        "bg_campus":    (40, 60, 40),
    }
    font = get_font(36, bold=True)
    for name, color in BACKGROUNDS.items():
        img = Image.new("RGB", (1920, 1080), color)
        draw = ImageDraw.Draw(img)
        draw.text((960, 540), f"[ {name.upper()} — PLACEHOLDER ]",
                  fill=(255, 255, 255, 160), font=font, anchor="mm")
        img.save(os.path.join(bg_dir, f"{name}.webp"), "webp", quality=85)
        print(f"  Created background: {name}.webp")

if __name__ == "__main__":
    sprite_dir = "game/images/sprites"
    os.makedirs(sprite_dir, exist_ok=True)

    total = 0
    for key, info in CHARACTERS.items():
        exprs = STUDENT_EXPRS if info["type"] == "student" else PROF_EXPRS
        for expr_name, delta in exprs.items():
            make_sprite(key, info, expr_name, delta, sprite_dir)
            total += 1

    make_backgrounds("game/images/backgrounds")

    print(f"\nDone. {total} sprites + 6 backgrounds written.")
    print("Replace these WebP files with final artwork before release.")
