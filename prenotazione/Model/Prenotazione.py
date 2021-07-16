import json

o = json.load(open("prenotazioni.json"))

class Prenotazione():

        def __init__(self, lista_tavoli, orario):
            super(Prenotazione, self).__init__()
            self.listatavoli = lista_tavoli
            self.orario = orario
            self.disponibile = True

        def is_disponibile(self):
            return self.disponibile

        def prenota(self):
            o.orario
            self.disponibile = False



