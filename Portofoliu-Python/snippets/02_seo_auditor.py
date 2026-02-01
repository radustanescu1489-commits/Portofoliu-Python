import requests
from bs4 import BeautifulSoup

# Script: 02_seo_auditor.py
# Scop: Analizează o pagină web pentru elemente esențiale SEO (Search Engine Optimization)

def audit_seo(url):
    print(f"🔍 Încep analiza pentru: {url} ...\n")
    
    try:
        # Folosim un User-Agent ca să părem un browser real, nu un robot
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"❌ Eroare: Nu pot accesa site-ul (Cod {response.status_code})")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 1. Verificăm Titlul Paginii (<title>)
        # Este cel mai important element pentru Google
        if soup.title:
            print(f"✅ TITLU GĂSIT: {soup.title.string.strip()}")
            print(f"   Lungime: {len(soup.title.string)} caractere (Ideal: 50-60)")
        else:
            print("❌ TITLU LIPSA! (Grav pentru SEO)")

        # 2. Verificăm Meta Descrierea
        # Este textul care apare sub link în Google
        meta_desc = soup.find("meta", attrs={"name": "description"})
        if meta_desc and meta_desc.get("content"):
            desc_content = meta_desc["content"]
            print(f"✅ DESCRIERE GĂSITĂ: {desc_content[:50]}...") # Arătăm doar primele 50 caractere
        else:
            print("⚠️ DESCRIERE LIPSA! (Site-ul va avea CTR mic)")

        # 3. Verificăm H1 (Titlul principal din pagină)
        # Trebuie să existe un singur H1 pe pagină
        h1_tags = soup.find_all("h1")
        if len(h1_tags) == 1:
            print(f"✅ H1 CORECT: {h1_tags[0].text.strip()}")
        elif len(h1_tags) == 0:
            print("❌ H1 LIPSA! (Google nu înțelege despre ce e pagina)")
        else:
            print(f"⚠️ ATENȚIE: