from Carrello.Model.Carrello import Carrello

class ControllerCarrello():
    def __init__(self, login):
        super(ControllerCarrello, self).__init__()
        self.Model = Carrello(login)

    def get_carrello(self):
        return self.Model.lista_prodotti

    def getAggiungi(self, Prodotto, personalizzazione):
        self.Model.aggiungi_al_carrello(Prodotto, personalizzazione)

    def getTotale(self):
        return self.Model.calcolaTotale()

    def svuotaCarrello(self):
        self.Model.svuotaCarrello()

    def Conferma(self):
        return self.Model.confermaOrdine()


    def getCodice(self):
        return self.Model.codice

    def eliminaProdotto(self,index):
        self.Model.eliminaProdotto(index)