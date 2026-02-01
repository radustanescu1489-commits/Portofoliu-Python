import ollama
import os

# Script: 07_code_explainer.py
# Scop: Citește un fișier de cod (Python) și explică ce face, pas cu pas.

def explica_codul():
    # TRUC: Îi cerem scriptului să se citească pe EL ÎNSUȘI!
    # __file__ este o variabilă specială care conține numele scriptului curent
    nume_fisier = os.path.basename(__file__)
    
    print(f"🧐 Citesc fișierul: {nume_fisier} ...")
    
    with open(nume_fisier, "r", encoding="utf-8") as f:
        cod_sursa = f.read()

    print("🧠 Analizez logica... (Așteaptă AI-ul)\n")

    prompt = f"""
    Ești un profesor expert de Python.
    Explică-mi simplu, pentru un începător, ce face acest cod.
    Nu îmi da cod înapoi, ci doar explicația în limba română.
    
    CODUL:
    {cod_sursa}
    """
    
    try:
        raspuns = ollama.chat(model='llama3.2', messages=[
            {'role': 'user', 'content': prompt}
        ])
        
        explicatie = raspuns['message']['content']
        
        print("--- 🎓 EXPLICAȚIA PROFESORULUI AI ---")
        print(explicatie)
        print("-------------------------------------")

    except Exception as e:
        print(f"❌ Eroare: {e}")

if __name__ == "__main__":
    explica_codul()