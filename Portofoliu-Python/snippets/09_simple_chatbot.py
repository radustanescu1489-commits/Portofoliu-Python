import ollama

# Script: 09_simple_chatbot.py
# Scop: Un chatbot interactiv care ține minte contextul conversației.

def porneste_chat():
    print("--- 🤖 Chatbot Llama 3 (Local) ---")
    print("Scrie 'stop' sau 'exit' pentru a încheia.\n")

    # Aici este SECRETUL: Lista de istoric
    # Stocăm toată conversația ca AI-ul să aibă context
    istoric = []

    while True:
        # 1. Preluăm mesajul tău
        user_input = input("Tu: ")
        
        # Verificăm dacă vrei să ieși
        if user_input.lower() in ["stop", "exit", "pa"]:
            print("🤖 Chatbot: La revedere! O zi bună.")
            break

        # 2. Adăugăm mesajul tău în istoric
        istoric.append({'role': 'user', 'content': user_input})

        print("AI: (Gândește...)")

        try:
            # 3. Trimitem TOT istoricul, nu doar ultima întrebare
            raspuns = ollama.chat(model='llama3.2', messages=istoric)
            
            ai_message = raspuns['message']['content']
            
            # 4. Afișăm răspunsul
            print(f"🤖 Llama: {ai_message}\n")
            
            # 5. Adăugăm și răspunsul AI-ului în istoric (ca să știe ce a zis)
            istoric.append({'role': 'assistant', 'content': ai_message})

        except Exception as e:
            print(f"❌ Eroare: {e}")

if __name__ == "__main__":
    porneste_chat()