import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils.preprocess import preprocess

# Load dataset
faq_data = pd.read_csv("data/faqs.csv")

# Preprocess all FAQ questions
faq_data["Processed"] = faq_data["Question"].apply(preprocess)

# Create TF-IDF vectors
vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(faq_data["Processed"])


def get_answer(user_question):

    processed_question = preprocess(user_question)

    user_vector = vectorizer.transform([processed_question])

    similarity_scores = cosine_similarity(user_vector, faq_vectors)

    best_match = similarity_scores.argmax()

    score = similarity_scores[0][best_match]

    if score < 0.20:
        return "Sorry, I couldn't find a matching answer."

    return faq_data.iloc[best_match]["Answer"]