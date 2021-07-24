from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem

from AreaRiservata.View.ViewOrdine import Ui_ViewOrdine
from OrdiniAttivi.Controller.ControllerOrdiniAttivi import ControllerOrdiniAttivi


class Ui_OrdiniAttivi(object):
    def __init__(self, login):
        self.login = login
        self.ordini = ControllerOrdiniAttivi(self.login)


    def setupUi(self, OrdiniAttivi):
        OrdiniAttivi.setObjectName("OrdiniAttivi")
        OrdiniAttivi.resize(676, 562)
        self.listView = QtWidgets.QListView(OrdiniAttivi)
        self.listView.setGeometry(QtCore.QRect(50, 80, 571, 371))
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
        self.Carrello = QtWidgets.QLabel(OrdiniAttivi)
        self.Carrello.setGeometry(QtCore.QRect(210, 20, 251, 51))
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
        self.pushButton_3 = QtWidgets.QPushButton(OrdiniAttivi)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 470, 301, 61))
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

        self.retranslateUi(OrdiniAttivi)
        QtCore.QMetaObject.connectSlotsByName(OrdiniAttivi)

        self.pushButton_3.clicked.connect(self.clicked)




    def retranslateUi(self, OrdiniAttivi):
        _translate = QtCore.QCoreApplication.translate
        OrdiniAttivi.setWindowTitle(_translate("OrdiniAttivi", "OrdiniAttivi"))
        self.Carrello.setText(_translate("OrdiniAttivi", "Ordini Attivi"))
        self.pushButton_3.setText(_translate("OrdiniAttivi", "Visualizza Ordine"))

        for i in  self.ordini.ordiniCliente():

            app = i.codice
            item = QStandardItem()

            item.setText(app)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.model.appendRow(item)


    def clicked(self):
        selected = self.listView.selectedIndexes()[0].row()
        ordine = self.ordini.lista[selected]
        self.ViewOrdine = QtWidgets.QDialog()
        self.ui = Ui_ViewOrdine(ordine)
        self.ui.setupUi(self.ViewOrdine)
        self.ViewOrdine.show()