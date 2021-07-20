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
        with open("Prodotto/Database/personalizzazione.json") as f:
            personalizzazioni = json.load(f)
        for i in personalizzazioni:
            if i["nome"] == self.nome:

                for n in i["personalizzazione"]:
                    appoggio = Personalizzazione(n["tipo"],n["prezzo"])

                    self.personalizzazioni.append(appoggio)









    def personalizza(self, personalizzazione):
        self.personalizzazione = personalizzazione

    def get_personalizzazione_by_index(self, index):
        return self.personalizzazioni[index]



 

    def get_nome(self):
        return self.nome

