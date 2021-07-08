import json

class ControllerPrenotazione():

    lista_tavoli = json.load(open("listatavoli.json"))

    def __init__(self, Prenotazione):
        self.model = Prenotazione

    def get_lista_tavoli(self):
        return self.model.lista_tavoli

    def get_orario(self):
        return self.model.orario

    def get_disponibilita(self):
        if (self.model.lista_tavoli["disponibilità"] = true):
            return "disponibile"
        else:
            return "non disponibile"

