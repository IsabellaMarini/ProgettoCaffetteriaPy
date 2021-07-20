class Personalizzazione():

    def __init__(self, tipo, prezzo):
        self.tipo = tipo
        self.prezzo = prezzo

    def setNew(self, tipo, prezzo):
        self.tipo=tipo
        self.prezzo = prezzo


    def get_tipo(self):
        return self.tipo

    def get_prezzo(self):
        return self.prezzo