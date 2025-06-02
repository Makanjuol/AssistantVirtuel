import pyttsx3

def speak_text(text):
    """
    Lit le texte fourni à haute voix en utilisant pyttsx3.

    Args:
        text (str): Texte à lire.
    """
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)       # Vitesse de parole
        engine.setProperty('volume', 1.0)     # Volume (0.0 à 1.0)

        # Optionnel : choisir une voix (ex. voix française si disponible)
        voices = engine.getProperty('voices')
        for voice in voices:
            if "fr" in voice.id.lower():  # pour les systèmes avec voix françaises
                engine.setProperty('voice', voice.id)
                break

        # print("🔊 Lecture de la réponse...")
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"❌ Erreur synthèse vocale : {e}")
