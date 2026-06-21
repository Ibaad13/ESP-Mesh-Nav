# GitHub setup guide (for a complete beginner)

This walks you through everything from "I have a folder of files" to "I have a public, professional-looking GitHub repo I can link to professors." No prior GitHub experience assumed.

---

## 0. A few concepts first (30 seconds)

- **GitHub** = a website that hosts your code/files and shows them nicely, with version history.
- **Git** = the tool that tracks changes and uploads (pushes) them to GitHub. You'll use a tiny number of commands.
- **Repository ("repo")** = one project's folder, tracked by Git, hosted on GitHub.
- **README.md** = the homepage of your repo. GitHub automatically displays it when someone opens your repo. This is the most important file for making a strong first impression.

You do **not** need to memorize Git. You need about 5 commands, used in the same order, every time.

---

## 1. Create a GitHub account

1. Go to [github.com](https://github.com) and sign up (use an email you'll check regularly — professors may message you there, or you'll want notifications).
2. Pick a clean, professional username (not a gamer-tag style name) — this becomes part of your repo's URL and is visible on your profile, e.g. `github.com/<your-username>`.

---

## 2. Install Git on your computer

- **Windows:** download from [git-scm.com](https://git-scm.com/downloads), run the installer, accept the defaults.
- **Mac:** open Terminal and type `git --version` — if it's not installed, macOS will prompt you to install Xcode command line tools (or install via [git-scm.com](https://git-scm.com/downloads)).
- **Linux:** `sudo apt install git` (Debian/Ubuntu) or your distro's equivalent.

Verify it worked by opening a terminal (Command Prompt, Terminal, or PowerShell) and typing:
```bash
git --version
```
You should see something like `git version 2.43.0`.

### Tell Git who you are (one-time setup)

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```
Use the same email as your GitHub account.

---

## 3. Create the repository on GitHub

1. Log into GitHub, click the **+** icon top-right → **New repository**.
2. **Repository name:** `ESP-Mesh-Nav` (or whatever you decide on — no spaces; use hyphens).
3. **Description:** something like *"Indoor localization using a distributed ESP32 RSSI mesh, extended with IMU-EKF sensor fusion"*.
4. Set visibility to **Public** (professors need to be able to open it without an account or invite).
5. **Do not** check "Add a README" — you already have one ready to upload.
6. Click **Create repository**.

GitHub will show you a page with setup instructions and a URL like:
```
https://github.com/<your-username>/ESP-Mesh-Nav.git
```
Keep this page open — you'll need that URL in a minute.

---

## 4. Organize your local folder

On your own computer, create one folder (e.g. `ESP-Mesh-Nav`) and arrange your files to match the structure laid out in the main [`README.md`](README.md) and the [`FILE_MANIFEST.md`](FILE_MANIFEST.md) — those two documents tell you exactly which subfolders to create and what to name every file. Do that first; it's much easier to get the structure right before your first upload than to reorganize after.

---

## 5. Upload (push) your files to GitHub

Open a terminal, navigate into your project folder, then run these commands **in this exact order**, one at a time:

```bash
# 1. Turn this folder into a Git repository
git init

# 2. Stage all files (tell Git "track everything in this folder")
git add .

# 3. Take a snapshot of the current state with a message describing it
git commit -m "Initial commit: ESP32 mesh localization + EKF sensor fusion"

# 4. Rename the default branch to "main" (GitHub's current convention)
git branch -M main

# 5. Connect your local folder to the GitHub repo you created in step 3
git remote add origin https://github.com/<your-username>/ESP-Mesh-Nav.git

# 6. Upload everything
git push -u origin main
```

Replace `<your-username>` with your actual GitHub username. After step 6, refresh the GitHub page in your browser — your files (and your README, rendered nicely) should now be there.

### If `git push` asks for a password and rejects it

GitHub no longer accepts your account password directly for this. You have two options:
- **Easiest:** install [GitHub Desktop](https://desktop.github.com/) (a GUI app) — sign in there once, and it handles authentication for you. You can do all of steps 4–6 by just dragging your folder in and clicking "Publish repository" instead of using the terminal at all.
- **Terminal-only:** create a [Personal Access Token](https://github.com/settings/tokens) on GitHub and use that in place of your password when prompted.

---

## 6. Making changes later (the day-to-day workflow)

Every time you update something (add a result image, tweak the README, add new code):

```bash
git add .
git commit -m "Describe what you changed, e.g. 'Add Phase 2 hardware integration results'"
git push
```

That's the entire loop. `git init` and `git remote add` are **one-time** setup steps — you never repeat them for the same repo.

---

## 7. Uploading the EKF simulation video specifically

Regular files (images, code, docx, pdf) work fine with the steps above. Video is the one exception — see the explanation in [`docs/README.md`](docs/README.md) for why, and the exact steps to get it embedded properly.

---

## 8. Polishing before you send the link to a professor

- [ ] Open your repo in an incognito/private browser window and click through it as a stranger would — does the README make sense without any extra context from you?
- [ ] Check every image actually displays (broken image icons usually mean a filename typo or wrong folder — cross-check against `FILE_MANIFEST.md`)
- [ ] Make sure the repo is **Public**, not Private (Settings → scroll to "Danger Zone" → "Change visibility" if you need to switch it)
- [ ] Pin this repo to your GitHub profile: go to your profile page → "Customize your pins" → select it, so it's the first thing visible when someone opens your profile
- [ ] Consider adding GitHub "Topics" (on the repo's main page, click the gear icon next to "About") like `esp32`, `indoor-positioning`, `kalman-filter`, `robotics`, `sensor-fusion` — this helps with discoverability and signals relevant keywords at a glance

---

## 9. Optional next steps once you're comfortable

- **Releases:** Once Phase 2 hardware integration is done, create a GitHub "Release" (tag a version like `v1.0`) — good for marking a stable milestone a professor could reference.
- **GitHub Pages:** You can later turn this repo into a simple project website for free, but the README alone is already enough for an application — don't over-engineer this before you need to.
