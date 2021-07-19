from Menu.model.ListaProdotti import ListaProdotti


class ControllerListaProdotti():
    def __init__(self):
        super(ControllerListaProdotti, self).__init__()
        self.model = ListaProdotti()

    def get_bevande(self):
        return self.model.get_bevande()

    def get_cibi(self):
        return self.model.get_cibi()


