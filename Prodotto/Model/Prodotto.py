import json
p = json.load(open("personalizzazioni.json"))
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
        self.p.append(personalizzazioni)

    def personalizza(self):
        if (p.sottocategoria==self.sottocategoria):
            return p.personalizzazioni
