##  Thakurmar Jhuli — AI Voice-Based Storytelling App

**Thakurmar Jhuli** is an interactive **AI-powered storytelling web app** built with **Streamlit**, where you simply speak the kind of story you want to hear, and the app will generate and narrate it for you — just like grandma used to!

---

###  Demo


![_jAE2d1h](https://github.com/user-attachments/assets/008f8a06-5ac7-488b-ba49-ab473e2c2b0c)

---

###  Features

-  **Voice Command Input** — Tell the app what kind of story you want using your voice  
-  **Voice-to-Text** — Uses **Whisper LLM** to convert your voice into text  
-  **Story Generation** — Powered by **Gemma LLM** running via **Ollama**  
-  **Text-to-Speech** — Converts generated story to speech using **Play AI TTS** (via **Groq API**)  

---

###  Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io/) | UI Framework |
| [Whisper LLM](https://github.com/openai/whisper) | Voice-to-Text |
| [Gemma LLM](https://ai.google.dev/gemma) via [Ollama](https://ollama.com) | Story Generation |
| [Play HT / Play AI TTS](https://play.ht/) via [Groq API](https://console.groq.com) | Story Narration |
| Custom CSS | UI Theming & Styling |
| PNG/GIF Assets | Logo & Talking Animation |

---

###  Installation

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/thakurmar-jhuli.git
cd thakurmar-jhuli
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Start Streamlit**
```bash
streamlit run app.py
```

---

###  API Keys & Setup

- For Whisper, you can use the local model or OpenAI's API (your choice).
- For Gemma, make sure **Ollama** is installed and running.
- For Play AI TTS:
  - Get API Key from [Groq Console](https://console.groq.com)
  - Store it securely in a `.env` file or Streamlit secrets.

---
