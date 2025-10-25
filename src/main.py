import os
from datetime import datetime
from feeds import collect_all_feeds
from summarizer import summarize_text

# -----------------------------
# CONFIG
# -----------------------------
REPORTS_DIR = os.path.join("..", "reports")
if not os.path.exists(REPORTS_DIR):
    os.makedirs(REPORTS_DIR)

MAX_ARTICLES = 20  # Limit articles per daily brief

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def create_markdown_report(articles):
    today = datetime.now().strftime("%Y-%m-%d")
    generated_time = datetime.now().strftime("%H:%M:%S")

    md_content = f"# Cyber News Daily Brief - {today}\n"
    md_content += f"*Generated at {generated_time}*\n\n"

    # Table of contents
    md_content += "### Table of Contents\n"
    for idx, article in enumerate(articles[:MAX_ARTICLES], 1):
        safe_title = article['title'].replace("[", "").replace("]", "")
        md_content += f"{idx}. [{safe_title}](#{idx})\n"
    md_content += "\n---\n\n"

    # Article sections
    for idx, article in enumerate(articles[:MAX_ARTICLES], 1):
        title = article['title']
        link = article['link']
        source = article['source']
        summary = summarize_text(article['summary'])

        # Trim summary to 3 sentences max
        sentences = summary.split('. ')
        summary = '. '.join(sentences[:3]).strip()
        if not summary.endswith('.'):
            summary += '.'

        md_content += f"## {idx}. [{title}]({link})\n"
        md_content += f"*Source: {source}*\n\n"
        md_content += f"> {summary}\n\n"
        md_content += "---\n\n"

    return md_content, today

def save_markdown(md_content, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(md_content)

# -----------------------------
# MAIN FUNCTION
# -----------------------------
def generate_daily_brief():
    print("[*] Collecting news feeds...")
    articles = collect_all_feeds()
    print(f"[+] Total articles collected: {len(articles)}\n")

    md_content, today = create_markdown_report(articles)
    md_filename = os.path.join(REPORTS_DIR, f"Cyber_News_Brief_{today}.md")
    save_markdown(md_content, md_filename)

    print(f"\n✅ Daily brief saved as Markdown: {md_filename}")

# -----------------------------
# RUN SCRIPT
# -----------------------------
if __name__ == "__main__":
    generate_daily_brief()
