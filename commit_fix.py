"""Commit and push the screens.rpy fix."""
import subprocess, os

base = os.path.dirname(os.path.abspath(__file__))

def run(cmd, check=True):
    print(f"  > {cmd}")
    result = subprocess.run(cmd, cwd=base, shell=True,
                            capture_output=True, text=True)
    if result.stdout.strip():
        print("   OUT:", result.stdout.strip())
    if result.stderr.strip():
        print("   ERR:", result.stderr.strip())
    if check and result.returncode != 0:
        print(f"  ERROR: code {result.returncode}")
    return result

print("=== git status ===")
run("git status --short")

print("\n=== git add -A ===")
run("git add -A")

print("\n=== git commit ===")
run('git commit -m "fix: resolve Ren\'Py syntax errors in screens.rpy (for loop Jump conditional, xmargin child)"', check=False)

print("\n=== git push ===")
result = run("git push", check=False)
if result.returncode != 0:
    print("\n  Push needs authentication. Open a terminal and run:")
    print("     git push")
    print("  (your browser will open for GitHub login)")

print("\n=== Done ===")
