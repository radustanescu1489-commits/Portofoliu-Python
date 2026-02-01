import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

# Script: 12_audit_with_cookie_killer.py
# Scop: Audit SEO care trece automat de ferestrele de "Accept Cookies"

def omoara_cookies(driver):
    """
    Funcție care caută butoane de acceptare cookies și dă click pe ele.
    """
    print("🍪 Scanez pagina după butoane de Cookies...")
    
    # Lista de cuvinte cheie pe care le căutăm pe butoane
    # Adaugăm variante în RO și EN
    cuvinte_cheie = [
        "Acceptă tot", "Accept all", "De acord", "Accept", 
        "Allow all", "I agree", "Consent", "Acceptă cookie-urile"
    ]
    
    # ID-ul spec   icient la Google)
    try:
        google_btn = driver.find_elements(By.ID, "L2AGLb") # ID-ul butonului "Acceptă tot" la Google
        if google_btn:
            google_btn[0].click()
            print("🍪 VICTORIE: Am găsit și apăsat butonul de Google (ID: L2AGLb)!")
            time.sleep(3)
            return True
    except:
        pass

    # Căutare generală după text (XPath)
    for cuvant in cuvinte_cheie:
        try:
            # Caută orice element (buton, div, span) care conține textul respectiv
            xpath = f"//*[contains(text(), '{cuvant}')]"
            elemente = driver.find_elements(By.XPATH, xpath)
            
            for elem in elemente:
                # Verificăm dacă elementul e vizibil și e clickabil
                if elem.is_displayed() and elem.tag_name in ['button', 'div', 'span', 'a']:
                    elem.click()
                    print(f"🍪 VICTORIE: Am dat click pe un buton cu textul: '{cuvant}'")
                    time.sleep(3) # Așteptăm să dispară fereastra
                    return True
        except Exception:
            continue # Dacă dă eroare la un buton, trecem la următorul
            
    print("⚠️ Nu am găsit butoane evidente de Cookies. Continui auditul așa.")
    return False

def audit_profesional_v2(url):
    print(f"--- 🕵️‍♂️ Încep Auditul SEO (cu Cookie Killer) pentru: {url} ---\n")
    
    edge_options = Options()
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    edge_options.add_argument("--start-maximized") 
    edge_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0")

    driver = None
    scor_seo = 100 
    probleme_gasite = []

    try:
        driver = webdriver.Edge(options=edge_options)
        driver.get(url)
        
        print("⏳ Aștept 3 secunde încărcarea inițială...")
        time.sleep(3) 

        # --- MOMENTUL MAGIC: Încercăm să scăpăm de Cookies ---
        omoara_cookies(driver)
        # ----------------------------------------------------

        print("\n--- 📊 RAPORT ANALIZĂ FINALĂ ---")

        # --- CHECK 1: TITLUL ---
        titlu = driver.title
        print(f"✅ Titlu: {titlu}")
        if not titlu:
            scor_seo -= 20; probleme_gasite.append("Titlu LIPSA!")
        elif len(titlu) < 10 or len(titlu) > 70:
            scor_seo -= 10; probleme_gasite.append(f"Titlu neoptim ({len(titlu)} chars).")

        # --- CHECK 2: META DESCRIEREA ---
        try:
            meta = driver.find_element(By.XPATH, "//meta[@name='description']")
            desc = meta.get_attribute("content")
            print(f"✅ Descriere: {desc[:50]}...")
            if len(desc) < 50: scor_seo -= 5; probleme_gasite.append("Meta Descriere prea scurtă.")
        except:
            scor_seo -= 10; probleme_gasite.append("Meta Descriere LIPSA!")

        # --- CHECK 3: H1 ---
        h1s = driver.find_elements(By.TAG_NAME, "h1")
        if len(h1s) == 1:
            print(f"✅ H1 Corect: {h1s[0].text[:40]}...")
        elif len(h1s) == 0:
            # Mai verificăm o dată, poate cookie banner a ascuns H1
            scor_seo -= 20; probleme_gasite.append("H1 LIPSA!")
        else:
            scor_seo -= 10; probleme_gasite.append(f"Prea multe H1 ({len(h1s)}).")

        # --- CHECK 4: Conținut ---
        body_text = driver.find_element(By.TAG_NAME, "body").text
        cuvinte = len(body_text.split())
        print(f"📝 Volum conținut: ~{cuvinte} cuvinte")
        if cuvinte < 300:
            scor_seo -= 10; probleme_gasite.append("Conținut subțire (<300 cuvinte).")

        # --- REZULTAT ---
        print("\n" + "="*30)
        print(f"🏆 SCOR SEO FINAL: {scor_seo}/100")
        print("="*30)
        
        if scor_seo < 100:
            for p in probleme_gasite: print(f"   ❌ {p}")

    except Exception as e:
        print(f"❌ Eroare: {e}")
    finally:
        if driver: driver.quit()

if __name__ == "__main__":
    # testam pe site, ne folosim de altgoritmul pe care l-am creat 
    audit_profesional_v2("https://instalatoruldeai.ro")
