import json
import requests

def get():
    articles = 7

    # Get most recent top headlines from BBC News
    news = requests.get("http://newsapi.org/v2/top-headlines?", params={"sources": "bbc-news", "sortBy": "publishedAt", "pageSize": articles, "apiKey": "fdb4afeed23d42219491564bb280c362"})

    data = json.loads(news.text)

    todays_news = []

    for x in range(0, articles):
        todays_news.append(data['articles'][x]['title'])

    return todays_news
