import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 1. Starting URL (Practice website jahan se shuru karna hai)
current_url = "https://quotes.toscrape.com"
base_url = "https://quotes.toscrape.com"

all_quotes = []
seen_quotes = set() # Duplicates se bachne ke liye

print("🚀 Data Collection Pipeline Started...")

while current_url:
    print(current_url)
    
    # Server ko request bheji page download karne ke liye
    response = requests.get(current_url)
    
    # HTML ko parse kiya BeautifulSoup se
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Is website par har quote <div class="quote"> ke andar hota hai
    quotes = soup.find_all('div', class_='quote')
    
    for q in quotes:
        # Missing Text Handling: Agar koi cheez missing ho to 'N/A' ho jaye
        text_tag = q.find('span', class_='text')
        text = text_tag.text.strip() if text_tag else "N/A"
        
        author_tag = q.find('small', class_='author')
        author = author_tag.text.strip() if author_tag else "N/A"
        
        # Duplicate Check: Agar yeh quote pehle dekh chuke hain to skip karo
        if text not in seen_quotes:
            seen_quotes.add(text)
            all_quotes.append({
                'Quote': text,
                'Author': author
            })
            
    # Pagination Handling: Next page ka button dhoondo
    next_button = soup.find('li', class_='next')
    if next_button:
        next_link = next_button.find('a')['href']
        current_url = base_url + next_link  # Naya URL ban gaya agle page ka
        time.sleep(1)  # Server par load na dalne ke liye 1 second ka gap
    else:
        current_url = None  # Agar next button nahi mila, to loop khatam

# 2. Output Dataset: Data ko DataFrame mein daal kar CSV file banao
df = pd.DataFrame(all_quotes)
df.to_csv('forum_posts.csv', index=False)

print("\n")