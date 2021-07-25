import datetime as dt
import json

from prenotazione.Model.Prenotazione   import PrenotazioneAttiva



class ControllerPrenotazioneAttiva:

        def __init__(self, login):
            self.Model = PrenotazioneAttiva(login)
            self.login = login

            now = dt.datetime.now().hour
            today = dt.datetime.today()
            tomorrow = today+dt.timedelta(days=1)


            if now > 17 or now < 6:
                filePath = 'prenotazione/Database/prenotazioni-' + tomorrow.strftime("%d-%m-%Y") + '.json'

            else:
                filePath = 'prenotazione/Database/prenotazioni-' + today.strftime("%d-%m-%Y") + '.json'

            with open(filePath, 'r') as o:
                orari = json.load(o)


                for orario in orari:
                    i = 1
                    for tavolo in orario['tavoli']:


                        if orario['tavoli'][tavolo]['email'] == self.login.getEmail() and orario['tavoli'][tavolo]['ora'] > 0:
                            self.Model.set_orario(str(orario["orario"]))
                            self.Model.set_data(today.strftime("%d-%m-%Y"))
                            stringa = "Tavolo " + str(i)
                            self.Model.set_tavolo(stringa)

                        i += 1



        def get_orario(self):
            return self.Model.get_orario()

        def get_tavolo(self):
            return self.Model.get_tavolo()

        def get_data(self):
            return self.Model.get_data()