class ModelStoricoPrenotazioni():
    def __init__(self, prenotazioni, giorno):
        self.prenotazioni = prenotazioni
        self.giorno = giorno

    def get_prenotazioni(self):
        return self.prenotazioni

    def get_giorno(self):
        return self.giorno