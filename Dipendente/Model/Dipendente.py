class Dipendente():
    def __init__(self, nome, cognome, numero, email, password):
        super(Dipendente, self).__init__()
        self.nome=nome
        self.cognome=cognome
        self.numero=numero
        self.email=email
        self.password=password

    def get_dipendente(self):
        stringa = self.nome + " " + self.cognome
        return stringa
