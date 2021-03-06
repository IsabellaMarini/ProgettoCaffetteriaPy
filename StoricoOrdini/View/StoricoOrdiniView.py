

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem

from AreaRiservata.View.ViewOrdine import Ui_ViewOrdine
from StoricoOrdini.Model.StoricoOrdini import StoricoOrdiniModel


class Ui_StoricoOrdini(object):


    def setupUi(self, StoricoOrdini):
        StoricoOrdini.setObjectName("StoricoOrdini")
        StoricoOrdini.resize(797, 601)
        self.listView = QtWidgets.QListView(StoricoOrdini)
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
        self.Carrello = QtWidgets.QLabel(StoricoOrdini)
        self.Carrello.setGeometry(QtCore.QRect(270, 20, 251, 51))
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
        self.pushButton_3 = QtWidgets.QPushButton(StoricoOrdini)
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

        self.lista = StoricoOrdiniModel()

        self.retranslateUi(StoricoOrdini)
        QtCore.QMetaObject.connectSlotsByName(StoricoOrdini)

        self.pushButton_3.clicked.connect(self.clicked)

    def retranslateUi(self, StoricoOrdini):
        _translate = QtCore.QCoreApplication.translate
        StoricoOrdini.setWindowTitle(_translate("StoricoOrdini", "Storico Ordini"))
        self.Carrello.setText(_translate("StoricoOrdini", "Storico Ordini"))
        self.pushButton_3.setText(_translate("StoricoOrdini", "Visualizza Ordine"))


        for i in  self.lista.lista:

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
        ordine = self.lista.lista[selected]
        self.ViewOrdine = QtWidgets.QDialog()
        self.ui = Ui_ViewOrdine(ordine)
        self.ui.setupUi(self.ViewOrdine)
        self.ViewOrdine.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StoricoOrdini = QtWidgets.QDialog()
    ui = Ui_StoricoOrdini()
    ui.setupUi(StoricoOrdini)
    StoricoOrdini.show()
    sys.exit(app.exec_())
