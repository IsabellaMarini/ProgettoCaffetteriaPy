from Carrello.Model.Carrello import Carrello

class ControllerCarrello():
    def __init__(self):
        super(ControllerCarrello, self).__init__()
        self.Model=Carrello()

    def getAggiungi(self):
        self.Model.aggiungi_al_carrello()

    def getTotale(self):
        return self.Model.calcolaTotale()

    def getEliminaProdotto(self):
        self.Model.rimuoviProdotto()

    def getConferma(self):
        return self.Model.confermaOrdine()

    def getEliminaOrdine(self):
        self.Model.eliminaOrdine()