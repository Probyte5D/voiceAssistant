import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Seleziona voce italiana
voices = engine.getProperty('voices')
for voice in voices:
    if voice.languages and isinstance(voice.languages[0], bytes):
        if 'it' in voice.languages[0].decode('utf-8').lower():
            engine.setProperty('voice', voice.id)
            break

def parla(testo):
    print("Assistente:", testo)
    engine.say(testo)
    engine.runAndWait()

def ascolta_frase(prompt="Parla ora..."):
    riconoscitore = sr.Recognizer()
    with sr.Microphone() as source:
        parla(prompt)
        riconoscitore.adjust_for_ambient_noise(source)
        audio = riconoscitore.listen(source)
    try:
        return riconoscitore.recognize_google(audio, language="it-IT")
    except sr.UnknownValueError:
        parla("Non ho capito.")
        return None
    except sr.RequestError:
        parla("Errore di rete.")
        return None
