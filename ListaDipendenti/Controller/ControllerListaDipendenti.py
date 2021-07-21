from ListaDipendenti.Model.ListaDipendenti import ListaDipendenti

class ControllerListaDipendenti():
    def __init__(self):
        super(ControllerListaDipendenti, self).__init__()
        self.Model= ListaDipendenti()



    def getListaDipendente(self):
        return self.Model.ListaCompleta()

    def getAggiungiDipendente(self):
        self.Model.aggiungiDipendente()

    def getEliminaDipendente(self, index):
        self.Model.eliminaDipendente()

    def Getdipendente_by_index(self, index):
        return self.Model.getdipendente_by_index()

