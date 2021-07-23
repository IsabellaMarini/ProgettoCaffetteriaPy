
from PyQt5 import QtCore, QtGui, QtWidgets

from Home.View.HomeAmministratore import Ui_MainWindowAmministratore
from Home.View.HomeCliente import  Ui_MainWindowCliente
from Home.View.HomeDipendente import Ui_MainWindowDipendente

from Login.Controller.ControllerLogin import ControllerLogin
from Login.Model.Login import Login



class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(454, 215)
        Window.setMinimumSize(QtCore.QSize(454, 215))
        Window.setSizeIncrement(QtCore.QSize(1, 1))
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
        Window.setPalette(palette)
        Window.setAutoFillBackground(False)
        Window.setSizeGripEnabled(False)
        Window.setModal(False)
        self.pushButton = QtWidgets.QPushButton(Window)
        self.pushButton.setGeometry(QtCore.QRect(180, 160, 93, 28))
        self.pushButton.setMinimumSize(QtCore.QSize(93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.formWidget = QtWidgets.QWidget(Window)
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
        self.label_3 = QtWidgets.QLabel(Window)
        self.label_3.setGeometry(QtCore.QRect(140, 125, 211, 21))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)


        model = Login("def","def")
        self.controller = ControllerLogin(model)

        self.pushButton.clicked.connect(self.clicked)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Login"))
        self.pushButton.setText(_translate("Window", "Login"))
        self.label.setText(_translate("Window", "Email:"))
        self.label_2.setText(_translate("Window", "Password:"))
        self.label_3.setText(_translate("Window",
                                        "<html><head/><body><p><span style=\" font-size:9pt; color:#0055ff;\">Inserire email e password...</span></p></body></html>"))

    def clicked(self):
        app = self.lineEdit.text()
        self.controller.set_email(app)
        app = self.lineEdit_2.text()
        self.controller.set_password(app)
        self.controller.is_logged()
        if self.controller.getRole() == "Cliente":
           self.go_homeC()
        elif self.controller.getRole() == "Amministratore":
            self.go_homeA()
        elif self.controller.getRole() == "Dipendente":
            self.go_homeD()
        else:
            self.errore()


    def go_homeD(self):
        self.MainWindowDipendente = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowDipendente(self.controller)
        self.ui.setupUi(self.MainWindowDipendente)
        self.MainWindowDipendente.show()

    def go_homeA(self):
        self.MainWindowAmministratore = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowAmministratore()
        self.ui.setupUi(self.MainWindowAmministratore)
        self.MainWindowAmministratore.show()



    def go_homeC(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowCliente(self.controller)
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()



    def errore(self):
        self.label_3.setText("<html><head/><body><p><span style=\" font-size:9pt; color:#ff0000;\">Email e/o password sbagliati!</span></p></body></html>")
        self.label_3.adjustSize()

