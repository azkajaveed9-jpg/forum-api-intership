# Basic Sentiment Pipeline

## Overview
An end-to-end sentiment analysis pipeline that scrapes data, cleans text, trains a Naive Bayes model, and generates evaluation metrics along with a confusion matrix visual.

## Deliverables
- `data/raw_data.csv` & `data/cleaned_data.csv`: Scraped and processed dataset
- `models/sentiment_model.pkl` & `models/vectorizer.pkl`: Trained model files
- `reports/evaluation_report.txt`: Classification metrics report
- `reports/confusion_matrix.png`: Confusion Matrix heatmap plot

## How to Run
1. Activate virtual environment:
   ```bash
   .\venv\Scripts\activate