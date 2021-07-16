
from PyQt5 import QtCore, QtGui, QtWidgets


from Login.Controller import ControllerLogin

from Home.View import HomeCliente


class Ui_Login(object):
    def setupUi(self, Login):
        self.controller = None
        Login.setObjectName("Login")
        Login.resize(454, 215)
        Login.setMinimumSize(QtCore.QSize(454, 215))
        Login.setSizeIncrement(QtCore.QSize(1, 1))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 216, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 216, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 216, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        Login.setPalette(palette)
        Login.setAutoFillBackground(False)
        Login.setSizeGripEnabled(False)
        Login.setModal(False)
        self.pushButton = QtWidgets.QPushButton(Login)
        self.pushButton.setGeometry(QtCore.QRect(180, 160, 93, 28))
        self.pushButton.setMinimumSize(QtCore.QSize(93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.formWidget = QtWidgets.QWidget(Login)
        self.formWidget.setGeometry(QtCore.QRect(40, 30, 391, 101))
        self.formWidget.setObjectName("formWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(140, 125, 211, 21))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        self.pushButton.clicked.connect(self.clicked)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.pushButton.setText(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "Email:"))
        self.label_2.setText(_translate("Login", "Password:"))
        self.label_3.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:9pt; color:#0055ff;\">Inserire email e password...</span></p></body></html>"))


    def clicked(self):
            self.controller.set_email = self.get_from_entry1
            self.controller.set_password = self.get_from_entry2
            if self.controller.is_logged == "Cliente":
                self.go_homeC
            else:
                self.errore()





    def go_homeC(self):
         self.home_cliente = HomeCliente()
         self.home_cliente.show()










    def get_from_entry1(self):
        return  self.lineEdit.text()

    def get_from_entry2(self):
        return  self.lineEdit_2.text()


    def errore(self):
        self.label_3.setText("<html><head/><body><p><span style=\" font-size:9pt; color:#ff0000;\">Email e/o password sbagliati!</span></p></body></html>")
        self.label_3.adjustSize()

