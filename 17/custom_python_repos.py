import requests
import plotly.express as px

# Make API call.
url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

print(f"Status code: {r.status_code}")

response_dict = r.json()
repo_dicts = response_dict['items']

repo_links = []
stars = []
hover_texts = []

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']

    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']

    hover_text = (
        f"Owner: {owner}<br />"
        f"Stars: {repo_dict['stargazers_count']}<br />"
        f"Description: {description}"
    )

    hover_texts.append(hover_text)

# Create chart.
title = 'Most-Starred Python Projects on GitHub'

fig = px.bar(
    x=repo_links,
    y=stars,
    title=title,
    labels={
        'x': 'Repository',
        'y': 'Stars'
    },
    color=stars,
    color_continuous_scale='Viridis'
)

fig.update_traces(
    hovertext=hover_texts,
    hovertemplate='%{hovertext}<extra></extra>'
)

fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20,
)

fig.show()