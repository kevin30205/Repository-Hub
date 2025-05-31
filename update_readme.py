# For environment variable access
import os

# For HTTP requests to GitHub API
import requests

# For timestamp formatting
from datetime import datetime

# For Counter and defaultdict
import collections
from collections import Counter

# For interactive charts
import plotly.graph_objects as go 


# Get GitHub credentials from environment variables
GITHUB_TOKEN = os.getenv('GH_PAT')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')

if not GITHUB_USERNAME:
    # Fallback: try to get username from git config (for GitHub Actions)
    import subprocess
    try:
        GITHUB_USERNAME = subprocess.check_output(['git', 'config', 'user.name'], encoding='utf-8').strip()
    
    except Exception:
        raise Exception('GITHUB_USERNAME is not set. Please set the environment variable or check workflow configuration.')


# GitHub API endpoint for listing user repositories

# this URL can only access public repos.
# API_URL = f'https://api.github.com/users/{GITHUB_USERNAME}/repos?per_page=100&type=all&sort=updated'

# this URL can access both public and private repos.
API_URL = 'https://api.github.com/user/repos?per_page=100&type=all&sort=updated'


# HTTP headers for GitHub API authentication
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Directory to store generated charts
CHARTS_DIR = 'charts'

# Ensure the charts directory exists
os.makedirs(CHARTS_DIR, exist_ok=True)
