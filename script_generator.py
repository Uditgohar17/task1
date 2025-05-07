from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_script(article):
    summary = summarizer(article, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    return f"Here's the news update: {summary}"