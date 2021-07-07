class Prodotto():
    def __init__(self, nome, descrizione, immagine, valoriNutrizionali, listaIngredienti,
                 categoria, sottocategoria, prezzo, personalizzazioni):
        super(Prodotto, self).__init__()
        self.nome=nome
        self.descrizione=descrizione
        self.immagine=immagine
        self.valoriNutrizionali=valoriNutrizionali
        self.listaIngredienti=listaIngredienti
        self.categoria=categoria
        self.sottocategoria=sottocategoria
        self.prezzo=prezzo
        self.personalizzazioni=personalizzazioni