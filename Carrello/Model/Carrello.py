import random
from Prodotto.Model.Prodotto import Prodotto


class Carrello():

    def __init__(self):
        super(Carrello, self).__init__()
        self.lista_prodotti= []

    def aggiungi_al_carrello(self, prodotto_da_aggiugnere):
        self.lista_prodotti.append(prodotto_da_aggiugnere)

    def calcolaTotale(self):
        prezzi=[]
        for prodotto in self.lista_prodotti:
            prezzi.append(prodotto["prezzo"])
        costo=sum(prezzi)
        return costo

    def confermaOrdine(self):
        n=8
        codice=[]
        for i in range(n):
            numero=random.randint(1,10)
            codice.append(numero)
        return codice

    def rimuoviProdotto(self):
        for prodotto_da_eliminare in self.lista_prodotti:
            self.lista_prodotti.remove(Prodotto(
                prodotto_da_eliminare["nome"],
                prodotto_da_eliminare["immagine"],
                prodotto_da_eliminare["listaIngredienti"],
                prodotto_da_eliminare["categoria"],
                prodotto_da_eliminare["sottocategoria"],
                prodotto_da_eliminare["prezzo"]
            )
        )

    def eliminaOrdine(self, n):
        for i in range(n-1, -1, -1):
            self.lista_prodotti.remove(self.lista_prodotti[i])








