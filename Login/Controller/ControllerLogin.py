import json

class ControllerLogin():
    def __init__(self, login):
        self.model = login

    def set_email(self, email):
        self.model.setEmail(email)


    def set_password(self, password):
        self.model.setPassword(password)

    def getPassword(self):
        return self.model.password

    def getEmail(self):
        return self.model.email

    def getRole(self):
        return self.model.role



    def is_logged(self):

        fileObject = open("Login/Database/DatabaseLogin.json", "r")
        jsonContent = fileObject.read()
        aList = json.loads(jsonContent)
        self.model.setRole(None)
        for i in aList:
            if i["email"] == self.model.email and i["password"] == self.model.password :
                self.model.setRole(i["role"])








