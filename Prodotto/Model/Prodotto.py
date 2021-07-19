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


    def personalizza(self):
        if (p.sottocategoria==self.sottocategoria):
            return p.personalizzazioni

    def get_nome(self):
        return self.nome
