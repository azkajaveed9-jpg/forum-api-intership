import pandas as pd
import random
import os

def scrape_data():
    templates = {
        "positive": [
            "This product is absolute quality! Loved it completely.",
            "Great support, excellent features, and super fast delivery!",
            "Highly recommended! Worth every single penny.",
            "Fantastic user experience, smooth performance overall.",
            "Top notch build quality! Exceeded my expectations.",
            "Amazing results! Will definitely purchase again.",
            "Superb performance and outstanding design."
        ],
        "negative": [
            "Worst service ever. Very disappointed and angry.",
            "Horrible product, broke in just one single day.",
            "Terrible customer support, complete waste of money.",
            "Poor quality materials. Do not buy this product!",
            "Extremely slow and buggy experience. Very frustrating.",
            "Defective item delivered. Returning it immediately.",
            "Unsatisfactory experience, totally useless product."
        ],
        "neutral": [
            "It is okay, normal experience overall.",
            "Decent product for this price range.",
            "Average performance. Nothing special to mention.",
            "It works fine, but could be improved slightly.",
            "Standard delivery speed. Product is reasonable.",
            "Acceptable product, meets minimal basic needs.",
            "Fair experience. Neither great nor too bad."
        ]
    }
    
    data = []
    review_id = 1001
    
    # Generate 120 detailed sample reviews
    for _ in range(40):
        for sentiment, reviews in templates.items():
            text = random.choice(reviews)
            # Add noise for cleaner testing
            if random.random() > 0.5:
                text = f"  {text.upper()} !!! "
            data.append({"review_id": review_id, "text": text, "sentiment": sentiment})
            review_id += 1
            
    df = pd.DataFrame(data)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/raw_data.csv", index=False)
    print(f"✓ Scraped and generated {len(df)} raw sentiment records in 'data/raw_data.csv'")

if __name__ == "__main__":
    scrape_data()