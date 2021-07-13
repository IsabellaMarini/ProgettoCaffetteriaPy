from Dipendente.Model.Dipendente import Dipendente


class ControllerDipendente():
    def __init__(self):
        super(ControllerDipendente, self).__init__()
        self.Model=Dipendente

    def getNome(self):
        return self.Model.nome

    def getCognome(self):
        return self.Model.cognome

    def getNumero(self):
        return self.Model.numero

    def getEmail(self):
        return self.Model.email

    def getPassword(self):
        return self.Model.password

    def setNome(self, nome):
        self.Model.nome=nome

    def setCognome(self, cognome):
        self.Model.cognome=cognome

    def setNumero(self, numero):
        self.Model.numero=numero

    def setEmail(self, email):
        self.Model.email=email
