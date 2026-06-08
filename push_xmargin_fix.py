"""Commit and push the xmargin fix."""
import subprocess, os

base = os.path.dirname(os.path.abspath(__file__))

def run(cmd):
    print(f"  > {cmd}")
    r = subprocess.run(cmd, cwd=base, shell=True, capture_output=True, text=True)
    if r.stdout.strip(): print("   OUT:", r.stdout.strip())
    if r.stderr.strip(): print("   ERR:", r.stderr.strip())
    return r.returncode

print("=== git status ===")
run("git status --short")

print("\n=== git add ===")
run("git add -A")

print("\n=== git commit ===")
run('git commit -m "fix: replace invalid xmargin child statement with padding (30, 0) in screens.rpy HUD"')

print("\n=== git push ===")
run("git push")

print("\n=== Done ===")
