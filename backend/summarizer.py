from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# def summarize_text(text, max_length=100):
#     return summarizer(text, max_length=max_length, min_length=30, do_sample=False)[0]['summary_text']

def summarize_text(text):
    input_length = len(text.split())
    max_len = min(50, input_length)  # or 2 * input_length
    min_len = max(5, input_length // 2)

    try:
        summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"[Summarization error: {str(e)}]"