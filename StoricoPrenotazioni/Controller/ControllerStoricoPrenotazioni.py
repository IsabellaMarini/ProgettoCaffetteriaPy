import json
from os import listdir
from os.path import isfile, join

from StoricoPrenotazioni.Model.ModelStoricoPrenotazioni import ModelStoricoPrenotazioni


class ControllerStoricoPrenotazioni():
    def __init__(self):
        self.lista = []

        onlyfiles = [f for f in listdir("prenotazione/Database") if isfile(join("prenotazione/Database", f))]

        for i in onlyfiles:
            if len(i) > 25:
                stringa = i[-15 : -5]
                print(stringa)

                n = 0
                appoggio = "prenotazione/Database/" + i
                print(appoggio)
                with open(appoggio, 'r') as o:
                    orari = json.load(o)

                    for orario in orari:

                        for tavolo in orario['tavoli']:

                            if orario['tavoli'][tavolo]['email'] != None :
                                n += 1
                o.close()
                app = ModelStoricoPrenotazioni(n, stringa)
                self.lista.append(app)

