from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem







class Ui_CarrelloView(object):


    def __init__(self, carrello):
        self.controller = carrello

    def setupUi(self, CarrelloView):
        CarrelloView.setObjectName("CarrelloView")

        CarrelloView.resize(662, 559)

        self.pushButton = QtWidgets.QPushButton(CarrelloView)
        self.pushButton.setGeometry(QtCore.QRect(20, 480, 121, 61))
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
        font.setPointSize(18)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.listView = QtWidgets.QListView(CarrelloView)

        self.listView.setGeometry(QtCore.QRect(50, 80, 571, 311))
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
        self.Carrello = QtWidgets.QLabel(CarrelloView)
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
        font.setPointSize(24)
        font.setItalic(True)
        self.Carrello.setFont(font)
        self.Carrello.setAccessibleName("")
        self.Carrello.setObjectName("Carrello")
        self.pushButton_3 = QtWidgets.QPushButton(CarrelloView)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 480, 121, 61))
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
        font.setPointSize(18)
        font.setItalic(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(CarrelloView)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 480, 131, 61))
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
        font.setPointSize(18)
        font.setItalic(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(CarrelloView)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 480, 121, 61))
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
        font.setPointSize(18)
        font.setItalic(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(CarrelloView)

        self.label.setGeometry(QtCore.QRect(240, 410, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(18)

        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(CarrelloView)

        self.label_2.setGeometry(QtCore.QRect(350, 410, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(18)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")


        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)


        self.retranslateUi(CarrelloView)
        QtCore.QMetaObject.connectSlotsByName(CarrelloView)

        #self.pushButton.clicked.connect(Ui_ViewProdotto)
        #self.pushButton_2.clicked.connect()
        #self.pushButton_3.clicked.connect()
        #self.pushButton_4.clicked.connect()

    def retranslateUi(self, CarrelloView):
        _translate = QtCore.QCoreApplication.translate
        CarrelloView.setWindowTitle(_translate("CarrelloView", "CarrelloView"))
        self.pushButton.setText(_translate("CarrelloView", "Indietro"))
        self.Carrello.setText(_translate("CarrelloView", "Carrello"))
        self.pushButton_3.setText(_translate("CarrelloView", "Modifica"))
        self.pushButton_2.setText(_translate("CarrelloView", "Svuota"))
        self.pushButton_4.setText(_translate("CarrelloView", "Conferma"))

        self.label.setText(_translate("CarrelloView", "totale:"))
        stringa  = str(self.controller.getTotale()) + " €"
        self.label_2.setText(_translate("CarrelloView", stringa))


        for i in self.controller.get_carrello():
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

    def svouta(self):
        self.controller.svuotaCarrello()


    def conferma(self):
        print(self.controller.Conferma())

    def elimina(self):
        selected = self.listView.selectedIndexes()[0].row()
        self.controller.eliminaProdotto(selected)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CarrelloView= QtWidgets.QDialog()
    ui = Ui_CarrelloView()
    ui.setupUi(CarrelloView)
    CarrelloView.show()
    sys.exit(app.exec_())
