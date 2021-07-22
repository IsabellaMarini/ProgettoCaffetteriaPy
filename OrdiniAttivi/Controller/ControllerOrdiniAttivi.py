import pickle
import os
from OrdiniAttivi.Model import OrdiniAttivi
class ControllerOrdiniAttivi():
    def __init__(self, login):
        self.login = login
        self.lista = []
        self.lista_totale = []
        file_path = "OrdiniAttivi/Database/ordiniAttivi.pickle"
        if os.stat(file_path).st_size != 0:
            with open(file_path, 'rb') as f:
                self.lista_totale.append(pickle.load(f))
            f.close()

    def ordiniCliente(self):
        for i in self.lista_totale:
            app = i.codice
            app2 = self.login.email
            num = len(app2)
            if app[0:num-1] == app2 :
                self.lista.append(i)
        return self.lista

