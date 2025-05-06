import tkinter as tk
from voce import ascolta_frase, parla
from comandi import esegui_comando

def ascolta_comando():
    comando = ascolta_frase("Come posso aiutarti?")
    if comando:
        esegui_comando(comando, output_label)

# GUI
root = tk.Tk()
root.title("Assistente Vocale")
root.geometry("400x250")

tk.Label(root, text="Premi il pulsante per parlare", font=("Arial", 12)).pack(pady=20)
tk.Button(root, text="🎤 Ascolta", font=("Arial", 14), command=ascolta_comando).pack(pady=10)
output_label = tk.Label(root, text="", font=("Arial", 11), wraplength=350, justify="center")
output_label.pack(pady=20)

root.mainloop()
