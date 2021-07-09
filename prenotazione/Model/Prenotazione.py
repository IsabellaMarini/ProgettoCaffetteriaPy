import json
listatavoli = json.load(open("listatavoli.json"))

class Prenotazione():

    def __init__(self, lista_tavoli, orario):
        super(Prenotazione, self).__init__()
        self.listatavoli.append(lista_tavoli)
        self.orario = orario



    def is_disponibile(self):
        if(listatavoli.disponibilità == 1):
            return "è disponibile"
        else:
            return "non è disponibile"

