

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QStandardItem

from Dipendente.View.ViewDipendente import Ui_ViewDipendente
from ListaDipendenti.Model.ListaDipendenti import ListaDipendenti
from ListaDipendenti.Controller.ControllerListaDipendenti import ControllerListaDipendenti

class Ui_ListaDipendentiView(object):
    def __init__(self, gestionedipendenti):
        self.gestionedipendenti = gestionedipendenti

    def setupUi(self, ListaDipendentiView):
        ListaDipendentiView.setObjectName("ListaDipendentiView")
        ListaDipendentiView.resize(1197, 671)
        self.label = QtWidgets.QLabel(ListaDipendentiView)
        self.label.setGeometry(QtCore.QRect(450, 30, 221, 71))
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
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(18)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listView = QtWidgets.QListView(ListaDipendentiView)
        self.listView.setGeometry(QtCore.QRect(350, 100, 421, 261))
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(ListaDipendentiView)
        self.pushButton.setGeometry(QtCore.QRect(10, 410, 151, 81))
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
        self.pushButton_2 = QtWidgets.QPushButton(ListaDipendentiView)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 410, 291, 81))
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
        self.pushButton_3 = QtWidgets.QPushButton(ListaDipendentiView)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 410, 261, 81))
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
        self.pushButton_4 = QtWidgets.QPushButton(ListaDipendentiView)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 410, 241, 81))
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

        self.controller = ControllerListaDipendenti()

        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)

        self.retranslateUi(ListaDipendentiView)
        QtCore.QMetaObject.connectSlotsByName(ListaDipendentiView)

        self.pushButton_3.clicked.connect(self.clicked)
        self.pushButton_4.clicked.connect(self.elimina)

    def retranslateUi(self, ListaDipendentiView):
        _translate = QtCore.QCoreApplication.translate
        ListaDipendentiView.setWindowTitle(_translate("ListaDipendentiView", "ListaDipendenti"))
        self.label.setText(_translate("ListaDipendentiView", "ListaDipendenti"))
        self.pushButton.setText(_translate("ListaDipendentiView", "Indietro"))
        self.pushButton_2.setText(_translate("ListaDipendentiView", "Aggiungi dipendente"))
        self.pushButton_3.setText(_translate("ListaDipendentiView", "Visualizza dipendente"))
        self.pushButton_4.setText(_translate("ListaDipendentiView", "Elimina dipendente"))

        self.aList = self.controller.getListaDipendente()
        for i in self.aList:
            app = i.get_dipendente()


            item = QStandardItem()
            item.setText(app)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.model.appendRow(item)


    def clicked(self):
        selected = self.listView.selectedIndexes()[0].row()
        dipendente_selezionato = self.controller.Getdipendente_by_index(selected)

        self.ViewDipendente = QtWidgets.QDialog()
        self.ui = Ui_ViewDipendente(dipendente_selezionato)
        self.ui.setupUi(self.ViewDipendente)
        self.ViewDipendente.show()


    def elimina(self):

        selected = self.listView.selectedIndexes()[0].row()
        self.controller.getEliminaDipendente(selected)
        self.model.clear()

        for i in self.controller.getListaDipendente():
            app = i.get_dipendente()

            item = QStandardItem()
            item.setText(app)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.model.appendRow(item)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ListaDipendentiView = QtWidgets.QDialog()
    ui = Ui_ListaDipendentiView()
    ui.setupUi(ListaDipendentiView)
    ListaDipendentiView.show()
    sys.exit(app.exec_())
