import ollama

# Script: 05_sentiment_analyzer.py
# Scop: Analizează tonul mesajelor (Sentiment Analysis) folosind AI

def analizeaza_sentimente():
    # Lista de recenzii (simulăm date reale de la clienți)
    recenzii = [
        "Produsul este absolut genial, mi-a schimbat viața!",
        "O mizerie totală. S-a stricat după o zi. Nu recomand.",
        "Livrarea a fost ok, dar cutia era puțin îndoită.",
        "Nu știu ce să zic, e un produs normal.",
        "WOW! Cel mai bun raport calitate-preț de pe piață."
    ]

    print("--- 🧠 Încep analiza psihologică a clienților ---\n")

    for text in recenzii:
        # Prompt-ul: Cerem AI-ului să fie un "Clasificator"
        prompt = f"""
        Analizează sentimentul acestui text.
        Răspunde DOAR cu unul dintre cuvintele: "POZITIV", "NEGATIV" sau "NEUTRU".
        Fără alte explicații.
        
        Text: "{text}"
        """
        
        # Trimitem la Llama 3.2
        raspuns = ollama.chat(model='llama3.2', messages=[
            {'role': 'user', 'content': prompt}
        ])
        
        sentiment = raspuns['message']['content'].strip()
        
        # Facem rezultatul să arate frumos în consolă
        iconita = "❓"
        if "POZITIV" in sentiment.upper():
            iconita = "🟢" # Verde pentru fericire
        elif "NEGATIV" in sentiment.upper():
            iconita = "🔴" # Roșu pentru nervi
        elif "NEUTRU" in sentiment.upper():
            iconita = "🟡" # Galben pentru neutru
            
        print(f"{iconita} [{sentiment}] -> \"{text}\"")

if __name__ == "__main__":
    analizeaza_sentimente()