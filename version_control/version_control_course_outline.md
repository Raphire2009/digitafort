# Mastering Version Control: Git & GitHub on Windows (WSL) and Linux

**Course Goal:** By the end of this course, participants will be proficient in using Git for local version control, collaborating effectively on projects using GitHub, and setting up their development environment on both Windows (with WSL) and Linux.

**Target Audience:** Developers, students, and anyone looking to learn professional version control with Git and GitHub.

---

## Module 1: Introduction to Version Control & Git Fundamentals
*   **1.1 What is Version Control?**
    *   Why use VCS?
    *   Centralized vs. Distributed VCS
*   **1.2 Getting Started with Git**
    *   Introduction to Git
    *   Installation:
        *   **Windows:** Git Bash setup, WSL (Ubuntu/Debian) installation and configuration, Git installation within WSL.
        *   **Linux:** Git installation on common distributions (e.g., `apt` for Debian/Ubuntu, `yum`/`dnf` for Fedora/RHEL).
    *   Initial Git Configuration (`user.name`, `user.email`)
*   **1.3 The Basic Git Workflow**
    *   Working Directory, Staging Area, Local Repository
    *   `git init`
    *   `git status`
    *   `git add`
    *   `git commit`
    *   Viewing History (`git log`)
*   **1.4 Undoing Changes**
    *   `git restore` (undoing changes in working directory/staging area)
    *   `git reset` (un-staging, un-committing)
    *   `git revert` (undoing commits cleanly)

## Module 2: Branching and Merging in Git
*   **2.1 Understanding Branches**
    *   The importance of branching in development workflows
    *   `git branch` (create, list, delete)
    *   `git checkout` & `git switch`
*   **2.2 Merging Branches**
    *   `git merge` (fast-forward, three-way merge)
    *   Resolving Merge Conflicts (manual resolution)
*   **2.3 Introduction to Rebasing (Optional/Advanced)**
    *   `git rebase` (what it is, when to use, when *not* to use)

## Module 3: Collaborating with GitHub
*   **3.1 Introduction to GitHub**
    *   What is GitHub?
    *   Creating a GitHub account
    *   SSH Key setup (for both Windows/WSL and Linux)
*   **3.2 Working with Remote Repositories**
    *   Creating a new repository on GitHub
    *   `git clone` (getting a copy of a remote repo)
    *   `git push` (sending local changes to remote)
    *   `git pull` & `git fetch` (getting remote changes to local)
    *   Managing Remotes (`git remote`)
*   **3.3 GitHub Collaboration Workflow**
    *   Forking repositories
    *   Creating Pull Requests (PRs)
    *   Code Reviews
    *   Issues, Milestones, and Projects
    *   Basic GitHub Actions (brief overview)

## Module 4: Advanced Git Concepts & Best Practices
*   **4.1 Useful Git Commands**
    *   `git tag` (releasing versions)
    *   `git stash` (temporarily saving changes)
    *   `.gitignore` file (ignoring unwanted files)
    *   Git Aliases (shortcuts)
*   **4.2 Git Best Practices**
    *   Writing good commit messages
    *   Common branching strategies (e.g., Git Flow, GitHub Flow)
    *   Keeping your history clean