import json

class ControllerLogin():
    def __init__(self, login):
        self.model = login

    def set_email(self, email):
        self.model.email = email


    def set_password(self, password):
        self.model.password = password



    def is_logged(self):

        fileObject = open("Login/Database/DatabaseLogin.json", "r")
        jsonContent = fileObject.read()
        aList = json.loads(jsonContent)
        for i in aList:
            if aList[i]["email"] == self.model.email :
                if aList[i]["password"] == self.model.password :
                    self.model.role = aList[i]["role"]

        return self.model.role




