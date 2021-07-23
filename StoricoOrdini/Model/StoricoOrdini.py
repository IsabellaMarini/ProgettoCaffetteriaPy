import os
import pickle


class StoricoOrdiniModel():
    def __init__(self):
        self.lista = []
        file_path = "StoricoOrdini/storicoOrdini.pickle"
        if os.stat(file_path).st_size != 0:
            with open(file_path, 'rb') as f:
                self.lista= pickle.load(f)
            f.close()

    def get_lista(self):
        return self.lista