"""Deep scan all .rpy files for common Ren'Py syntax issues."""
import os, glob, re

base = os.path.dirname(os.path.abspath(__file__))
rpy_files = sorted(glob.glob(os.path.join(base, "game", "*.rpy")))

# Patterns that commonly cause Ren'Py build errors
problems = {
    "xpadding/ypadding as child statement": re.compile(r'^\s+(x|ypadding)\s+\d', re.MULTILINE),
    "xmargin/ymargin as child statement": re.compile(r'^\s+(x|ymargin)\s+\d', re.MULTILINE),
    "inline Jump() conditional": re.compile(r'Jump\([^)]+\)\s+if\s+'),
    "xsize/ysize with text properties misplaced": None,  # checked by context
    "missing $ for python": None,  # hard to detect automatically
}

print("=" * 70)
print("DEEP SCAN: Looking for common Ren'Py syntax issues")
print("=" * 70)

issues_found = 0
for rpy in rpy_files:
    with open(rpy, encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")
    fname = os.path.basename(rpy)
    file_issues = []

    # Check for xpadding/ypadding as child (indented)
    for i, line in enumerate(lines, 1):
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        # Children of hbox/vbox/frame are indented; xpadding/ypadding/xmargin/ymargin
        # are properties and should be at the same indent as the parent, not indented deeper
        if indent >= 8:  # deep child
            if re.match(r'^xpadding\s+\d', stripped) or re.match(r'^ypadding\s+\d', stripped):
                file_issues.append((i, "xpadding/ypadding as child", line.rstrip()))
            if re.match(r'^xmargin\s+\d', stripped) or re.match(r'^ymargin\s+\d', stripped):
                file_issues.append((i, "xmargin/ymargin as child", line.rstrip()))

        # Check for inline conditional in Jump
        if re.search(r'Jump\([^)]+\)\s+if\s+', line):
            file_issues.append((i, "inline Jump() conditional", line.rstrip()))

    if file_issues:
        issues_found += len(file_issues)
        print(f"\n  ⚠  {fname}")
        for ln, kind, text in file_issues:
            print(f"     L{ln} [{kind}]: {text[:90]}")

print("\n" + "=" * 70)
if issues_found == 0:
    print("✓ No common syntax issues detected.")
else:
    print(f"⚠ {issues_found} potential issue(s) found across {len(rpy_files)} files.")
print("=" * 70)
print(f"\nFiles scanned: {len(rpy_files)}")
for f in rpy_files:
    print(f"  - {os.path.basename(f)}")
