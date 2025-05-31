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


def fetch_repos():
    """
    Fetch all repositories for the user, handling pagination.
    Returns a list of repository dicts.
    """

    # List to store all repositories
    repos = []

    # Start from page 1
    page = 1

    # Loop through pages until no more repositories are returned
    while True:
        # Request one page of repositories
        resp = requests.get(f'{API_URL}&page={page}', headers=HEADERS)
        
        # Check for HTTP errors
        if resp.status_code != 200:
            raise Exception(f'GitHub API error: {resp.status_code} {resp.text}')
        
        # Parse the JSON response
        data = resp.json()
        
        # If no data is returned, we have reached the end of the list
        if not data:
            break  # No more repos
        
        # Extend the repos list with the current page of data
        repos.extend(data)

        # Next page
        page += 1
    
    return repos


def project_statistics(repos):
    """
    Return a summary of total, public, and private repo counts.
    """

    # Count total, public, and private repositories
    total = len(repos)
    public = sum(1 for r in repos if not r.get('private', False))
    private = sum(1 for r in repos if r.get('private', False))

    table = (
        f'| Type   | Count |\n'
        f'|--------|-------|\n'
        f'| Total  | {total} |\n'
        f'| Public | {public} |\n'
        f'| Private| {private} |\n'
    )
    return table


def language_statistics(repos):
    """
    Generate a markdown table of programming language statistics for all repositories.
    """

    # Count each programming language used in the repositories
    lang_count = collections.Counter()

    # Iterate through each repository and count languages
    for repo in repos:
        lang = repo.get('language') or 'Unknown'
        lang_count[lang] += 1
    
    # Calculate total count for percentage calculation
    total = sum(lang_count.values())

    # Markdown table header
    table = '| Language | Count | Percentage |\n|---|---|---|\n'
    for lang, count in lang_count.most_common():
        percent = f"{count/total*100:.1f}%"
        table += f'| {lang} | {count} | {percent} |\n'

    return table


def plotly_language_pie(repos):
    """
    Generate a programming language distribution pie chart (interactive HTML + PNG).
    """

    # Count each programming language used in the repositories
    lang_count = Counter(repo.get('language') or 'Unknown' for repo in repos)

    # zip the labels and values for the pie chart
    labels, values = zip(*lang_count.items())

    # Create pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    
    # Update layout for the pie chart
    fig.update_layout(
        title_text='Language Distribution',
        template='plotly_dark',
        paper_bgcolor='#181c20',
        plot_bgcolor='#181c20',
        font=dict(color='#e0e0e0'),
        margin=dict(l=40, r=40, t=60, b=40)
    )

    # Save the pie chart as HTML and PNG
    fig.write_html(os.path.join(CHARTS_DIR, 'language_pie.html'))
    fig.write_image(os.path.join(CHARTS_DIR, 'language_pie.png'))


def categorize_repos(repos):
    """
    Categorize repositories by their topics. Repos without topics are grouped as 'Unassigned'.

    Returns a dict: {topic: [repo, ...]}
    """

    # Use defaultdict to group repositories by topics
    categories = collections.defaultdict(list)

    # Iterate through each repository and categorize by topics
    for repo in repos:
        
        # Get the topics for the repository, default to an empty list if not set
        topics = repo.get('topics', [])

        if topics:
            for topic in topics:
                categories[topic].append(repo)
        else:
            categories['Unassigned'].append(repo)

    return categories


def generate_categorized_table(categories):
    """
    Generate a markdown table for each category (topic), listing repo info, sorted by category name (A-Z),
    and show the count of repos in each category.
    """

    # initialize markdown content
    md = ''

    # Iterate through each category and generate a markdown table
    # Sort categories alphabetically
    for cat in sorted(categories.keys()):
        
        repos = categories[cat]

        # Show count in heading
        md += f'### {cat} ({len(repos)})\n\n'

        # Table header
        md += '| Name | Status | Stars | Last Updated | Description | Link |\n'
        md += '|---|---|---|---|---|---|\n'

        # Iterate through each repository in the category
        # the repos are sorted by last updated time in descending order by default
        for repo in repos:
            name = repo['name']

            private = 'Private' if repo['private'] else 'Public'
            
            stars = repo['stargazers_count']

            updated = repo['updated_at'][:10]

            desc = repo['description'] or ''

            url = repo['html_url']

            # update the markdown table with repo info
            md += f'| {name} | {private} | {stars} | {updated} | {desc} | [🔗]({url}) |\n'

        # Add a newline at the end for better formatting
        md += '\n'
    
    return md

