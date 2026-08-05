import pandas as pd
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def train():
    df = pd.read_csv("data/cleaned_data.csv")
    
    X = df['cleaned_text']
    y = df['sentiment']
    
    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)
    
    model = MultinomialNB()
    model.fit(X_vec, y)
    
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/sentiment_model.pkl")
    joblib.dump(vectorizer, "models/vectorizer.pkl")
    print("✓ Model and vectorizer saved to 'models/' directory")

if __name__ == "__main__":
    train()