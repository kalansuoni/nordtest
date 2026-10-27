from operator import itemgetter

import requests
import plotly.express as px

# Make an API call and check the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:30]:
    url = (
        f'https://hacker-news.firebaseio.com/v0/item/'
        f'{submission_id}.json'
    )

    r = requests.get(url)
    response_dict = r.json()

    try:
        comments = response_dict['descendants']
        title = response_dict['title']
        hn_link = (
            f"https://news.ycombinator.com/item?id={submission_id}"
        )

        submission_dict = {
            'title': title,
            'comments': comments,
            'link': hn_link,
        }
        submission_dicts.append(submission_dict)

    except KeyError:
        # Skip promotional posts and other items
        continue

submission_dicts = sorted(
    submission_dicts,
    key=itemgetter('comments'),
    reverse=True
)

titles, comments, hover_texts = [], [], []

for submission_dict in submission_dicts:
    title_link = (
        f"<a href='{submission_dict['link']}'>{submission_dict['title']}</a>"
    )

    titles.append(title_link)
    comments.append(submission_dict['comments'])
    hover_texts.append(
        f"Comments: {submission_dict['comments']}"
    )

fig = px.bar(
    x=titles,
    y=comments,
    title='Most Active Hacker News Discussions',
    labels={
        'x': 'Discussion',
        'y': 'Number of Comments'
    }
)

fig.update_traces(
    hovertext=hover_texts,
    hovertemplate='%{hovertext}<extra></extra>'
)

fig.update_layout(
    title_font_size=28,
    xaxis_title='Discussion',
    yaxis_title='Comments'
)

fig.show()