from transformers import pipeline

MODEL_NAME = "sshleifer/distilbart-cnn-12-6"

summarizer = pipeline(
    "summarization",
    model=MODEL_NAME,
    tokenizer=MODEL_NAME,
    device=-1  # CPU
)

def summarize_text(text, max_tokens=80):
    """
    Summarize input text concisely and suppress Hugging Face warnings.
    """
    # If input is shorter than max_tokens, set max_len = input length + 5
    input_len = len(text.split())
    max_len = min(max_tokens, input_len + 5)

    summary = summarizer(
        text,
        max_length=max_len,
        min_length=20,
        do_sample=False,
        truncation=True  # suppress warning
    )
    return summary[0]["summary_text"].strip()
