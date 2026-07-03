import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Load English stopwords
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove punctuation and stopwords
    cleaned_tokens = []

    for word in tokens:
        if word not in string.punctuation and word not in stop_words:
            cleaned_tokens.append(word)

    return " ".join(cleaned_tokens)