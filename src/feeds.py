import feedparser
import json
import os
from datetime import datetime

def load_feeds():
    script_dir = os.path.dirname(os.path.abspath(__file__))  # src folder
    data_file = os.path.join(script_dir, "../data/feeds.json")
    
    with open(data_file, "r") as f:
        data = json.load(f)
    return data["feeds"]

def fetch_feed_entries(url):
    feed = feedparser.parse(url)
    return [{
        "title": entry.title,
        "link": entry.link,
        "published": entry.get("published", "N/A"),
        "summary": entry.get("summary", ""),
        "source": feed.feed.get("title", url)
    } for entry in feed.entries]

def collect_all_feeds():
    feeds = load_feeds()
    all_entries = []
    for url in feeds:
        print(f"[+] Fetching from {url}")
        try:
            entries = fetch_feed_entries(url)
            all_entries.extend(entries)
        except Exception as e:
            print(f"[-] Error fetching {url}: {e}")
    return all_entries

if __name__ == "__main__":
    entries = collect_all_feeds()
    print(f"\n✅ Collected {len(entries)} total news articles at {datetime.now()}")
    for item in entries[:5]:
        print(f"- {item['title']} ({item['source']})")
