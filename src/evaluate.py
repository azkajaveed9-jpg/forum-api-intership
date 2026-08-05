import pandas as pd
import numpy as np
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_recall_fscore_support

def evaluate_model():
    df = pd.read_csv("data/cleaned_data.csv")
    model = joblib.load("models/sentiment_model.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")
    
    X_vec = vectorizer.transform(df['cleaned_text'])
    predictions = model.predict(X_vec)
    probabilities = model.predict_proba(X_vec)
    confidence_scores = np.max(probabilities, axis=1)
    
    # Calculate global metrics
    acc = accuracy_score(df['sentiment'], predictions)
    prec, rec, f1, _ = precision_recall_fscore_support(df['sentiment'], predictions, average='macro')
    
    labels = sorted(df['sentiment'].unique())
    cm = confusion_matrix(df['sentiment'], predictions, labels=labels)
    report_text = classification_report(df['sentiment'], predictions)
    
    os.makedirs("reports", exist_ok=True)
    
    # 1. Generate text evaluation report matching the image format
    with open("reports/evaluation_report.txt", "w") as f:
        f.write(f"Accuracy  : {acc:.4f}\n")
        f.write(f"Precision : {prec:.4f}\n")
        f.write(f"Recall    : {rec:.4f}\n")
        f.write(f"F1 Score  : {f1:.4f}\n\n")
        f.write("=" * 60 + "\n")
        f.write("CLASSIFICATION REPORT\n")
        f.write("=" * 60 + "\n\n")
        f.write(report_text)
        f.write("\n" + "=" * 60 + "\n")
        f.write("CONFUSION MATRIX\n")
        f.write("=" * 60 + "\n\n")
        f.write(str(cm) + "\n")
        
    # 2. Save PNG Confusion Matrix plot
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.tight_layout()
    plt.savefig("reports/confusion_matrix.png")
    plt.close()
    
    # 3. Create Final Output Dataset (Post-prediction Statistics table)
    df['actual_sentiment'] = df['sentiment']
    df['predicted_sentiment'] = predictions
    df['confidence'] = np.round(confidence_scores, 4)
    
    # Save formatted predictions CSV
    df_output = df[['text', 'actual_sentiment', 'predicted_sentiment', 'confidence']]
    df_output.to_csv("data/output_predictions.csv", index=False)
    
    print("✓ Full Evaluation Report, Confusion Matrix, and Output Dataset generated successfully!")

if __name__ == "__main__":
    evaluate_model()