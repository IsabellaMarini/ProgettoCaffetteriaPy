


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem

from Menu.controller.ControllerListaProdotti import ControllerListaProdotti


class Ui_ViewMenuAmm(object):
    def setupUi(self, ViewMenuAmm):
        ViewMenuAmm.setObjectName("ViewMenuAmm")
        ViewMenuAmm.resize(888, 688)
        self.pushButton_3 = QtWidgets.QPushButton(ViewMenuAmm)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 100, 331, 81))
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
        font.setPointSize(26)
        font.setItalic(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.listView = QtWidgets.QListView(ViewMenuAmm)
        self.listView.setGeometry(QtCore.QRect(140, 190, 681, 391))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.listView.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(14)
        font.setItalic(True)
        self.listView.setFont(font)
        self.listView.setObjectName("listView")
        self.pushButton_2 = QtWidgets.QPushButton(ViewMenuAmm)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 100, 331, 81))
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
        font.setPointSize(26)
        font.setItalic(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(ViewMenuAmm)
        self.pushButton.setGeometry(QtCore.QRect(190, 610, 231, 61))
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
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(ViewMenuAmm)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 610, 221, 61))
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
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")


        self.controller = ControllerListaProdotti()

        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)


        self.retranslateUi(ViewMenuAmm)
        QtCore.QMetaObject.connectSlotsByName(ViewMenuAmm)

        self.pushButton_2.clicked.connect(self.bevande)
        self.pushButton_3.clicked.connect(self.cibo)

    def retranslateUi(self, ViewMenuAmm):
        _translate = QtCore.QCoreApplication.translate
        ViewMenuAmm.setWindowTitle(_translate("ViewMenuAmm", "Menu"))
        self.pushButton_3.setText(_translate("ViewMenuAmm", "Cibo"))
        self.pushButton_2.setText(_translate("ViewMenuAmm", "Bevande"))
        self.pushButton.setText(_translate("ViewMenuAmm", "Elimina Prodotto"))
        self.pushButton_4.setText(_translate("ViewMenuAmm", "Aggiungi Prodotto"))


        self.aList = self.controller.get_bevande()
        for i in self.aList:
            app = i.get_nome()


            item = QStandardItem()
            item.setText(app)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.model.appendRow(item)



    def bevande(self):

        self.model.clear()
        self.aList = self.controller.get_bevande()
        for i in self.aList:
            app = i.get_nome()


            item = QStandardItem()
            item.setText(app)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.model.appendRow(item)

    def cibo(self):

        self.model.clear()
        self.aList = self.controller.get_cibi()
        for i in self.aList:
            app = i.get_nome()


            item = QStandardItem()
            item.setText(app)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.model.appendRow(item)

    def clicked(self):
        selected = self.listView.selectedIndexes()[0].row()



        if self.aList == self.controller.get_bevande():
            prodotto_selezionato = self.controller.get_bevanda_by_index(selected)
        else:
            prodotto_selezionato = self.controller.get_cibo_by_index(selected)



        self.ViewMenuAmm = QtWidgets.QDialog()
        self.ui = Ui_ViewMenuAmm(prodotto_selezionato, self.carrello)
        self.ui.setupUi(self.ViewProdotto)
        self.ViewProdotto.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewMenuAmm = QtWidgets.QDialog()
    ui = Ui_ViewMenuAmm()
    ui.setupUi(ViewMenuAmm)
    ViewMenuAmm.show()
    sys.exit(app.exec_())
