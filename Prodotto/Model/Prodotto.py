import json

p = json.load(open("Menu/data/lista_prodotti_iniziali.json"))

class Prodotto():

    def __init__(self, nome, immagine, listaIngredienti,
                 categoria, sottocategoria, prezzo):
        super(Prodotto, self).__init__()
        self.nome=nome
        self.immagine=immagine
        self.listaIngredienti=listaIngredienti
        self.categoria=categoria
        self.sottocategoria=sottocategoria
        self.prezzo=prezzo

        self.personalizzazioni = []

    def personalizza(self):
        with open("Prodotto/Database/personalizzazioni.json") as p:
            self.personalizzazioni = json.load(p)
        if (self.personalizzazioni.sottocategoria==self.sottocategoria):
            return self.personalizzazioni.personalizzazioni



 

    def get_nome(self):
        return self.nome

