import requests
import os
from dotenv import dotenv_values,load_dotenv

load_dotenv()
key = os.getenv("NEWS_API")

def get_news():
    try:
        country = input("Enter Country name: ")
        url = "https://newsapi.org/v2/top-headlines"
        p = {'country': country,'apiKey':key}
        r = requests.get(url,params=p)
        r.raise_for_status()
        data = r.json()
        articles = data['articles']
        if len(articles)==0:
            print("No News found")
            return
        print("\n================Top 3 News===============")
        for i, article in enumerate(articles[:3], start=1):
            print(f"\nNews {i}")
            print("-" * 30)
            print("Title:", article["title"])
            print("Author:", article["author"])
            print("Description:", article["description"])
            print("Source:", article["source"]["name"])
            print("URL:", article["url"])
    except requests.exceptions.RequestException as e:
        print("Error",e)

get_news()