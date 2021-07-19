from Prodotto.Model.Prodotto import Prodotto

class ControllerProdotto():

    def __init__(self,Prodotto):
        self.Model=Prodotto

    def getNome(self):
        return self.Model.nome



    def getListaIngredienti(self):
        return self.Model.listaIngredienti

    def getCategoria(self):
        return self.Model.categoria

    def getSottocategoria(self):
        return self.Model.sottocategoria

    def getPrezzo(self):
        return self.Model.prezzo

    def getPersonalizzazioni(self):
        return self.Model.personalizzazioni

    def setNome(self, nome):
        self.Model.nome=nome

    def setDescrizione(self, descrizione):
        self.Model.descrizione = descrizione

    def setImmagine(self, immagine):
        self.Model.immagine = immagine

    def setValoriNutrizionali(self, valoriNutrizionali):
        self.Model.valoriNutrizionali = valoriNutrizionali

    def setListaIngredienti(self, listaIngredienti):
        self.Model.listaIngredienti = listaIngredienti

    def setCategoria(self, categoria):
        self.Model.categoria = categoria

    def setSottocategoria(self, sottocategoria):
        self.Model.sottocategoria = sottocategoria

    def setPrezzo(self, prezzo):
        self.Model.prezzo = prezzo

    def setPersonalizzazioni(self, personalizzazioni):
        self.Model.personalizzazioni = personalizzazioni

    def getPersonalizza(self):
        self.Model.personalizza()






