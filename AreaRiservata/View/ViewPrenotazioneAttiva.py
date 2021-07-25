from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem

from prenotazione.Controller.ControllerPrenotazione import ControllerPrenotazioneAttiva




class Ui_PrenotazioniAttive(object):

    def __init__(self, login):
        self.login = login
        self.prenotazioni = ControllerPrenotazioneAttiva(self.login)


    def setupUi(self, PrenotazioniAttive):
        PrenotazioniAttive.setObjectName("PrenotazioniAttive")
        PrenotazioniAttive.resize(797, 601)
        self.listView = QtWidgets.QListView(PrenotazioniAttive)
        self.listView.setGeometry(QtCore.QRect(50, 80, 701, 421))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.listView.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(16)
        font.setItalic(True)
        self.listView.setFont(font)
        self.listView.setObjectName("listView")
        self.Carrello = QtWidgets.QLabel(PrenotazioniAttive)
        self.Carrello.setGeometry(QtCore.QRect(210, 10, 411, 51))
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
        self.Carrello.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(26)
        font.setItalic(True)
        self.Carrello.setFont(font)
        self.Carrello.setAccessibleName("")
        self.Carrello.setObjectName("Carrello")
        self.pushButton_3 = QtWidgets.QPushButton(PrenotazioniAttive)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 520, 301, 61))
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
        self.pushButton_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(24)
        font.setItalic(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(PrenotazioniAttive)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 520, 371, 61))
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
        self.pushButton_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(24)
        font.setItalic(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)

        self.retranslateUi(PrenotazioniAttive)
        QtCore.QMetaObject.connectSlotsByName(PrenotazioniAttive)


    def retranslateUi(self, PrenotazioniAttive):
        _translate = QtCore.QCoreApplication.translate
        PrenotazioniAttive.setWindowTitle(_translate("PrenotazioniAttive", "Prenotazioni Attive"))
        self.Carrello.setText(_translate("PrenotazioniAttive", "Prenotazioni Attive"))
        self.pushButton_3.setText(_translate("PrenotazioniAttive", "Indietro"))
        self.pushButton_4.setText(_translate("PrenotazioniAttive", "Elimina Prenotazione"))




        app = self.prenotazioni.get_orario
        app1 = self.prenotazioni.get_tavolo
        app2 = self.prenotazioni.get_data
        stringa = app1 + " ( " + app2 + " " + app + " )"
        item = QStandardItem()
        item.setText(stringa)
        item.setEditable(False)
        font = item.font()
        font.setPointSize(18)
        item.setFont(font)
        self.model.appendRow(item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PrenotazioniAttive = QtWidgets.QDialog()
    ui = Ui_PrenotazioniAttive()
    ui.setupUi(PrenotazioniAttive)
    PrenotazioniAttive.show()
    sys.exit(app.exec_())
