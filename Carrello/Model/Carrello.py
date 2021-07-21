import time
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
            ts = time.time()
            self.codice = self.login.getEmail()+ str(ts)
            print(self.codice)





    def eliminaProdotto(self, index):
        self.lista_prodotti.pop(index)

    def svuotaCarrello(self):
        self.lista_prodotti.clear()








