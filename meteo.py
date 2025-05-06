import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def ottieni_meteo(città):
    if not api_key:
        return "Chiave API mancante."
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": città, "appid": api_key, "units": "metric", "lang": "it"}
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if data["cod"] != "404":
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"A {città} ci sono {temp}°C con {desc}."
        else:
            return "Città non trovata."
    except:
        return "Errore nel recupero del meteo."
