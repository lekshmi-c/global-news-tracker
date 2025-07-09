# Global News Topic Tracker

This app fetches trending topics from Google News and summarizes them using a large language model (LLM).

## Features
- News scraping using BeautifulSoup
- Summarization using Hugging Face Transformers (BART model)
- FastAPI as backend
- Streamlit as frontend

## Installation

```bash
pip install -r requirements.txt
```

## Run FastAPI

```bash
uvicorn backend.main:app --reload
```

## Run Streamlit

```bash
streamlit run frontend/news-app.py
```