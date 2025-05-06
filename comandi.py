import requests
import os
import time
from googletrans import Translator
from voce import parla, ascolta_frase
from dotenv import load_dotenv

load_dotenv()
weather_api_key = os.getenv("API_KEY")
news_api_key = os.getenv("API_KEY_NEWS")

def traduci_testo(testo):
    traduttore = Translator()
    tradotto = traduttore.translate(testo, dest='it')
    return tradotto.text

def ottieni_meteo(città):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={città}&appid={weather_api_key}&units=metric&lang=it"
    try:
        response = requests.get(url)
        dati = response.json()
        if dati["cod"] != "404":
            temperatura = dati["main"]["temp"]
            descrizione = dati["weather"][0]["description"]
            return f"La temperatura a {città} è di {temperatura}°C con {descrizione}."
        else:
            return "Città non trovata."
    except:
        return "Errore nel recupero dei dati meteo."

def ottieni_notizie():
    url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={news_api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        if data["status"] == "ok":
            notizie = data["articles"][:3]
            testo = "Le ultime notizie: "
            for i, articolo in enumerate(notizie, 1):
                titolo = traduci_testo(articolo["title"])
                descrizione = traduci_testo(articolo["description"]) if articolo["description"] else ""
                testo += f"\n{i}. {titolo} - {descrizione}"
            return testo
        else:
            return "Errore nel recupero delle notizie."
    except:
        return "Errore nel recupero delle notizie."

def esegui_comando(comando, output_label):
    comando = comando.lower()

    if "meteo" in comando or "tempo" in comando:
        parla("Di quale città vuoi sapere il meteo?")
        citta = ascolta_frase("Dimmi la città.")
        if citta:
            risultato = ottieni_meteo(citta)
            parla(risultato)
            output_label.config(text=risultato)

    elif "notizie" in comando:
        testo = ottieni_notizie()
        parla(testo)
        output_label.config(text=testo)

    elif "orario" in comando:
        ora = time.strftime("%H:%M")
        parla(f"L'ora attuale è {ora}")
        output_label.config(text=f"Ora attuale: {ora}")

    elif "saluta" in comando:
        parla("Ciao! Come posso aiutarti oggi?")
        output_label.config(text="Assistente: Ciao!")

    elif "aiuto" in comando or "comandi" in comando:
        guida = (
            "Puoi chiedermi: meteo, orario, notizie, saluta, oppure aiuto per ripetere questi comandi."
        )
        parla(guida)
        output_label.config(text=guida)

    else:
        risposta = "Comando non riconosciuto. Puoi dire: meteo, orario, notizie, saluta o aiuto."
        parla(risposta)
        output_label.config(text=risposta)
