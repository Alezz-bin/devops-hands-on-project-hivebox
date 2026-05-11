[![Dynamic DevOps Roadmap](https://img.shields.io/badge/Dynamic_DevOps_Roadmap-559e11?style=for-the-badge&logo=Vercel&logoColor=white)](https://devopsroadmap.io/getting-started/)
[![Community](https://img.shields.io/badge/Join_Community-%23FF6719?style=for-the-badge&logo=substack&logoColor=white)](https://newsletter.devopsroadmap.io/subscribe)
[![Telegram Group](https://img.shields.io/badge/Telegram_Group-%232ca5e0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/DevOpsHive/985)
[![Fork on GitHub](https://img.shields.io/badge/Fork_On_GitHub-%2336465D?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)

# HiveBox - DevOps End-to-End Hands-On Project

<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox" style="display: block; padding: .5em 0; text-align: center;">
    <img alt="HiveBox - DevOps End-to-End Hands-On Project" border="0" width="90%" src="https://devopsroadmap.io/img/projects/hivebox-devops-end-to-end-project.png" />
  </a>
</p>

> [!CAUTION]
> **[Fork](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)** this repo, and create PRs in your fork, **NOT** in this repo!

> [!TIP]
> If you are looking for the full roadmap, including this project, go back to the [getting started](https://devopsroadmap.io/getting-started) page.

This repository is the starting point for [HiveBox](https://devopsroadmap.io/projects/hivebox/), the end-to-end hands-on project.

You can fork this repository and start implementing the [HiveBox](https://devopsroadmap.io/projects/hivebox/) project. HiveBox project follows the same Dynamic MVP-style mindset used in the [roadmap](https://devopsroadmap.io/).

The project aims to cover the whole Software Development Life Cycle (SDLC). That means each phase will cover all aspects of DevOps, such as planning, coding, containers, testing, continuous integration, continuous delivery, infrastructure, etc.

Happy DevOpsing ♾️

## Before you start

Here is a pre-start checklist:

- ⭐ <a target="_blank" href="https://github.com/DevOpsHiveHQ/dynamic-devops-roadmap">Star the **roadmap** repo</a> on GitHub for better visibility.
- ✉️ <a target="_blank" href="https://newsletter.devopsroadmap.io/subscribe">Join the community</a> for the project community activities, which include mentorship, job posting, online meetings, workshops, career tips and tricks, and more.
- 🌐 <a target="_blank" href="https://t.me/DevOpsHive/985">Join the Telegram group</a> for interactive communication.

## Preparation

- [Create GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) (if you don't have one), then [fork this repository](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork) and start from there.
- [Create GitHub project board](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project) for this repository (use `Kanban` template).
- Each phase should be presented as a pull request against the `main` branch. Don’t push directly to the main branch!
- Document as you go. Always assume that someone else will read your project at any phase.
- You can get senseBox IDs by checking the [openSenseMap](https://opensensemap.org/) website. Use 3 senseBox IDs close to each other (you can use the following [5eba5fbad46fb8001b799786](https://opensensemap.org/explore/5eba5fbad46fb8001b799786), [5c21ff8f919bf8001adf2488](https://opensensemap.org/explore/5c21ff8f919bf8001adf2488), and [5ade1acf223bd80019a1011c](https://opensensemap.org/explore/5ade1acf223bd80019a1011c)). Just copy the IDs, you will need them in the next steps.

<br/>
<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox/" imageanchor="1">
    <img src="https://img.shields.io/badge/Get_Started_Now-559e11?style=for-the-badge&logo=Vercel&logoColor=white" />
  </a><br/>
</p>

---

## Implementation

### Project Overview

HiveBox is a Python-based application that reports its current version. The entry point is `main.py`, which prints the application version and exits cleanly. It is containerized using Docker with a lightweight `python:3.11-slim` base image.

---

## Testing the Application

This section documents how to test the HiveBox application both locally and inside a Docker container.

### Prerequisites

| Tool | Minimum Version | Purpose |
|------|----------------|---------|
| Python | 3.11+ | Run the app locally |
| Docker | 20.10+ | Build and run the containerized app |

> [!NOTE]
> Docker Desktop must be running before executing any Docker commands.
> You can verify Docker is running with: `docker info`

---

### 1. Local Testing (Python)

Run the application directly with Python to verify it prints the version and exits with code `0`.

```bash
# From the project root directory
python main.py
```

**Expected output:**
```
$v0.0.1
```

**Expected exit code:** `0`

To check the exit code explicitly on Windows PowerShell:

```powershell
python main.py
echo $LASTEXITCODE   # Should print: 0
```

---

### 2. Docker Build Testing

Build the Docker image to verify the `Dockerfile` is valid and the image compiles successfully.

```bash
docker build -t hivebox:local .
```

**Expected output:** A successful build ending with a line similar to:
```
Successfully tagged hivebox:local
```

Verify the image was created:

```bash
docker images hivebox
```

---

### 3. Docker Run Testing

Run the container and verify the application produces the correct output.

```bash
docker run --rm hivebox:local
```

**Expected output:**
```
$v0.0.1
```

**Expected container exit code:** `0`

To capture and verify the exit code in PowerShell:

```powershell
docker run --rm hivebox:local
echo $LASTEXITCODE   # Should print: 0
```

---

### 4. Dockerfile Linting (Hadolint)

Lint the `Dockerfile` with [Hadolint](https://github.com/hadolint/hadolint) to catch best-practice violations before building.

```bash
hadolint Dockerfile
```

**Expected output:** No warnings or errors (silent output = pass).

> [!TIP]
> If Hadolint is not installed, you can run it via Docker without a local install:
> ```bash
> docker run --rm -i hadolint/hadolint < Dockerfile
> ```

---

### 5. Full Test Checklist

Use this checklist to confirm the application is working correctly end-to-end:

- [ ] `python main.py` prints `$v0.0.1` and exits with code `0`
- [ ] `docker build -t hivebox:local .` completes without errors
- [ ] `docker run --rm hivebox:local` prints `$v0.0.1` and exits with code `0`
- [ ] `hadolint Dockerfile` reports no linting issues

---

### Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| `docker: command not found` | Docker not installed | Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) |
| `error during connect` on `docker ps` | Docker Desktop is not running | Launch Docker Desktop from the system tray |
| `python: command not found` | Python not on PATH | Install Python 3.11+ or use `python3` |
| Container exits with code `1` | Application error in `main.py` | Check `main.py` for syntax/runtime errors |
