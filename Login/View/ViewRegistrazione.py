from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Login.Controller.ControllerLogin import ControllerLogin
from Login.Model.Login import Login


class Ui_Registrazione(object):
    def setupUi(self, Registrazione):
        Registrazione.setObjectName("Registrazione")
        Registrazione.resize(454, 215)
        Registrazione.setMinimumSize(QtCore.QSize(454, 215))
        Registrazione.setSizeIncrement(QtCore.QSize(1, 1))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 216, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 216, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 216, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        Registrazione.setPalette(palette)
        Registrazione.setAutoFillBackground(False)
        Registrazione.setSizeGripEnabled(False)
        Registrazione.setModal(False)
        self.formWidget = QtWidgets.QWidget(Registrazione)
        self.formWidget.setGeometry(QtCore.QRect(40, 30, 391, 101))
        self.formWidget.setObjectName("formWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(Registrazione)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Registrazione)
        self.label_4.setGeometry(QtCore.QRect(150, 0, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Registrazione)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 170, 93, 28))
        self.pushButton_2.setMinimumSize(QtCore.QSize(93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Registrazione)
        QtCore.QMetaObject.connectSlotsByName(Registrazione)

        model = Login("def", "def")
        self.controller = ControllerLogin(model)

        self.pushButton_2.clicked.connect(self.registrazione)

    def retranslateUi(self, Registrazione):
        _translate = QtCore.QCoreApplication.translate
        Registrazione.setWindowTitle(_translate("Registrazione", "Registrazione"))
        self.label.setText(_translate("Registrazione", "Email:"))
        self.label_2.setText(_translate("Registrazione", "Password:"))
        self.label_3.setText(_translate("Registrazione", "<html><head/><body><p><span style=\" color:#0055ff;\">Inserire email e password del nuovo account</span></p></body></html>"))
        self.label_4.setText(_translate("Registrazione", "Registrazione"))
        self.pushButton_2.setText(_translate("Registrazione", "Registrati"))




    def registrazione(self):
        app = self.lineEdit.text()
        self.controller.set_email(app)
        app = self.lineEdit_2.text()
        self.controller.set_password(app)
        if(self.controller.registrazione()) == 1:
            self.label_3.setText("<html><head/><body><p><span style=\" color:#ff0000;\">Email già esistente!</span></p></body></html>")
        else:
            self.popUp()


    def popUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Conferma")
        msg.setText("Registrazione Completata!")

        x = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Registrazione = QtWidgets.QDialog()
    ui = Ui_Registrazione()
    ui.setupUi(Registrazione)
    Registrazione.show()
    sys.exit(app.exec_())
