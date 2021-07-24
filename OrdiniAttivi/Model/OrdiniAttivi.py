class OrdiniAttivi():
    def __init__(self, lista_prodotti, codice):
        self.lista_prodotti = lista_prodotti
        self.codice = codice

    def get_codice(self):
        return self.codice

    def get_lista(self):
        return self.lista_prodotti

    def get_totale(self):
        prezzi = []

        for prodotto in self.lista_prodotti:
            app = float(prodotto.prezzo)

            prezzi.append(app.__round__(2))
            app = float(prodotto.personalizzazione.prezzo)

            prezzi.append(app.__round__(2))
        costo = sum(prezzi)
        return costo.__round__(2)