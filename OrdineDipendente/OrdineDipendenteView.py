
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem

from OrdiniAttivi.Controller.ControllerOrdiniAttivi import ControllerOrdiniAttivi


class Ui_ViewOrdineDipendente(object):
    def __init__(self,lista):
        self.lista = lista
    def setupUi(self, ViewOrdineDipendente):
        ViewOrdineDipendente.setObjectName("ViewOrdineDipendente")
        ViewOrdineDipendente.resize(673, 518)
        self.listView = QtWidgets.QListView(ViewOrdineDipendente)
        self.listView.setGeometry(QtCore.QRect(50, 70, 571, 371))
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
        self.Carrello = QtWidgets.QLabel(ViewOrdineDipendente)
        self.Carrello.setGeometry(QtCore.QRect(160, 10, 401, 51))
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
        self.Carrello_4 = QtWidgets.QLabel(ViewOrdineDipendente)
        self.Carrello_4.setGeometry(QtCore.QRect(220, 460, 111, 51))
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
        self.Carrello_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(20)
        font.setItalic(True)
        self.Carrello_4.setFont(font)
        self.Carrello_4.setAccessibleName("")
        self.Carrello_4.setObjectName("Carrello_4")
        self.Carrello_5 = QtWidgets.QLabel(ViewOrdineDipendente)
        self.Carrello_5.setGeometry(QtCore.QRect(350, 460, 181, 51))
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
        self.Carrello_5.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(20)
        font.setItalic(True)
        self.Carrello_5.setFont(font)
        self.Carrello_5.setAccessibleName("")
        self.Carrello_5.setObjectName("Carrello_5")

        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)

        self.retranslateUi(ViewOrdineDipendente)
        QtCore.QMetaObject.connectSlotsByName(ViewOrdineDipendente)



    def retranslateUi(self, ViewOrdineDipendente):
        _translate = QtCore.QCoreApplication.translate
        ViewOrdineDipendente.setWindowTitle(_translate("ViewOrdineDipendente", "Ordine"))
        self.Carrello.setText(_translate("ViewOrdineDipendente", "Prodotti dell\'ordine"))
        self.Carrello_4.setText(_translate("ViewOrdineDipendente", "Totale:"))
        stringa = str(self.lista.get_totale()) + "€"
        self.Carrello_5.setText(_translate("ViewOrdineDipendente", stringa))

        for i in  self.lista.lista_prodotti:
            app1 = i.get_nome()
            app2 = i.personalizzazione.tipo

            app3 = float(i.prezzo)
            app4 = float(i.personalizzazione.prezzo)
            prezzo = app3 + app4
            app5 = str(prezzo)
            stri = app1 + " ( " + app2 + ")    " + app5 + "€"
            item = QStandardItem()
            item.setText(stri)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.model.appendRow(item)



