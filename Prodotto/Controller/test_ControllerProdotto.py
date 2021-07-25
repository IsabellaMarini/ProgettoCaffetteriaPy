from unittest import TestCase

from Prodotto.Controller.ControllerProdotto import ControllerProdotto
from Prodotto.Model.Prodotto import Prodotto


class test_ControllerProdotto(TestCase):
    def test_Prodotto(self):
        self.Prodotto = Prodotto(nome="a", immagine = "a", listaIngredienti ="a", listaIngredienti2="", listaIngredienti3="",
                 categoria="a", sottocategoria="a", prezzo=1)
        self.Controller = ControllerProdotto(self.Prodotto)
        self.assertIsNone(self.Controller.Model.personalizzazioni)
