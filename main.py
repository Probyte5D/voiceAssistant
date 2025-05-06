import pyttsx3
import tkinter as tk
import requests
import speech_recognition as sr
import time
import os
from dotenv import load_dotenv

#  Carica variabili d'ambiente dal file .env
load_dotenv()

# Ottieni la chiave API dal file .env
api_key = os.getenv("API_KEY")

# Inizializza il motore vocale
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Seleziona voce italiana (se disponibile)
voices = engine.getProperty('voices')
for voice in voices:
    if voice.languages and isinstance(voice.languages[0], bytes):
        if 'it' in voice.languages[0].decode('utf-8').lower():
            engine.setProperty('voice', voice.id)
            break

# Funzione per far parlare il programma
def parla(audio):
    print("Assistente:", audio)
    engine.say(audio)
    engine.runAndWait()

# Funzione per ottenere il meteo
def ottieni_meteo(città):
    if not api_key:
        return "Chiave API non trovata. Assicurati di aver configurato il file .env correttamente."
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={città}&appid={api_key}&units=metric&lang=it"
    try:
        response = requests.get(complete_url)
        data = response.json()
        if data["cod"] != "404":
            temperatura = data["main"]["temp"]
            descrizione = data["weather"][0]["description"]
            return f"La temperatura a {città} è di {temperatura}°C con {descrizione}."
        else:
            return "Città non trovata."
    except:
        return "Errore nel recupero dei dati meteo."

# Funzione per salutare l'utente
def saluta():
    parla("Ciao! Come posso aiutarti oggi?")

# Funzione per leggere l'orario
def orario():
    ora_corrente = time.strftime("%H:%M")
    parla(f"L'ora attuale è {ora_corrente}")

# Funzione per eseguire i comandi vocali
def esegui_comando(comando):
    if "meteo" in comando.lower() or "tempo" in comando.lower():
        parla("Di quale città vuoi sapere il meteo?")
        ascolta_citta()
    elif "come stai" in comando.lower():
        parla("Sto bene, grazie per avermelo chiesto!")
    elif "orario" in comando.lower():
        orario()
    elif "saluta" in comando.lower():
        saluta()
    else:
        parla("Comando non riconosciuto. Prova con 'che tempo fa a Roma' o 'orario'.")

# Funzione per ascoltare comandi vocali
def ascolta_comando():
    riconoscitore = sr.Recognizer()
    with sr.Microphone() as source:
        parla("Ciao, in cosa posso aiutarti? Potrei dirti il meteo o l'orario attuale")
        riconoscitore.adjust_for_ambient_noise(source)
        audio = riconoscitore.listen(source)
    try:
        comando = riconoscitore.recognize_google(audio, language='it-IT')
        print(f"Comando: {comando}")
        esegui_comando(comando)
    except sr.UnknownValueError:
        parla("Non ho capito, puoi ripetere?")
    except sr.RequestError:
        parla("Errore di rete, riprova più tardi.")

# Funzione per ascoltare il nome della città
def ascolta_citta():
    riconoscitore = sr.Recognizer()
    with sr.Microphone() as source:
        parla("Dimmi la città.")
        riconoscitore.adjust_for_ambient_noise(source)
        audio = riconoscitore.listen(source)
    try:
        citta = riconoscitore.recognize_google(audio, language='it-IT')
        print(f"Città: {citta}")
        risultato = ottieni_meteo(citta)
        parla(risultato)
        output_label.config(text=risultato)
    except sr.UnknownValueError:
        parla("Non ho capito la città, ripeti.")
    except sr.RequestError:
        parla("Errore di rete, riprova più tardi.")

# Interfaccia grafica
root = tk.Tk()
root.title("Assistente Vocale - Meteo e Comandi")
root.geometry("400x250")

label = tk.Label(root, text="Premi il pulsante per parlare", font=("Arial", 12))
label.pack(pady=20)

button = tk.Button(root, text="🎤 Ascolta", font=("Arial", 14), command=ascolta_comando)
button.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 11), wraplength=350, justify="center")
output_label.pack(pady=20)

root.mainloop()
