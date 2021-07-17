
from prenotazione.Model.Prenotazione import Prenotazione


class ControllerPrenotazione():


    def __init__(self,):
        self.Model = Prenotazione

    def get_lista_tavoli(self):
        return self.Model.lista_tavoli

    def get_orario(self):
        return self.Model.orario

    def get_disponibilita(self):
        return self.Model.disponibile

    def set_lista_tavoli(self, lista_tavoli):
        self.Model.lista_tavoli = lista_tavoli

    def set_orario(self, orario):
        self.Model.orario = orario

    def getRefresh(self):
        self.Model.refresh()

    def getPrenota(self):
        self.Model.prenota()


