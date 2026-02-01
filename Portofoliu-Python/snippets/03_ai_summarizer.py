import requests
from bs4 import BeautifulSoup
import ollama

# Script: 03_ai_summarizer.py
# Scop: Citește o pagină web și folosește AI-ul local pentru a face un rezumat

def summarize_website(url):
    print(f"--- 1. Citesc site-ul: {url} ---")
    
    try:
        # Pasul 1: Descărcăm conținutul
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        if response.status_code != 200:
            print("❌ Nu pot accesa site-ul.")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Pasul 2: Curățăm textul
        # Luăm doar paragrafele <p>, ignorăm meniurile și reclamele
        paragrafe = soup.find_all('p')
        text_curat = " ".join([p.text for p in paragrafe])
        
        # IMPORTANT: Tăiem textul dacă e prea lung (pentru viteză)
        # Luăm primele 3000 de caractere
        text_curat = text_curat[:3000]
        
        if len(text_curat) < 100:
            print("❌ Site-ul are prea puțin text pentru a fi rezumat.")
            return

        print("--- 2. Trimit textul la AI (Gândește...) ---")
        
        # Pasul 3: Discutăm cu Ollama
        prompt = f"""
        Citește următorul text și fă un rezumat scurt, în limba română, de maxim 3 idei principale (bullet points).
        
        TEXT:
        {text_curat}
        """
        
        rezultat = ollama.chat(model='llama3.2', messages=[
            {'role': 'user', 'content': prompt}
        ])
        
        # Pasul 4: Afișăm rezultatul
        print("\n📝 REZUMAT GENERAT DE AI:\n")
        print(rezultat['message']['content'])
        print("\n---------------------------------")

    except Exception as e:
        print(f"❌ Eroare: {e}")

if __name__ == "__main__":
    # Testăm pe o pagină Wikipedia (sau orice articol de știri)
    link = "https://ro.wikipedia.org/wiki/Inteligen%C8%9B%C4%83_artificial%C4%83"
    summarize_website(link)