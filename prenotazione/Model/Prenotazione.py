import datetime as dt
from Login.Model.Login import Login



class PrenotazioneAttiva():

    def __init__(self, login):
        self.login = login
        self.orario = None
        self.data = None
        self.tavolo = None



    def get_orario(self):
        return self.orario

    def get_tavolo(self):
        return self.tavolo

    def get_data(self):
        return self.data

    def set_orario(self, orario):
        self.orario = orario

    def set_tavolo(self, tavolo):
        self.tavolo = tavolo

    def set_data(self, data):
        self.data = data

