import pandas as pd
import re
import os

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()  # Lowercasing
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove punctuation & numbers
    text = re.sub(r'\s+', ' ', text)  # Remove multiple spaces
    return text.strip()

def clean_dataset():
    if not os.path.exists("data/raw_data.csv"):
        print("Raw data file not found!")
        return

    df = pd.read_csv("data/raw_data.csv")
    df['cleaned_text'] = df['text'].apply(clean_text)
    
    # Drop empty cleaned rows if any
    df = df[df['cleaned_text'] != ""]
    
    df.to_csv("data/cleaned_data.csv", index=False)
    print(f"✓ Cleaned {len(df)} records and saved to 'data/cleaned_data.csv'")

if __name__ == "__main__":
    clean_dataset()