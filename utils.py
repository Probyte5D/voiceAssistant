from googletrans import Translator

def traduci_testo(testo):
    traduttore = Translator()
    tradotto = traduttore.translate(testo, dest='it')
    return tradotto.text
