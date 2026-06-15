from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

items = {
    "Titanic": "romance drama ship",
    "Inception": "sci-fi thriller dream",
    "Avatar": "sci-fi fantasy alien",
    "The Notebook": "romance drama love",
    "Interstellar": "sci-fi space adventure"
}

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(items.values())

def recommend(item_name, top_n=2):
    if item_name not in items:
        return f"Item '{item_name}' not found."
    idx = list(items.keys()).index(item_name)
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    similar_indices = cosine_sim.argsort()[-top_n-1:-1][::-1]
    recommendations = [list(items.keys())[i] for i in similar_indices]
    return recommendations

if __name__ == "__main__":
    print("Recommendations for Titanic:", recommend("Titanic"))
    print("Recommendations for Inception:", recommend("Inception"))
