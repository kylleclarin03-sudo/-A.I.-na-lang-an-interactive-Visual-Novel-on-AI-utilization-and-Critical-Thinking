import os, glob

GAME = os.path.dirname(os.path.abspath(__file__))

errors = []

## 1. No duplicate label ai_used_result
rpy_files = glob.glob(os.path.join(GAME, "*.rpy"))
count = 0
for f in rpy_files:
    txt = open(f, encoding="utf-8", errors="ignore").read()
    count += txt.count("label ai_used_result:")
if count != 1:
    errors.append(f"DUPLICATE: ai_used_result found {count} times (need 1)")

## 2. No xpadding/xmargin as standalone child statements
for f in rpy_files:
    txt = open(f, encoding="utf-8", errors="ignore").read()
    for line in txt.splitlines():
        stripped = line.strip()
        if stripped.startswith("xpadding ") or stripped.startswith("xmargin "):
            if not any(c in line for c in ["=", "#", "define", "style"]):
                errors.append(f"BAD CHILD: {line.strip()} in {os.path.basename(f)}")

## 3. No renpy.save_slots_per_page()
for f in rpy_files:
    if "save_slots_per_page" in open(f, encoding="utf-8", errors="ignore").read():
        errors.append(f"OLD API: save_slots_per_page in {os.path.basename(f)}")

## 4. transforms.rpy exists
if not os.path.isfile(os.path.join(GAME, "transforms.rpy")):
    errors.append("MISSING: game/transforms.rpy not found")

## 5. No complex easing in ATL (web compat) — only check non-comment lines
if os.path.isfile(os.path.join(GAME, "transforms.rpy")):
    txt = open(os.path.join(GAME, "transforms.rpy"), encoding="utf-8").read()
    for line in txt.splitlines():
        stripped = line.strip()
        if stripped.startswith("##"):
            continue  # skip comments
        if "cubic" in stripped and "cubic-bezier" not in stripped:
            errors.append(f"ATL: 'cubic' found in transforms.rpy (may crash on web)")
        if "back_" in stripped:
            errors.append(f"ATL: 'back_' found in transforms.rpy (may crash on web)")

if errors:
    print("\n".join(["ERRORS:"] + errors))
else:
    print("✓  All checks passed. Safe to commit and push.")