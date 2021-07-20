
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem

from Carrello.Model.Carrello import Carrello
from Carrello.Controller.ControllerCarrello import ControllerCarrello
from Prodotto.View.ViewProdotto import Ui_ViewProdotto


class Ui_CarrelloView(object):
    def __init__(self):
        self.model=Carrello
        self.controller=ControllerCarrello

    def setupUi(self, CarrelloView):
        CarrelloView.setObjectName("CarrelloView")
        CarrelloView.resize(968, 579)
        self.pushButton = QtWidgets.QPushButton(CarrelloView)
        self.pushButton.setGeometry(QtCore.QRect(140, 370, 121, 61))
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
        font.setPointSize(15)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.listView = QtWidgets.QListView(CarrelloView)
        self.listView.setGeometry(QtCore.QRect(360, 130, 256, 192))
        self.listView.setObjectName("listView")
        self.Carrello = QtWidgets.QLabel(CarrelloView)
        self.Carrello.setGeometry(QtCore.QRect(450, 70, 81, 31))
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
        font.setPointSize(15)
        font.setItalic(True)
        self.Carrello.setFont(font)
        self.Carrello.setAccessibleName("")
        self.Carrello.setObjectName("Carrello")
        self.pushButton_3 = QtWidgets.QPushButton(CarrelloView)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 370, 121, 61))
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
        font.setPointSize(15)
        font.setItalic(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(CarrelloView)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 370, 131, 61))
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
        font.setPointSize(15)
        font.setItalic(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(CarrelloView)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 370, 121, 61))
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
        font.setPointSize(15)
        font.setItalic(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(CarrelloView)
        QtCore.QMetaObject.connectSlotsByName(CarrelloView)

        self.pushButton.clicked.connect(Ui_ViewProdotto)
        self.pushButton_2.clicked.connect(self.controller.getEliminaOrdine())
        self.pushButton_3.clicked.connect(self.controller.getEliminaProdotto())
        self.pushButton_4.clicked.connect(self.controller.getConferma())

    def retranslateUi(self, CarrelloView):
        _translate = QtCore.QCoreApplication.translate
        CarrelloView.setWindowTitle(_translate("CarrelloView", "CarrelloView"))
        self.pushButton.setText(_translate("CarrelloView", "Indietro"))
        self.Carrello.setText(_translate("CarrelloView", "Carrello"))
        self.pushButton_3.setText(_translate("CarrelloView", "Modifica"))
        self.pushButton_2.setText(_translate("CarrelloView", "Svuota"))
        self.pushButton_4.setText(_translate("CarrelloView", "Conferma"))

        b=self.controller().getAggiungi()
        self.List=b

        for i in self.List:
            a = i.get_nome()

            item = QStandardItem()
            item.setText(a)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.model.appendRow(item)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CarrelloView= QtWidgets.QDialog()
    ui = Ui_CarrelloView()
    ui.setupUi(CarrelloView)
    CarrelloView().show()
    sys.exit(app.exec_())

