import json



class Prenotazione():

        def __init__(self, lista_tavoli, orario, email):
            super(Prenotazione, self).__init__()
            self.lista_tavoli = lista_tavoli
            self.orario = orario
            self.disponibile = True
            self.email = email


        def prenota(self):

            self.disponibile = False

        def refresh(self):
            with open('prenotazione/Database/prenotazioni.json') as o:
                self.orario = json.load(o)
            if (o.orario == self.orario):
                return self.disponibile
            else:
                self.disponibile = True

