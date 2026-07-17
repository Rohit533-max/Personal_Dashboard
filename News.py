import requests
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("NEWS_API")

def get_news(country):
    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "country": country,
        "apiKey": key
    }

    try:
        r = requests.get(url, params=params)
        r.raise_for_status()

        data = r.json()
        articles = data.get("articles", [])

        if not articles:
            return {"error": "No news found"}

        return {
            "articles": articles[:3]
        }

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    
print(get_news('us'))