import json
class ControllerProdotto():

    personalizzazioni= json.load(open"personalizzazioni.json")

    def __init__(self, Prodotto):
        self.model=Prodotto

    def getNome(self):
        return self.model.nome

    def getDescrizione(self):
        return self.model.descrizione

    def getImmagine(self):
        return self.model.immagine

    def getValoriNutrizionali(self):
        return self.model.valoriNutrizionali

    def getListaIngredienti(self):
        return self.model.listaIngredienti

    def getCategoria(self):
        return self.model.categoria

    def getSottocategoria(self):
        return self.model.sottocategoria

    def getPrezzo(self):
        return self.model.prezzo

    def getPersonalizzazioni(self):
        return self.model.personalizzazioni

    def setNome(self, nome):
        self.model.nome=nome

    def setDescrizione(self, descrizione):
        self.model.descrizione = descrizione

    def setImmagine(self, immagine):
        self.model.immagine = immagine

    def setValoriNutrizionali(self, valoriNutrizionali):
        self.model.valoriNutrizionali = valoriNutrizionali

    def setListaIngredienti(self, listaIngredienti):
        self.model.listaIngredienti = listaIngredienti

    def setCategoria(self, categoria):
        self.model.categoria = categoria

    def setSottocategoria(self, sottocategoria):
        self.model.sottocategoria = sottocategoria

    def setPrezzo(self, prezzo):
        self.model.prezzo = prezzo

    def setPersonalizzazioni(self, personalizzazioni):
        self.model.personalizzazioni = personalizzazioni

    def personalizza(self):


