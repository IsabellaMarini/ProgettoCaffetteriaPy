import json

from Prodotto.Model.Personalizzazione import Personalizzazione


class Prodotto():

    def __init__(self, nome, immagine, listaIngredienti, listaIngredienti2, listaIngredienti3,
                 categoria, sottocategoria, prezzo):
        super(Prodotto, self).__init__()
        self.nome=nome
        self.immagine=immagine
        self.listaIngredienti1=listaIngredienti
        self.listaIngredienti2=listaIngredienti2
        self.listaIngredienti3=listaIngredienti3
        self.categoria=categoria
        self.sottocategoria=sottocategoria
        self.prezzo=prezzo
        self.personalizzazione = None
        self.personalizzazioni = []



    def personalizza(self):
        with open("Prodotto/Database/personalizzazione.json") as f:
            personalizzazioni = json.load(f)
        for i in personalizzazioni:
            if i["nome"] == self.nome:
                for n in i["personalizzazioni"]:
                    appoggio = Personalizzazione(n["tipo"],n["prezzo"])
                    self.personalizzazioni.append(appoggio)




 

    def get_nome(self):
        return self.nome

