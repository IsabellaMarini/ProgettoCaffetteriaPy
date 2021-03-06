from PyQt5 import QtCore, QtGui, QtWidgets

from Carrello.Controller.ControllerCarrello import ControllerCarrello
from ListaDipendenti.Controller.ControllerListaDipendenti import ControllerListaDipendenti
from ListaDipendenti.View.ViewListaDipendenti import Ui_ListaDipendentiView
from Menu.View.ViewMenuAmm import Ui_ViewMenuAmm
from StoricoOrdini.View.StoricoOrdiniView import Ui_StoricoOrdini
from StoricoPrenotazioni.View.ViewStoricoPrenotazioni import Ui_StroricoPrenotazioni


class Ui_MainWindowAmministratore(object):

    def __init__(self, login):
        self.login=login
        self.carrello=ControllerCarrello(self.login)

    def setupUi(self, MainWindowAmministratore):
        MainWindowAmministratore.setObjectName("MainWindowAmministratore")
        MainWindowAmministratore.resize(752, 551)
        MainWindowAmministratore.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindowAmministratore)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 130, 621, 371))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(50, 40, 231, 131))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 40, 231, 131))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 210, 231, 131))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 210, 231, 131))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 10, 291, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 204, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(206, 186, 115))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 204, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(18)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 60, 281, 81))
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
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(28)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.logo_3 = QtWidgets.QLabel(self.centralwidget)
        self.logo_3.setGeometry(QtCore.QRect(20, 10, 141, 141))
        self.logo_3.setText("")
        self.logo_3.setPixmap(QtGui.QPixmap("Pictures/logo.png"))
        self.logo_3.setScaledContents(True)
        self.logo_3.setObjectName("logo_3")
        MainWindowAmministratore.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowAmministratore)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 752, 26))
        self.menubar.setObjectName("menubar")
        MainWindowAmministratore.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowAmministratore)
        self.statusbar.setObjectName("statusbar")
        MainWindowAmministratore.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowAmministratore)
        QtCore.QMetaObject.connectSlotsByName(MainWindowAmministratore)

        self.pushButton_2.clicked.connect(self.go_gestionedipendenti)
        self.pushButton.clicked.connect(self.go_menuamministratore)
        self.pushButton_3.clicked.connect(self.go_storico_ordini)
        self.pushButton_4.clicked.connect(self.go_storico_prenotazioni)

    def retranslateUi(self, MainWindowAmministratore):
        _translate = QtCore.QCoreApplication.translate
        MainWindowAmministratore.setWindowTitle(_translate("MainWindowAmministratore", "Home"))
        self.pushButton.setText(_translate("MainWindowAmministratore", "Men??"))
        self.pushButton_2.setText(_translate("MainWindowAmministratore", "Gestione Dipendenti"))
        self.pushButton_3.setText(_translate("MainWindowAmministratore", "Storico Ordini"))
        self.pushButton_4.setText(_translate("MainWindowAmministratore", "Storico Prenotazioni"))
        self.label.setText(_translate("MainWindowAmministratore", "  Benvenuti nell\'app del "))
        self.label_2.setText(_translate("MainWindowAmministratore", "Penguin Caf??"))

    def go_gestionedipendenti(self):
        self.ListaDipendenti = QtWidgets.QDialog()
        self.ui = Ui_ListaDipendentiView()
        self.ui.setupUi(self.ListaDipendenti)
        self.ListaDipendenti.show()

    def go_menuamministratore(self):
        self.ViewMenuAmm = QtWidgets.QDialog()
        self.ui = Ui_ViewMenuAmm(self.carrello)
        self.ui.setupUi(self.ViewMenuAmm)
        self.ViewMenuAmm.show()


    def go_storico_ordini(self):
        self.StoricoOrdini = QtWidgets.QDialog()
        self.ui = Ui_StoricoOrdini()
        self.ui.setupUi(self.StoricoOrdini)
        self.StoricoOrdini.show()

    def go_storico_prenotazioni(self):
        self.StroricoPrenotazioni = QtWidgets.QDialog()
        self.ui = Ui_StroricoPrenotazioni()
        self.ui.setupUi(self.StroricoPrenotazioni)
        self.StroricoPrenotazioni.show()