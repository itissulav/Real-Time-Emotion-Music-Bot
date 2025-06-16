import joblib
from sentence_transformers import SentenceTransformer

# 1. Load classifier and embedding model
clf = joblib.load("models/emotion_embed_classifier.joblib")
embedder = SentenceTransformer("all-MiniLM-L6-v2")  # Or load from disk if you saved it with joblib

# 2. Predict function
def predict_emotion(text: str) -> str:
    text = text.lower().strip()
    embedding = embedder.encode([text])
    return clf.predict(embedding)[0]

# 3. Interactive test
if __name__ == "__main__":
    while True:
        text = input("Tell me about your day (or type 'exit'): ")
        if text.lower() == "exit":
            break
        emotion = predict_emotion(text)
        print("→ Predicted Emotion:", emotion)
