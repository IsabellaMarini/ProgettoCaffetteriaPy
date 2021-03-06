from PyQt5 import QtCore, QtGui, QtWidgets

from AreaRiservata.View.ViewOrdiniAttivi import Ui_OrdiniAttivi
from AreaRiservata.View.ViewPrenotazioneAttiva import Ui_PrenotazioniAttive


class Ui_AreaRiservata(object):
    def __init__(self, login):
        self.login = login

    def setupUi(self, AreaRiservata):
        AreaRiservata.setObjectName("AreaRiservata")
        AreaRiservata.resize(578, 492)
        self.pushButton_2 = QtWidgets.QPushButton(AreaRiservata)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 310, 351, 121))
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
        self.pushButton_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(22)
        font.setItalic(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(AreaRiservata)
        self.label.setGeometry(QtCore.QRect(160, 40, 321, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(24)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(AreaRiservata)
        self.pushButton.setGeometry(QtCore.QRect(120, 150, 351, 121))
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
        font.setPointSize(22)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(AreaRiservata)
        QtCore.QMetaObject.connectSlotsByName(AreaRiservata)

        self.pushButton_2.clicked.connect(self.go_OrdiniAttivi)
        self.pushButton.clicked.connect(self.go_PrenotazioneAttiva)

    def retranslateUi(self, AreaRiservata):
        _translate = QtCore.QCoreApplication.translate
        AreaRiservata.setWindowTitle(_translate("AreaRiservata", "AreaRiservata"))
        self.pushButton_2.setText(_translate("AreaRiservata", "Ordini Attivi"))
        self.label.setText(_translate("AreaRiservata", "Area Riservata "))
        self.pushButton.setText(_translate("AreaRiservata", "Prenotazioni Attive"))


    def go_OrdiniAttivi(self):
        self.OrdiniAttivi = QtWidgets.QDialog()
        self.ui = Ui_OrdiniAttivi(self.login)
        self.ui.setupUi(self.OrdiniAttivi)
        self.OrdiniAttivi.show()


    def go_PrenotazioneAttiva(self):
        self.PrenotazioniAttive = QtWidgets.QDialog()
        self.ui = Ui_PrenotazioniAttive(self.login)
        self.ui.setupUi(self.PrenotazioniAttive)
        self.PrenotazioniAttive.show()