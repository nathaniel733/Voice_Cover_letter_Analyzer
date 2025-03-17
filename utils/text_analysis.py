import language_tool_python
from nltk.tokenize import word_tokenize
from rake_nltk import Rake
from nltk.corpus import words
from rake_nltk import Rake
import spacy
import nltk
nltk.download('stopwords')
nltk.download('punkt_tab')

def analyze_text(text):
    # Initialize LanguageTool for grammar checking
    tool = language_tool_python.LanguageTool('en-US')

    # Grammar check
    matches = tool.check(text)
    grammar_score = max(0, 100 - len(matches))

    # Vocabulary analysis
    english_vocab = set(words.words())
    word_tokens = word_tokenize(text)
    vocab_count = sum(1 for word in word_tokens if word.lower() in english_vocab)
    vocab_score = (vocab_count / len(word_tokens)) * 100 if word_tokens else 0

    # Fluency scoring
    word_count = len(text.split())
    audio_duration = 180  # Placeholder duration, replace dynamically if possible
    words_per_minute = (word_count / audio_duration) * 60
    if words_per_minute > 120:
        fluency_score = 100
    elif words_per_minute > 80:
        fluency_score = 80
    else:
        fluency_score = 60

    # Key phrase extraction
    rake = Rake()
    rake.extract_keywords_from_text(text)
    key_phrases = rake.get_ranked_phrases()[:5]  # List of key phrases

    # Overall score
    overall_score = (grammar_score + vocab_score + fluency_score) / 3

    return {
        "Grammar Score": grammar_score,
        "Vocabulary Score": vocab_score,
        "Fluency Score": fluency_score,
        "Overall Score": overall_score
    }, key_phrases
