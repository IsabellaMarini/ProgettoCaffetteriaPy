import json
import os
import pickle



from Dipendente.Model.Dipendente import Dipendente
from ListaDipendenti.Model.ListaDipendenti import ListaDipendenti

class ControllerListaDipendenti():
    def __init__(self):
        self.Model = ListaDipendenti()
        super(ControllerListaDipendenti, self).__init__()


    def getListaDipendente(self):
        return self.Model.ListaCompleta()

    def aggiungiDipendente(self, dipendente):
        self.Model.aggiungiDipendente(dipendente)

    def getEliminaDipendente(self, index):
        self.Model.eliminaDipendente(index)

    def Getdipendente_by_index(self, index):
        return self.Model.getdipendente_by_index(index)

    def getSaveData(self):
        self.Model.saveData()

    def getRefreshData(self):
        self.Model.refreshData()

