import pyttsx3
import speech_recognition as sr

# Inizializza il motore vocale
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

def ascolta_frase(messaggio_iniziale="Dimmi qualcosa"):
    parla(messaggio_iniziale)
    riconoscitore = sr.Recognizer()
    with sr.Microphone() as source:
        riconoscitore.adjust_for_ambient_noise(source)
        audio = riconoscitore.listen(source)
    try:
        comando = riconoscitore.recognize_google(audio, language='it-IT')
        print("Utente:", comando)
        return comando
    except sr.UnknownValueError:
        parla("Non ho capito, puoi ripetere?")
        return None
    except sr.RequestError:
        parla("Errore di rete, riprova più tardi.")
        return None

def parla_comandi():
    comandi = (
        "Puoi dirmi: che tempo fa, che ore sono, dammi le notizie, salutami, oppure chiedere aiuto."
    )
    parla(comandi)
