from ListaDipendenti.Model.ListaDipendenti import ListaDipendenti

class ControllerListaDipendenti():
    def __init__(self):
        super(ControllerListaDipendenti, self).__init__()
        self.Model= ListaDipendenti

    def getListaDipendente(self):
        self.Model.ListaDipendente()

    def getAggiungiDipendente(self):
        self.Model.aggiungiDipendente()

    def getEliminaDipendente(self):
        self.Model.eliminaDipendente()

