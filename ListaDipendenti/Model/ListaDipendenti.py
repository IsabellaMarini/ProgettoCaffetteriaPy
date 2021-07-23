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

   # def elimina_ordine(self, ordine):
       # for i in self.listadipendenti:
          #  if ordine == i:
            #    self.listadipendenti.remove(i)
            #    self.lista.remove(i)

     #   with open('OrdiniAttivi/Database/ordiniAttivi.pickle', 'wb') as handle:
     #       pickle.dump(self.listadipendenti, handle, pickle.HIGHEST_PROTOCOL)
      #  handle.close()


    def getdipendente_by_index(self, index):
        return self.listadipendenti[index]

