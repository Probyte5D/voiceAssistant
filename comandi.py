import requests
import os
import time
from deep_translator import GoogleTranslator
from voce import parla, ascolta_frase
from dotenv import load_dotenv
from googleapiclient.discovery import build
import webbrowser

# Carica la tua API Key
load_dotenv()
api_key = os.getenv("API_KEY_YT")

# Crea il client YouTube
youtube = build('youtube', 'v3', developerKey=api_key)

def cerca_video_youtube(query):
    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=query,
        type="video"
    )
    response = request.execute()

    video_url = f"https://www.youtube.com/watch?v={response['items'][0]['id']['videoId']}"
    return video_url

def riproduci_musica(output_label=None):
    parla("Quale canzone vuoi ascoltare?")
    brano = ascolta_frase("Dimmi il titolo del brano.")
    
    if not brano:
        parla("Non ho capito il titolo.")
        return
    
    parla(f"Cerco {brano} su YouTube.")
    try:
        # Cerca il video su YouTube
        video_url = cerca_video_youtube(brano)

        # Avvia il video nel browser
        webbrowser.open(video_url)

        if output_label:
            output_label.config(text=f"🎵 In riproduzione: {video_url}")

    except Exception as e:
        parla("Errore durante la riproduzione della musica.")
        print("Errore:", e)

# Esegui il comando musica
def esegui_comando(comando, output_label):
    comando = comando.lower()

    if "musica" in comando or "canzone" in comando:
        riproduci_musica(output_label)
    else:
        risposta = "Comando non riconosciuto. Puoi dire: musica."
        parla(risposta)
        output_label.config(text=risposta)


