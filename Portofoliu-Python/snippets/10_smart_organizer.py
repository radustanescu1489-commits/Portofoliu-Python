import ollama

# Script: 10_smart_organizer.py
# Scop: Organizează fișierele în funcție de sensul numelui lor (Semantic Sorting)

def organizator_inteligent():
    # Simulam un folder "Downloads" dezordonat
    fisiere_dezordonate = [
        "factura_orange_ianuarie.pdf",
        "poze_vacanta_grecia.jpg",
        "contract_munca_semnat.docx",
        "reteta_prajitura.txt",
        "curs_python_incepatori.mp4",
        "bilet_avion_wizz.pdf",
        "setup_minecraft.exe",
        "raport_financiar_2025.xlsx"
    ]

    print("--- 📂 AI File Organizer (Simulare) ---")
    print(f"Analizez {len(fisiere_dezordonate)} fișiere...\n")

    categorii = ["Financiar", "Personal", "Munca", "Software", "Altele"]

    for fisier in fisiere_dezordonate:
        # Întrebăm AI-ul unde să pună fișierul
        prompt = f"""
        Am un fișier numit: "{fisier}".
        Alege cea mai potrivită categorie din lista asta: {categorii}.
        Răspunde DOAR cu numele categoriei.
        """
        
        try:
            raspuns = ollama.chat(model='llama3.2', messages=[
                {'role': 'user', 'content': prompt}
            ])
            
            categoria_aleasa = raspuns['message']['content'].strip()
            
            # Curățăm răspunsul (uneori AI-ul pune punct la final)
            categoria_aleasa = categoria_aleasa.replace(".", "")
            
            print(f"📄 '{fisier}' \t--> 📂 Folder: [{categoria_aleasa}]")
            
        except Exception as e:
            print(f"❌ Eroare la {fisier}: {e}")

    print("\n✅ Analiză completă. (În modul real, aș fi creat folderele și aș fi mutat fișierele).")

if __name__ == "__main__":
    organizator_inteligent()