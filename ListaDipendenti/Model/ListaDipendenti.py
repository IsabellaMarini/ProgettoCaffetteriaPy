import json
from Dipendente.Model.Dipendente import Dipendente


class ListaDipendenti():
    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.listadipendenti = []
        with open("ListaDipendenti/Database/listaDipendenti.json") as l:
            appoggio = json.load(l)
        self.listadipendenti.append(appoggio)


    def ListaDipendente(self):
        return self.listadipendenti

    def aggiungiDipendente(self):
        for dipendenteDaAggiungere in self.listadipendenti:
           self.listadipendenti.append(Dipendente (dipendenteDaAggiungere["nome"],
                                       dipendenteDaAggiungere["cognome"],
                                       dipendenteDaAggiungere["numero"],
                                       dipendenteDaAggiungere["email"],
                                       dipendenteDaAggiungere["password"]
                                     ))

    def eliminaDipendente(self):
        self.listadipendenti.remove(Dipendente)




