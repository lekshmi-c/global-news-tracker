from fastapi import FastAPI
from backend.news_scraper import fetch_google_news
from backend.summarizer import summarize_text

app = FastAPI()

@app.get("/summarized-news/")
def get_news_summary():
    articles = fetch_google_news()
    summarized_articles = [
        {"headline": a["headline"], "summary": summarize_text(a["headline"])}
        for a in articles
    ]
    return summarized_articles
