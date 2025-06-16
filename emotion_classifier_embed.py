import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sentence_transformers import SentenceTransformer
import joblib

# 1. Load dataset
df = pd.read_csv("data/emotion_dataset_expanded.csv")

# 2. Preprocess
df['processed_text'] = df['text'].str.lower()

# 3. Split
X_train, X_test, y_train, y_test = train_test_split(
    df['processed_text'], df['emotion'], test_size=0.2, random_state=42
)

# 4. Load sentence transformer
model = SentenceTransformer('all-MiniLM-L6-v2')

# 5. Get embeddings
X_train_embed = model.encode(X_train.tolist(), show_progress_bar=True)
X_test_embed = model.encode(X_test.tolist(), show_progress_bar=True)

# 6. Train classifier
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train_embed, y_train)

# 7. Evaluate
y_pred = clf.predict(X_test_embed)
print(classification_report(y_test, y_pred))

# 8. Save classifier and embedding model
joblib.dump(clf, "models/emotion_embed_classifier.joblib")
joblib.dump(model, "models/sentence_embedding_model.joblib")
