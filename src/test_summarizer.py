from summarizer import summarize_text

sample_text = (
    "APT36 Targets Indian Government with Golang-Based DeskRAT Malware Campaign. "
    "The group has been seen sending phishing emails to government employees and "
    "exploiting recent vulnerabilities in internal systems. Researchers warn that "
    "attacks may escalate in the coming months."
)

summary = summarize_text(sample_text)
print("Summary:", summary)
