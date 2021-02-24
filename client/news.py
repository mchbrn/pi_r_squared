import json
import requests

articles = 7

# Get most recent top headlines from BBC News
news = requests.get("http://newsapi.org/v2/top-headlines?", params={"sources": "bbc-news", "sortBy": "publishedAt", "pageSize": articles, "apiKey": "fdb4afeed23d42219491564bb280c362"})

data = json.loads(news.text)

for x in range(0, articles):
    print(data['articles'][x]['title'])
