import json



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

        self.personalizzazioni = self.personalizza()

    def personalizza(self):
        with open("Prodotto/Database/personalizzazioni.json") as f:
            personalizzazioni = json.load(f)
        for i in personalizzazioni:
            if i["sottocategoria"] == self.nome:
                return i["personalizzazioni"]



 

    def get_nome(self):
        return self.nome

