import json




class Prodotto():

    def __init__(self, nome, immagine, listaIngredienti,
                 categoria, sottocategoria, prezzo, personalizzazioni):
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