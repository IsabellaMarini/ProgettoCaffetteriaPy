import json
import os
import pickle

from Dipendente.Model.Dipendente import Dipendente


class ListaDipendenti():
    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.listadipendenti = []


    def ListaCompleta(self):
        return self.listadipendenti

    def aggiungiDipendente(self, dipendente):
        self.listadipendenti.append(dipendente)


    def eliminaDipendente(self, dipendente):
       for i in self.listadipendenti:
          if dipendente == i:
              self.listadipendenti.remove(i)




    def getdipendente_by_index(self, index):
        return self.listadipendenti[index]