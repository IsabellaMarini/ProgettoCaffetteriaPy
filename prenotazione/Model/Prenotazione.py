import json


class Prenotazione():
    lista_tavoli = json.load(open("listatavoli.json"))
        def __init__(self, lista_tavoli, orario):
            super(Prenotazione, self).__init__()
            self.lista_tavoli = lista_tavoli
            self.orario = orario



        def is_disponibile(self):
            lista_tavoli["disponibilità"]
            return self.lista_tavoli

