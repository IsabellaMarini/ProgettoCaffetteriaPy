import json

class ControllerLogin():
    def __init__(self, login):
        self.model = login
        self.role = None


    def is_logged(self):

        fileObject = open("DatabaseLogin.json", "r")
        jsonContent = fileObject.read()
        aList = json.loads(jsonContent)
        for i in aList:
            if aList[i]["email"] == self.model.email :
                if aList[i]["password"] == self.model.password :
                    self.role = aList[i]["role"]

        return self.role




