from Carrello.Model.Carrello import Carrello

class ControllerCarrello():
    def __init__(self):
        super(ControllerCarrello, self).__init__()
        self.Model=Carrello()

    def get_carrello(self):
        return self.Model.lista_prodotti

    def getAggiungi(self, Prodotto):
        self.Model.aggiungi_al_carrello(Prodotto)

    def getTotale(self):
        return self.Model.calcolaTotale()

    def getEliminaProdotto(self):
        self.Model.rimuoviProdotto()

    def getConferma(self):
        return self.Model.confermaOrdine()

    def getEliminaOrdine(self):
        self.Model.eliminaOrdine()