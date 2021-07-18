
from Login.Model.Login import Login
from prenotazione.Model.Prenotazione import Prenotazione


class PrenotazioneAttiva():

    def __init__(self):
        self.login = Login
        self.prenotazione = Prenotazione

    def show_prenotazione(self):
        if (self.prenotazione.email == Prenotazione.email) :
            return self.prenotazione
        else:
            print("Non ci sono prenotazioni attive!")


