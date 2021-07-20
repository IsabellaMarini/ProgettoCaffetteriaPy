from Carrello.Model.Carrello import Carrello

class ControllerCarrello():
    def __init__(self):
        super(ControllerCarrello, self).__init__()
        self.Model = Carrello()

    def get_carrello(self):
        return self.Model.lista_prodotti

    def getAggiungi(self, Prodotto):
        self.Model.aggiungi_al_carrello(Prodotto)

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