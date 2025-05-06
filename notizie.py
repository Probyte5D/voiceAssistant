import requests
import os
from dotenv import load_dotenv
from utils import traduci_testo

load_dotenv()
news_api_key = os.getenv("API_KEY_NEWS")

def ottieni_notizie():
    url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={news_api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        if data["status"] == "ok":
            articoli = data["articles"][:3]
            testo = "Le ultime notizie:"
            for i, art in enumerate(articoli, 1):
                titolo = traduci_testo(art["title"])
                descrizione = traduci_testo(art["description"] or "")
                testo += f"\n{i}. {titolo} - {descrizione}"
            return testo
        return "Errore nel recupero notizie."
    except:
        return "Errore di rete."
