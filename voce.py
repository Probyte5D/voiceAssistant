import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Voce italiana se disponibile
for voice in engine.getProperty('voices'):
    if 'it' in voice.name.lower() or 'italian' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def parla(testo):
    print("Assistente:", testo)
    engine.say(testo)
    engine.runAndWait()

def ascolta_frase(frase_iniziale=None):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if frase_iniziale:
            parla(frase_iniziale)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        comando = r.recognize_google(audio, language="it-IT")
        print("Hai detto:", comando)
        return comando
    except:
        parla("Non ho capito, puoi ripetere?")
        return None

def parla_comandi():
    parla("Puoi chiedermi: meteo, orario, notizie, musica, oppure saluta.")
