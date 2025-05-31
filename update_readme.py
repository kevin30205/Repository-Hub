# For environment variable access
import os

# For HTTP requests to GitHub API
import requests

# For timestamp formatting
from datetime import datetime, timezone, timedelta

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
    fig.write_image(os.path.join(CHARTS_DIR, 'language_pie.png'), width=1200, height=800)


def plotly_star_bar(repos):
    """
    Generate a bar chart for top 10 repos by star count (interactive HTML + PNG).
    """

    # Sort repositories by star count and take the top 10
    sorted_repos = sorted(repos, key=lambda r: r['stargazers_count'], reverse=True)[:10]

    # Prepare data for the bar chart
    names = [repo['name'] for repo in sorted_repos]
    stars = [repo['stargazers_count'] for repo in sorted_repos]

    # Create horizontal bar chart
    fig = go.Figure([go.Bar(x=stars[::-1], y=names[::-1], orientation='h', marker_color='#4e8cff')])
    
    # Update layout for the bar chart
    fig.update_layout(
        title_text='Top 10 Repositories by Stars',
        xaxis_title='Stars',
        yaxis_title='Repository',
        template='plotly_dark',
        paper_bgcolor='#181c20',
        plot_bgcolor='#181c20',
        font=dict(color='#e0e0e0'),
        margin=dict(l=60, r=40, t=60, b=40),
        xaxis=dict(range=[0, max(stars) * 1.1 if stars else 1], zeroline=True, zerolinecolor='#888')
    )

    # Save the bar chart as HTML and PNG
    fig.write_html(os.path.join(CHARTS_DIR, 'star_bar.html'))
    fig.write_image(os.path.join(CHARTS_DIR, 'star_bar.png'), width=1200, height=800)


def plotly_repo_time_line(repos):
    """
    Generate a line chart showing cumulative repo count over time (interactive HTML + PNG).
    """

    # Extract creation dates and count occurrences
    dates = [repo['created_at'][:10] for repo in repos]
    date_count = Counter(dates)
    sorted_dates = sorted(date_count.items())
    x = [d for d, _ in sorted_dates]
    y = [c for _, c in sorted_dates]
    
    y_cum = []
    total = 0
    
    # Calculate cumulative counts
    for v in y:
        total += v
        y_cum.append(total)
    
    # Create line chart
    fig = go.Figure([go.Scatter(x=x, y=y_cum, mode='lines+markers', line=dict(color='#4e8cff'))])
    
    # Update layout for the line chart
    fig.update_layout(
        title_text='Repository Count Over Time',
        xaxis_title='Date',
        yaxis_title='Cumulative Repo Count',
        template='plotly_dark',
        paper_bgcolor='#181c20',
        plot_bgcolor='#181c20',
        font=dict(color='#e0e0e0'),
        margin=dict(l=60, r=40, t=60, b=40),
        yaxis=dict(range=[0, max(y_cum) * 1.1 if y_cum else 1], zeroline=True, zerolinecolor='#888')
    )

    # Save the line chart as HTML and PNG
    fig.write_html(os.path.join(CHARTS_DIR, 'repo_timeline.html'))
    fig.write_image(os.path.join(CHARTS_DIR, 'repo_timeline.png'), width=1200, height=800)


def plotly_topic_bar(repos):
    """
    Generate a bar chart for top 10 topics by repo count (interactive HTML + PNG).
    """

    # Count occurrences of each topic across all repositories
    topic_count = Counter()
    
    # Iterate through each repository and count topics
    for repo in repos:
        topics = repo.get('topics', [])
        
        if topics:
            for t in topics:
                topic_count[t] += 1
        
        else:
            topic_count['Unassigned'] += 1
    
    # If no topics are found, return early
    if not topic_count:
        return
    
    # Get the top 10 topics and their counts
    topics, counts = zip(*topic_count.most_common(10))
    
    # Create horizontal bar chart
    fig = go.Figure([go.Bar(x=counts[::-1], y=topics[::-1], orientation='h', marker_color='#4e8cff')])
    
    # Update layout for the bar chart
    fig.update_layout(
        title_text='Top 10 Topics by Repository Count',
        xaxis_title='Repository Count',
        yaxis_title='Topic',
        template='plotly_dark',
        paper_bgcolor='#181c20',
        plot_bgcolor='#181c20',
        font=dict(color='#e0e0e0'),
        margin=dict(l=60, r=40, t=60, b=40),
        xaxis=dict(range=[0, max(counts) * 1.1 if counts else 1], zeroline=True, zerolinecolor='#888')
    )

    # Save the bar chart as HTML and PNG
    fig.write_html(os.path.join(CHARTS_DIR, 'topic_bar.html'))
    fig.write_image(os.path.join(CHARTS_DIR, 'topic_bar.png'), width=1200, height=800)


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


def update_readme(repo_stats_table, lang_table, cat_table):
    """
    Update the README.md file with the latest statistics, charts, and categorized repo list.
    """

    # Read the existing README content
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the section to update
    start = content.find('## GitHub Repository Dashboard')

    # If the section is not found, raise an exception
    if start == -1:
        raise Exception('README.md missing "## GitHub Repository Dashboard" heading')
    
    # Split the content to insert new statistics and charts
    # before: the content before the section
    # after: the content after the section, including the first '---' line
    # the first '---' ensures that the new content is inserted below '---'
    before = content[:start]
    after = content[start:]
    after = after.split('---')[0] + '---\n\n'
    
    # Compose new README content with updated chart paths
    new_content = (
        
        # existing content before the section
        before + after +

        # repository statistics table
        '### Repository Information Overview\n\n' + repo_stats_table + '\n' +

        # programming language statistics table
        '### Language Distribution Overview\n\n' + lang_table + '\n' +
        
        # language distribution pie chart
        '![Language Distribution Overview](charts/language_pie.png)\n\n' +
        
        # star bar chart
        '### Top 10 Repositories by Star Count\n\n' +

        '![Top 10 Repositories by Star Count](charts/star_bar.png)\n\n' +
        
        # repository count over time line chart
        '### Repository Creation Trend\n\n' +
        
        '![Repository Creation Trend](charts/repo_timeline.png)\n\n' +

        # top 10 topics by repository count bar chart
        '### Top 10 Topics by Repository Count\n\n' +
        
        '![Top 10 Topics by Repository Count](charts/topic_bar.png)\n\n' +

        '### Categorized Repository Index\n\n' + cat_table +
        
        f'\n> Last auto update: {datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S UTC+8")}\n'
    )

    # Write updated content to README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)


def main():
    """
    Main entry: fetch repo data, generate stats, charts, and update README.
    """

    # Fetch all repositories
    repos = fetch_repos()

    # Generate project statistics table
    stats_table = project_statistics(repos)

    # Generate language statistics table
    lang_table = language_statistics(repos)
    
    # Categorize repositories by topic
    categories = categorize_repos(repos)
    
    # Generate categorized repo markdown tables
    cat_table = generate_categorized_table(categories)
    
    # Generate all charts (interactive HTML + PNG)
    plotly_language_pie(repos)
    plotly_star_bar(repos)
    plotly_repo_time_line(repos)
    plotly_topic_bar(repos)
    
    # Update README with all generated content
    update_readme(
        repo_stats_table=stats_table,
        lang_table=lang_table,
        cat_table=cat_table
    )


if __name__ == '__main__':
    # Script entry point
    main()

