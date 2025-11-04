
# 📰 Global News Tracker

## 🧭 Overview
The **Global News Tracker** is an AI-powered web application that automatically fetches trending news from **Google News**, summarizes the articles using **LLMs (Large Language Models)**, and identifies key topics using **semantic embeddings**.

It helps users quickly understand global events by presenting concise summaries and visual insights.

---

## 🌟 Features
- 🔍 **Automated News Scraping** — Fetches live news data from Google News RSS feed.
- 🧠 **AI-Powered Summarization** — Uses `facebook/bart-large-cnn` to summarize long articles into short highlights.
- 🗂️ **Topic Grouping via Embeddings** — Clusters related news headlines using sentence embeddings from `all-MiniLM-L6-v2`.
- 📊 **Visual Analytics** — Displays summaries and frequency of topics in a clean Streamlit dashboard.
- ⚡ **Backend + Frontend Integration** — FastAPI handles AI logic, Streamlit displays UI.

---

## 🧰 Tech Stack

| Component | Technology Used | Purpose |
|------------|----------------|----------|
| **Frontend** | Streamlit | Interactive dashboard UI |
| **Backend** | FastAPI | API endpoints for summarization, news fetching, and embeddings |
| **Scraping** | `feedparser` | Extracts latest articles from Google News RSS feeds |
| **Summarization Model** | `facebook/bart-large-cnn` | Summarizes lengthy news articles |
| **Embedding Model** | `all-MiniLM-L6-v2` | Converts text into vector embeddings for topic similarity |
| **Vector Operations** | `sentence-transformers` | Used for encoding and similarity search |
| **Deep Learning Framework** | `torch (PyTorch)` | Runs both summarizer and embedding models |
| **Data Handling** | `pandas` | Tabular management and cleaning of news data |
| **Visualization** | `matplotlib` / `Streamlit Charts` | Display of graphs and topic counts |

---

## 🧩 Project Architecture

```
Frontend (Streamlit)
    │
    │── Displays news, summaries, and charts
    │── Calls FastAPI endpoints
    │
Backend (FastAPI)
    │
    ├── summarizer.py → Summarizes text using BART
    ├── embeddings.py → SentenceTransformer for embeddings
    ├── fetch_news.py → RSS feed parsing with feedparser
    │
    └── API endpoints return structured JSON data
```

---

## 🧠 Models Used

| Model | Description | Source |
|--------|--------------|---------|
| `facebook/bart-large-cnn` | Pre-trained Transformer model fine-tuned for text summarization | Hugging Face |
| `all-MiniLM-L6-v2` | Lightweight embedding model for sentence similarity and topic grouping | SentenceTransformers |

---

## 🔥 Role of PyTorch
PyTorch acts as the computational backbone for the deep learning models used. It performs tensor operations, enables GPU acceleration, and powers both the summarization and embedding models.

---

## 🧩 Folder Structure
```
global-news-tracker/
│
├── backend/
│   ├── api.py             # FastAPI app with endpoints
│   ├── summarizer.py      # Summarization logic using BART
│   ├── embeddings.py      # SentenceTransformer for embeddings
│   ├── fetch_news.py      # RSS feed parsing with feedparser
│   └── __init__.py
│
├── frontend/
│   ├── news-app.py        # Streamlit frontend app
│   └── __init__.py
│
├── requirements.txt
└── README.md
```

---

## ⚠️ Issues Faced & Fixes

| Issue | Cause | Fix |
|--------|--------|-----|
| **`ImportError: cannot import name 'summarize_text'`** | Function not defined or incorrect path | Added `summarize_text()` inside `summarizer.py` and confirmed import path |
| **`NameError: name 'torch' is not defined`** | PyTorch not imported in `summarizer.py` | Added `import torch` at the top of the file |
| **Virtual Environment Confusion** | Running app outside venv caused package mismatches | Installed dependencies globally or activated venv properly before running |
| **Feedparser encoding errors** | Some RSS feeds contained special characters | Added `errors='ignore'` and ensured UTF-8 encoding |
| **Long summarization time** | Large number of news items summarized in one go | Batched summarization or limited articles per request |

---

## 💡 Future Improvements
- 🌐 Add multilingual summarization support  
- 📈 Integrate with a database (e.g., MongoDB) for storing historical trends  
- ⚙️ Add caching to reduce model reloading time  
- 🤖 Add keyword extraction using spaCy or KeyBERT  
- 📅 Automate daily summary generation  

---

## 🏁 How to Run the Project

### 1️⃣ Start Backend
```bash
cd backend
uvicorn api:app --reload
```

### 2️⃣ Start Frontend
```bash
cd frontend
streamlit run news-app.py
```

### 3️⃣ View in Browser
👉 http://localhost:8501

---

## 📦 Dependencies
```
transformers
sentence-transformers
torch
feedparser
fastapi
uvicorn
streamlit
pandas
matplotlib
```
