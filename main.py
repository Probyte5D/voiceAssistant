import tkinter as tk
from voce import ascolta_frase, parla, parla_comandi
from comandi import esegui_comando

def ascolta_comando():
    comando = ascolta_frase("Come posso aiutarti?")
    if comando:
        esegui_comando(comando, output_label)

# GUI
root = tk.Tk()
root.title("Assistente Vocale")
root.geometry("400x300")

tk.Label(root, text="Premi il pulsante per parlare", font=("Arial", 12)).pack(pady=10)

tk.Button(root, text="🎤 Ascolta", font=("Arial", 14), command=ascolta_comando).pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 11), wraplength=350, justify="center")
output_label.pack(pady=10)

# Comandi disponibili nella GUI
comandi_supportati = (
    "Comandi disponibili:\n"
    "- 'meteo' (es: che tempo fa a Roma)\n"
    "- 'orario'\n"
    "- 'notizie'\n"
    "- 'saluta'\n"
    "- 'aiuto'"
)
comandi_label = tk.Label(root, text=comandi_supportati, font=("Arial", 9), wraplength=350, justify="left", fg="gray")
comandi_label.pack(pady=10)

# All'avvio suggerisce cosa può fare
parla_comandi()

root.mainloop()
