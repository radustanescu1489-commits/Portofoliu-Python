# 🤖 Python & Local AI Automation Portfolio

O colecție de 10 scripturi Python care demonstrează automatizarea task-urilor reale folosind **Web Scraping** și **Local LLMs** (Ollama / Llama 3.2).

Toate procesările AI se fac **local**, garantând confidențialitatea datelor (fără API keys, fără cloud).

## 🛠️ Tehnologii Folosite
* **Python 3.12**
* **Ollama** (Running Llama 3.2 3B Model)
* **BeautifulSoup4** (Web Scraping)
* **Requests** (HTTP Networking)

## 📂 Lista Proiectelor (`/snippets`)

### 🌐 Web Scraping & Analiză
| Script | Descriere |
| :--- | :--- |
| `01_book_scraper.py` | Extrage date (Titlu/Preț) de pe site-uri de e-commerce și le salvează în CSV. |
| `02_seo_auditor.py` | Analizează tehnic pagini web (Meta tags, H1, Title) pentru SEO. |
| `03_ai_summarizer.py` | Citește un articol web și generează automat un rezumat cu puncte cheie. |

### 🧠 Procesare AI & NLP
| Script | Descriere |
| :--- | :--- |
| `04_fake_data_generator.py` | Generează date fictive de test (Nume, Email, Job) în format CSV. |
| `05_sentiment_analyzer.py` | Clasifică automat feedback-ul clienților (Pozitiv/Negativ). |
| `06_ai_translator.py` | Traduce documente text confidențiale fără a le trimite pe internet. |
| `07_code_explainer.py` | Un script care își citește propriul cod și explică logica din spate. |

### 🤖 Utilitare Inteligente
| Script | Descriere |
| :--- | :--- |
| `08_blog_generator.py` | Asistent de marketing: generează titluri și structuri de articole. |
| `09_simple_chatbot.py` | Un chatbot CLI care reține istoricul conversației (Context Aware). |
| `10_smart_organizer.py` | Simulează organizarea fișierelor în foldere bazat pe semnificația numelui (Semantic Sorting). |

## 🚀 Cum să le folosești

1. **Instalează dependențele:**
   ```bash
   pip install -r requirements.txt