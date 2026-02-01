import ollama

# Script: 04_fake_data_generator.py
# Scop: Generează date de test (Mock Data) folosind creativitatea AI-ului

def genereaza_date_fictive(numar_persoane=5):
    print(f"--- 🤖 Inventez {numar_persoane} persoane virtuale (Așteaptă...) ---")
    
    # Prompt Engineering: Suntem foarte specifici cu AI-ul
    # Îi cerem format CSV (Comma Separated Values) ca să îl putem salva direct
    prompt = f"""
    Generează o listă cu {numar_persoane} persoane fictive din România.
    Vreau să conțină: Nume Complet, Email Fictiv, Oraș, Meserie.
    
    IMPORTANT:
    - Răspunde DOAR cu datele, în format CSV.
    - Nu scrie introduceri sau alte cuvinte.
    - Formatul să fie: Nume,Email,Oras,Meserie
    """
    
    try:
        raspuns = ollama.chat(model='llama3.2', messages=[
            {'role': 'user', 'content': prompt}
        ])
        
        continut = raspuns['message']['content']
        
        # Salvăm rezultatul într-un fișier
        nume_fisier = "date_fictive.csv"
        with open(nume_fisier, "w", encoding="utf-8") as f:
            f.write(continut)
            
        print(f"\n✅ Gata! Datele au fost salvate în '{nume_fisier}'.")
        print("Iată un preview:")
        print("--------------------------------")
        print(continut)
        print("--------------------------------")

    except Exception as e:
        print(f"❌ Eroare: {e}")

if __name__ == "__main__":
    genereaza_date_fictive(5)