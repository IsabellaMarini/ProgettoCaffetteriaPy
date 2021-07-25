from unittest import TestCase


from Login.Controller.ControllerLogin import ControllerLogin
from Login.Model.Login import Login


class test_ControlloreCliente(TestCase):



    def test_LoginDipendente(self):
        self.Login = Login(email="3", password="3")
        self.ControllerLogin = ControllerLogin(self.Login)
        self.assertIsNone(self.ControllerLogin.getRole())
        self.ControllerLogin.is_logged()
        self.assertListEqual(self.ControllerLogin.getRole(), "Dipendente", msg="Corretto")

    def test_LoginCliente(self):
        self.Login = Login(email="1", password="1")
        self.ControllerLogin = ControllerLogin(self.Login)
        self.assertIsNone(self.ControllerLogin.getRole())
        self.ControllerLogin.is_logged()
        self.assertListEqual(self.ControllerLogin.getRole(), "Amministratore", msg="Corretto")

    def test_LoginPasswordSbagliata(self):
        self.Login = Login(email="2", password="1")
        self.ControllerLogin = ControllerLogin(self.Login)
        self.assertIsNone(self.ControllerLogin.getRole())
        self.ControllerLogin.is_logged()
        self.assertIsNone(self.ControllerLogin.getRole())

    def test_cliente(self):
        self.Login = Login(email="2", password="2")
        self.ControllerLogin = ControllerLogin(self.Login)
        self.assertIsNone(self.ControllerLogin.getRole())

