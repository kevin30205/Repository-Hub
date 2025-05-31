# Repository Hub

**Repository Hub** is a powerful and intuitive tool designed to help developers effortlessly discover, track, and manage their GitHub repositories. Say goodbye to scattered projects and endless searching! With **Repository Hub**, you get a unified, high-level overview of all your projects, making it easier than ever to grasp your codebase, identify key statistics, and quickly navigate to what matters most.

**Repository Hub** automatically aggregates all the GitHub repository information and updates the README daily.

---

## Core Features

* **Comprehensive Repository Overview:** Get an instant, structured view of all your repositories—personal, organizational, private, and public—all in one place.
* **Key Stats at a Glance:** Quickly assess the health and status of each project with immediate access to essential metrics like primary languages, star counts, and last updated times.
* **Intuitive Topic-Based Classification:** Effortlessly pinpoint and organize projects using a clear, categorized table, making it simple to filter by relevant topics.
* **Direct Access:** Seamlessly navigate from this centralized overview straight to any repository on GitHub with a single click.
* **Enhanced Project Discovery:** Easily re-familiarize yourself with older projects or uncover hidden gems across your entire portfolio.

---

## Automated Updates & Aggregated Data

This project ensures your repository list is always up-to-date and comprehensive.

* **Auto-Update Frequency:** The project automatically updates its data **every day at 00:00 (UTC)**.
* **Aggregated Content Includes:**
    * Repository Name
    * Visibility (Public/Private)
    * Description
    * Topics
    * Direct Project Link
    * Primary Language
    * Star Count
    * Last Updated Time
    * ...and more!


## Get Started

### Get your GitHub Personal Access Token

1. Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens).
2. Click "Fine-grained token".
3. Click "Generate new token".
4. Set a token name, description, expiration.
5. Select your desired repository access:
    * **Public repositories**
        * Read-only access to public repositories.
    * **All repositories**
        * This applies to all current and future repositories you own. Also includes public repositories (read-only).
    * **Only select repositories**
        * Select at least one repository. Max 50 repositories. Also includes public repositories (read-only).

    If you only want to track public repositories, select **Public repositories**.

    If you want to track both public and private repositories, select **All repositories** or just authorized this repo by selecting **Only select repositories**.
6. Permissions:
    * Set `Repository permissions - Contents` to `Read and Write`.
7. Click "Generate token" at the bottom.
8. Copy the generated token and save it securely (you won't be able to see it again).
9. Use this token as the value for `GH_PAT` in your GitHub repository secrets and local environment variables.

> Warning: Never share your token publicly. Treat it like a password.

