import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Dipendente.Controller.ControllerDipendente import ControllerDipendente
from Dipendente.Model.Dipendente import Dipendente
from ListaDipendenti.Controller.ControllerListaDipendenti import ControllerListaDipendenti


class Ui_AggiungiDipendente(object):
    def __init__(self, controller, callback):
        super(Ui_AggiungiDipendente, self).__init__()
        self.controller2= controller
        self.callback=callback
    def setupUi(self, AggiungiDipendente):
        AggiungiDipendente.setObjectName("AggiungiDipendente")
        AggiungiDipendente.resize(1050, 669)
        self.ListView = QtWidgets.QListView(AggiungiDipendente)
        self.ListView.setGeometry(QtCore.QRect(220, 140, 491, 301))
        self.ListView.setObjectName("ListView")
        self.pushButton = QtWidgets.QPushButton(AggiungiDipendente)
        self.pushButton.setGeometry(QtCore.QRect(380, 470, 171, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(14)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(AggiungiDipendente)
        self.label.setGeometry(QtCore.QRect(380, 70, 251, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(14)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AggiungiDipendente)
        self.label_2.setGeometry(QtCore.QRect(250, 170, 81, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AggiungiDipendente)
        self.label_3.setGeometry(QtCore.QRect(250, 230, 101, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AggiungiDipendente)
        self.label_4.setGeometry(QtCore.QRect(250, 280, 111, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AggiungiDipendente)
        self.label_5.setGeometry(QtCore.QRect(250, 330, 81, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_5.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(AggiungiDipendente)
        self.label_6.setGeometry(QtCore.QRect(250, 380, 111, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(AggiungiDipendente)
        self.lineEdit.setGeometry(QtCore.QRect(360, 180, 291, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(AggiungiDipendente)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 240, 291, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(AggiungiDipendente)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 290, 291, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(AggiungiDipendente)
        self.lineEdit_4.setGeometry(QtCore.QRect(360, 340, 291, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(AggiungiDipendente)
        self.lineEdit_5.setGeometry(QtCore.QRect(360, 390, 291, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(AggiungiDipendente)
        QtCore.QMetaObject.connectSlotsByName(AggiungiDipendente)

        self.controller2 = ControllerListaDipendenti()
        self.controller = ControllerDipendente()

        self.pushButton.clicked.connect(self.aggiungi_dipendente)

    def retranslateUi(self, AggiungiDipendente):
        _translate = QtCore.QCoreApplication.translate
        AggiungiDipendente.setWindowTitle(_translate("AggiungiDipendente", "AggiungiDipendente"))
        self.pushButton.setText(_translate("AggiungiDipendente", "Conferma"))
        self.label.setText(_translate("AggiungiDipendente", "Aggiungi Dipendente"))
        self.label_2.setText(_translate("AggiungiDipendente", "Nome:"))
        self.label_3.setText(_translate("AggiungiDipendente", "Cognome:"))
        self.label_4.setText(_translate("AggiungiDipendente", "Numero:"))
        self.label_5.setText(_translate("AggiungiDipendente", "E-mail:"))
        self.label_6.setText(_translate("AggiungiDipendente", "Password:"))


    def aggiungi_dipendente(self):
        nome = self.lineEdit.text()

        cognome = self.lineEdit_2.text()

        numero = self.lineEdit_3.text()

        email = self.lineEdit_4.text()

        password = self.lineEdit_5.text()




        #if (
         #       nome == "" or cognome == "" or numero == "" or email == "" or password == "" ):
          #  QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                # QMessageBox.Ok, QMessageBox.Ok)
       # else:
        self.controller2.aggiungiDipendente(
            Dipendente( nome, cognome, numero, email, password))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AggiungiDipendente = QtWidgets.QDialog()
    ui = Ui_AggiungiDipendente()
    ui.setupUi(AggiungiDipendente)
    AggiungiDipendente.show()
    sys.exit(app.exec_())
