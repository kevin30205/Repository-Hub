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

    If you want to track both public and private repositories, select **All repositories**.
    
    If you only want to track authorized repos, select **Only select repositories** and add the repos manually.
6. Permissions:
    * Set `Repository permissions - Contents` to `Read and Write`.
7. Click "Generate token" at the bottom.
8. Copy the generated token and save it securely (you won't be able to see it again).
9. Use this token as the value for `GH_PAT` in your GitHub repository secrets and local environment variables.

> Warning: Never share your token publicly. Treat it like a password.


### Set up GitHub Actions Automation

1. Go to **Repository Hub** repository page.
2. Click "Settings" → "Secrets and variables" → "Actions".
3. Click "New repository secret".
4. Add a secret named `GH_PAT` with your GitHub Personal Access Token.
    > The Secret Name should be aligned with the configuration in the GitHub workflow file. We named `GH_PAT` in this repo.
5. Click "Add Secret".
6. Go to "Settings" → "Actions" → "General" → "Workflow permissions".
7. Select **Read and write permissions**.
    * Workflows have read and write permissions in the repository for all scopes.
8. Click "Save".
9. Make sure the GitHub Workflow file `.github/workflows/update.yml` exists.
10. The workflow will run automatically every day at 00:00 (UTC), or you can trigger it manually from the Actions page.


### Preview and Update Locally (Optional)

The section describe the steps if you want to update **Repository Hub** locally.


#### 1. Prepare your local environment

- Make sure you have Python 3 installed on your computer. You can check by running:
    ```bash
    python --version
    ```
- (Recommended) Create and activate a Conda environment:
    ```bash
    conda create -n Repository-Hub python=3.10
    conda activate Repository-Hub
    ```
- Install required packages:
    ```bash
    # by pip
    pip install requests plotly kaleido

    # by conda
    conda install -c conda-forge requests plotly kaleido-core -y
    ```

#### 2. Preview the result locally

You can run the script on your own computer to preview the generated README and charts before pushing to GitHub:

- Set environment variables in your terminal (replace with your own values):
    ```bash
    # linux
    export GH_PAT="<your GitHub Personal Access Token>"
    export GITHUB_USERNAME="<your GitHub username>"

    # windows
    $env:GH_PAT="<your GitHub Personal Access Token>"
    $env:GITHUB_USERNAME="<your GitHub username>"
    ```
- Run the script:
    ```bash
    python update_readme.py
    ```
- Check the generated README.md and chart files in your project folder.


---

## GitHub Repository Dashboard

> The aggregated contents are automatically generated by the script and updated in this section.

---

### Repository Information Overview

| Type   | Count |
|--------|-------|
| Total  | 270 |
| Public | 1 |
| Private| 269 |

### Language Distribution Overview

| Language | Count | Percentage |
|---|---|---|
| Python | 201 | 74.4% |
| C++ | 26 | 9.6% |
| Jupyter Notebook | 13 | 4.8% |
| Markdown | 8 | 3.0% |
| HTML | 7 | 2.6% |
| TeX | 3 | 1.1% |
| Shell | 3 | 1.1% |
| JavaScript | 2 | 0.7% |
| Unknown | 2 | 0.7% |
| Kotlin | 1 | 0.4% |
| Cuda | 1 | 0.4% |
| CSS | 1 | 0.4% |
| TypeScript | 1 | 0.4% |
| Svelte | 1 | 0.4% |

![Language Distribution Overview](charts/language_pie.png)

### Top 10 Repositories by Star Count

![Top 10 Repositories by Star Count](charts/star_bar.png)

### Repository Creation Trend

![Repository Creation Trend](charts/repo_timeline.png)

### Top 10 Topics by Repository Count

![Top 10 Topics by Repository Count](charts/topic_bar.png)

### Categorized Repository Index

### 3d-generation

* **Total Repositories:** 11

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| GaussianIP_survey | Private | 0 | 2025-05-29 | 2025-06-18 | Python | Survey of GaussianIP (CVPR 2025) | [🔗](https://github.com/kevin30205/GaussianIP_survey) |
| DreamGaussian4D_survey | Private | 0 | 2025-05-11 | 2025-06-18 | Python | Survey of DreamGaussian4D (arXiv 2023) | [🔗](https://github.com/kevin30205/DreamGaussian4D_survey) |
| HumanNorm_survey | Private | 0 | 2025-05-09 | 2025-06-18 | Python | Survey of HumanNorm (CVPR 2024) | [🔗](https://github.com/kevin30205/HumanNorm_survey) |
| GaussianDreamerPro_survey | Private | 0 | 2025-05-06 | 2025-06-18 | C++ | Survey of GaussianDreamerPro (arXiv 2024) | [🔗](https://github.com/kevin30205/GaussianDreamerPro_survey) |
| Stable-Dreamfusion_survey | Private | 0 | 2025-04-24 | 2025-06-18 | Python | Survey of Stable-Dreamfusion (ICLR 2023) | [🔗](https://github.com/kevin30205/Stable-Dreamfusion_survey) |
| DreamCraft3D_survey | Private | 0 | 2025-04-24 | 2025-06-18 | Python | Survey of DreamCraft3D (ICLR 2024) | [🔗](https://github.com/kevin30205/DreamCraft3D_survey) |
| LucidDreamer_survey | Private | 0 | 2025-04-20 | 2025-06-18 | Python | Survey of LucidDreamer (CVPR 2024) | [🔗](https://github.com/kevin30205/LucidDreamer_survey) |
| Fantasia3D_survey | Private | 0 | 2025-04-19 | 2025-06-18 | Python | Survey of Fantasia3D (ICCV 2023) | [🔗](https://github.com/kevin30205/Fantasia3D_survey) |
| GaussianDreamer_survey | Private | 0 | 2025-04-18 | 2025-06-18 | Python | Survey of GaussianDreamer (CVPR 2024) | [🔗](https://github.com/kevin30205/GaussianDreamer_survey) |
| GSGEN_survey | Private | 0 | 2025-04-14 | 2025-06-18 | Python | Survey of GSGEN (CVPR 2024) | [🔗](https://github.com/kevin30205/GSGEN_survey) |
| DreamGaussian_survey | Private | 0 | 2025-04-13 | 2025-06-18 | Python | Survey of DreamGaussian (ICLR 2024) | [🔗](https://github.com/kevin30205/DreamGaussian_survey) |

### Unassigned

* **Total Repositories:** 2

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| competation-pawpularity | Public | 0 | 2023-04-25 | 2025-03-27 | Jupyter Notebook |  | [🔗](https://github.com/RxChi1d/competation-pawpularity) |
| Japanese_Study | Private | 0 | 2025-02-23 | 2025-02-23 | Unknown | The Japanese Study Notes. | [🔗](https://github.com/kevin30205/Japanese_Study) |

### acceleration

* **Total Repositories:** 2

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| DashGaussian_survey | Private | 0 | 2025-06-07 | 2025-06-18 | C++ | Survey of DashGaussian (CVPR 2025) | [🔗](https://github.com/kevin30205/DashGaussian_survey) |
| InstantSplat_survey | Private | 0 | 2025-04-08 | 2025-06-18 | Python | Survey of InstantSplat (arXiv 2024) | [🔗](https://github.com/kevin30205/InstantSplat_survey) |

### avatar

* **Total Repositories:** 31

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| GaussianIP_survey | Private | 0 | 2025-05-29 | 2025-06-18 | Python | Survey of GaussianIP (CVPR 2025) | [🔗](https://github.com/kevin30205/GaussianIP_survey) |
| HAHA_survey | Private | 0 | 2025-05-21 | 2025-06-18 | Python | Survey of HAHA (ACCV 2024) | [🔗](https://github.com/kevin30205/HAHA_survey) |
| RoGSplat_survey | Private | 0 | 2025-05-09 | 2025-06-18 | Python | Survey of RoGSplat (CVPR 2025) | [🔗](https://github.com/kevin30205/RoGSplat_survey) |
| HumanNorm_survey | Private | 0 | 2025-05-09 | 2025-06-18 | Python | Survey of HumanNorm (CVPR 2024) | [🔗](https://github.com/kevin30205/HumanNorm_survey) |
| Relighting4D_survey | Private | 0 | 2025-04-05 | 2025-06-18 | Python | Survey of Relighting4D (ECCV 2022) | [🔗](https://github.com/kevin30205/Relighting4D_survey) |
| GART_survey | Private | 0 | 2025-04-17 | 2025-06-18 | Python | Survey of GART (CVPR 2024) | [🔗](https://github.com/kevin30205/GART_survey) |
| AnimatableGaussians_survey | Private | 0 | 2025-04-19 | 2025-06-18 | Python | Survey of Animatable Gaussians (CVPR 2024) | [🔗](https://github.com/kevin30205/AnimatableGaussians_survey) |
| ARAH_survey | Private | 0 | 2025-04-04 | 2025-06-18 | Python | Survey of ARAH (ECCV 2022) | [🔗](https://github.com/kevin30205/ARAH_survey) |
| Neural-Human-Performer_survey | Private | 0 | 2025-04-05 | 2025-06-18 | Python | Survey of Neural Human Performer (NeurIPS 2021) | [🔗](https://github.com/kevin30205/Neural-Human-Performer_survey) |
| IntrinsicAvatar_survey | Private | 0 | 2025-04-05 | 2025-06-18 | Python | Survey of IntrinsicAvatar (CVPR 2024) | [🔗](https://github.com/kevin30205/IntrinsicAvatar_survey) |
| TAVA_survey | Private | 0 | 2025-04-04 | 2025-06-18 | Python | Survey of TAVA (ECCV 2022) | [🔗](https://github.com/kevin30205/TAVA_survey) |
| Neural-Body_survey | Private | 0 | 2025-04-05 | 2025-06-18 | Python | Survey of Neural Body (CVPR 2021) | [🔗](https://github.com/kevin30205/Neural-Body_survey) |
| 3DGS-Avatar_survey | Private | 0 | 2025-04-04 | 2025-06-18 | Python | Survey of 3DGS-Avatar (CVPR 2024) | [🔗](https://github.com/kevin30205/3DGS-Avatar_survey) |
| GPS-Gaussian_survey | Private | 0 | 2025-04-03 | 2025-06-18 | C++ | Survey of GPS-Gaussian (CVPR 2024) | [🔗](https://github.com/kevin30205/GPS-Gaussian_survey) |
| GoMAvatar_survey | Private | 0 | 2025-03-31 | 2025-06-18 | Python | Survey of GoMAvatar (CVPR 2024) | [🔗](https://github.com/kevin30205/GoMAvatar_survey) |
| Animatable-NeRF_survey | Private | 0 | 2025-03-29 | 2025-06-18 | Python | Survey of Animatable-NeRF (ICCV 2021) | [🔗](https://github.com/kevin30205/Animatable-NeRF_survey) |
| SplattingAvatar_survey | Private | 0 | 2025-03-30 | 2025-06-18 | Python | Survey of SplattingAvatar (CVPR 2024) | [🔗](https://github.com/kevin30205/SplattingAvatar_survey) |
| GaussianAvatar_survey | Private | 0 | 2025-03-31 | 2025-06-18 | Python | Survey of GaussianAvatar (CVPR 2024) | [🔗](https://github.com/kevin30205/GaussianAvatar_survey) |
| HUGS_survey | Private | 0 | 2025-03-30 | 2025-06-18 | Python | Survey of HUGS (CVPR 2024) | [🔗](https://github.com/kevin30205/HUGS_survey) |
| HumanNeRF-SE_survey | Private | 0 | 2025-03-29 | 2025-06-18 | Python | Survey of HumanNeRF-SE (CVPR 2024) | [🔗](https://github.com/kevin30205/HumanNeRF-SE_survey) |
| OccFusion_survey | Private | 0 | 2025-03-28 | 2025-06-18 | Python | Survey of OccFusion (NeurIPS 2024) | [🔗](https://github.com/kevin30205/OccFusion_survey) |
| InstantAvatar_survey | Private | 0 | 2025-03-28 | 2025-06-18 | Python | Survey of InstantAvatar (CVPR 2023) | [🔗](https://github.com/kevin30205/InstantAvatar_survey) |
| GauHuman_survey | Private | 0 | 2025-03-28 | 2025-06-18 | Python | Survey of GauHuman (CVPR 2024) | [🔗](https://github.com/kevin30205/GauHuman_survey) |
| OccNeRF_survey | Private | 0 | 2024-01-30 | 2025-06-18 | Python | Survey of OccNeRF (ICCV 2023) | [🔗](https://github.com/kevin30205/OccNeRF_survey) |
| TransHuman_survey | Private | 0 | 2023-11-26 | 2025-06-18 | Python | Survey of TransHuman (ICCV 2023) | [🔗](https://github.com/kevin30205/TransHuman_survey) |
| SHERF_survey | Private | 0 | 2023-11-26 | 2025-06-18 | Python | Survey of SHERF (ICCV 2023) | [🔗](https://github.com/kevin30205/SHERF_survey) |
| NVR-in-Minutes_survey | Private | 0 | 2023-09-26 | 2025-06-18 | Python | Survey of NVR-in-Minutes (CVPR 2023) | [🔗](https://github.com/kevin30205/NVR-in-Minutes_survey) |
| Neuman_survey | Private | 0 | 2023-08-13 | 2025-06-18 | Python | Survey of Neuman (ECCV 2022) | [🔗](https://github.com/kevin30205/Neuman_survey) |
| MonoHuman_survey | Private | 0 | 2023-08-27 | 2025-06-18 | Python | Survey of MonoHuman (CVPR 2023) | [🔗](https://github.com/kevin30205/MonoHuman_survey) |
| HumanNeRF_survey | Private | 0 | 2023-08-27 | 2025-06-18 | Python | Survey of HumanNeRF (CVPR 2022) | [🔗](https://github.com/kevin30205/HumanNeRF_survey) |
| Vid2Avatar_survey | Private | 0 | 2023-09-26 | 2025-06-18 | Python | Survey of Vid2Avatar (CVPR 2023) | [🔗](https://github.com/kevin30205/Vid2Avatar_survey) |

### compression

* **Total Repositories:** 17

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| GaussianSpa_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of GaussianSpa (CVPR 2025) | [🔗](https://github.com/kevin30205/GaussianSpa_survey) |
| TC-GS_survey | Private | 0 | 2025-06-05 | 2025-06-18 | C++ | Survey of TC-GS (ICME 2025) | [🔗](https://github.com/kevin30205/TC-GS_survey) |
| PUP-3D-GS_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of PUP 3D-GS (CVPR 2025) | [🔗](https://github.com/kevin30205/PUP-3D-GS_survey) |
| CAT-3DGS_survey | Private | 0 | 2025-06-05 | 2025-06-18 | Python | Survey of CAT-3DGS (ICLR 2025) | [🔗](https://github.com/kevin30205/CAT-3DGS_survey) |
| ControlGS_survey | Private | 0 | 2025-05-29 | 2025-06-18 | C++ | Survey of ControlGS (arXiv 2025) | [🔗](https://github.com/kevin30205/ControlGS_survey) |
| Self-Organizing-Gaussians_survey | Private | 0 | 2025-05-14 | 2025-06-18 | Python | Survey of Self-Organizing Gaussians (ECCV 2024) | [🔗](https://github.com/kevin30205/Self-Organizing-Gaussians_survey) |
| MaskGaussian_survey | Private | 0 | 2025-04-21 | 2025-06-18 | C++ | Survey of MaskGaussian (CVPR 2025) | [🔗](https://github.com/kevin30205/MaskGaussian_survey) |
| ContextGS_survey | Private | 0 | 2025-04-09 | 2025-06-18 | Python | Survey of ContextGS (NeurIPS 2024) | [🔗](https://github.com/kevin30205/ContextGS_survey) |
| Mini-Splatting_survey | Private | 0 | 2025-04-11 | 2025-06-18 | Python | Survey of Mini-Splatting (ECCV 2024) | [🔗](https://github.com/kevin30205/Mini-Splatting_survey) |
| FCGS_survey | Private | 0 | 2025-04-12 | 2025-06-18 | C++ | Survey of FCGS (ICLR 2025) | [🔗](https://github.com/kevin30205/FCGS_survey) |
| EAGLES_survey | Private | 0 | 2025-04-11 | 2025-06-18 | C++ | Survey of EAGLES (ECCV 2024) | [🔗](https://github.com/kevin30205/EAGLES_survey) |
| PCGS_survey | Private | 0 | 2025-04-10 | 2025-06-18 | C++ | Survey of PCGS (arXiv 2025) | [🔗](https://github.com/kevin30205/PCGS_survey) |
| HAC-plus_survey | Private | 0 | 2025-04-09 | 2025-06-18 | C++ | Survey of HAC++ (arXiv 2025) | [🔗](https://github.com/kevin30205/HAC-plus_survey) |
| C3DGS_survey | Private | 0 | 2025-04-11 | 2025-06-18 | Python | Survey of C3DGS (CVPR 2024) | [🔗](https://github.com/kevin30205/C3DGS_survey) |
| Compact-3DGS_survey | Private | 0 | 2025-04-10 | 2025-06-18 | Python | Survey of Compact-3DGS (CVPR 2024) | [🔗](https://github.com/kevin30205/Compact-3DGS_survey) |
| LightGaussian_survey | Private | 0 | 2025-04-10 | 2025-06-18 | Python | Survey of LightGaussian (NeurIPS 2024) | [🔗](https://github.com/kevin30205/LightGaussian_survey) |
| HAC_survey | Private | 0 | 2025-04-09 | 2025-06-18 | Python | Survey of HAC (ECCV 2024) | [🔗](https://github.com/kevin30205/HAC_survey) |

### dataset

* **Total Repositories:** 1

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| NeRF_Datasets | Private | 0 | 2023-09-05 | 2025-06-01 | Shell | Datasets used in NeRF Projects | [🔗](https://github.com/kevin30205/NeRF_Datasets) |

### deblur

* **Total Repositories:** 7

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| Gaussian-Splatting-on-the-Move_survey | Private | 0 | 2025-04-30 | 2025-06-18 | Python | Survey of Gaussian Splatting on the Move (ECCV 2024) | [🔗](https://github.com/kevin30205/Gaussian-Splatting-on-the-Move_survey) |
| BeNeRF_survey | Private | 0 | 2025-04-28 | 2025-06-18 | Python | Survey of BeNeRF (ECCV 2024) | [🔗](https://github.com/kevin30205/BeNeRF_survey) |
| BAGS_survey | Private | 0 | 2025-05-04 | 2025-06-18 | Python | Survey of BAGS (ECCV 2024) | [🔗](https://github.com/kevin30205/BAGS_survey) |
| BAD-Gaussians_survey | Private | 0 | 2025-04-30 | 2025-06-18 | Python | Survey of BAD-Gaussians (ECCV 2024) | [🔗](https://github.com/kevin30205/BAD-Gaussians_survey) |
| Deblurring-3D-Gaussian-Splatting_survey | Private | 0 | 2025-04-01 | 2025-06-18 | Python | Survey of Deblurring 3D Gaussian Splatting (ECCV 2024) | [🔗](https://github.com/kevin30205/Deblurring-3D-Gaussian-Splatting_survey) |
| BAD-NeRF_survey | Private | 0 | 2024-03-13 | 2025-06-18 | Python | Survey of BAD-NeRF (CVPR 2023) | [🔗](https://github.com/kevin30205/BAD-NeRF_survey) |
| Deblur-NeRF_survey | Private | 0 | 2024-01-10 | 2025-06-18 | Python | Survey of Deblur-NeRF (CVPR 2022) | [🔗](https://github.com/kevin30205/Deblur-NeRF_survey) |

### depth-estimation

* **Total Repositories:** 4

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| Prompt-Depth-Anything_survey | Private | 0 | 2025-06-05 | 2025-06-19 | Python | Survey of Prompt Depth Anything (CVPR 2025) | [🔗](https://github.com/kevin30205/Prompt-Depth-Anything_survey) |
| Video-Depth-Anything_survey | Private | 0 | 2025-06-05 | 2025-06-19 | Python | Survey of Video Depth Anything (CVPR 2025) | [🔗](https://github.com/kevin30205/Video-Depth-Anything_survey) |
| Depth-Anything-V2_survey | Private | 0 | 2025-06-05 | 2025-06-19 | Python | Survey of Depth-Anything-V2 (NeurIPS 2024) | [🔗](https://github.com/kevin30205/Depth-Anything-V2_survey) |
| Depth-Anything_survey | Private | 0 | 2025-06-05 | 2025-06-19 | Python | Survey of Depth Anything (CVPR 2024) | [🔗](https://github.com/kevin30205/Depth-Anything_survey) |

### dynamic

* **Total Repositories:** 16

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| MoDec-GS_survey | Private | 0 | 2025-06-08 | 2025-06-18 | Python | Survey of MoDec-GS (CVPR 2025) | [🔗](https://github.com/kevin30205/MoDec-GS_survey) |
| GaussianPrediction_survey | Private | 0 | 2025-05-30 | 2025-06-18 | HTML | Survey of GaussianPrediction (SIGGRAPH 2024) | [🔗](https://github.com/kevin30205/GaussianPrediction_survey) |
| GaGS_survey | Private | 0 | 2025-05-15 | 2025-06-18 | C++ | Survey of GaGS (CVPR 2024) | [🔗](https://github.com/kevin30205/GaGS_survey) |
| 4DGaussians_survey | Private | 0 | 2025-05-07 | 2025-06-18 | Jupyter Notebook | Survey of 4DGaussians (CVPR 2024) | [🔗](https://github.com/kevin30205/4DGaussians_survey) |
| TiNeuVox_survey | Private | 0 | 2025-04-30 | 2025-06-18 | Python | Survey of TiNeuVox (SIGGRAPH Asia 2022) | [🔗](https://github.com/kevin30205/TiNeuVox_survey) |
| SpacetimeGaussians_survey | Private | 0 | 2025-04-13 | 2025-06-18 | Python | Survey of SpacetimeGaussians (CVPR 2024) | [🔗](https://github.com/kevin30205/SpacetimeGaussians_survey) |
| Deformable-3D-Gaussians_survey | Private | 0 | 2025-04-12 | 2025-06-18 | Python | Survey of Deformable 3D Gaussians (CVPR 2024) | [🔗](https://github.com/kevin30205/Deformable-3D-Gaussians_survey) |
| 4D-Gaussian-Splatting_survey | Private | 0 | 2025-04-01 | 2025-06-18 | Python | Survey of 4D Gaussian Splatting (ICLR 2024) | [🔗](https://github.com/kevin30205/4D-Gaussian-Splatting_survey) |
| Tensor4D_survey | Private | 0 | 2024-03-23 | 2025-06-18 | Python | Survey of Tensor4D (CVPR 2023) | [🔗](https://github.com/kevin30205/Tensor4D_survey) |
| RoDynRF_survey | Private | 0 | 2024-04-12 | 2025-06-18 | Python | Survey of RoDynRF (CVPR 2023) | [🔗](https://github.com/kevin30205/RoDynRF_survey) |
| DynamicNeRF_survey | Private | 0 | 2024-04-12 | 2025-06-18 | Python | Survey of DynamicNeRF (ICCV 2021) | [🔗](https://github.com/kevin30205/DynamicNeRF_survey) |
| HyperNeRF_survey | Private | 0 | 2023-11-26 | 2025-06-18 | Python | Survey of HyperNeRF (SIGGRAPH Asia 2021) | [🔗](https://github.com/kevin30205/HyperNeRF_survey) |
| ENeRF_survey | Private | 0 | 2024-02-17 | 2025-06-18 | Python | Survey of ENeRF (SIGGRAPH Asia 2022) | [🔗](https://github.com/kevin30205/ENeRF_survey) |
| LocalRF_survey | Private | 0 | 2024-01-10 | 2025-06-18 | Python | Survey of LocalRF (CVPR 2023) | [🔗](https://github.com/kevin30205/LocalRF_survey) |
| K-Planes_survey | Private | 0 | 2023-08-13 | 2025-06-18 | Python | Survey of K-Planes (CVPR 2023) | [🔗](https://github.com/kevin30205/K-Planes_survey) |
| HexPlane_survey | Private | 0 | 2023-08-18 | 2025-06-18 | Python | Survey of HexPlane (CVPR 2023) | [🔗](https://github.com/kevin30205/HexPlane_survey) |

### gaussian-splatting

* **Total Repositories:** 126

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| ABC-GS_survey | Private | 0 | 2025-06-15 | 2025-06-18 | Python | Survey of ABC-GS (ICME 2025) | [🔗](https://github.com/kevin30205/ABC-GS_survey) |
| StopThePop_survey | Private | 0 | 2025-06-14 | 2025-06-18 | Python | Survey of StopThePop (SIGGRAPH 2024) | [🔗](https://github.com/kevin30205/StopThePop_survey) |
| 3DGRUT_survey | Private | 0 | 2025-06-09 | 2025-06-18 | Python | Survey of 3DGRUT (CVPR 2025) | [🔗](https://github.com/kevin30205/3DGRUT_survey) |
| 4DTAM_survey | Private | 0 | 2025-06-11 | 2025-06-18 | C++ | Survey of 4DTAM (CVPR 2025) | [🔗](https://github.com/kevin30205/4DTAM_survey) |
| PanSplat_survey | Private | 0 | 2025-06-10 | 2025-06-18 | Python | Survey of PanSplat (CVPR 2025) | [🔗](https://github.com/kevin30205/PanSplat_survey) |
| RNG_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of RNG (CVPR 2025) | [🔗](https://github.com/kevin30205/RNG_survey) |
| GaussianShader_survey | Private | 0 | 2025-06-08 | 2025-06-18 | C++ | Survey of GaussianShader (CVPR 2024) | [🔗](https://github.com/kevin30205/GaussianShader_survey) |
| ReCap_survey | Private | 0 | 2025-06-08 | 2025-06-18 | Python | Survey of ReCap (CVPR 2025) | [🔗](https://github.com/kevin30205/ReCap_survey) |
| Luminance-GS_survey | Private | 0 | 2025-06-10 | 2025-06-18 | Python | Survey of Luminance-GS (CVPR 2025) | [🔗](https://github.com/kevin30205/Luminance-GS_survey) |
| FisherRF_survey | Private | 0 | 2025-06-08 | 2025-06-18 | Python | Survey of FisherRF (ECCV 2024) | [🔗](https://github.com/kevin30205/FisherRF_survey) |
| MoDec-GS_survey | Private | 0 | 2025-06-08 | 2025-06-18 | Python | Survey of MoDec-GS (CVPR 2025) | [🔗](https://github.com/kevin30205/MoDec-GS_survey) |
| Sparse2DGS_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of Sparse2DGS (CVPR 2025) | [🔗](https://github.com/kevin30205/Sparse2DGS_survey) |
| DashGaussian_survey | Private | 0 | 2025-06-07 | 2025-06-18 | C++ | Survey of DashGaussian (CVPR 2025) | [🔗](https://github.com/kevin30205/DashGaussian_survey) |
| GaussianSpa_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of GaussianSpa (CVPR 2025) | [🔗](https://github.com/kevin30205/GaussianSpa_survey) |
| EOGS_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of EOGS (CVPR 2025) | [🔗](https://github.com/kevin30205/EOGS_survey) |
| GS-LPM_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of GS-LPM (CVPR 2025) | [🔗](https://github.com/kevin30205/GS-LPM_survey) |
| TC-GS_survey | Private | 0 | 2025-06-05 | 2025-06-18 | C++ | Survey of TC-GS (ICME 2025) | [🔗](https://github.com/kevin30205/TC-GS_survey) |
| PUP-3D-GS_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of PUP 3D-GS (CVPR 2025) | [🔗](https://github.com/kevin30205/PUP-3D-GS_survey) |
| Speedy-Splat_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of Speedy-Splat (CVPR 2025) | [🔗](https://github.com/kevin30205/Speedy-Splat_survey) |
| CAT-3DGS_survey | Private | 0 | 2025-06-05 | 2025-06-18 | Python | Survey of CAT-3DGS (ICLR 2025) | [🔗](https://github.com/kevin30205/CAT-3DGS_survey) |
| GS-3_survey | Private | 0 | 2025-05-30 | 2025-06-18 | Python | Survey of GS^3 (SIGGRAPH Asia 2024) | [🔗](https://github.com/kevin30205/GS-3_survey) |
| GS-IR_survey | Private | 0 | 2025-05-30 | 2025-06-18 | C++ | Survey of GS-IR (arXiv 2023) | [🔗](https://github.com/kevin30205/GS-IR_survey) |
| GI-GS_survey | Private | 0 | 2025-05-30 | 2025-06-18 | C++ | Survey of GI-GS (ICLR 2025) | [🔗](https://github.com/kevin30205/GI-GS_survey) |
| GaussianPrediction_survey | Private | 0 | 2025-05-30 | 2025-06-18 | HTML | Survey of GaussianPrediction (SIGGRAPH 2024) | [🔗](https://github.com/kevin30205/GaussianPrediction_survey) |
| AdR-Gaussian_survey | Private | 0 | 2025-05-30 | 2025-06-18 | Python | Survey of AdR-Gaussian (SIGGRAPH Asia 2024) | [🔗](https://github.com/kevin30205/AdR-Gaussian_survey) |
| CoR-GS_survey | Private | 0 | 2025-05-29 | 2025-06-18 | Python | Survey of CoR-GS (ECCV 2024) | [🔗](https://github.com/kevin30205/CoR-GS_survey) |
| GaussianIP_survey | Private | 0 | 2025-05-29 | 2025-06-18 | Python | Survey of GaussianIP (CVPR 2025) | [🔗](https://github.com/kevin30205/GaussianIP_survey) |
| SparseGS_survey | Private | 0 | 2025-05-19 | 2025-06-18 | Python | Survey of SparseGS (3DV 2025) | [🔗](https://github.com/kevin30205/SparseGS_survey) |
| HAHA_survey | Private | 0 | 2025-05-21 | 2025-06-18 | Python | Survey of HAHA (ACCV 2024) | [🔗](https://github.com/kevin30205/HAHA_survey) |
| Deformable-Radial-Kernel-Splatting_survey | Private | 0 | 2025-05-21 | 2025-06-18 | Python | Survey of Deformable Radial Kernel Splatting (CVPR 2025) | [🔗](https://github.com/kevin30205/Deformable-Radial-Kernel-Splatting_survey) |
| ControlGS_survey | Private | 0 | 2025-05-29 | 2025-06-18 | C++ | Survey of ControlGS (arXiv 2025) | [🔗](https://github.com/kevin30205/ControlGS_survey) |
| hierarchical-3d-gaussians_survey | Private | 0 | 2025-05-21 | 2025-06-18 | Python | Survey of Hierarchical 3D Gaussians (SIGGRAPH 2024) | [🔗](https://github.com/kevin30205/hierarchical-3d-gaussians_survey) |
| BBSplat_survey | Private | 0 | 2025-05-15 | 2025-06-18 | Python | Survey of BBSplat (arXiv 2024) | [🔗](https://github.com/kevin30205/BBSplat_survey) |
| DRGS_survey | Private | 0 | 2025-05-19 | 2025-06-18 | Python | Survey of DRGS (CVPRW 2024) | [🔗](https://github.com/kevin30205/DRGS_survey) |
| Gaussian-Splatting-on-the-Move_survey | Private | 0 | 2025-04-30 | 2025-06-18 | Python | Survey of Gaussian Splatting on the Move (ECCV 2024) | [🔗](https://github.com/kevin30205/Gaussian-Splatting-on-the-Move_survey) |
| Taming-3DGS_survey | Private | 0 | 2025-05-18 | 2025-06-18 | Python | Survey of Taming 3DGS (SIGGRAPH Asia 2024) | [🔗](https://github.com/kevin30205/Taming-3DGS_survey) |
| SteepGS_survey | Private | 0 | 2025-05-19 | 2025-06-18 | Python | Survey of SteepGS (CVPR 2025) | [🔗](https://github.com/kevin30205/SteepGS_survey) |
| CoherentGS_survey | Private | 0 | 2025-05-14 | 2025-06-18 | Python | Survey of CoherentGS (ECCV 2024) | [🔗](https://github.com/kevin30205/CoherentGS_survey) |
| GaGS_survey | Private | 0 | 2025-05-15 | 2025-06-18 | C++ | Survey of GaGS (CVPR 2024) | [🔗](https://github.com/kevin30205/GaGS_survey) |
| Analytic-Splatting_survey | Private | 0 | 2025-05-15 | 2025-06-18 | Python | Survey of Analytic-Splatting (ECCV 2024) | [🔗](https://github.com/kevin30205/Analytic-Splatting_survey) |
| OP43DGS_survey | Private | 0 | 2025-05-14 | 2025-06-18 | Cuda | Survey of OP43DGS (ECCV 2024) | [🔗](https://github.com/kevin30205/OP43DGS_survey) |
| HoGS_survey | Private | 0 | 2025-05-13 | 2025-06-18 | C++ | Survey of HoGS (CVPR 2025) | [🔗](https://github.com/kevin30205/HoGS_survey) |
| Sparse-Voxels-Rasterizer_survey | Private | 0 | 2025-05-13 | 2025-06-18 | Jupyter Notebook | Survey of Sparse Voxels Rasterizer (CVPR 2025) | [🔗](https://github.com/kevin30205/Sparse-Voxels-Rasterizer_survey) |
| GES_survey | Private | 0 | 2025-05-14 | 2025-06-18 | Python | Survey of GES (CVPR 2024) | [🔗](https://github.com/kevin30205/GES_survey) |
| Self-Organizing-Gaussians_survey | Private | 0 | 2025-05-14 | 2025-06-18 | Python | Survey of Self-Organizing Gaussians (ECCV 2024) | [🔗](https://github.com/kevin30205/Self-Organizing-Gaussians_survey) |
| 3D-Student-Splatting-and-Scooping_survey | Private | 0 | 2025-05-13 | 2025-06-18 | Python | Survey of 3D Student Splatting and Scooping (CVPR 2025) | [🔗](https://github.com/kevin30205/3D-Student-Splatting-and-Scooping_survey) |
| AtomGS_survey | Private | 0 | 2025-05-12 | 2025-06-18 | Python | Survey of AtomGS (BMVC 2024) | [🔗](https://github.com/kevin30205/AtomGS_survey) |
| RoGSplat_survey | Private | 0 | 2025-05-09 | 2025-06-18 | Python | Survey of RoGSplat (CVPR 2025) | [🔗](https://github.com/kevin30205/RoGSplat_survey) |
| Beta-Splatting_survey | Private | 0 | 2025-05-12 | 2025-06-18 | Python | Survey of Beta Splatting (SIGGRAPH 2025) | [🔗](https://github.com/kevin30205/Beta-Splatting_survey) |
| MonoGS_survey | Private | 0 | 2025-05-11 | 2025-06-18 | Python | Survey of MonoGS (CVPR 2024) | [🔗](https://github.com/kevin30205/MonoGS_survey) |
| DreamGaussian4D_survey | Private | 0 | 2025-05-11 | 2025-06-18 | Python | Survey of DreamGaussian4D (arXiv 2023) | [🔗](https://github.com/kevin30205/DreamGaussian4D_survey) |
| HumanNorm_survey | Private | 0 | 2025-05-09 | 2025-06-18 | Python | Survey of HumanNorm (CVPR 2024) | [🔗](https://github.com/kevin30205/HumanNorm_survey) |
| SGCR_survey | Private | 0 | 2025-05-12 | 2025-06-18 | Python | Survey of SGCR (CVPR 2025) | [🔗](https://github.com/kevin30205/SGCR_survey) |
| TeT-Splatting_survey | Private | 0 | 2025-05-07 | 2025-06-18 | Jupyter Notebook | Survey of TeT-Splatting (NeurIPS 2024) | [🔗](https://github.com/kevin30205/TeT-Splatting_survey) |
| IRGS_survey | Private | 0 | 2025-05-07 | 2025-06-18 | HTML | Survey of IRGS (CVPR 2025) | [🔗](https://github.com/kevin30205/IRGS_survey) |
| SC-GS_survey | Private | 0 | 2025-05-07 | 2025-06-18 | Python | Survey of SC-GS (CVPR 2024) | [🔗](https://github.com/kevin30205/SC-GS_survey) |
| 4DGaussians_survey | Private | 0 | 2025-05-07 | 2025-06-18 | Jupyter Notebook | Survey of 4DGaussians (CVPR 2024) | [🔗](https://github.com/kevin30205/4DGaussians_survey) |
| Ref-Gaussian_survey | Private | 0 | 2025-05-05 | 2025-06-18 | C++ | Survey of Ref-Gaussian (ICLR 2025) | [🔗](https://github.com/kevin30205/Ref-Gaussian_survey) |
| RaDe-GS_survey | Private | 0 | 2025-04-30 | 2025-06-18 | C++ | Survey of RaDe-GS (arXiv 2024) | [🔗](https://github.com/kevin30205/RaDe-GS_survey) |
| GaussianDreamerPro_survey | Private | 0 | 2025-05-06 | 2025-06-18 | C++ | Survey of GaussianDreamerPro (arXiv 2024) | [🔗](https://github.com/kevin30205/GaussianDreamerPro_survey) |
| 3DGS-DR_survey | Private | 0 | 2025-05-05 | 2025-06-18 | Python | Survey of 3DGS-DR (SIGGRAPH 2024) | [🔗](https://github.com/kevin30205/3DGS-DR_survey) |
| BAGS_survey | Private | 0 | 2025-05-04 | 2025-06-18 | Python | Survey of BAGS (ECCV 2024) | [🔗](https://github.com/kevin30205/BAGS_survey) |
| DoF-Gaussian_survey | Private | 0 | 2025-05-02 | 2025-06-18 | Python | Survey of DoF-Gaussian (CVPR 2025) | [🔗](https://github.com/kevin30205/DoF-Gaussian_survey) |
| DropGaussian_survey | Private | 0 | 2025-05-04 | 2025-06-18 | Python | Survey of DropGaussian (CVPR 2025) | [🔗](https://github.com/kevin30205/DropGaussian_survey) |
| MAtCha-Gaussians_survey | Private | 0 | 2025-04-30 | 2025-06-18 | Python | Survey of MAtCha Gaussians (CVPR 2025) | [🔗](https://github.com/kevin30205/MAtCha-Gaussians_survey) |
| Gaussian-Frosting_survey | Private | 0 | 2025-04-30 | 2025-06-18 | Python | Survey of Gaussian Frosting (ECCV 2024) | [🔗](https://github.com/kevin30205/Gaussian-Frosting_survey) |
| BAD-Gaussians_survey | Private | 0 | 2025-04-30 | 2025-06-18 | Python | Survey of BAD-Gaussians (ECCV 2024) | [🔗](https://github.com/kevin30205/BAD-Gaussians_survey) |
| SplatFormer_survey | Private | 0 | 2025-04-25 | 2025-06-18 | Python | Survey of SplatFormer (ICLR 2025) | [🔗](https://github.com/kevin30205/SplatFormer_survey) |
| GaussHDR_survey | Private | 0 | 2025-04-25 | 2025-06-18 | Python | Survey of GaussHDR (CVPR 2025) | [🔗](https://github.com/kevin30205/GaussHDR_survey) |
| NexusGS_survey | Private | 0 | 2025-04-26 | 2025-06-18 | Python | Survey of NexusGS (CVPR 2025) | [🔗](https://github.com/kevin30205/NexusGS_survey) |
| HDR-GS_survey | Private | 0 | 2025-04-25 | 2025-06-18 | Python | Survey of HDR-GS (NeurIPS 2024) | [🔗](https://github.com/kevin30205/HDR-GS_survey) |
| r2_gaussian_survey | Private | 0 | 2025-04-23 | 2025-06-18 | Python | Survey of R2 Gaussian (NeurIPS 2024) | [🔗](https://github.com/kevin30205/r2_gaussian_survey) |
| 3D-Convex-Splatting_survey | Private | 0 | 2025-04-21 | 2025-06-18 | Python | Survey of 3D Convex Splatting (CVPR 2025) | [🔗](https://github.com/kevin30205/3D-Convex-Splatting_survey) |
| X-Gaussian_survey | Private | 0 | 2025-04-22 | 2025-06-18 | Python | Survey of X-Gaussian (ECCV 2024) | [🔗](https://github.com/kevin30205/X-Gaussian_survey) |
| LucidDreamer_survey | Private | 0 | 2025-04-20 | 2025-06-18 | Python | Survey of LucidDreamer (CVPR 2024) | [🔗](https://github.com/kevin30205/LucidDreamer_survey) |
| FSGS_survey | Private | 0 | 2025-04-21 | 2025-06-18 | Python | Survey of FSGS (ECCV 2024) | [🔗](https://github.com/kevin30205/FSGS_survey) |
| Ref-GS_survey | Private | 0 | 2025-04-22 | 2025-06-18 | Python | Survey of Ref-GS (CVPR 2025) | [🔗](https://github.com/kevin30205/Ref-GS_survey) |
| SuGaR_survey | Private | 0 | 2025-04-22 | 2025-06-18 | C++ | Survey of SuGaR (CVPR 2024) | [🔗](https://github.com/kevin30205/SuGaR_survey) |
| Vol3DGS_survey | Private | 0 | 2025-04-21 | 2025-06-18 | Python | Survey of Vol3DGS (CVPR 2025) | [🔗](https://github.com/kevin30205/Vol3DGS_survey) |
| GFSGS_survey | Private | 0 | 2025-04-21 | 2025-06-18 | Python | Survey of GFSGS (CVPR 2025) | [🔗](https://github.com/kevin30205/GFSGS_survey) |
| MaskGaussian_survey | Private | 0 | 2025-04-21 | 2025-06-18 | C++ | Survey of MaskGaussian (CVPR 2025) | [🔗](https://github.com/kevin30205/MaskGaussian_survey) |
| DNGaussian_survey | Private | 0 | 2025-04-21 | 2025-06-18 | Python | Survey of DNGaussian (CVPR 2024) | [🔗](https://github.com/kevin30205/DNGaussian_survey) |
| DropoutGS_survey | Private | 0 | 2025-04-21 | 2025-06-18 | Python | Survey of DropoutGS (CVPR 2025) | [🔗](https://github.com/kevin30205/DropoutGS_survey) |
| GART_survey | Private | 0 | 2025-04-17 | 2025-06-18 | Python | Survey of GART (CVPR 2024) | [🔗](https://github.com/kevin30205/GART_survey) |
| EnvGS_survey | Private | 0 | 2025-04-18 | 2025-06-18 | Python | Survey of EnvGS (CVPR 2025) | [🔗](https://github.com/kevin30205/EnvGS_survey) |
| AnimatableGaussians_survey | Private | 0 | 2025-04-19 | 2025-06-18 | Python | Survey of Animatable Gaussians (CVPR 2024) | [🔗](https://github.com/kevin30205/AnimatableGaussians_survey) |
| GaussianDreamer_survey | Private | 0 | 2025-04-18 | 2025-06-18 | Python | Survey of GaussianDreamer (CVPR 2024) | [🔗](https://github.com/kevin30205/GaussianDreamer_survey) |
| GSGEN_survey | Private | 0 | 2025-04-14 | 2025-06-18 | Python | Survey of GSGEN (CVPR 2024) | [🔗](https://github.com/kevin30205/GSGEN_survey) |
| DreamGaussian_survey | Private | 0 | 2025-04-13 | 2025-06-18 | Python | Survey of DreamGaussian (ICLR 2024) | [🔗](https://github.com/kevin30205/DreamGaussian_survey) |
| SpacetimeGaussians_survey | Private | 0 | 2025-04-13 | 2025-06-18 | Python | Survey of SpacetimeGaussians (CVPR 2024) | [🔗](https://github.com/kevin30205/SpacetimeGaussians_survey) |
| ContextGS_survey | Private | 0 | 2025-04-09 | 2025-06-18 | Python | Survey of ContextGS (NeurIPS 2024) | [🔗](https://github.com/kevin30205/ContextGS_survey) |
| Mini-Splatting_survey | Private | 0 | 2025-04-11 | 2025-06-18 | Python | Survey of Mini-Splatting (ECCV 2024) | [🔗](https://github.com/kevin30205/Mini-Splatting_survey) |
| GSDF_survey | Private | 0 | 2025-04-10 | 2025-06-18 | Python | Survey of GSDF (NeurIPS 2024) | [🔗](https://github.com/kevin30205/GSDF_survey) |
| Grendel-GS_survey | Private | 0 | 2025-04-12 | 2025-06-18 | Python | Survey of Grendel-GS (ICLR 2025) | [🔗](https://github.com/kevin30205/Grendel-GS_survey) |
| Deformable-3D-Gaussians_survey | Private | 0 | 2025-04-12 | 2025-06-18 | Python | Survey of Deformable 3D Gaussians (CVPR 2024) | [🔗](https://github.com/kevin30205/Deformable-3D-Gaussians_survey) |
| FCGS_survey | Private | 0 | 2025-04-12 | 2025-06-18 | C++ | Survey of FCGS (ICLR 2025) | [🔗](https://github.com/kevin30205/FCGS_survey) |
| EAGLES_survey | Private | 0 | 2025-04-11 | 2025-06-18 | C++ | Survey of EAGLES (ECCV 2024) | [🔗](https://github.com/kevin30205/EAGLES_survey) |
| 3DGS-MCMC_survey | Private | 0 | 2025-04-08 | 2025-06-18 | Python | Survey of 3DGS-MCMC (NeurIPS 2024) | [🔗](https://github.com/kevin30205/3DGS-MCMC_survey) |
| PCGS_survey | Private | 0 | 2025-04-10 | 2025-06-18 | C++ | Survey of PCGS (arXiv 2025) | [🔗](https://github.com/kevin30205/PCGS_survey) |
| HAC-plus_survey | Private | 0 | 2025-04-09 | 2025-06-18 | C++ | Survey of HAC++ (arXiv 2025) | [🔗](https://github.com/kevin30205/HAC-plus_survey) |
| C3DGS_survey | Private | 0 | 2025-04-11 | 2025-06-18 | Python | Survey of C3DGS (CVPR 2024) | [🔗](https://github.com/kevin30205/C3DGS_survey) |
| Octree-GS_survey | Private | 0 | 2025-04-09 | 2025-06-18 | C++ | Survey of Octree-GS (arXiv 2024) | [🔗](https://github.com/kevin30205/Octree-GS_survey) |
| Scaffold-GS_survey | Private | 0 | 2025-04-09 | 2025-06-18 | C++ | Survey of Scaffold-GS (CVPR 2024) | [🔗](https://github.com/kevin30205/Scaffold-GS_survey) |
| Compact-3DGS_survey | Private | 0 | 2025-04-10 | 2025-06-18 | Python | Survey of Compact-3DGS (CVPR 2024) | [🔗](https://github.com/kevin30205/Compact-3DGS_survey) |
| LightGaussian_survey | Private | 0 | 2025-04-10 | 2025-06-18 | Python | Survey of LightGaussian (NeurIPS 2024) | [🔗](https://github.com/kevin30205/LightGaussian_survey) |
| HAC_survey | Private | 0 | 2025-04-09 | 2025-06-18 | Python | Survey of HAC (ECCV 2024) | [🔗](https://github.com/kevin30205/HAC_survey) |
| InstantSplat_survey | Private | 0 | 2025-04-08 | 2025-06-18 | Python | Survey of InstantSplat (arXiv 2024) | [🔗](https://github.com/kevin30205/InstantSplat_survey) |
| 3D-HGS_survey | Private | 0 | 2025-04-08 | 2025-06-18 | Python | Survey of 3D-HGS (CVPR 2025) | [🔗](https://github.com/kevin30205/3D-HGS_survey) |
| 4D-Gaussian-Splatting_survey | Private | 0 | 2025-04-01 | 2025-06-18 | Python | Survey of 4D Gaussian Splatting (ICLR 2024) | [🔗](https://github.com/kevin30205/4D-Gaussian-Splatting_survey) |
| 3DGS-Avatar_survey | Private | 0 | 2025-04-04 | 2025-06-18 | Python | Survey of 3DGS-Avatar (CVPR 2024) | [🔗](https://github.com/kevin30205/3DGS-Avatar_survey) |
| Gaussian-Opacity-Fields_survey | Private | 0 | 2025-04-01 | 2025-06-18 | Python | Survey of Gaussian Opacity Fields (GOF) (SIGGRAPH ASIA 2024) | [🔗](https://github.com/kevin30205/Gaussian-Opacity-Fields_survey) |
| GPS-Gaussian_survey | Private | 0 | 2025-04-03 | 2025-06-18 | C++ | Survey of GPS-Gaussian (CVPR 2024) | [🔗](https://github.com/kevin30205/GPS-Gaussian_survey) |
| GoMAvatar_survey | Private | 0 | 2025-03-31 | 2025-06-18 | Python | Survey of GoMAvatar (CVPR 2024) | [🔗](https://github.com/kevin30205/GoMAvatar_survey) |
| Mani-GS_survey | Private | 0 | 2025-04-03 | 2025-06-18 | Python | Survey of Mani-GS (CVPR 2025) | [🔗](https://github.com/kevin30205/Mani-GS_survey) |
| 2D-Gaussian-Splatting_survey | Private | 0 | 2025-04-01 | 2025-06-18 | Python | Survey of 2D Gaussian Splatting (SIGGRAPH 2024) | [🔗](https://github.com/kevin30205/2D-Gaussian-Splatting_survey) |
| Relightable-3D-Gaussian_survey | Private | 0 | 2025-04-03 | 2025-06-18 | Python | Survey of Relightable 3D Gaussian (ECCV 2024) | [🔗](https://github.com/kevin30205/Relightable-3D-Gaussian_survey) |
| Mip-Splatting_survey | Private | 0 | 2025-04-01 | 2025-06-18 | Python | Survey of Mip-Splatting (CVPR 2024) | [🔗](https://github.com/kevin30205/Mip-Splatting_survey) |
| 3D-Gaussian-Splatting_survey | Private | 0 | 2025-03-31 | 2025-06-18 | Python | Survey of 3D Gaussian Splatting (SIGGRAPH 2023) | [🔗](https://github.com/kevin30205/3D-Gaussian-Splatting_survey) |
| LangSplat_survey | Private | 0 | 2025-04-01 | 2025-06-18 | Python | Survey of LangSplat (CVPR 2024) | [🔗](https://github.com/kevin30205/LangSplat_survey) |
| Deblurring-3D-Gaussian-Splatting_survey | Private | 0 | 2025-04-01 | 2025-06-18 | Python | Survey of Deblurring 3D Gaussian Splatting (ECCV 2024) | [🔗](https://github.com/kevin30205/Deblurring-3D-Gaussian-Splatting_survey) |
| SplattingAvatar_survey | Private | 0 | 2025-03-30 | 2025-06-18 | Python | Survey of SplattingAvatar (CVPR 2024) | [🔗](https://github.com/kevin30205/SplattingAvatar_survey) |
| GaussianAvatar_survey | Private | 0 | 2025-03-31 | 2025-06-18 | Python | Survey of GaussianAvatar (CVPR 2024) | [🔗](https://github.com/kevin30205/GaussianAvatar_survey) |
| HUGS_survey | Private | 0 | 2025-03-30 | 2025-06-18 | Python | Survey of HUGS (CVPR 2024) | [🔗](https://github.com/kevin30205/HUGS_survey) |
| OccFusion_survey | Private | 0 | 2025-03-28 | 2025-06-18 | Python | Survey of OccFusion (NeurIPS 2024) | [🔗](https://github.com/kevin30205/OccFusion_survey) |
| GauHuman_survey | Private | 0 | 2025-03-28 | 2025-06-18 | Python | Survey of GauHuman (CVPR 2024) | [🔗](https://github.com/kevin30205/GauHuman_survey) |
| awesome-3D-gaussian-splatting_tool | Private | 0 | 2025-06-04 | 2025-06-04 | HTML | The list of papers and resources focused on 3D Gaussian Splatting. | [🔗](https://github.com/kevin30205/awesome-3D-gaussian-splatting_tool) |

### generalization

* **Total Repositories:** 5

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| RoGSplat_survey | Private | 0 | 2025-05-09 | 2025-06-18 | Python | Survey of RoGSplat (CVPR 2025) | [🔗](https://github.com/kevin30205/RoGSplat_survey) |
| Neural-Human-Performer_survey | Private | 0 | 2025-04-05 | 2025-06-18 | Python | Survey of Neural Human Performer (NeurIPS 2021) | [🔗](https://github.com/kevin30205/Neural-Human-Performer_survey) |
| GPS-Gaussian_survey | Private | 0 | 2025-04-03 | 2025-06-18 | C++ | Survey of GPS-Gaussian (CVPR 2024) | [🔗](https://github.com/kevin30205/GPS-Gaussian_survey) |
| TransHuman_survey | Private | 0 | 2023-11-26 | 2025-06-18 | Python | Survey of TransHuman (ICCV 2023) | [🔗](https://github.com/kevin30205/TransHuman_survey) |
| SHERF_survey | Private | 0 | 2023-11-26 | 2025-06-18 | Python | Survey of SHERF (ICCV 2023) | [🔗](https://github.com/kevin30205/SHERF_survey) |

### generative-ai

* **Total Repositories:** 3

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| Gemini_API_Guideline | Private | 0 | 2025-01-28 | 2025-06-20 | Markdown | The guideline of Gemini API. | [🔗](https://github.com/kevin30205/Gemini_API_Guideline) |
| Wan2.1_survey | Private | 0 | 2025-06-05 | 2025-06-19 | Python | Survey of Wan2.1 | [🔗](https://github.com/kevin30205/Wan2.1_survey) |
| FramePack_survey | Private | 0 | 2025-04-24 | 2025-06-18 | Python | Survey of FramePack (arXiv 2025) | [🔗](https://github.com/kevin30205/FramePack_survey) |

### nerf

* **Total Repositories:** 61

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| LAENeRF_survey | Private | 0 | 2025-06-14 | 2025-06-18 | HTML | Survey of LAENeRF (CVPR 2024) | [🔗](https://github.com/kevin30205/LAENeRF_survey) |
| ActiveNeRF_survey | Private | 0 | 2025-06-10 | 2025-06-18 | Python | Survey of  ActiveNeRF (ECCV 2022) | [🔗](https://github.com/kevin30205/ActiveNeRF_survey) |
| NRHints_survey | Private | 0 | 2025-05-30 | 2025-06-18 | Python | Survey of NRHints (SIGGRAPH 2023) | [🔗](https://github.com/kevin30205/NRHints_survey) |
| TensoIR_survey | Private | 0 | 2025-05-06 | 2025-06-18 | Python | Survey of TensoIR (CVPR 2023) | [🔗](https://github.com/kevin30205/TensoIR_survey) |
| InvRender_survey | Private | 0 | 2025-05-06 | 2025-06-18 | Python | Survey of InvRender (CVPR 2022) | [🔗](https://github.com/kevin30205/InvRender_survey) |
| BeNeRF_survey | Private | 0 | 2025-04-28 | 2025-06-18 | Python | Survey of BeNeRF (ECCV 2024) | [🔗](https://github.com/kevin30205/BeNeRF_survey) |
| HDR-NeRF_survey | Private | 0 | 2025-04-26 | 2025-06-18 | Python | Survey of HDR-NeRF (CVPR 2022) | [🔗](https://github.com/kevin30205/HDR-NeRF_survey) |
| SCINeRF_survey | Private | 0 | 2025-04-28 | 2025-06-18 | Python | Survey of SCINeRF (CVPR 2024) | [🔗](https://github.com/kevin30205/SCINeRF_survey) |
| TiNeuVox_survey | Private | 0 | 2025-04-30 | 2025-06-18 | Python | Survey of TiNeuVox (SIGGRAPH Asia 2022) | [🔗](https://github.com/kevin30205/TiNeuVox_survey) |
| HDR-Plenoxels_survey | Private | 0 | 2025-04-26 | 2025-06-18 | Python | Survey of HDR-Plenoxels (ECCV 2022) | [🔗](https://github.com/kevin30205/HDR-Plenoxels_survey) |
| SAX-NeRF_survey | Private | 0 | 2025-04-22 | 2025-06-18 | Python | Survey of SAX-NeRF (CVPR 2024) | [🔗](https://github.com/kevin30205/SAX-NeRF_survey) |
| Stable-Dreamfusion_survey | Private | 0 | 2025-04-24 | 2025-06-18 | Python | Survey of Stable-Dreamfusion (ICLR 2023) | [🔗](https://github.com/kevin30205/Stable-Dreamfusion_survey) |
| Relighting4D_survey | Private | 0 | 2025-04-05 | 2025-06-18 | Python | Survey of Relighting4D (ECCV 2022) | [🔗](https://github.com/kevin30205/Relighting4D_survey) |
| ARAH_survey | Private | 0 | 2025-04-04 | 2025-06-18 | Python | Survey of ARAH (ECCV 2022) | [🔗](https://github.com/kevin30205/ARAH_survey) |
| Neural-Human-Performer_survey | Private | 0 | 2025-04-05 | 2025-06-18 | Python | Survey of Neural Human Performer (NeurIPS 2021) | [🔗](https://github.com/kevin30205/Neural-Human-Performer_survey) |
| IntrinsicAvatar_survey | Private | 0 | 2025-04-05 | 2025-06-18 | Python | Survey of IntrinsicAvatar (CVPR 2024) | [🔗](https://github.com/kevin30205/IntrinsicAvatar_survey) |
| TAVA_survey | Private | 0 | 2025-04-04 | 2025-06-18 | Python | Survey of TAVA (ECCV 2022) | [🔗](https://github.com/kevin30205/TAVA_survey) |
| Neural-Body_survey | Private | 0 | 2025-04-05 | 2025-06-18 | Python | Survey of Neural Body (CVPR 2021) | [🔗](https://github.com/kevin30205/Neural-Body_survey) |
| Animatable-NeRF_survey | Private | 0 | 2025-03-29 | 2025-06-18 | Python | Survey of Animatable-NeRF (ICCV 2021) | [🔗](https://github.com/kevin30205/Animatable-NeRF_survey) |
| HumanNeRF-SE_survey | Private | 0 | 2025-03-29 | 2025-06-18 | Python | Survey of HumanNeRF-SE (CVPR 2024) | [🔗](https://github.com/kevin30205/HumanNeRF-SE_survey) |
| InstantAvatar_survey | Private | 0 | 2025-03-28 | 2025-06-18 | Python | Survey of InstantAvatar (CVPR 2023) | [🔗](https://github.com/kevin30205/InstantAvatar_survey) |
| Tensor4D_survey | Private | 0 | 2024-03-23 | 2025-06-18 | Python | Survey of Tensor4D (CVPR 2023) | [🔗](https://github.com/kevin30205/Tensor4D_survey) |
| REF_square_NeRF_survey | Private | 0 | 2024-04-17 | 2025-06-18 | Python | Survey of REF Square NeRF (arXiv 2023/11) | [🔗](https://github.com/kevin30205/REF_square_NeRF_survey) |
| Eikonal-Fields_survey | Private | 0 | 2024-04-17 | 2025-06-18 | Python | Survey of Eikonal Fields (SIGGRAPH 2022) | [🔗](https://github.com/kevin30205/Eikonal-Fields_survey) |
| RoDynRF_survey | Private | 0 | 2024-04-12 | 2025-06-18 | Python | Survey of RoDynRF (CVPR 2023) | [🔗](https://github.com/kevin30205/RoDynRF_survey) |
| DynamicNeRF_survey | Private | 0 | 2024-04-12 | 2025-06-18 | Python | Survey of DynamicNeRF (ICCV 2021) | [🔗](https://github.com/kevin30205/DynamicNeRF_survey) |
| NeRFReN_survey | Private | 0 | 2024-03-23 | 2025-06-18 | Python | Survey of NeRFReN (CVPR 2022) | [🔗](https://github.com/kevin30205/NeRFReN_survey) |
| BAD-NeRF_survey | Private | 0 | 2024-03-13 | 2025-06-18 | Python | Survey of BAD-NeRF (CVPR 2023) | [🔗](https://github.com/kevin30205/BAD-NeRF_survey) |
| HyperNeRF_survey | Private | 0 | 2023-11-26 | 2025-06-18 | Python | Survey of HyperNeRF (SIGGRAPH Asia 2021) | [🔗](https://github.com/kevin30205/HyperNeRF_survey) |
| Deblur-NeRF_survey | Private | 0 | 2024-01-10 | 2025-06-18 | Python | Survey of Deblur-NeRF (CVPR 2022) | [🔗](https://github.com/kevin30205/Deblur-NeRF_survey) |
| NeuS_survey | Private | 0 | 2024-03-13 | 2025-06-18 | Python | Survey of NeuS (NeurIPS 2021) | [🔗](https://github.com/kevin30205/NeuS_survey) |
| ENeRF_survey | Private | 0 | 2024-02-17 | 2025-06-18 | Python | Survey of ENeRF (SIGGRAPH Asia 2022) | [🔗](https://github.com/kevin30205/ENeRF_survey) |
| OccNeRF_survey | Private | 0 | 2024-01-30 | 2025-06-18 | Python | Survey of OccNeRF (ICCV 2023) | [🔗](https://github.com/kevin30205/OccNeRF_survey) |
| LocalRF_survey | Private | 0 | 2024-01-10 | 2025-06-18 | Python | Survey of LocalRF (CVPR 2023) | [🔗](https://github.com/kevin30205/LocalRF_survey) |
| Ref-NeuS_survey | Private | 0 | 2024-01-10 | 2025-06-18 | Python | Survey of Ref-NeuS (ICCV 2023) | [🔗](https://github.com/kevin30205/Ref-NeuS_survey) |
| NeRFplusplus_survey | Private | 0 | 2023-11-26 | 2025-06-18 | Python | Survey of NeRF++ (arXiv 2020) | [🔗](https://github.com/kevin30205/NeRFplusplus_survey) |
| NoPe-NeRF_survey | Private | 0 | 2023-08-29 | 2025-06-18 | Python | Survey of NoPe-NeRF (CVPR 2023) | [🔗](https://github.com/kevin30205/NoPe-NeRF_survey) |
| TransHuman_survey | Private | 0 | 2023-11-26 | 2025-06-18 | Python | Survey of TransHuman (ICCV 2023) | [🔗](https://github.com/kevin30205/TransHuman_survey) |
| SHERF_survey | Private | 0 | 2023-11-26 | 2025-06-18 | Python | Survey of SHERF (ICCV 2023) | [🔗](https://github.com/kevin30205/SHERF_survey) |
| TILTED_survey | Private | 0 | 2023-09-25 | 2025-06-18 | Python | Survey of TILTED (ICCV 2023) | [🔗](https://github.com/kevin30205/TILTED_survey) |
| Ref-NeRF_pl_survey | Private | 0 | 2023-09-12 | 2025-06-18 | Python | Survey of Ref-NeRF (CVPR 2022) [PyTorch Lightning Version] | [🔗](https://github.com/kevin30205/Ref-NeRF_pl_survey) |
| Strivec_survey | Private | 0 | 2023-11-08 | 2025-06-18 | Python | Survey of Strivec (ICCV 2023) | [🔗](https://github.com/kevin30205/Strivec_survey) |
| K-Planes_survey | Private | 0 | 2023-08-13 | 2025-06-18 | Python | Survey of K-Planes (CVPR 2023) | [🔗](https://github.com/kevin30205/K-Planes_survey) |
| HexPlane_survey | Private | 0 | 2023-08-18 | 2025-06-18 | Python | Survey of HexPlane (CVPR 2023) | [🔗](https://github.com/kevin30205/HexPlane_survey) |
| Tri-MipRF_survey | Private | 0 | 2023-10-07 | 2025-06-18 | Python | Survey of Tri-MipRF (ICCV 2023) | [🔗](https://github.com/kevin30205/Tri-MipRF_survey) |
| TensoRF_survey | Private | 0 | 2023-08-16 | 2025-06-18 | Python | Survey of TensoRF (ECCV 2022) | [🔗](https://github.com/kevin30205/TensoRF_survey) |
| EfficientNeRF_survey | Private | 0 | 2023-08-30 | 2025-06-18 | Python | Survey of EfficientNeRF (CVPR 2022) | [🔗](https://github.com/kevin30205/EfficientNeRF_survey) |
| ABLE-NeRF_survey | Private | 0 | 2023-08-29 | 2025-06-18 | Python | Survey of ABLE-NeRF (CVPR 2023) | [🔗](https://github.com/kevin30205/ABLE-NeRF_survey) |
| Zip-NeRF_survey | Private | 0 | 2023-09-15 | 2025-06-18 | Python | Survey of Zip-NeRF (ICCV 2023) [PyTorch Version] | [🔗](https://github.com/kevin30205/Zip-NeRF_survey) |
| SinNeRF_survey | Private | 0 | 2023-08-30 | 2025-06-18 | Python | Survey of SinNeRF (ECCV 2022) | [🔗](https://github.com/kevin30205/SinNeRF_survey) |
| mipNeRF_PyTorch_survey | Private | 0 | 2023-08-13 | 2025-06-18 | Python | Survey of mipNeRF (ICCV 2021) [Pytorch Version] | [🔗](https://github.com/kevin30205/mipNeRF_PyTorch_survey) |
| Plenoxels_survey | Private | 0 | 2023-09-14 | 2025-06-18 | C++ | Survey of Plenoxels (CVPR 2022) | [🔗](https://github.com/kevin30205/Plenoxels_survey) |
| NVR-in-Minutes_survey | Private | 0 | 2023-09-26 | 2025-06-18 | Python | Survey of NVR-in-Minutes (CVPR 2023) | [🔗](https://github.com/kevin30205/NVR-in-Minutes_survey) |
| Neuman_survey | Private | 0 | 2023-08-13 | 2025-06-18 | Python | Survey of Neuman (ECCV 2022) | [🔗](https://github.com/kevin30205/Neuman_survey) |
| NeRF_PyTorch_survey | Private | 0 | 2023-08-28 | 2025-06-18 | Python | Survey of NeRF (ECCV 2020) [Pytorch Version] | [🔗](https://github.com/kevin30205/NeRF_PyTorch_survey) |
| MonoHuman_survey | Private | 0 | 2023-08-27 | 2025-06-18 | Python | Survey of MonoHuman (CVPR 2023) | [🔗](https://github.com/kevin30205/MonoHuman_survey) |
| Instant-NGP_survey | Private | 0 | 2023-09-14 | 2025-06-18 | Python | Survey of Instant-NGP (SIGGRAPH 2022) [Pytorch Version] | [🔗](https://github.com/kevin30205/Instant-NGP_survey) |
| HumanNeRF_survey | Private | 0 | 2023-08-27 | 2025-06-18 | Python | Survey of HumanNeRF (CVPR 2022) | [🔗](https://github.com/kevin30205/HumanNeRF_survey) |
| DVGOv2_survey | Private | 0 | 2023-09-03 | 2025-06-18 | Python | Survey of DVGO_v2 (CVPR 2022) | [🔗](https://github.com/kevin30205/DVGOv2_survey) |
| DVGOv1_survey | Private | 0 | 2023-09-04 | 2025-06-18 | Python | Survey of DVGO_v1 (CVPR 2022) | [🔗](https://github.com/kevin30205/DVGOv1_survey) |
| Vid2Avatar_survey | Private | 0 | 2023-09-26 | 2025-06-18 | Python | Survey of Vid2Avatar (CVPR 2023) | [🔗](https://github.com/kevin30205/Vid2Avatar_survey) |

### personal

* **Total Repositories:** 22

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| Conference_Paper_Summary | Private | 0 | 2025-02-01 | 2025-06-21 | Python | Paper Summary of Conferences. | [🔗](https://github.com/kevin30205/Conference_Paper_Summary) |
| Repository-Hub | Private | 1 | 2025-05-31 | 2025-06-21 | Python | Repository Hub: The Centralized GitHub Repository Dashboard & Overview. | [🔗](https://github.com/kevin30205/Repository-Hub) |
| Conference_Paper_Downloader | Private | 0 | 2025-01-26 | 2025-06-20 | Python | Customized Usage of Conference Paper Downloader. | [🔗](https://github.com/kevin30205/Conference_Paper_Downloader) |
| C_Programming_Language | Private | 0 | 2025-02-23 | 2025-06-20 | Markdown | The Guideline of C Programming Language. | [🔗](https://github.com/kevin30205/C_Programming_Language) |
| OccNeRF_optimized | Private | 0 | 2024-01-30 | 2025-06-20 | Python | The optimized code based on OccNeRF done by myself. | [🔗](https://github.com/kevin30205/OccNeRF_optimized) |
| Grounded-Segment-Anything_mine | Private | 0 | 2024-02-18 | 2025-06-20 | Jupyter Notebook | Customized Usage of Grounded-Segment-Anything by myself | [🔗](https://github.com/kevin30205/Grounded-Segment-Anything_mine) |
| Gemini_API_Guideline | Private | 0 | 2025-01-28 | 2025-06-20 | Markdown | The guideline of Gemini API. | [🔗](https://github.com/kevin30205/Gemini_API_Guideline) |
| Linux_Command_Memorandum | Private | 0 | 2025-02-07 | 2025-06-20 | Markdown | A handy reference guide for common Linux commands. | [🔗](https://github.com/kevin30205/Linux_Command_Memorandum) |
| Meeting_Record | Private | 0 | 2024-08-04 | 2025-06-19 | Markdown | The Database of Meeting Recording | [🔗](https://github.com/kevin30205/Meeting_Record) |
| Course_Record | Private | 0 | 2024-08-05 | 2025-06-19 | Markdown | The Database of Course Recording | [🔗](https://github.com/kevin30205/Course_Record) |
| Traffic_Record | Private | 0 | 2023-12-14 | 2025-06-19 | Markdown | The Database of Traffic Record | [🔗](https://github.com/kevin30205/Traffic_Record) |
| Document_Converter | Private | 0 | 2025-01-27 | 2025-06-19 | Python | Customized Usage of Document Converter. | [🔗](https://github.com/kevin30205/Document_Converter) |
| faster-whisper_mine | Private | 0 | 2025-01-10 | 2025-06-19 | Python | Customized Usage of faster-whisper. | [🔗](https://github.com/kevin30205/faster-whisper_mine) |
| Curriculum-Vitae | Private | 0 | 2025-06-09 | 2025-06-09 | TeX | My Curriculum Vitae | [🔗](https://github.com/kevin30205/Curriculum-Vitae) |
| Command_Memorandum | Private | 0 | 2023-09-05 | 2025-06-04 | Shell | Commonly and frequently used Commands on Command-Line Interface (CLI) | [🔗](https://github.com/kevin30205/Command_Memorandum) |
| Academic-Homepage | Private | 0 | 2025-05-20 | 2025-06-03 | HTML | My academic personal website. | [🔗](https://github.com/kevin30205/Academic-Homepage) |
| NeRF_Datasets | Private | 0 | 2023-09-05 | 2025-06-01 | Shell | Datasets used in NeRF Projects | [🔗](https://github.com/kevin30205/NeRF_Datasets) |
| LeetCode_Practice | Private | 0 | 2024-07-30 | 2025-06-01 | Python | The code practice on LeetCode. | [🔗](https://github.com/kevin30205/LeetCode_Practice) |
| HumanNeRF_optimized | Private | 0 | 2023-12-12 | 2025-06-01 | Shell | The optimized code based on HumanNeRF done by myself. | [🔗](https://github.com/kevin30205/HumanNeRF_optimized) |
| opencc-python_mine | Private | 0 | 2025-01-12 | 2025-06-01 | Python | Customized Usage of opencc-python. | [🔗](https://github.com/kevin30205/opencc-python_mine) |
| Document_Converter_marker | Private | 0 | 2025-01-28 | 2025-06-01 | Python | About Customized Usage of Document Converter using Marker. | [🔗](https://github.com/kevin30205/Document_Converter_marker) |
| Python_Programming_Language | Private | 0 | 2025-02-23 | 2025-06-01 | Python | The Guideline of Python Programming Language. | [🔗](https://github.com/kevin30205/Python_Programming_Language) |

### pose-estimation

* **Total Repositories:** 2

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| 4D-Humans_mine | Private | 0 | 2024-02-26 | 2025-06-20 | Python | 4D-Humans is used to preprocess the data to obtain the SMPL parameters. | [🔗](https://github.com/kevin30205/4D-Humans_mine) |
| PHALP_survey | Private | 0 | 2025-04-07 | 2025-06-01 | Python | Survey of PHALP (CVPR 2022) | [🔗](https://github.com/kevin30205/PHALP_survey) |

### relighting

* **Total Repositories:** 6

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| RNG_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of RNG (CVPR 2025) | [🔗](https://github.com/kevin30205/RNG_survey) |
| ReCap_survey | Private | 0 | 2025-06-08 | 2025-06-18 | Python | Survey of ReCap (CVPR 2025) | [🔗](https://github.com/kevin30205/ReCap_survey) |
| NRHints_survey | Private | 0 | 2025-05-30 | 2025-06-18 | Python | Survey of NRHints (SIGGRAPH 2023) | [🔗](https://github.com/kevin30205/NRHints_survey) |
| GS-3_survey | Private | 0 | 2025-05-30 | 2025-06-18 | Python | Survey of GS^3 (SIGGRAPH Asia 2024) | [🔗](https://github.com/kevin30205/GS-3_survey) |
| Relighting4D_survey | Private | 0 | 2025-04-05 | 2025-06-18 | Python | Survey of Relighting4D (ECCV 2022) | [🔗](https://github.com/kevin30205/Relighting4D_survey) |
| Relightable-3D-Gaussian_survey | Private | 0 | 2025-04-03 | 2025-06-18 | Python | Survey of Relightable 3D Gaussian (ECCV 2024) | [🔗](https://github.com/kevin30205/Relightable-3D-Gaussian_survey) |

### segmentation

* **Total Repositories:** 3

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| SAM-2_survey | Private | 0 | 2025-06-07 | 2025-06-19 | Jupyter Notebook | Survey of SAM 2 (ICLR 2025) | [🔗](https://github.com/kevin30205/SAM-2_survey) |
| SAM-HQ_survey | Private | 0 | 2025-06-07 | 2025-06-19 | Jupyter Notebook | Survey of SAM-HQ (NeurIPS 2023) | [🔗](https://github.com/kevin30205/SAM-HQ_survey) |
| Segment-Anything_survey | Private | 0 | 2025-06-07 | 2025-06-19 | Jupyter Notebook | Survey of Segment Anything (ICCV 2023) | [🔗](https://github.com/kevin30205/Segment-Anything_survey) |

### slam

* **Total Repositories:** 1

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| MonoGS_survey | Private | 0 | 2025-05-11 | 2025-06-18 | Python | Survey of MonoGS (CVPR 2024) | [🔗](https://github.com/kevin30205/MonoGS_survey) |

### smpl

* **Total Repositories:** 3

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| 4D-Humans_mine | Private | 0 | 2024-02-26 | 2025-06-20 | Python | 4D-Humans is used to preprocess the data to obtain the SMPL parameters. | [🔗](https://github.com/kevin30205/4D-Humans_mine) |
| PHALP_survey | Private | 0 | 2025-04-07 | 2025-06-01 | Python | Survey of PHALP (CVPR 2022) | [🔗](https://github.com/kevin30205/PHALP_survey) |
| SMPL-X_survey | Private | 0 | 2025-03-31 | 2025-06-01 | Python | Survey of SMPL-X (CVPR 2019) | [🔗](https://github.com/kevin30205/SMPL-X_survey) |

### sparse-view

* **Total Repositories:** 10

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| CoR-GS_survey | Private | 0 | 2025-05-29 | 2025-06-18 | Python | Survey of CoR-GS (ECCV 2024) | [🔗](https://github.com/kevin30205/CoR-GS_survey) |
| SparseGS_survey | Private | 0 | 2025-05-19 | 2025-06-18 | Python | Survey of SparseGS (3DV 2025) | [🔗](https://github.com/kevin30205/SparseGS_survey) |
| DRGS_survey | Private | 0 | 2025-05-19 | 2025-06-18 | Python | Survey of DRGS (CVPRW 2024) | [🔗](https://github.com/kevin30205/DRGS_survey) |
| CoherentGS_survey | Private | 0 | 2025-05-14 | 2025-06-18 | Python | Survey of CoherentGS (ECCV 2024) | [🔗](https://github.com/kevin30205/CoherentGS_survey) |
| DropGaussian_survey | Private | 0 | 2025-05-04 | 2025-06-18 | Python | Survey of DropGaussian (CVPR 2025) | [🔗](https://github.com/kevin30205/DropGaussian_survey) |
| NexusGS_survey | Private | 0 | 2025-04-26 | 2025-06-18 | Python | Survey of NexusGS (CVPR 2025) | [🔗](https://github.com/kevin30205/NexusGS_survey) |
| FSGS_survey | Private | 0 | 2025-04-21 | 2025-06-18 | Python | Survey of FSGS (ECCV 2024) | [🔗](https://github.com/kevin30205/FSGS_survey) |
| DNGaussian_survey | Private | 0 | 2025-04-21 | 2025-06-18 | Python | Survey of DNGaussian (CVPR 2024) | [🔗](https://github.com/kevin30205/DNGaussian_survey) |
| DropoutGS_survey | Private | 0 | 2025-04-21 | 2025-06-18 | Python | Survey of DropoutGS (CVPR 2025) | [🔗](https://github.com/kevin30205/DropoutGS_survey) |
| SinNeRF_survey | Private | 0 | 2023-08-30 | 2025-06-18 | Python | Survey of SinNeRF (ECCV 2022) | [🔗](https://github.com/kevin30205/SinNeRF_survey) |

### study

* **Total Repositories:** 11

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| Conference_Paper_Summary | Private | 0 | 2025-02-01 | 2025-06-21 | Python | Paper Summary of Conferences. | [🔗](https://github.com/kevin30205/Conference_Paper_Summary) |
| C_Programming_Language | Private | 0 | 2025-02-23 | 2025-06-20 | Markdown | The Guideline of C Programming Language. | [🔗](https://github.com/kevin30205/C_Programming_Language) |
| OccNeRF_optimized | Private | 0 | 2024-01-30 | 2025-06-20 | Python | The optimized code based on OccNeRF done by myself. | [🔗](https://github.com/kevin30205/OccNeRF_optimized) |
| Linux_Command_Memorandum | Private | 0 | 2025-02-07 | 2025-06-20 | Markdown | A handy reference guide for common Linux commands. | [🔗](https://github.com/kevin30205/Linux_Command_Memorandum) |
| LeetCode_Practice | Private | 0 | 2024-07-30 | 2025-06-01 | Python | The code practice on LeetCode. | [🔗](https://github.com/kevin30205/LeetCode_Practice) |
| HumanNeRF_optimized | Private | 0 | 2023-12-12 | 2025-06-01 | Shell | The optimized code based on HumanNeRF done by myself. | [🔗](https://github.com/kevin30205/HumanNeRF_optimized) |
| numpy-ml_survey | Private | 0 | 2025-02-06 | 2025-06-01 | Python | Survey of numpy-ml. | [🔗](https://github.com/kevin30205/numpy-ml_survey) |
| Algorithms-Python_survey | Private | 0 | 2025-02-07 | 2025-06-01 | Python | Survey of Python Algorithms. | [🔗](https://github.com/kevin30205/Algorithms-Python_survey) |
| Algorithms-Explanation_survey | Private | 0 | 2025-02-07 | 2025-06-01 | Unknown | Survey of Algorithms-Explanation | [🔗](https://github.com/kevin30205/Algorithms-Explanation_survey) |
| Algorithms-C-Plus-Plus_survey | Private | 0 | 2025-02-07 | 2025-06-01 | C++ | Survey of C-Plus-Plus Algorithms. | [🔗](https://github.com/kevin30205/Algorithms-C-Plus-Plus_survey) |
| Python_Programming_Language | Private | 0 | 2025-02-23 | 2025-06-01 | Python | The Guideline of Python Programming Language. | [🔗](https://github.com/kevin30205/Python_Programming_Language) |

### survey

* **Total Repositories:** 206

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| 4D-Humans_mine | Private | 0 | 2024-02-26 | 2025-06-20 | Python | 4D-Humans is used to preprocess the data to obtain the SMPL parameters. | [🔗](https://github.com/kevin30205/4D-Humans_mine) |
| fish-speech_survey | Private | 0 | 2025-06-06 | 2025-06-19 | Python | Survey of Fish Speech | [🔗](https://github.com/kevin30205/fish-speech_survey) |
| bark_survey | Private | 0 | 2025-06-05 | 2025-06-19 | Jupyter Notebook | Survey of bark (Suno) | [🔗](https://github.com/kevin30205/bark_survey) |
| Wan2.1_survey | Private | 0 | 2025-06-05 | 2025-06-19 | Python | Survey of Wan2.1 | [🔗](https://github.com/kevin30205/Wan2.1_survey) |
| Prompt-Depth-Anything_survey | Private | 0 | 2025-06-05 | 2025-06-19 | Python | Survey of Prompt Depth Anything (CVPR 2025) | [🔗](https://github.com/kevin30205/Prompt-Depth-Anything_survey) |
| Video-Depth-Anything_survey | Private | 0 | 2025-06-05 | 2025-06-19 | Python | Survey of Video Depth Anything (CVPR 2025) | [🔗](https://github.com/kevin30205/Video-Depth-Anything_survey) |
| Depth-Anything-V2_survey | Private | 0 | 2025-06-05 | 2025-06-19 | Python | Survey of Depth-Anything-V2 (NeurIPS 2024) | [🔗](https://github.com/kevin30205/Depth-Anything-V2_survey) |
| Depth-Anything_survey | Private | 0 | 2025-06-05 | 2025-06-19 | Python | Survey of Depth Anything (CVPR 2024) | [🔗](https://github.com/kevin30205/Depth-Anything_survey) |
| SAM-2_survey | Private | 0 | 2025-06-07 | 2025-06-19 | Jupyter Notebook | Survey of SAM 2 (ICLR 2025) | [🔗](https://github.com/kevin30205/SAM-2_survey) |
| SAM-HQ_survey | Private | 0 | 2025-06-07 | 2025-06-19 | Jupyter Notebook | Survey of SAM-HQ (NeurIPS 2023) | [🔗](https://github.com/kevin30205/SAM-HQ_survey) |
| Segment-Anything_survey | Private | 0 | 2025-06-07 | 2025-06-19 | Jupyter Notebook | Survey of Segment Anything (ICCV 2023) | [🔗](https://github.com/kevin30205/Segment-Anything_survey) |
| ABC-GS_survey | Private | 0 | 2025-06-15 | 2025-06-18 | Python | Survey of ABC-GS (ICME 2025) | [🔗](https://github.com/kevin30205/ABC-GS_survey) |
| LAENeRF_survey | Private | 0 | 2025-06-14 | 2025-06-18 | HTML | Survey of LAENeRF (CVPR 2024) | [🔗](https://github.com/kevin30205/LAENeRF_survey) |
| StopThePop_survey | Private | 0 | 2025-06-14 | 2025-06-18 | Python | Survey of StopThePop (SIGGRAPH 2024) | [🔗](https://github.com/kevin30205/StopThePop_survey) |
| 3DGRUT_survey | Private | 0 | 2025-06-09 | 2025-06-18 | Python | Survey of 3DGRUT (CVPR 2025) | [🔗](https://github.com/kevin30205/3DGRUT_survey) |
| 4DTAM_survey | Private | 0 | 2025-06-11 | 2025-06-18 | C++ | Survey of 4DTAM (CVPR 2025) | [🔗](https://github.com/kevin30205/4DTAM_survey) |
| ActiveNeRF_survey | Private | 0 | 2025-06-10 | 2025-06-18 | Python | Survey of  ActiveNeRF (ECCV 2022) | [🔗](https://github.com/kevin30205/ActiveNeRF_survey) |
| PanSplat_survey | Private | 0 | 2025-06-10 | 2025-06-18 | Python | Survey of PanSplat (CVPR 2025) | [🔗](https://github.com/kevin30205/PanSplat_survey) |
| RNG_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of RNG (CVPR 2025) | [🔗](https://github.com/kevin30205/RNG_survey) |
| GaussianShader_survey | Private | 0 | 2025-06-08 | 2025-06-18 | C++ | Survey of GaussianShader (CVPR 2024) | [🔗](https://github.com/kevin30205/GaussianShader_survey) |
| ReCap_survey | Private | 0 | 2025-06-08 | 2025-06-18 | Python | Survey of ReCap (CVPR 2025) | [🔗](https://github.com/kevin30205/ReCap_survey) |
| Luminance-GS_survey | Private | 0 | 2025-06-10 | 2025-06-18 | Python | Survey of Luminance-GS (CVPR 2025) | [🔗](https://github.com/kevin30205/Luminance-GS_survey) |
| FisherRF_survey | Private | 0 | 2025-06-08 | 2025-06-18 | Python | Survey of FisherRF (ECCV 2024) | [🔗](https://github.com/kevin30205/FisherRF_survey) |
| MoDec-GS_survey | Private | 0 | 2025-06-08 | 2025-06-18 | Python | Survey of MoDec-GS (CVPR 2025) | [🔗](https://github.com/kevin30205/MoDec-GS_survey) |
| Sparse2DGS_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of Sparse2DGS (CVPR 2025) | [🔗](https://github.com/kevin30205/Sparse2DGS_survey) |
| DashGaussian_survey | Private | 0 | 2025-06-07 | 2025-06-18 | C++ | Survey of DashGaussian (CVPR 2025) | [🔗](https://github.com/kevin30205/DashGaussian_survey) |
| GaussianSpa_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of GaussianSpa (CVPR 2025) | [🔗](https://github.com/kevin30205/GaussianSpa_survey) |
| EOGS_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of EOGS (CVPR 2025) | [🔗](https://github.com/kevin30205/EOGS_survey) |
| GS-LPM_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of GS-LPM (CVPR 2025) | [🔗](https://github.com/kevin30205/GS-LPM_survey) |
| TC-GS_survey | Private | 0 | 2025-06-05 | 2025-06-18 | C++ | Survey of TC-GS (ICME 2025) | [🔗](https://github.com/kevin30205/TC-GS_survey) |
| PUP-3D-GS_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of PUP 3D-GS (CVPR 2025) | [🔗](https://github.com/kevin30205/PUP-3D-GS_survey) |
| Speedy-Splat_survey | Private | 0 | 2025-06-07 | 2025-06-18 | Python | Survey of Speedy-Splat (CVPR 2025) | [🔗](https://github.com/kevin30205/Speedy-Splat_survey) |
| NRHints_survey | Private | 0 | 2025-05-30 | 2025-06-18 | Python | Survey of NRHints (SIGGRAPH 2023) | [🔗](https://github.com/kevin30205/NRHints_survey) |
| CAT-3DGS_survey | Private | 0 | 2025-06-05 | 2025-06-18 | Python | Survey of CAT-3DGS (ICLR 2025) | [🔗](https://github.com/kevin30205/CAT-3DGS_survey) |
| GS-3_survey | Private | 0 | 2025-05-30 | 2025-06-18 | Python | Survey of GS^3 (SIGGRAPH Asia 2024) | [🔗](https://github.com/kevin30205/GS-3_survey) |
| GS-IR_survey | Private | 0 | 2025-05-30 | 2025-06-18 | C++ | Survey of GS-IR (arXiv 2023) | [🔗](https://github.com/kevin30205/GS-IR_survey) |
| GI-GS_survey | Private | 0 | 2025-05-30 | 2025-06-18 | C++ | Survey of GI-GS (ICLR 2025) | [🔗](https://github.com/kevin30205/GI-GS_survey) |
| GaussianPrediction_survey | Private | 0 | 2025-05-30 | 2025-06-18 | HTML | Survey of GaussianPrediction (SIGGRAPH 2024) | [🔗](https://github.com/kevin30205/GaussianPrediction_survey) |
| AdR-Gaussian_survey | Private | 0 | 2025-05-30 | 2025-06-18 | Python | Survey of AdR-Gaussian (SIGGRAPH Asia 2024) | [🔗](https://github.com/kevin30205/AdR-Gaussian_survey) |
| CoR-GS_survey | Private | 0 | 2025-05-29 | 2025-06-18 | Python | Survey of CoR-GS (ECCV 2024) | [🔗](https://github.com/kevin30205/CoR-GS_survey) |
| GaussianIP_survey | Private | 0 | 2025-05-29 | 2025-06-18 | Python | Survey of GaussianIP (CVPR 2025) | [🔗](https://github.com/kevin30205/GaussianIP_survey) |
| SparseGS_survey | Private | 0 | 2025-05-19 | 2025-06-18 | Python | Survey of SparseGS (3DV 2025) | [🔗](https://github.com/kevin30205/SparseGS_survey) |
| HAHA_survey | Private | 0 | 2025-05-21 | 2025-06-18 | Python | Survey of HAHA (ACCV 2024) | [🔗](https://github.com/kevin30205/HAHA_survey) |
| Deformable-Radial-Kernel-Splatting_survey | Private | 0 | 2025-05-21 | 2025-06-18 | Python | Survey of Deformable Radial Kernel Splatting (CVPR 2025) | [🔗](https://github.com/kevin30205/Deformable-Radial-Kernel-Splatting_survey) |
| ControlGS_survey | Private | 0 | 2025-05-29 | 2025-06-18 | C++ | Survey of ControlGS (arXiv 2025) | [🔗](https://github.com/kevin30205/ControlGS_survey) |
| TensoIR_survey | Private | 0 | 2025-05-06 | 2025-06-18 | Python | Survey of TensoIR (CVPR 2023) | [🔗](https://github.com/kevin30205/TensoIR_survey) |
| hierarchical-3d-gaussians_survey | Private | 0 | 2025-05-21 | 2025-06-18 | Python | Survey of Hierarchical 3D Gaussians (SIGGRAPH 2024) | [🔗](https://github.com/kevin30205/hierarchical-3d-gaussians_survey) |
| BBSplat_survey | Private | 0 | 2025-05-15 | 2025-06-18 | Python | Survey of BBSplat (arXiv 2024) | [🔗](https://github.com/kevin30205/BBSplat_survey) |
| DRGS_survey | Private | 0 | 2025-05-19 | 2025-06-18 | Python | Survey of DRGS (CVPRW 2024) | [🔗](https://github.com/kevin30205/DRGS_survey) |
| Gaussian-Splatting-on-the-Move_survey | Private | 0 | 2025-04-30 | 2025-06-18 | Python | Survey of Gaussian Splatting on the Move (ECCV 2024) | [🔗](https://github.com/kevin30205/Gaussian-Splatting-on-the-Move_survey) |
| Taming-3DGS_survey | Private | 0 | 2025-05-18 | 2025-06-18 | Python | Survey of Taming 3DGS (SIGGRAPH Asia 2024) | [🔗](https://github.com/kevin30205/Taming-3DGS_survey) |
| SteepGS_survey | Private | 0 | 2025-05-19 | 2025-06-18 | Python | Survey of SteepGS (CVPR 2025) | [🔗](https://github.com/kevin30205/SteepGS_survey) |
| CoherentGS_survey | Private | 0 | 2025-05-14 | 2025-06-18 | Python | Survey of CoherentGS (ECCV 2024) | [🔗](https://github.com/kevin30205/CoherentGS_survey) |
| GaGS_survey | Private | 0 | 2025-05-15 | 2025-06-18 | C++ | Survey of GaGS (CVPR 2024) | [🔗](https://github.com/kevin30205/GaGS_survey) |
| Analytic-Splatting_survey | Private | 0 | 2025-05-15 | 2025-06-18 | Python | Survey of Analytic-Splatting (ECCV 2024) | [🔗](https://github.com/kevin30205/Analytic-Splatting_survey) |
| OP43DGS_survey | Private | 0 | 2025-05-14 | 2025-06-18 | Cuda | Survey of OP43DGS (ECCV 2024) | [🔗](https://github.com/kevin30205/OP43DGS_survey) |
| HoGS_survey | Private | 0 | 2025-05-13 | 2025-06-18 | C++ | Survey of HoGS (CVPR 2025) | [🔗](https://github.com/kevin30205/HoGS_survey) |
| Sparse-Voxels-Rasterizer_survey | Private | 0 | 2025-05-13 | 2025-06-18 | Jupyter Notebook | Survey of Sparse Voxels Rasterizer (CVPR 2025) | [🔗](https://github.com/kevin30205/Sparse-Voxels-Rasterizer_survey) |
| GES_survey | Private | 0 | 2025-05-14 | 2025-06-18 | Python | Survey of GES (CVPR 2024) | [🔗](https://github.com/kevin30205/GES_survey) |
| Self-Organizing-Gaussians_survey | Private | 0 | 2025-05-14 | 2025-06-18 | Python | Survey of Self-Organizing Gaussians (ECCV 2024) | [🔗](https://github.com/kevin30205/Self-Organizing-Gaussians_survey) |
| 3D-Student-Splatting-and-Scooping_survey | Private | 0 | 2025-05-13 | 2025-06-18 | Python | Survey of 3D Student Splatting and Scooping (CVPR 2025) | [🔗](https://github.com/kevin30205/3D-Student-Splatting-and-Scooping_survey) |
| AtomGS_survey | Private | 0 | 2025-05-12 | 2025-06-18 | Python | Survey of AtomGS (BMVC 2024) | [🔗](https://github.com/kevin30205/AtomGS_survey) |
| RoGSplat_survey | Private | 0 | 2025-05-09 | 2025-06-18 | Python | Survey of RoGSplat (CVPR 2025) | [🔗](https://github.com/kevin30205/RoGSplat_survey) |
| Beta-Splatting_survey | Private | 0 | 2025-05-12 | 2025-06-18 | Python | Survey of Beta Splatting (SIGGRAPH 2025) | [🔗](https://github.com/kevin30205/Beta-Splatting_survey) |
| MonoGS_survey | Private | 0 | 2025-05-11 | 2025-06-18 | Python | Survey of MonoGS (CVPR 2024) | [🔗](https://github.com/kevin30205/MonoGS_survey) |
| DreamGaussian4D_survey | Private | 0 | 2025-05-11 | 2025-06-18 | Python | Survey of DreamGaussian4D (arXiv 2023) | [🔗](https://github.com/kevin30205/DreamGaussian4D_survey) |
| HumanNorm_survey | Private | 0 | 2025-05-09 | 2025-06-18 | Python | Survey of HumanNorm (CVPR 2024) | [🔗](https://github.com/kevin30205/HumanNorm_survey) |
| SGCR_survey | Private | 0 | 2025-05-12 | 2025-06-18 | Python | Survey of SGCR (CVPR 2025) | [🔗](https://github.com/kevin30205/SGCR_survey) |
| TeT-Splatting_survey | Private | 0 | 2025-05-07 | 2025-06-18 | Jupyter Notebook | Survey of TeT-Splatting (NeurIPS 2024) | [🔗](https://github.com/kevin30205/TeT-Splatting_survey) |
| InvRender_survey | Private | 0 | 2025-05-06 | 2025-06-18 | Python | Survey of InvRender (CVPR 2022) | [🔗](https://github.com/kevin30205/InvRender_survey) |
| IRGS_survey | Private | 0 | 2025-05-07 | 2025-06-18 | HTML | Survey of IRGS (CVPR 2025) | [🔗](https://github.com/kevin30205/IRGS_survey) |
| BeNeRF_survey | Private | 0 | 2025-04-28 | 2025-06-18 | Python | Survey of BeNeRF (ECCV 2024) | [🔗](https://github.com/kevin30205/BeNeRF_survey) |
| SC-GS_survey | Private | 0 | 2025-05-07 | 2025-06-18 | Python | Survey of SC-GS (CVPR 2024) | [🔗](https://github.com/kevin30205/SC-GS_survey) |
| 4DGaussians_survey | Private | 0 | 2025-05-07 | 2025-06-18 | Jupyter Notebook | Survey of 4DGaussians (CVPR 2024) | [🔗](https://github.com/kevin30205/4DGaussians_survey) |
| Ref-Gaussian_survey | Private | 0 | 2025-05-05 | 2025-06-18 | C++ | Survey of Ref-Gaussian (ICLR 2025) | [🔗](https://github.com/kevin30205/Ref-Gaussian_survey) |
| RaDe-GS_survey | Private | 0 | 2025-04-30 | 2025-06-18 | C++ | Survey of RaDe-GS (arXiv 2024) | [🔗](https://github.com/kevin30205/RaDe-GS_survey) |
| GaussianDreamerPro_survey | Private | 0 | 2025-05-06 | 2025-06-18 | C++ | Survey of GaussianDreamerPro (arXiv 2024) | [🔗](https://github.com/kevin30205/GaussianDreamerPro_survey) |
| 3DGS-DR_survey | Private | 0 | 2025-05-05 | 2025-06-18 | Python | Survey of 3DGS-DR (SIGGRAPH 2024) | [🔗](https://github.com/kevin30205/3DGS-DR_survey) |
| BAGS_survey | Private | 0 | 2025-05-04 | 2025-06-18 | Python | Survey of BAGS (ECCV 2024) | [🔗](https://github.com/kevin30205/BAGS_survey) |
| DoF-Gaussian_survey | Private | 0 | 2025-05-02 | 2025-06-18 | Python | Survey of DoF-Gaussian (CVPR 2025) | [🔗](https://github.com/kevin30205/DoF-Gaussian_survey) |
| DropGaussian_survey | Private | 0 | 2025-05-04 | 2025-06-18 | Python | Survey of DropGaussian (CVPR 2025) | [🔗](https://github.com/kevin30205/DropGaussian_survey) |
| MAtCha-Gaussians_survey | Private | 0 | 2025-04-30 | 2025-06-18 | Python | Survey of MAtCha Gaussians (CVPR 2025) | [🔗](https://github.com/kevin30205/MAtCha-Gaussians_survey) |
| HDR-NeRF_survey | Private | 0 | 2025-04-26 | 2025-06-18 | Python | Survey of HDR-NeRF (CVPR 2022) | [🔗](https://github.com/kevin30205/HDR-NeRF_survey) |
| Gaussian-Frosting_survey | Private | 0 | 2025-04-30 | 2025-06-18 | Python | Survey of Gaussian Frosting (ECCV 2024) | [🔗](https://github.com/kevin30205/Gaussian-Frosting_survey) |
| SCINeRF_survey | Private | 0 | 2025-04-28 | 2025-06-18 | Python | Survey of SCINeRF (CVPR 2024) | [🔗](https://github.com/kevin30205/SCINeRF_survey) |
| BAD-Gaussians_survey | Private | 0 | 2025-04-30 | 2025-06-18 | Python | Survey of BAD-Gaussians (ECCV 2024) | [🔗](https://github.com/kevin30205/BAD-Gaussians_survey) |
| TiNeuVox_survey | Private | 0 | 2025-04-30 | 2025-06-18 | Python | Survey of TiNeuVox (SIGGRAPH Asia 2022) | [🔗](https://github.com/kevin30205/TiNeuVox_survey) |
| SplatFormer_survey | Private | 0 | 2025-04-25 | 2025-06-18 | Python | Survey of SplatFormer (ICLR 2025) | [🔗](https://github.com/kevin30205/SplatFormer_survey) |
| HDR-Plenoxels_survey | Private | 0 | 2025-04-26 | 2025-06-18 | Python | Survey of HDR-Plenoxels (ECCV 2022) | [🔗](https://github.com/kevin30205/HDR-Plenoxels_survey) |
| GaussHDR_survey | Private | 0 | 2025-04-25 | 2025-06-18 | Python | Survey of GaussHDR (CVPR 2025) | [🔗](https://github.com/kevin30205/GaussHDR_survey) |
| SAX-NeRF_survey | Private | 0 | 2025-04-22 | 2025-06-18 | Python | Survey of SAX-NeRF (CVPR 2024) | [🔗](https://github.com/kevin30205/SAX-NeRF_survey) |
| NexusGS_survey | Private | 0 | 2025-04-26 | 2025-06-18 | Python | Survey of NexusGS (CVPR 2025) | [🔗](https://github.com/kevin30205/NexusGS_survey) |
| HDR-GS_survey | Private | 0 | 2025-04-25 | 2025-06-18 | Python | Survey of HDR-GS (NeurIPS 2024) | [🔗](https://github.com/kevin30205/HDR-GS_survey) |
| FramePack_survey | Private | 0 | 2025-04-24 | 2025-06-18 | Python | Survey of FramePack (arXiv 2025) | [🔗](https://github.com/kevin30205/FramePack_survey) |
| r2_gaussian_survey | Private | 0 | 2025-04-23 | 2025-06-18 | Python | Survey of R2 Gaussian (NeurIPS 2024) | [🔗](https://github.com/kevin30205/r2_gaussian_survey) |
| Stable-Dreamfusion_survey | Private | 0 | 2025-04-24 | 2025-06-18 | Python | Survey of Stable-Dreamfusion (ICLR 2023) | [🔗](https://github.com/kevin30205/Stable-Dreamfusion_survey) |
| 3D-Convex-Splatting_survey | Private | 0 | 2025-04-21 | 2025-06-18 | Python | Survey of 3D Convex Splatting (CVPR 2025) | [🔗](https://github.com/kevin30205/3D-Convex-Splatting_survey) |
| DreamCraft3D_survey | Private | 0 | 2025-04-24 | 2025-06-18 | Python | Survey of DreamCraft3D (ICLR 2024) | [🔗](https://github.com/kevin30205/DreamCraft3D_survey) |
| X-Gaussian_survey | Private | 0 | 2025-04-22 | 2025-06-18 | Python | Survey of X-Gaussian (ECCV 2024) | [🔗](https://github.com/kevin30205/X-Gaussian_survey) |
| LucidDreamer_survey | Private | 0 | 2025-04-20 | 2025-06-18 | Python | Survey of LucidDreamer (CVPR 2024) | [🔗](https://github.com/kevin30205/LucidDreamer_survey) |
| FSGS_survey | Private | 0 | 2025-04-21 | 2025-06-18 | Python | Survey of FSGS (ECCV 2024) | [🔗](https://github.com/kevin30205/FSGS_survey) |
| Ref-GS_survey | Private | 0 | 2025-04-22 | 2025-06-18 | Python | Survey of Ref-GS (CVPR 2025) | [🔗](https://github.com/kevin30205/Ref-GS_survey) |
| SuGaR_survey | Private | 0 | 2025-04-22 | 2025-06-18 | C++ | Survey of SuGaR (CVPR 2024) | [🔗](https://github.com/kevin30205/SuGaR_survey) |
| Vol3DGS_survey | Private | 0 | 2025-04-21 | 2025-06-18 | Python | Survey of Vol3DGS (CVPR 2025) | [🔗](https://github.com/kevin30205/Vol3DGS_survey) |
| GFSGS_survey | Private | 0 | 2025-04-21 | 2025-06-18 | Python | Survey of GFSGS (CVPR 2025) | [🔗](https://github.com/kevin30205/GFSGS_survey) |
| MaskGaussian_survey | Private | 0 | 2025-04-21 | 2025-06-18 | C++ | Survey of MaskGaussian (CVPR 2025) | [🔗](https://github.com/kevin30205/MaskGaussian_survey) |
| DNGaussian_survey | Private | 0 | 2025-04-21 | 2025-06-18 | Python | Survey of DNGaussian (CVPR 2024) | [🔗](https://github.com/kevin30205/DNGaussian_survey) |
| DropoutGS_survey | Private | 0 | 2025-04-21 | 2025-06-18 | Python | Survey of DropoutGS (CVPR 2025) | [🔗](https://github.com/kevin30205/DropoutGS_survey) |
| Relighting4D_survey | Private | 0 | 2025-04-05 | 2025-06-18 | Python | Survey of Relighting4D (ECCV 2022) | [🔗](https://github.com/kevin30205/Relighting4D_survey) |
| GART_survey | Private | 0 | 2025-04-17 | 2025-06-18 | Python | Survey of GART (CVPR 2024) | [🔗](https://github.com/kevin30205/GART_survey) |
| Fantasia3D_survey | Private | 0 | 2025-04-19 | 2025-06-18 | Python | Survey of Fantasia3D (ICCV 2023) | [🔗](https://github.com/kevin30205/Fantasia3D_survey) |
| EnvGS_survey | Private | 0 | 2025-04-18 | 2025-06-18 | Python | Survey of EnvGS (CVPR 2025) | [🔗](https://github.com/kevin30205/EnvGS_survey) |
| AnimatableGaussians_survey | Private | 0 | 2025-04-19 | 2025-06-18 | Python | Survey of Animatable Gaussians (CVPR 2024) | [🔗](https://github.com/kevin30205/AnimatableGaussians_survey) |
| GaussianDreamer_survey | Private | 0 | 2025-04-18 | 2025-06-18 | Python | Survey of GaussianDreamer (CVPR 2024) | [🔗](https://github.com/kevin30205/GaussianDreamer_survey) |
| GSGEN_survey | Private | 0 | 2025-04-14 | 2025-06-18 | Python | Survey of GSGEN (CVPR 2024) | [🔗](https://github.com/kevin30205/GSGEN_survey) |
| DreamGaussian_survey | Private | 0 | 2025-04-13 | 2025-06-18 | Python | Survey of DreamGaussian (ICLR 2024) | [🔗](https://github.com/kevin30205/DreamGaussian_survey) |
| SpacetimeGaussians_survey | Private | 0 | 2025-04-13 | 2025-06-18 | Python | Survey of SpacetimeGaussians (CVPR 2024) | [🔗](https://github.com/kevin30205/SpacetimeGaussians_survey) |
| ContextGS_survey | Private | 0 | 2025-04-09 | 2025-06-18 | Python | Survey of ContextGS (NeurIPS 2024) | [🔗](https://github.com/kevin30205/ContextGS_survey) |
| Mini-Splatting_survey | Private | 0 | 2025-04-11 | 2025-06-18 | Python | Survey of Mini-Splatting (ECCV 2024) | [🔗](https://github.com/kevin30205/Mini-Splatting_survey) |
| GSDF_survey | Private | 0 | 2025-04-10 | 2025-06-18 | Python | Survey of GSDF (NeurIPS 2024) | [🔗](https://github.com/kevin30205/GSDF_survey) |
| ARAH_survey | Private | 0 | 2025-04-04 | 2025-06-18 | Python | Survey of ARAH (ECCV 2022) | [🔗](https://github.com/kevin30205/ARAH_survey) |
| Grendel-GS_survey | Private | 0 | 2025-04-12 | 2025-06-18 | Python | Survey of Grendel-GS (ICLR 2025) | [🔗](https://github.com/kevin30205/Grendel-GS_survey) |
| Deformable-3D-Gaussians_survey | Private | 0 | 2025-04-12 | 2025-06-18 | Python | Survey of Deformable 3D Gaussians (CVPR 2024) | [🔗](https://github.com/kevin30205/Deformable-3D-Gaussians_survey) |
| FCGS_survey | Private | 0 | 2025-04-12 | 2025-06-18 | C++ | Survey of FCGS (ICLR 2025) | [🔗](https://github.com/kevin30205/FCGS_survey) |
| EAGLES_survey | Private | 0 | 2025-04-11 | 2025-06-18 | C++ | Survey of EAGLES (ECCV 2024) | [🔗](https://github.com/kevin30205/EAGLES_survey) |
| 3DGS-MCMC_survey | Private | 0 | 2025-04-08 | 2025-06-18 | Python | Survey of 3DGS-MCMC (NeurIPS 2024) | [🔗](https://github.com/kevin30205/3DGS-MCMC_survey) |
| Neural-Human-Performer_survey | Private | 0 | 2025-04-05 | 2025-06-18 | Python | Survey of Neural Human Performer (NeurIPS 2021) | [🔗](https://github.com/kevin30205/Neural-Human-Performer_survey) |
| PCGS_survey | Private | 0 | 2025-04-10 | 2025-06-18 | C++ | Survey of PCGS (arXiv 2025) | [🔗](https://github.com/kevin30205/PCGS_survey) |
| HAC-plus_survey | Private | 0 | 2025-04-09 | 2025-06-18 | C++ | Survey of HAC++ (arXiv 2025) | [🔗](https://github.com/kevin30205/HAC-plus_survey) |
| C3DGS_survey | Private | 0 | 2025-04-11 | 2025-06-18 | Python | Survey of C3DGS (CVPR 2024) | [🔗](https://github.com/kevin30205/C3DGS_survey) |
| Octree-GS_survey | Private | 0 | 2025-04-09 | 2025-06-18 | C++ | Survey of Octree-GS (arXiv 2024) | [🔗](https://github.com/kevin30205/Octree-GS_survey) |
| Scaffold-GS_survey | Private | 0 | 2025-04-09 | 2025-06-18 | C++ | Survey of Scaffold-GS (CVPR 2024) | [🔗](https://github.com/kevin30205/Scaffold-GS_survey) |
| IntrinsicAvatar_survey | Private | 0 | 2025-04-05 | 2025-06-18 | Python | Survey of IntrinsicAvatar (CVPR 2024) | [🔗](https://github.com/kevin30205/IntrinsicAvatar_survey) |
| TAVA_survey | Private | 0 | 2025-04-04 | 2025-06-18 | Python | Survey of TAVA (ECCV 2022) | [🔗](https://github.com/kevin30205/TAVA_survey) |
| Compact-3DGS_survey | Private | 0 | 2025-04-10 | 2025-06-18 | Python | Survey of Compact-3DGS (CVPR 2024) | [🔗](https://github.com/kevin30205/Compact-3DGS_survey) |
| LightGaussian_survey | Private | 0 | 2025-04-10 | 2025-06-18 | Python | Survey of LightGaussian (NeurIPS 2024) | [🔗](https://github.com/kevin30205/LightGaussian_survey) |
| HAC_survey | Private | 0 | 2025-04-09 | 2025-06-18 | Python | Survey of HAC (ECCV 2024) | [🔗](https://github.com/kevin30205/HAC_survey) |
| InstantSplat_survey | Private | 0 | 2025-04-08 | 2025-06-18 | Python | Survey of InstantSplat (arXiv 2024) | [🔗](https://github.com/kevin30205/InstantSplat_survey) |
| 3D-HGS_survey | Private | 0 | 2025-04-08 | 2025-06-18 | Python | Survey of 3D-HGS (CVPR 2025) | [🔗](https://github.com/kevin30205/3D-HGS_survey) |
| Neural-Body_survey | Private | 0 | 2025-04-05 | 2025-06-18 | Python | Survey of Neural Body (CVPR 2021) | [🔗](https://github.com/kevin30205/Neural-Body_survey) |
| 4D-Gaussian-Splatting_survey | Private | 0 | 2025-04-01 | 2025-06-18 | Python | Survey of 4D Gaussian Splatting (ICLR 2024) | [🔗](https://github.com/kevin30205/4D-Gaussian-Splatting_survey) |
| 3DGS-Avatar_survey | Private | 0 | 2025-04-04 | 2025-06-18 | Python | Survey of 3DGS-Avatar (CVPR 2024) | [🔗](https://github.com/kevin30205/3DGS-Avatar_survey) |
| Gaussian-Opacity-Fields_survey | Private | 0 | 2025-04-01 | 2025-06-18 | Python | Survey of Gaussian Opacity Fields (GOF) (SIGGRAPH ASIA 2024) | [🔗](https://github.com/kevin30205/Gaussian-Opacity-Fields_survey) |
| GPS-Gaussian_survey | Private | 0 | 2025-04-03 | 2025-06-18 | C++ | Survey of GPS-Gaussian (CVPR 2024) | [🔗](https://github.com/kevin30205/GPS-Gaussian_survey) |
| GoMAvatar_survey | Private | 0 | 2025-03-31 | 2025-06-18 | Python | Survey of GoMAvatar (CVPR 2024) | [🔗](https://github.com/kevin30205/GoMAvatar_survey) |
| Mani-GS_survey | Private | 0 | 2025-04-03 | 2025-06-18 | Python | Survey of Mani-GS (CVPR 2025) | [🔗](https://github.com/kevin30205/Mani-GS_survey) |
| 2D-Gaussian-Splatting_survey | Private | 0 | 2025-04-01 | 2025-06-18 | Python | Survey of 2D Gaussian Splatting (SIGGRAPH 2024) | [🔗](https://github.com/kevin30205/2D-Gaussian-Splatting_survey) |
| Relightable-3D-Gaussian_survey | Private | 0 | 2025-04-03 | 2025-06-18 | Python | Survey of Relightable 3D Gaussian (ECCV 2024) | [🔗](https://github.com/kevin30205/Relightable-3D-Gaussian_survey) |
| Mip-Splatting_survey | Private | 0 | 2025-04-01 | 2025-06-18 | Python | Survey of Mip-Splatting (CVPR 2024) | [🔗](https://github.com/kevin30205/Mip-Splatting_survey) |
| Animatable-NeRF_survey | Private | 0 | 2025-03-29 | 2025-06-18 | Python | Survey of Animatable-NeRF (ICCV 2021) | [🔗](https://github.com/kevin30205/Animatable-NeRF_survey) |
| 3D-Gaussian-Splatting_survey | Private | 0 | 2025-03-31 | 2025-06-18 | Python | Survey of 3D Gaussian Splatting (SIGGRAPH 2023) | [🔗](https://github.com/kevin30205/3D-Gaussian-Splatting_survey) |
| LangSplat_survey | Private | 0 | 2025-04-01 | 2025-06-18 | Python | Survey of LangSplat (CVPR 2024) | [🔗](https://github.com/kevin30205/LangSplat_survey) |
| Deblurring-3D-Gaussian-Splatting_survey | Private | 0 | 2025-04-01 | 2025-06-18 | Python | Survey of Deblurring 3D Gaussian Splatting (ECCV 2024) | [🔗](https://github.com/kevin30205/Deblurring-3D-Gaussian-Splatting_survey) |
| SplattingAvatar_survey | Private | 0 | 2025-03-30 | 2025-06-18 | Python | Survey of SplattingAvatar (CVPR 2024) | [🔗](https://github.com/kevin30205/SplattingAvatar_survey) |
| GaussianAvatar_survey | Private | 0 | 2025-03-31 | 2025-06-18 | Python | Survey of GaussianAvatar (CVPR 2024) | [🔗](https://github.com/kevin30205/GaussianAvatar_survey) |
| HUGS_survey | Private | 0 | 2025-03-30 | 2025-06-18 | Python | Survey of HUGS (CVPR 2024) | [🔗](https://github.com/kevin30205/HUGS_survey) |
| HumanNeRF-SE_survey | Private | 0 | 2025-03-29 | 2025-06-18 | Python | Survey of HumanNeRF-SE (CVPR 2024) | [🔗](https://github.com/kevin30205/HumanNeRF-SE_survey) |
| OccFusion_survey | Private | 0 | 2025-03-28 | 2025-06-18 | Python | Survey of OccFusion (NeurIPS 2024) | [🔗](https://github.com/kevin30205/OccFusion_survey) |
| InstantAvatar_survey | Private | 0 | 2025-03-28 | 2025-06-18 | Python | Survey of InstantAvatar (CVPR 2023) | [🔗](https://github.com/kevin30205/InstantAvatar_survey) |
| GauHuman_survey | Private | 0 | 2025-03-28 | 2025-06-18 | Python | Survey of GauHuman (CVPR 2024) | [🔗](https://github.com/kevin30205/GauHuman_survey) |
| Tensor4D_survey | Private | 0 | 2024-03-23 | 2025-06-18 | Python | Survey of Tensor4D (CVPR 2023) | [🔗](https://github.com/kevin30205/Tensor4D_survey) |
| REF_square_NeRF_survey | Private | 0 | 2024-04-17 | 2025-06-18 | Python | Survey of REF Square NeRF (arXiv 2023/11) | [🔗](https://github.com/kevin30205/REF_square_NeRF_survey) |
| Eikonal-Fields_survey | Private | 0 | 2024-04-17 | 2025-06-18 | Python | Survey of Eikonal Fields (SIGGRAPH 2022) | [🔗](https://github.com/kevin30205/Eikonal-Fields_survey) |
| RoDynRF_survey | Private | 0 | 2024-04-12 | 2025-06-18 | Python | Survey of RoDynRF (CVPR 2023) | [🔗](https://github.com/kevin30205/RoDynRF_survey) |
| DynamicNeRF_survey | Private | 0 | 2024-04-12 | 2025-06-18 | Python | Survey of DynamicNeRF (ICCV 2021) | [🔗](https://github.com/kevin30205/DynamicNeRF_survey) |
| NeRFReN_survey | Private | 0 | 2024-03-23 | 2025-06-18 | Python | Survey of NeRFReN (CVPR 2022) | [🔗](https://github.com/kevin30205/NeRFReN_survey) |
| BAD-NeRF_survey | Private | 0 | 2024-03-13 | 2025-06-18 | Python | Survey of BAD-NeRF (CVPR 2023) | [🔗](https://github.com/kevin30205/BAD-NeRF_survey) |
| HyperNeRF_survey | Private | 0 | 2023-11-26 | 2025-06-18 | Python | Survey of HyperNeRF (SIGGRAPH Asia 2021) | [🔗](https://github.com/kevin30205/HyperNeRF_survey) |
| Deblur-NeRF_survey | Private | 0 | 2024-01-10 | 2025-06-18 | Python | Survey of Deblur-NeRF (CVPR 2022) | [🔗](https://github.com/kevin30205/Deblur-NeRF_survey) |
| NeuS_survey | Private | 0 | 2024-03-13 | 2025-06-18 | Python | Survey of NeuS (NeurIPS 2021) | [🔗](https://github.com/kevin30205/NeuS_survey) |
| ENeRF_survey | Private | 0 | 2024-02-17 | 2025-06-18 | Python | Survey of ENeRF (SIGGRAPH Asia 2022) | [🔗](https://github.com/kevin30205/ENeRF_survey) |
| OccNeRF_survey | Private | 0 | 2024-01-30 | 2025-06-18 | Python | Survey of OccNeRF (ICCV 2023) | [🔗](https://github.com/kevin30205/OccNeRF_survey) |
| LocalRF_survey | Private | 0 | 2024-01-10 | 2025-06-18 | Python | Survey of LocalRF (CVPR 2023) | [🔗](https://github.com/kevin30205/LocalRF_survey) |
| Ref-NeuS_survey | Private | 0 | 2024-01-10 | 2025-06-18 | Python | Survey of Ref-NeuS (ICCV 2023) | [🔗](https://github.com/kevin30205/Ref-NeuS_survey) |
| NeRFplusplus_survey | Private | 0 | 2023-11-26 | 2025-06-18 | Python | Survey of NeRF++ (arXiv 2020) | [🔗](https://github.com/kevin30205/NeRFplusplus_survey) |
| NoPe-NeRF_survey | Private | 0 | 2023-08-29 | 2025-06-18 | Python | Survey of NoPe-NeRF (CVPR 2023) | [🔗](https://github.com/kevin30205/NoPe-NeRF_survey) |
| TransHuman_survey | Private | 0 | 2023-11-26 | 2025-06-18 | Python | Survey of TransHuman (ICCV 2023) | [🔗](https://github.com/kevin30205/TransHuman_survey) |
| SHERF_survey | Private | 0 | 2023-11-26 | 2025-06-18 | Python | Survey of SHERF (ICCV 2023) | [🔗](https://github.com/kevin30205/SHERF_survey) |
| TILTED_survey | Private | 0 | 2023-09-25 | 2025-06-18 | Python | Survey of TILTED (ICCV 2023) | [🔗](https://github.com/kevin30205/TILTED_survey) |
| Ref-NeRF_pl_survey | Private | 0 | 2023-09-12 | 2025-06-18 | Python | Survey of Ref-NeRF (CVPR 2022) [PyTorch Lightning Version] | [🔗](https://github.com/kevin30205/Ref-NeRF_pl_survey) |
| Strivec_survey | Private | 0 | 2023-11-08 | 2025-06-18 | Python | Survey of Strivec (ICCV 2023) | [🔗](https://github.com/kevin30205/Strivec_survey) |
| K-Planes_survey | Private | 0 | 2023-08-13 | 2025-06-18 | Python | Survey of K-Planes (CVPR 2023) | [🔗](https://github.com/kevin30205/K-Planes_survey) |
| HexPlane_survey | Private | 0 | 2023-08-18 | 2025-06-18 | Python | Survey of HexPlane (CVPR 2023) | [🔗](https://github.com/kevin30205/HexPlane_survey) |
| Tri-MipRF_survey | Private | 0 | 2023-10-07 | 2025-06-18 | Python | Survey of Tri-MipRF (ICCV 2023) | [🔗](https://github.com/kevin30205/Tri-MipRF_survey) |
| TensoRF_survey | Private | 0 | 2023-08-16 | 2025-06-18 | Python | Survey of TensoRF (ECCV 2022) | [🔗](https://github.com/kevin30205/TensoRF_survey) |
| EfficientNeRF_survey | Private | 0 | 2023-08-30 | 2025-06-18 | Python | Survey of EfficientNeRF (CVPR 2022) | [🔗](https://github.com/kevin30205/EfficientNeRF_survey) |
| ABLE-NeRF_survey | Private | 0 | 2023-08-29 | 2025-06-18 | Python | Survey of ABLE-NeRF (CVPR 2023) | [🔗](https://github.com/kevin30205/ABLE-NeRF_survey) |
| Zip-NeRF_survey | Private | 0 | 2023-09-15 | 2025-06-18 | Python | Survey of Zip-NeRF (ICCV 2023) [PyTorch Version] | [🔗](https://github.com/kevin30205/Zip-NeRF_survey) |
| SinNeRF_survey | Private | 0 | 2023-08-30 | 2025-06-18 | Python | Survey of SinNeRF (ECCV 2022) | [🔗](https://github.com/kevin30205/SinNeRF_survey) |
| mipNeRF_PyTorch_survey | Private | 0 | 2023-08-13 | 2025-06-18 | Python | Survey of mipNeRF (ICCV 2021) [Pytorch Version] | [🔗](https://github.com/kevin30205/mipNeRF_PyTorch_survey) |
| Plenoxels_survey | Private | 0 | 2023-09-14 | 2025-06-18 | C++ | Survey of Plenoxels (CVPR 2022) | [🔗](https://github.com/kevin30205/Plenoxels_survey) |
| NVR-in-Minutes_survey | Private | 0 | 2023-09-26 | 2025-06-18 | Python | Survey of NVR-in-Minutes (CVPR 2023) | [🔗](https://github.com/kevin30205/NVR-in-Minutes_survey) |
| Neuman_survey | Private | 0 | 2023-08-13 | 2025-06-18 | Python | Survey of Neuman (ECCV 2022) | [🔗](https://github.com/kevin30205/Neuman_survey) |
| NeRF_PyTorch_survey | Private | 0 | 2023-08-28 | 2025-06-18 | Python | Survey of NeRF (ECCV 2020) [Pytorch Version] | [🔗](https://github.com/kevin30205/NeRF_PyTorch_survey) |
| MonoHuman_survey | Private | 0 | 2023-08-27 | 2025-06-18 | Python | Survey of MonoHuman (CVPR 2023) | [🔗](https://github.com/kevin30205/MonoHuman_survey) |
| Instant-NGP_survey | Private | 0 | 2023-09-14 | 2025-06-18 | Python | Survey of Instant-NGP (SIGGRAPH 2022) [Pytorch Version] | [🔗](https://github.com/kevin30205/Instant-NGP_survey) |
| HumanNeRF_survey | Private | 0 | 2023-08-27 | 2025-06-18 | Python | Survey of HumanNeRF (CVPR 2022) | [🔗](https://github.com/kevin30205/HumanNeRF_survey) |
| DVGOv2_survey | Private | 0 | 2023-09-03 | 2025-06-18 | Python | Survey of DVGO_v2 (CVPR 2022) | [🔗](https://github.com/kevin30205/DVGOv2_survey) |
| DVGOv1_survey | Private | 0 | 2023-09-04 | 2025-06-18 | Python | Survey of DVGO_v1 (CVPR 2022) | [🔗](https://github.com/kevin30205/DVGOv1_survey) |
| Vid2Avatar_survey | Private | 0 | 2023-09-26 | 2025-06-18 | Python | Survey of Vid2Avatar (CVPR 2023) | [🔗](https://github.com/kevin30205/Vid2Avatar_survey) |
| PHALP_survey | Private | 0 | 2025-04-07 | 2025-06-01 | Python | Survey of PHALP (CVPR 2022) | [🔗](https://github.com/kevin30205/PHALP_survey) |
| numpy-ml_survey | Private | 0 | 2025-02-06 | 2025-06-01 | Python | Survey of numpy-ml. | [🔗](https://github.com/kevin30205/numpy-ml_survey) |
| Algorithms-Python_survey | Private | 0 | 2025-02-07 | 2025-06-01 | Python | Survey of Python Algorithms. | [🔗](https://github.com/kevin30205/Algorithms-Python_survey) |
| Algorithms-Explanation_survey | Private | 0 | 2025-02-07 | 2025-06-01 | Unknown | Survey of Algorithms-Explanation | [🔗](https://github.com/kevin30205/Algorithms-Explanation_survey) |
| Algorithms-C-Plus-Plus_survey | Private | 0 | 2025-02-07 | 2025-06-01 | C++ | Survey of C-Plus-Plus Algorithms. | [🔗](https://github.com/kevin30205/Algorithms-C-Plus-Plus_survey) |
| SMPL-X_survey | Private | 0 | 2025-03-31 | 2025-06-01 | Python | Survey of SMPL-X (CVPR 2019) | [🔗](https://github.com/kevin30205/SMPL-X_survey) |

### toolbox

* **Total Repositories:** 40

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| Quarkdown_tool | Private | 0 | 2025-06-20 | 2025-06-20 | Kotlin | Quarkdown: A modern Markdown-based typesetting system. | [🔗](https://github.com/kevin30205/Quarkdown_tool) |
| WSL_tool | Private | 0 | 2025-06-20 | 2025-06-20 | C++ | WSL: Windows Subsystem for Linux | [🔗](https://github.com/kevin30205/WSL_tool) |
| ChatReviewer_tool | Private | 0 | 2025-06-20 | 2025-06-20 | Python | ChatReviewer is a tool to analyze the papers and gives suggestions. | [🔗](https://github.com/kevin30205/ChatReviewer_tool) |
| ChatPaper_tool | Private | 0 | 2025-06-20 | 2025-06-20 | Python | ChatPaper is a tool to summarize papers. | [🔗](https://github.com/kevin30205/ChatPaper_tool) |
| NTHU-Thesis-Template_tool | Private | 0 | 2025-06-10 | 2025-06-10 | TeX | The LaTeX NTHU thesis template. | [🔗](https://github.com/kevin30205/NTHU-Thesis-Template_tool) |
| Awesome-CV_tool | Private | 0 | 2025-06-09 | 2025-06-09 | TeX | Awesome CV is the LaTeX template for job application. | [🔗](https://github.com/kevin30205/Awesome-CV_tool) |
| STORM_tool | Private | 0 | 2025-06-04 | 2025-06-04 | Python | STORM: An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. | [🔗](https://github.com/kevin30205/STORM_tool) |
| Anthropic-courses_tool | Private | 0 | 2025-06-04 | 2025-06-04 | Jupyter Notebook | Anthropic's educational courses. | [🔗](https://github.com/kevin30205/Anthropic-courses_tool) |
| Anthropic-prompt-eng-interactive-tutorial_tool | Private | 0 | 2025-06-04 | 2025-06-04 | Jupyter Notebook | Anthropic's Interactive Prompt Engineering Tutorial. | [🔗](https://github.com/kevin30205/Anthropic-prompt-eng-interactive-tutorial_tool) |
| awesome-3D-gaussian-splatting_tool | Private | 0 | 2025-06-04 | 2025-06-04 | HTML | The list of papers and resources focused on 3D Gaussian Splatting. | [🔗](https://github.com/kevin30205/awesome-3D-gaussian-splatting_tool) |
| Personal-Academic-Website_tool | Private | 0 | 2025-06-04 | 2025-06-04 | CSS | Personal Academic Website: A skeleton-site for a personal academic website written in Jekyll. | [🔗](https://github.com/kevin30205/Personal-Academic-Website_tool) |
| Academic-Project-Page-Template_tool | Private | 0 | 2025-06-04 | 2025-06-04 | JavaScript | Academic Project Page Template: A project page template for academic papers. | [🔗](https://github.com/kevin30205/Academic-Project-Page-Template_tool) |
| GitHub-Profile-Achievements_tool | Private | 0 | 2025-06-04 | 2025-06-04 | Markdown | GitHub Profile Achievements: A collection listing all Achievements available on the GitHub profile. | [🔗](https://github.com/kevin30205/GitHub-Profile-Achievements_tool) |
| GitHub-Achievements_tool | Private | 0 | 2025-06-04 | 2025-06-04 | Markdown | GitHub Achievements: A Complete List of GitHub Profile Badges and Achievements. | [🔗](https://github.com/kevin30205/GitHub-Achievements_tool) |
| WhisperX_tool | Private | 0 | 2025-06-04 | 2025-06-04 | Python | WhisperX is the Automatic Speech Recognition with Word-level Timestamps Diarization. | [🔗](https://github.com/kevin30205/WhisperX_tool) |
| transcribe-anything_tool | Private | 0 | 2025-06-04 | 2025-06-04 | Python | transcribe-anything is the service that transcribe vedios using Whisper AI. | [🔗](https://github.com/kevin30205/transcribe-anything_tool) |
| vit-pytorch_tool | Private | 0 | 2025-06-04 | 2025-06-04 | Python | vit-pytorch is the implementation of Vision Transformer in Pytorch. | [🔗](https://github.com/kevin30205/vit-pytorch_tool) |
| yt-dlp_tool | Private | 0 | 2025-01-10 | 2025-06-01 | Python | yt-dlp is the tool for downloading videos from supported websites. | [🔗](https://github.com/kevin30205/yt-dlp_tool) |
| faster-whisper_tool | Private | 0 | 2025-01-10 | 2025-06-01 | Python | faster-whisper is the tool for generating transcriptions from videos/audios. | [🔗](https://github.com/kevin30205/faster-whisper_tool) |
| OpenCC_tool | Private | 0 | 2025-01-12 | 2025-06-01 | C++ | OpenCC is the tool for conversion between Traditional and Simplified Chinese. | [🔗](https://github.com/kevin30205/OpenCC_tool) |
| opencc-python_tool | Private | 0 | 2025-01-12 | 2025-06-01 | Python | opencc-python is the Python version of OpenCC. | [🔗](https://github.com/kevin30205/opencc-python_tool) |
| MarkItDown_tool | Private | 0 | 2025-01-12 | 2025-06-01 | Python | MarkItDown is a tool for converting files and office documents to Markdown. | [🔗](https://github.com/kevin30205/MarkItDown_tool) |
| btop_tool | Private | 0 | 2025-01-13 | 2025-06-01 | C++ | btop is a tool of resource monitor. | [🔗](https://github.com/kevin30205/btop_tool) |
| waveterm_tool | Private | 0 | 2025-01-13 | 2025-06-01 | TypeScript | waveterm is a tool of an open-source, cross-platform terminal for seamless workflows. | [🔗](https://github.com/kevin30205/waveterm_tool) |
| Crawling-CV-Conference-Papers_tool | Private | 0 | 2025-01-26 | 2025-06-01 | Jupyter Notebook | Crawling-CV-Conference-Papers is a tool for crawling conference papers. | [🔗](https://github.com/kevin30205/Crawling-CV-Conference-Papers_tool) |
| Docling_tool | Private | 0 | 2025-01-27 | 2025-06-01 | Python | Docling is a tool for converting various document formats to HTML, Markdown, etc.. | [🔗](https://github.com/kevin30205/Docling_tool) |
| Metrics_tool | Private | 0 | 2025-01-27 | 2025-06-01 | JavaScript | Metrics is a tool that can be embedded everywhere, including the GitHub profile readme. | [🔗](https://github.com/kevin30205/Metrics_tool) |
| awesome-chatgpt-prompts_tool | Private | 0 | 2025-01-27 | 2025-06-01 | HTML | Awesome ChatGPT Prompts is a repository with the collection of prompts for AI. | [🔗](https://github.com/kevin30205/awesome-chatgpt-prompts_tool) |
| whisper_tool | Private | 0 | 2025-01-27 | 2025-06-01 | Python | Whisper is a general-purpose speech recognition model proposed by OpenAI. | [🔗](https://github.com/kevin30205/whisper_tool) |
| autocut_tool | Private | 0 | 2025-01-27 | 2025-06-01 | Python | AutoCut is a tool that can automatically generate subtitles and cut the video by editing the subtitle file. | [🔗](https://github.com/kevin30205/autocut_tool) |
| stable-diffusion_tool | Private | 0 | 2025-01-27 | 2025-06-01 | Jupyter Notebook | Stable Diffusion is a latent text-to-image diffusion model. | [🔗](https://github.com/kevin30205/stable-diffusion_tool) |
| stable-diffusion-webui_tool | Private | 0 | 2025-01-27 | 2025-06-01 | Python | Stable Diffusion web UI is a web interface for Stable Diffusion. | [🔗](https://github.com/kevin30205/stable-diffusion-webui_tool) |
| AutoGPT_tool | Private | 0 | 2025-01-27 | 2025-06-01 | Python | AutoGPT is a powerful platform that allows you to create, deploy, and manage continuous AI agents that automate complex workflows. | [🔗](https://github.com/kevin30205/AutoGPT_tool) |
| fastsdcpu_tool | Private | 0 | 2025-01-27 | 2025-06-01 | Python | FastSD CPU is a faster version of Stable Diffusion on CPU. | [🔗](https://github.com/kevin30205/fastsdcpu_tool) |
| whishper_tool | Private | 0 | 2025-01-27 | 2025-06-01 | Svelte | Whishper is an open-source, 100% local audio transcription and subtitling suite with a full-featured web UI. | [🔗](https://github.com/kevin30205/whishper_tool) |
| vision-parse_tool | Private | 0 | 2025-01-27 | 2025-06-01 | Python | Vision Parse: Parse PDFs into markdown using Vision LLMs. | [🔗](https://github.com/kevin30205/vision-parse_tool) |
| marker_tool | Private | 0 | 2025-01-27 | 2025-06-01 | Python | Marker: Converting PDFs and images to markdown, JSON, and HTML quickly and accurately. | [🔗](https://github.com/kevin30205/marker_tool) |
| PyMuPDF_RAG_tool | Private | 0 | 2025-01-28 | 2025-06-01 | Python | The Tool from RAG (Retrieval-Augmented Generation) Chatbot Examples Using PyMuPDF. | [🔗](https://github.com/kevin30205/PyMuPDF_RAG_tool) |
| thefuck_tool | Private | 0 | 2025-02-06 | 2025-06-01 | Python | thefuck is the tool that corrects the previous console command. | [🔗](https://github.com/kevin30205/thefuck_tool) |
| Academic-Pages-GitHub-Pages_tool | Private | 0 | 2025-05-19 | 2025-06-01 | HTML | Academic Pages is the GitHub Pages template constructed by Jekyll. | [🔗](https://github.com/kevin30205/Academic-Pages-GitHub-Pages_tool) |

### tts

* **Total Repositories:** 2

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| fish-speech_survey | Private | 0 | 2025-06-06 | 2025-06-19 | Python | Survey of Fish Speech | [🔗](https://github.com/kevin30205/fish-speech_survey) |
| bark_survey | Private | 0 | 2025-06-05 | 2025-06-19 | Jupyter Notebook | Survey of bark (Suno) | [🔗](https://github.com/kevin30205/bark_survey) |

### x-ray

* **Total Repositories:** 3

| Name | Status | Stars | Creation Date | Last Updated | Primary Language | Description | Link |
|---|---|---|---|---|---|---|---|
| SAX-NeRF_survey | Private | 0 | 2025-04-22 | 2025-06-18 | Python | Survey of SAX-NeRF (CVPR 2024) | [🔗](https://github.com/kevin30205/SAX-NeRF_survey) |
| r2_gaussian_survey | Private | 0 | 2025-04-23 | 2025-06-18 | Python | Survey of R2 Gaussian (NeurIPS 2024) | [🔗](https://github.com/kevin30205/r2_gaussian_survey) |
| X-Gaussian_survey | Private | 0 | 2025-04-22 | 2025-06-18 | Python | Survey of X-Gaussian (ECCV 2024) | [🔗](https://github.com/kevin30205/X-Gaussian_survey) |



---


> Last auto update: 2025-06-22 09:40:59 UTC+8
