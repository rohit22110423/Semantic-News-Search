import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWSAPI_KEY")

def fetch_articles(query="technology", days=7, limit=100):
    from_date = (datetime.utcnow() - timedelta(days=days)).strftime("%Y-%m-%d")
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "from": from_date,
        "language": "en",
        "pageSize": limit,
        "sortBy": "publishedAt",
        "apiKey": API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("❌ Error fetching articles:", response.text)
        return []
    articles = response.json().get("articles", [])
    texts = [
        f"{a['title']} {a.get('description', '')} {a.get('content', '')}"
        for a in articles
    ]
    return texts
