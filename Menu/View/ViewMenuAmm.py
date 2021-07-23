

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QStandardItem

from Prodotto.View.ViewPersonalizzazione import Ui_Personalizzazione
from Menu.controller.ControllerListaProdotti import ControllerListaProdotti

from Prodotto.View.ViewProdotto import Ui_ViewProdotto


class Ui_ViewMenuAmm(object):
    def __init__(self, carrello):
        self.carrello=carrello

    def setupUi(self, ViewMenuAmm):
        ViewMenuAmm.setObjectName("ViewMenuAmm")
        ViewMenuAmm.resize(1121, 660)
        self.pushButton_3 = QtWidgets.QPushButton(ViewMenuAmm)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 20, 331, 81))
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
        self.listView.setGeometry(QtCore.QRect(250, 120, 681, 391))
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
        self.pushButton_2.setGeometry(QtCore.QRect(150, 30, 331, 81))
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
        self.pushButton.setGeometry(QtCore.QRect(20, 530, 201, 61))
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
        self.pushButton_4 = QtWidgets.QPushButton(ViewMenuAmm)
        self.pushButton_4.setGeometry(QtCore.QRect(900, 530, 211, 61))
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
        font.setPointSize(14)
        font.setItalic(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(ViewMenuAmm)
        self.pushButton_5.setGeometry(QtCore.QRect(620, 530, 221, 61))
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
        self.pushButton_5.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(14)
        font.setItalic(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(ViewMenuAmm)
        self.pushButton_6.setGeometry(QtCore.QRect(280, 530, 301, 61))
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
        self.pushButton_6.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(14)
        font.setItalic(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")

        self.controller = ControllerListaProdotti()

        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)

        self.retranslateUi(ViewMenuAmm)
        QtCore.QMetaObject.connectSlotsByName(ViewMenuAmm)

        self.pushButton_2.clicked.connect(self.bevande)
        self.pushButton_3.clicked.connect(self.cibo)
        self.pushButton_5.clicked.connect(self.clicked)
        self.pushButton_6.clicked.connect(self.personalizza)

    def retranslateUi(self, ViewMenuAmm):
        _translate = QtCore.QCoreApplication.translate
        ViewMenuAmm.setWindowTitle(_translate("ViewMenuAmm", "Menu"))
        self.pushButton_3.setText(_translate("ViewMenuAmm", "Cibo"))
        self.pushButton_2.setText(_translate("ViewMenuAmm", "Bevande"))
        self.pushButton.setText(_translate("ViewMenuAmm", "Elimina Prodotto"))
        self.pushButton_4.setText(_translate("ViewMenuAmm", "Aggiungi Prodotto"))
        self.pushButton_5.setText(_translate("ViewMenuAmm", "Visualizza Prodotto"))
        self.pushButton_6.setText(_translate("ViewMenuAmm", "Visualizza personalizzazioni"))


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


        self.ViewProdotto= QtWidgets.QDialog()
        self.ui = Ui_ViewProdotto(prodotto_selezionato, self.carrello)
        self.ui.setupUi(self.ViewProdotto)
        self.ViewProdotto.show()


    def personalizza(self):
        self.Personalizzazione = QtWidgets.QDialog()
        self.ui = Ui_Personalizzazione(self.prodotto, self.carrello)
        self.ui.setupUi(self.Personalizzazione)
        self.Personalizzazione.show()

