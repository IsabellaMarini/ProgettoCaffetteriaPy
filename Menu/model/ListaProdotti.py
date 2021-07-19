import json


from Prodotto.Model.Prodotto import Prodotto


class ListaProdotti():


    def __init__(self):
        super(ListaProdotti, self).__init__()
        self.lista_bevande = []  # lista vuota nel momento dell'istanzazione
        self.lista_cibi = []

        with open("Menu/data/lista_prodotti_iniziali.json") as f: #file di configurazione iniziale
            lista_prodotti_iniziali = json.load(f)
        for prodotto_iniziale in lista_prodotti_iniziali:
            if prodotto_iniziale["categoria"]=="Bevande":
                self.aggiungi_bevanda(Prodotto(prodotto_iniziale["nome"],  prodotto_iniziale["immagine"],
                                                prodotto_iniziale["lista_ingredienti"],
                                                prodotto_iniziale["categoria"], prodotto_iniziale["sottocategoria"],
                                                prodotto_iniziale["prezzo"]))

            elif prodotto_iniziale["categoria"] =="Cibo":
                self.aggiungi_cibo(Prodotto(prodotto_iniziale["nome"],  prodotto_iniziale["immagine"],
                                                prodotto_iniziale["lista_ingredienti"],
                                                prodotto_iniziale["categoria"], prodotto_iniziale["sottocategoria"],
                                                prodotto_iniziale["prezzo"]))





    def aggiungi_bevanda(self, prodotto):
        self.lista_bevande.append(prodotto) #metodo che aggiunge un nuovo prodotto alla lista dei prodotti cioè il menu,mi serve per costruire la lista

    def aggiungi_cibo(self, prodotto):
        self.lista_cibi.append(prodotto)

    def get_cibo_by_index(self, index):
        return self.lista_cibi[index]

    def get_bevanda_by_index(self, index):
        return self.lista_bevande[index]

    def get_bevande(self):
        return self.lista_bevande

    def get_cibi(self):
        return self.lista_cibi