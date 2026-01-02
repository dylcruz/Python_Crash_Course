from operator import itemgetter
import requests
import plotly.express as px

# Make an API call, and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Make a new API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article
    try:
        hn_link = f"https://news.ycombinator.com/item?id={submission_id}" 
        title = response_dict['title']
        chart_link = f"<a href='{hn_link}'>{title}</a>"
        submission_dict = {
            'title': title,
            'hn_link': hn_link,
            'comments': response_dict['descendants'],
            'chart_link': chart_link,
        }
    except KeyError:
        print(f"Missing descendants for post: {response_dict['title']}")
        continue
    submission_dicts.append(submission_dict)

fig = px.bar(
    x=[sub_dict['chart_link'] for sub_dict in submission_dicts],
    y=[sub_dict['comments'] for sub_dict in submission_dicts],
    labels={"x": "Post", "y": "Comments"},
    title='Comments on Hacker-News Current Top Posts'
)

fig.show()