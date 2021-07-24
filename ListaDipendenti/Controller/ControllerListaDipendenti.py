import json
import os
import pickle



from Dipendente.Model.Dipendente import Dipendente
from ListaDipendenti.Model.ListaDipendenti import ListaDipendenti
from Login.Controller.ControllerLogin import ControllerLogin
from Login.Model.Login import Login


class ControllerListaDipendenti():
    def __init__(self):
        super(ControllerListaDipendenti, self).__init__()
        self.Model= ListaDipendenti()

        if os.path.isfile('ListaDipendenti/Database/listaDipendenti.pickle'):
            with open('ListaDipendenti/Database/listaDipendenti.pickle', 'rb') as f:
                listadipendenti = pickle.load(f)
            self.Model = listadipendenti
        else:
             with open('ListaDipendenti/Database/listaDipendenti.json') as f:
                         listaDipendenti = json.load(f)
                         for dipendente in listaDipendenti:
                                 self.Model.aggiungiDipendente(
                                                                 Dipendente(dipendente["nome"], dipendente["cognome"], dipendente["numero"], dipendente["email"], dipendente["password"])
                                 )
                                 with open('ListaDipendenti/Database/listaDipendenti.pickle', 'wb') as handle:
                                        pickle.dump(self.Model, handle, pickle.HIGHEST_PROTOCOL)

    def getListaDipendente(self):
        return self.Model.ListaCompleta()

    def aggiungiDipendente(self, dipendente):
        self.Model.aggiungiDipendente(dipendente)
        with open('ListaDipendenti/Database/listaDipendenti.pickle', 'wb') as handle:
            pickle.dump(self.Model, handle, pickle.HIGHEST_PROTOCOL)

        login = Login(dipendente.email, dipendente.password)
        controller = ControllerLogin(login)
        controller.registrazioneDipendente()

    def getEliminaDipendente(self, dipendente):
        app = dipendente
        login = Login(app.email, app.password)
        controller = ControllerLogin(login)
        controller.eliminaDipendente()
        self.Model.eliminaDipendente(app)
        with open('ListaDipendenti/Database/listaDipendenti.pickle', 'wb') as handle:
            pickle.dump(self.Model, handle, pickle.HIGHEST_PROTOCOL)
        handle.close()
