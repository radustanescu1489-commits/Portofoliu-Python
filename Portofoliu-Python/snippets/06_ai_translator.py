import ollama
import os

# Script: 06_ai_translator.py
# Scop: Traduce conținutul fișierelor text folosind AI, păstrând datele private.

def translator_privat():
    # PASUL 1: Creăm un fișier de test (în Engleză)
    # În viața reală, ai avea deja acest fișier.
    nume_fisier_input = "contract_draft.txt"
    text_original = """
    CONFIDENTIAL AGREEMENT
    This is a private document between Client A and Provider B.
    The goal of this project is to build a local AI infrastructure.
    No data shall leave the local server.
    Signed: John Doe.
    """
    
    # Îl scriem pe disk
    with open(nume_fisier_input, "w", encoding="utf-8") as f:
        f.write(text_original)
    
    print(f"📄 Am găsit fișierul: {nume_fisier_input}")
    print("🌍 Încep traducerea în Română... (Gândește...)")

    # PASUL 2: Citim fișierul
    with open(nume_fisier_input, "r", encoding="utf-8") as f:
        continut = f.read()

    # PASUL 3: Trimitem la AI pentru traducere
    prompt = f"""
    Tradu următorul text în limba Română.
    Păstrează tonul formal și profesional.
    Nu adăuga comentarii, doar textul tradus.
    
    TEXT DE TRADUS:
    {continut}
    """
    
    try:
        raspuns = ollama.chat(model='llama3.2', messages=[
            {'role': 'user', 'content': prompt}
        ])
        
        text_tradus = raspuns['message']['content']
        
        # PASUL 4: Salvăm traducerea
        nume_fisier_output = "contract_tradus_RO.txt"
        with open(nume_fisier_output, "w", encoding="utf-8") as f:
            f.write(text_tradus)
            
        print("\n✅ Succes! Traducerea a fost salvată.")
        print(f"📂 Fișier creat: {nume_fisier_output}")
        print("\n--- PREVIEW ---")
        print(text_tradus)
        
    except Exception as e:
        print(f"❌ Eroare: {e}")

if __name__ == "__main__":
    translator_privat()