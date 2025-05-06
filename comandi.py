from voce import parla, ascolta_frase
from meteo import ottieni_meteo
from notizie import ottieni_notizie
import time

def esegui_comando(comando, output_label=None):
    if "meteo" in comando.lower():
        città = ascolta_frase("Dimmi la città.")
        if città:
            risultato = ottieni_meteo(città)
            parla(risultato)
            if output_label: output_label.config(text=risultato)
    elif "orario" in comando.lower():
        ora = time.strftime("%H:%M")
        parla(f"Ora attuale: {ora}")
    elif "notizie" in comando.lower():
        notizie = ottieni_notizie()
        parla(notizie)
        if output_label: output_label.config(text=notizie)
    elif "saluta" in comando.lower() or "ciao" in comando.lower():
        parla("Ciao! Come posso aiutarti oggi?")
    else:
        parla("Comando non riconosciuto.")
