import pickle
import time
import os

from OrdiniAttivi.Model.OrdiniAttivi import OrdiniAttivi
from Prodotto.Model.Prodotto import Prodotto
from Login.Controller.ControllerLogin import ControllerLogin

class Carrello():

    def __init__(self, login):
        super(Carrello, self).__init__()
        self.lista_prodotti=[]
        self.codice = None
        self.login = login


    def aggiungi_al_carrello(self, prodotto_da_aggiugnere):
        self.lista_prodotti.append(prodotto_da_aggiugnere)

    def calcolaTotale(self):
        prezzi=[]

        for prodotto in self.lista_prodotti:
            app =float(prodotto.prezzo)

            prezzi.append(app.__round__(2))
            app = float(prodotto.personalizzazione.prezzo)

            prezzi.append(app.__round__(2))
        costo=sum(prezzi)
        return costo.__round__(2)

    def confermaOrdine(self):
        if self.calcolaTotale() != 0:
            lista = []
            ts = time.time()
            self.codice = self.login.getEmail()+ str(ts)
            print(self.codice)
            file_path = "OrdiniAttivi/Database/ordiniAttivi.pickle"
            if os.stat(file_path).st_size != 0:
                with open(file_path, 'rb') as f:

                    lista =pickle.load(f)
                for i in lista:
                    print(i.codice)


            with open('OrdiniAttivi/Database/ordiniAttivi.pickle', 'wb') as handle:
                app = OrdiniAttivi(self.lista_prodotti, self.codice)
                print  (app)
                print (app.codice)
                print(app.lista_prodotti[0].nome)
                lista.append(app)
                pickle.dump(lista, handle, pickle.HIGHEST_PROTOCOL)
            handle.close()
            self.svuotaCarrello()




    def eliminaProdotto(self, index):
        self.lista_prodotti.pop(index)

    def svuotaCarrello(self):
        self.lista_prodotti.clear()








