"""
gitpush.py — Initialize git, commit all project files, and push to GitHub.
Run: python gitpush.py
"""
import subprocess, os, sys

base = os.path.dirname(os.path.abspath(__file__))
remote_url = "https://github.com/kylleclarin03-sudo/-A.I.-na-lang-an-interactive-Visual-Novel-on-AI-utilization-and-Critical-Thinking.git"

def run(cmd, check=True):
    print(f"  > {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    result = subprocess.run(
        cmd, cwd=base, shell=isinstance(cmd, str),
        capture_output=True, text=True
    )
    if result.stdout.strip():
        print("   ", result.stdout.strip())
    if result.stderr.strip():
        print("   STDERR:", result.stderr.strip())
    if check and result.returncode != 0:
        print(f"  ERROR: command failed (code {result.returncode})")
        sys.exit(1)
    return result

print("=== Step 1: Git init ===")
run(["git", "init"])

print("\n=== Step 2: Configure user ===")
run(["git", "config", "user.email", "kylleclarin03@gmail.com"])
run(["git", "config", "user.name", "kylleclarin03-sudo"])

print("\n=== Step 3: Stage all files ===")
run(["git", "add", "-A"])

print("\n=== Step 4: Commit ===")
run(["git", "commit", "-m",
     "feat: complete A.I. na lang! visual novel v1.0\n\n"
     "- Full 8-chapter Taglish story + Prologue\n"
     "- 6 endings (Special Good, Good Guilt, Good Solid, Redemption, Bad, Caught)\n"
     "- 10 characters, 30 placeholder WebP sprites, 6 backgrounds\n"
     "- HUD with CT meter, Motivation bar, Grade display\n"
     "- Quick menu with phone AI overlay\n"
     "- 5 minigame screens (Networking, Programming, Cybersecurity)\n"
     "- Mobile-first gui.rpy with Ren'Py variant scaling\n"
     "- progressive_download.txt for fast web load\n"
     "- GitHub Actions automated Pages deployment"])

print("\n=== Step 5: Set remote origin ===")
# Remove existing remote if present (ignore error)
run(["git", "remote", "remove", "origin"], check=False)
run(["git", "remote", "add", "origin", remote_url])

print("\n=== Step 6: Set branch to main ===")
run(["git", "branch", "-M", "main"])

print("\n=== Step 7: Push to GitHub ===")
result = run(["git", "push", "-u", "origin", "main", "--force"], check=False)
if result.returncode != 0:
    print("\n  Push failed. Common reasons:")
    print("  1. Not logged into GitHub — run: git credential-manager configure")
    print("  2. Auth token not stored — run: git push (browser will open for login)")
    print("\n  To push manually:")
    print(f"     git remote add origin {remote_url}")
    print("     git branch -M main")
    print("     git push -u origin main --force")
else:
    print("\n=== SUCCESS! ===")
    print("Code pushed to GitHub.")
    print("GitHub Actions will now build and deploy to GitHub Pages.")
    print("Check progress at:")
    print("  https://github.com/kylleclarin03-sudo/-A.I.-na-lang-an-interactive-Visual-Novel-on-AI-utilization-and-Critical-Thinking/actions")
    print("\nGame will be live at:")
    print("  https://kylleclarin03-sudo.github.io/-A.I.-na-lang-an-interactive-Visual-Novel-on-AI-utilization-and-Critical-Thinking/")
