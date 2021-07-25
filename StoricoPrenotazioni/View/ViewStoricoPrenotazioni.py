from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem

from StoricoPrenotazioni.Controller.ControllerStoricoPrenotazioni import ControllerStoricoPrenotazioni


class Ui_StroricoPrenotazioni(object):
    def __init__(self):
        self.controller = ControllerStoricoPrenotazioni()
    def setupUi(self, StroricoPrenotazioni):
        StroricoPrenotazioni.setObjectName("StroricoPrenotazioni")
        StroricoPrenotazioni.resize(797, 601)
        self.listView = QtWidgets.QListView(StroricoPrenotazioni)
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
        self.Carrello = QtWidgets.QLabel(StroricoPrenotazioni)
        self.Carrello.setGeometry(QtCore.QRect(220, 20, 401, 51))
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
        self.pushButton_3 = QtWidgets.QPushButton(StroricoPrenotazioni)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 520, 301, 61))
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

        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)

        self.retranslateUi(StroricoPrenotazioni)
        QtCore.QMetaObject.connectSlotsByName(StroricoPrenotazioni)

        self.pushButton_3.clicked.connect(StroricoPrenotazioni.reject)

    def retranslateUi(self, StroricoPrenotazioni):
        _translate = QtCore.QCoreApplication.translate
        StroricoPrenotazioni.setWindowTitle(_translate("StroricoPrenotazioni", "Strorico Prenotazioni"))
        self.Carrello.setText(_translate("StroricoPrenotazioni", "Storico Prenotazioni"))
        self.pushButton_3.setText(_translate("StroricoPrenotazioni", "Indietro"))

        for i in  self.controller.lista:

            app = i.get_giorno()
            app2 = i.get_prenotazioni()
            stringa = "Prenotazioni:   " + str(app2) + " ( " + app + " )"
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
    StroricoPrenotazioni = QtWidgets.QDialog()
    ui = Ui_StroricoPrenotazioni()
    ui.setupUi(StroricoPrenotazioni)
    StroricoPrenotazioni.show()
    sys.exit(app.exec_())
