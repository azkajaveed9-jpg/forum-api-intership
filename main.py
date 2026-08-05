from src.scraper import scrape_data
from src.cleaner import clean_dataset
from src.train_model import train
from src.evaluate import evaluate_model

def run_pipeline():
    print("--- STARTING SENTIMENT PIPELINE ---")
    scrape_data()
    clean_dataset()
    train()
    evaluate_model()
    print("\n✓ ALL STEPS COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    run_pipeline()