class Login():
    def __init__(self, email, password):
        super(Login, self).__init__()
        self.email = email
        self.password = password
        self.role = None

    def setEmail(self, email):
        self.email = email
    def setPassword(self, password):
        self.password = password

    def setRole(self, role):
        self.role = role



