from transformers import pipeline

def summarize_text(text):
    # Load summarization pipeline
    ActualText = text
    summarizer = pipeline("summarization")
    
    # Generate summary
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    
    # Extract summarized text
    return summary[0]['summary_text']
