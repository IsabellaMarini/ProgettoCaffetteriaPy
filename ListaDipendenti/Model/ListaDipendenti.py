from json
from Dipendente.Model.Dipendente import Dipendente
lD=json.load(open("ListaDipendenti.json"))

class ListaDipendenti():
    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.lD.append(ListaDipendenti)

    def ListaDipendente(self):
        return self.lD

    def aggiungiDipendente(self, Dipendente):
        for dipendenteDaAggiungere in lD:
           self.lD.append(Dipendente( dipendenteDaAggiungere["nome"],
                                       dipendenteDaAggiungere["cognome"],
                                       dipendenteDaAggiungere["numero"],
                                       dipendenteDaAggiungere["email"],
                                       dipendenteDaAggiungere["password"]
                                     ))

    def eliminaDipendente(self, Dipendente):
        self.lD.remove(Dipendente)




