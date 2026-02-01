import requests
from bs4 import BeautifulSoup
import csv

# Script: 01_book_scraper.py
# Scop: Demonstrează Web Scraping simplu și salvarea în CSV

def scrape_books():
    url = "http://books.toscrape.com/"
    print(f"--- Începem extragerea de pe {url} ---")
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Deschidem fișierul pentru scriere
            with open('rezultate_carti.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Titlu', 'Pret', 'Stoc']) # Header
                
                carti = soup.find_all("article", class_="product_pod")
                
                for carte in carti:
                    titlu = carte.find("h3").find("a")["title"]
                    pret = carte.find("p", class_="price_color").text
                    stoc = carte.find("p", class_="instock availability").text.strip()
                    
                    writer.writerow([titlu, pret, stoc])
            
            print(f"✅ Succes! Am salvat {len(carti)} cărți în 'rezultate_carti.csv'.")
        else:
            print(f"❌ Eroare la site: {response.status_code}")
            
    except Exception as e:
        print(f"❌ A apărut o eroare: {e}")

if __name__ == "__main__":
    scrape_books()