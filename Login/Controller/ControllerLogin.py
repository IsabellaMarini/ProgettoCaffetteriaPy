import json
import pickle
import os
from Login.Model.Login import Login


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



        file_path = "Login/Database/login.pickle"
        if os.stat(file_path).st_size != 0:
            with open(file_path, 'rb') as f:
                aList = pickle.load(f)
            f.close()
        self.model.setRole(None)
        for i in aList:
            if i.email == self.model.email and i.password == self.model.password :
                self.model.setRole(i.role)








    def registrazione(self):
        file_path = "Login/Database/login.pickle"
        if os.stat(file_path).st_size != 0:
            with open(file_path, 'rb') as f:
                aList = pickle.load(f)
            f.close()
        for i in aList:
             if i.email == self.model.email:
                return 1

        self.model.setRole("Cliente")
        aList.append(self.model)
        with open('Login/Database/login.pickle', 'wb') as handle:
            pickle.dump(aList, handle, pickle.HIGHEST_PROTOCOL)
        handle.close()









