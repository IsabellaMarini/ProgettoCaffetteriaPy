import sys
from PyQt5 import QtWidgets
from Login.View.ViewLogin import Ui_Login

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
