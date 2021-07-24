import json
import os
import pickle

from Dipendente.Model.Dipendente import Dipendente


class ListaDipendenti():
    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.listadipendenti = []
        self.refreshData()


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

    def refreshData(self):
        if os.path.isfile('ListaDipendenti/Database/listaDipendenti.pickle'):
            with open('ListaDipendenti/Database/listaDipendenti.pickle', 'rb') as f:
                listaDipendenti = pickle.load(f)
            self.Model = listaDipendenti
        else:
            with open('ListaDipendenti/Database/listaDipendenti.json') as f:
                listaDipendenti = json.load(f)
                for dipendente in listaDipendenti:
                    self.Model.aggiungiDipendente(
                        Dipendente(dipendente["nome"], dipendente["cognome"], dipendente["numero"], dipendente["email"],
                                   dipendente["password"])
                    )
                    with open('ListaDipendenti/Database/listaDipendenti.pickle', 'wb') as handle:
                        pickle.dump(self.Model, handle, pickle.HIGHEST_PROTOCOL)

    def saveData(self):
        with open('ListaDipendenti/Database/listaDipendenti.pickle', 'wb') as handle:
            pickle.dump(self.listadipendenti, handle, pickle.HIGHEST_PROTOCOL)

