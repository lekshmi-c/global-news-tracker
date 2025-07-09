import requests
from bs4 import BeautifulSoup

def fetch_google_news(query="world", max_articles=10):
    query = query.replace(" ", "+")  # URL-safe query
    url = f"https://news.google.com/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = []

    for item in soup.select("article")[:max_articles]:
        headline = item.text.strip()
        link = item.find('a', href=True)
        if link:
            articles.append({
                "headline": headline,
                "url": f"https://news.google.com{link['href'][1:]}"
            })
    return articles

