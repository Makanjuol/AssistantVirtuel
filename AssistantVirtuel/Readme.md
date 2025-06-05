
# Assistant Vocal Intelligent
====================================
Assistant vocal capable de :
- 🎙️ Enregistrer ou recevoir un fichier audio
- 📝 Transcrire la parole en texte
- 🤖 Générer une réponse avec GPT-3.5 ou DeepSeek localement
- 🔊 Lire la réponse avec synthèse vocale
- 🖥️ Fournir une interface web simple avec historique et export

---

## 🛠️ Installation

### 1. Cloner le projet
```bash
git clone https://github.com/Makanjuol/AssistantVirtuel
cd AssistantVirtuel
````

### 2. Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate        # ou venv\Scripts\activate (Windows)
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 📦 Bibliothèques à installer

Le fichier `requirements.txt` inclut :

* `fastapi`
* `uvicorn`
* `python-dotenv`
* `openai`
* `requests`
* `speechrecognition`
* `pyttsx3`
* `pydub`

Et pour la version locale avec DeepSeek :

* [Installe Ollama](https://ollama.com/download)

Puis dans le terminal :

```bash
ollama run mistral
```

⚠️ Pour l’audio `.mp3`, tu dois aussi :

* Installer **ffmpeg**

  * Avec winget install ffmpeg`
  * Ou : [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

---
### Clé OpenAI

Crée un fichier `.env` à la racine :

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxx
```

Sans clé valide, l’assistant utilise **DeepSeek automatiquement**.

---

## Lancement

===============================
Assistant Vocal - Phase 1 (CLI)
===============================

Assistant vocal intelligent en ligne de commande :

- 🎙️ Enregistre la voix avec un micro
- 📝 Transcrit la voix en texte (speech_recognition)
- 🤖 Génère une réponse avec GPT-3.5 ou DeepSeek (local)
- 🔊 Lit la réponse avec pyttsx3



Utilisation
-----------

1. Lancer DeepSeek si local :
   ollama run mistral

2. Lancer le programme :
   python -m AssistantCLI.main 




===============================
Assistant Vocal - Phase 2 (API REST + Interface Web)
===============================

Assistant vocal avec API FastAPI et interface web.

### 1. Démarrer Ollama avec DeepSeek

```bash
ollama run mistral
```

### 2. Lancer le serveur FastAPI

```bash
uvicorn ApiRest.main:app --reload
```

### 3. Ouvrir l’interface web

[http://localhost:8000](http://localhost:8000)

---

## Exemples d’utilisation



1. Dans l’interface :

   * Cliquer sur "Choisir un fichier" ou "Enregistrer la voix"
   * Cliquer sur "Envoyer"

2. Une fois envoyé, s'afficheront:

   * La transcription de l'audio ou de l'enregistrement envoyé
   * La réponse générée par l'IA
   * La lecture vocale 
   * L’historique des échanges 📜

### 📁 Exporter l’historique

Clique sur **"Exporter l’historique"** pour obtenir un fichier `pdf` de tous les échanges.


---

##  Structure du projet

```
AssistantVirtuel/
├── ApiRest/
│   ├── main.py
│   └── endpoints/
│       ├── assistant.py
│       ├── upload.py
│       ├── transcription.py
│       ├── generation.py
│       └── synthesis.py
├── AssistantCLI/
│   ├── chat_engine.py
│   ├── main.py
│   ├── transcriber.py
│   ├── recorder.py
│   └── VoiceOutout.py
├── web_interface/
│   ├── index.html
│   └── style.css
├── uploaded_audio/
├── response_audio/
├── requirements.txt
├── .env
└── Readme.md


---


