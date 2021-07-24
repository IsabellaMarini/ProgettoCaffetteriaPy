import datetime as dt
import json

from PrenotazioniAttive.Model.PrenotazioneAttiva import PrenotazioneAttiva



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
                    for tavolo in orario['tavoli']:
                        if orario['tavoli'][tavolo]['email'] == self.login.getEmail() and orario['tavoli'][tavolo]['ora'] > now:
                            self.Model.set_orario(orario['tavoli'][tavolo]['ora'])
                            self.Model.set_data(today.strftime("%d-%m-%Y"))
                            self.Model.set_tavolo( orario['tavoli'][tavolo])

                            print(self.Model.orario)
                            print(self.Model.data)
                            print(self.Model.tavolo)



