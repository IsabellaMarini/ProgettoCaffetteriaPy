class OrdiniAttivi():
    def __init__(self, lista_prodotti, codice):
        self.lista_prodotti = lista_prodotti
        self.codice = codice

    def get_codice(self):
        return self.codice

    def get_lista(self):
        return self.lista_prodotti