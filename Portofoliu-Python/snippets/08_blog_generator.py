import ollama

# Script: 08_blog_generator.py
# Scop: Generează idei de titluri și structura pentru articole de blog.

def genereaza_idei():
    print("--- ✍️ Asistentul tău de Content Marketing ---")
    print("Despre ce vrei să scrii azi? (ex: 'Programare Python', 'Turism în Brașov', 'Dieta Keto')")
    
    # Preluăm input de la utilizator de la tastatură
    subiect = input("Scrie subiectul aici: ")
    
    print(f"\n🧠 Generez o structură virală pentru '{subiect}'... (Așteaptă)\n")

    prompt = f"""
    Ești un expert în Marketing și SEO.
    Vreau să scriu un articol de blog despre: "{subiect}".
    
    Te rog să generezi:
    1. Un titlu atractiv (Clickbait pozitiv).
    2. O introducere scurtă (Hook).
    3. O listă cu 3 subtitluri (capitole) despre care să vorbesc.
    
    Răspunde în limba Română, formatat clar.
    """
    
    try:
        raspuns = ollama.chat(model='llama3.2', messages=[
            {'role': 'user', 'content': prompt}
        ])
        
        print("---------------------------------------")
        print(raspuns['message']['content'])
        print("---------------------------------------")
        
    except Exception as e:
        print(f"❌ Eroare: {e}")

if __name__ == "__main__":
    genereaza_idei()