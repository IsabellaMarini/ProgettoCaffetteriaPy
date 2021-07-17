from PrenotazioneAttiva.Model.PrenotazioneAttiva import PrenotazioneAttiva


class ControllerPrenotazioneAttiva:

        def __init__(self):
            self.Model = PrenotazioneAttiva

        def get_prenotazione(self):
            return self.Model.prenotazione

        def get_login(self):
            return self.Model.login

        def get_show_prenotazione(self):
            return self.Model.show_prenotazione()