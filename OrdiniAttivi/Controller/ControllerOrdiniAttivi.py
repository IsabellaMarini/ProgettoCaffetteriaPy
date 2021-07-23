import pickle
import os
from OrdiniAttivi.Model import OrdiniAttivi
class ControllerOrdiniAttivi():
    def __init__(self, login):
        self.login = login
        self.lista = []
        self.lista_totale = []
        file_path = "OrdiniAttivi/Database/ordiniAttivi.pickle"
        if os.stat(file_path).st_size != 0:
            with open(file_path, 'rb') as f:
                self.lista_totale = pickle.load(f)
            f.close()

    def ordiniCliente(self):
        for i in self.lista_totale:

            app =i.codice
            app2 = self.login.getEmail()
            num = len(app2)
            print(app[0:num])
            if app[0:num] == app2 :
                self.lista.append(i)
        return self.lista


    def elimina_ordine(self, ordine):
        for i in self.lista_totale:
            if ordine == i :
                self.lista_totale.remove(i)
                self.lista.remove(i)

        with open('OrdiniAttivi/Database/ordiniAttivi.pickle', 'wb') as handle:
           pickle.dump(self.lista_totale, handle, pickle.HIGHEST_PROTOCOL)
        handle.close()


    def convalida_ordine(self, codice):
        for i in self.lista_totale:
            if codice == i.codice:
                app = i
                self.lista_totale.remove(i)
                with open('OrdiniAttivi/Database/ordiniAttivi.pickle', 'wb') as handle:
                    pickle.dump(self.lista_totale, handle, pickle.HIGHEST_PROTOCOL)
                handle.close()

                lista_app = []
                file_path = "StoricoOrdini/storicoOrdini.pickle"
                if os.stat(file_path).st_size != 0:
                    with open(file_path, 'rb') as f:

                        lista_app = pickle.load(f)
                    f.close()
                    for i in lista_app:
                        print(i.codice)

                with open(file_path, 'wb') as handle:

                    print(app)
                    print(app.codice)
                    print(app.lista_prodotti[0].nome)
                    lista_app.append(app)
                    pickle.dump(lista_app, handle, pickle.HIGHEST_PROTOCOL)
                handle.close()

                return app
        return 0