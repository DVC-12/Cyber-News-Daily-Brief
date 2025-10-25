# Cyber News Daily Brief

## Overview

**Cyber News Daily Brief** is a Python project that automatically collects, summarizes, and formats the latest cybersecurity news from multiple sources. It generates a clean Markdown report containing:

- Headlines
- Sources
- Article links
- Concise summaries (3 sentences max)
- Table of Contents for easy navigation

This project runs fully offline on Windows and uses a local NLP model for summarization.

---

## Features

- Collects news from multiple sources (The Hacker News, BleepingComputer, KrebsOnSecurity, DarkReading, CISA)
- Summarizes articles using Hugging Face Transformers
- Generates a professional Markdown report
- Optional limit on the number of articles per daily brief
- Fully local, no cloud API required

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/YourUsername/cyber-news-daily-brief.git
cd cyber-news-daily-brief
Install dependencies

Make sure you have Python 3.13+ installed. Then run:

pip install -r requirements.txt


requirements.txt should include:

transformers
torch
feedparser


Markdown2 and WeasyPrint are optional. If you only want Markdown reports, you don’t need WeasyPrint.

Usage

Make sure feeds.json in the data/ folder contains your RSS feed URLs. Example:

[
    {
        "name": "The Hacker News",
        "url": "https://thehackernews.com/feeds/posts/default"
    },
    {
        "name": "BleepingComputer",
        "url": "https://www.bleepingcomputer.com/feed/"
    }
]


Run the script:

python src/main.py


The daily brief Markdown report will be saved in the reports/ folder:

reports/Cyber_News_Brief_YYYY-MM-DD.md

