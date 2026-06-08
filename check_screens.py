"""Check screens.rpy for xpadding / ypadding / line 307 issues."""
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "game", "screens.rpy")
with open(path, encoding="utf-8") as f:
    lines = f.readlines()

print("=== xpadding / ypadding scan ===")
hits = 0
for i, line in enumerate(lines, 1):
    if "xpadding" in line or "ypadding" in line:
        print(f"  L{i}: {line.rstrip()}")
        hits += 1
if hits == 0:
    print("  None found.")

print("\n=== Lines 295-320 (minigame header) ===")
for i in range(295, 320):
    if i < len(lines):
        print(f"  L{i+1}: {lines[i].rstrip()}")
