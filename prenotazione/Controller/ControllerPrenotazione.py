
from prenotazione.Model.Prenotazione import Prenotazione


class ControllerPrenotazione():


    def __init__(self,):
        self.model = Prenotazione

    def get_lista_tavoli(self):
        return self.model.lista_tavoli

    def get_orario(self):
        return self.model.orario

    def get_disponibilita(self):
        return self.model.is_disponibile()

