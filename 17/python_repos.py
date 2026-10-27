import requests
import plotly.express as px

# Change the language here
url = 'https://api.github.com/search/repositories'
url += '?q=language:javascript+sort:stars+stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

response_dict = r.json()

repo_dicts = response_dict['items']

repo_names = []
stars = []
hover_texts = []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    hover_text = (
        f"Owner: {repo_dict['owner']['login']}<br />"
        f"Description: {repo_dict['description']}"
    )
    hover_texts.append(hover_text)

title = 'Most-Starred JavaScript Projects on GitHub'

fig = px.bar(
    x=repo_names,
    y=stars,
    title=title,
    labels={'x': 'Repository', 'y': 'Stars'},
)

fig.update_traces(
    hovertext=hover_texts,
    hovertemplate='%{hovertext}<extra></extra>'
)

fig.show()