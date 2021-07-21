from PyQt5.QtGui import QStandardItem

from ListaDipendenti.Model.ListaDipendenti import ListaDipendenti
from ListaDipendenti.Controller.ControllerListaDipendenti import ControllerListaDipendenti

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListaDipendentiView(object):
    def __init__(self, Gestionedipendenti):
        self.gestionedipendenti = Gestionedipendenti

    def setupUi(self, ListaDipendentiView):
        ListaDipendentiView.setObjectName("ListaDipendentiView")
        ListaDipendentiView.resize(854, 642)
        self.label = QtWidgets.QLabel(ListaDipendentiView)
        self.label.setGeometry(QtCore.QRect(290, 30, 211, 71))
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
        self.listView.setGeometry(QtCore.QRect(180, 110, 421, 261))
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(ListaDipendentiView)
        self.pushButton.setGeometry(QtCore.QRect(140, 430, 151, 81))
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
        self.pushButton_2.setGeometry(QtCore.QRect(410, 430, 291, 81))
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

        self.controller = ControllerListaDipendenti()

        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)

        self.retranslateUi(ListaDipendentiView)
        QtCore.QMetaObject.connectSlotsByName(ListaDipendentiView)

        #self.pushButton.clicked.connect()
        #self.pushButton_2.clicked.connect()

    def retranslateUi(self, ListaDipendentiView):
        _translate = QtCore.QCoreApplication.translate
        ListaDipendentiView.setWindowTitle(_translate("ListaDipendentiView", "ListaDipendenti"))
        self.label.setText(_translate("ListaDipendentiView", "ListaDipendenti"))
        self.pushButton.setText(_translate("ListaDipendentiView", "Indietro"))
        self.pushButton_2.setText(_translate("ListaDipendentiView", "Aggiungi dipendente"))

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ListaDipendentiView = QtWidgets.QDialog()
    ui = Ui_ListaDipendentiView
    ui.setupUi(ListaDipendentiView)
    ListaDipendentiView.show()
    sys.exit(app.exec_())
