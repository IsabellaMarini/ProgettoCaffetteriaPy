import json
import datetime as dt
import os


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QMessageBox


class ClickableLabel(QLabel):
    clicked = pyqtSignal()
    def __init__(self, parent=None):
        QLabel.__init__(self, parent=parent)
        self.clickable = True

    def mousePressEvent(self, event):
        self.clicked.emit()

    def setClickable(self, clickable):
        self.clickable = clickable

    def isClickable(self):
        return self.clickable



class Ui_PrenotazioneView(object):


    def __init__(self, login):
        self.login = login
        self.labelTable = []
        self.prenotabile = True
        self.orario_Prenotazione = -1

        now = dt.datetime.now().hour+1
        today = dt.datetime.today()
        if now > 17:
            today += dt.timedelta(days=1)

        self.filePath = 'prenotazione/Database/prenotazioni-' + today.strftime("%d-%m-%Y") + '.json'

        if not os.path.exists(self.filePath):
            with open('prenotazione/Database/prenotazioni-vuoto.json', 'r') as o:
                self.orari = json.load(o)
            with open(self.filePath, 'w') as o:
                json.dump(self.orari, o, ensure_ascii=False, indent=4)


        with open(self.filePath, 'r') as o:
            self.orari = json.load(o)

            for orario in self.orari:
                tav_num = 0

                if int(orario['orario'][:2]) < now:
                    continue

                for tavolo in orario['tavoli']:
                    if orario['tavoli'][tavolo]['email'] == self.login.getEmail():
                        self.prenotabile = False
                        self.orario_Prenotazione = int(orario['orario'][:2])

                    tav_num += 1


    def setupUi(self, PrenotazioneView):
        PrenotazioneView.setObjectName("PrenotazioneView")
        PrenotazioneView.resize(835, 629)
        self.timeEdit = QtWidgets.QTimeEdit(PrenotazioneView)
        self.timeEdit.setGeometry(QtCore.QRect(415, 54, 118, 24))
        now = dt.datetime.now().hour+1

        if now > 17 or now < 6:
            self.timeEdit.setMinimumTime(QtCore.QTime(6, 0, 0))

        else:
            self.timeEdit.setMinimumTime(QtCore.QTime(now, 0, 0))
        self.timeEdit.setMaximumTime(QtCore.QTime(17, 0, 0))



        self.timeEdit.setObjectName("timeEdit")
        self.label = QtWidgets.QLabel(PrenotazioneView)
        self.label.setGeometry(QtCore.QRect(330, 100, 161, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(208, 190, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 204, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 190, 111))
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
        self.frame = QtWidgets.QFrame(PrenotazioneView)
        self.frame.setGeometry(QtCore.QRect(100, 160, 631, 371))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = ClickableLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 71, 71))
        self.label_2.setText("tavolo1")
        self.label_2.setPixmap(QtGui.QPixmap("Pictures/TavoloI.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_4 = ClickableLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(280, 30, 71, 71))
        self.label_4.setText("tavolo2")
        self.label_4.setPixmap(QtGui.QPixmap("Pictures/TavoloI.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = ClickableLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(480, 30, 71, 71))
        self.label_5.setText("tavolo3")
        self.label_5.setPixmap(QtGui.QPixmap("Pictures/TavoloI.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = ClickableLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(80, 160, 71, 71))
        self.label_6.setText("tavolo4")
        self.label_6.setPixmap(QtGui.QPixmap("Pictures/TavoloI.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_8 = ClickableLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(280, 160, 71, 71))
        self.label_8.setText("tavolo5")
        self.label_8.setPixmap(QtGui.QPixmap("Pictures/TavoloI.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = ClickableLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(480, 160, 71, 71))
        self.label_9.setText("tavolo6")
        self.label_9.setPixmap(QtGui.QPixmap("Pictures/TavoloI.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = ClickableLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(80, 280, 64, 69))
        self.label_10.setText("tavolo7")
        self.label_10.setPixmap(QtGui.QPixmap("Pictures/TavoloE.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = ClickableLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(210, 280, 64, 69))
        self.label_11.setText("tavolo8")
        self.label_11.setPixmap(QtGui.QPixmap("Pictures/TavoloE.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = ClickableLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(350, 280, 64, 69))
        self.label_12.setText("tavolo9")
        self.label_12.setPixmap(QtGui.QPixmap("Pictures/TavoloE.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = ClickableLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(480, 280, 64, 69))
        self.label_13.setText("tavolo10")
        self.label_13.setPixmap(QtGui.QPixmap("Pictures/TavoloE.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(PrenotazioneView)
        self.pushButton.setGeometry(QtCore.QRect(330, 550, 161, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(219, 188, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(219, 188, 124))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(148, 148, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Al Bayan")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(PrenotazioneView)
        self.label_7.setGeometry(QtCore.QRect(250, 30, 160, 70))
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
        self.label_7.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(18)
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setTextFormat(QtCore.Qt.PlainText)
        self.label_7.setObjectName("label_7")

        font2 = QtGui.QFont()
        font2.setFamily("Harlow Solid Italic")
        font2.setPointSize(13)
        font2.setItalic(True)
        self.label_15 = QtWidgets.QLabel(PrenotazioneView)
        self.label_15.setGeometry(QtCore.QRect(250, 60, 260, 70))
        self.label_15.setFont(font2)
        self.label_15.setTextFormat(QtCore.Qt.PlainText)
        self.label_15.setObjectName("label_15")
        self.label_15.setPalette(palette)

        self.retranslateUi(PrenotazioneView)
        QtCore.QMetaObject.connectSlotsByName(PrenotazioneView)

        self.labelTable.append(self.label_2)
        self.labelTable.append(self.label_4)
        self.labelTable.append(self.label_5)
        self.labelTable.append(self.label_6)
        self.labelTable.append(self.label_8)
        self.labelTable.append(self.label_9)
        self.labelTable.append(self.label_10)
        self.labelTable.append(self.label_11)
        self.labelTable.append(self.label_12)
        self.labelTable.append(self.label_13)

        self.label_2.clicked.connect(lambda: self.selezionaTavoloUpdate(1))
        self.label_4.clicked.connect(lambda: self.selezionaTavoloUpdate(2))
        self.label_5.clicked.connect(lambda: self.selezionaTavoloUpdate(3))
        self.label_6.clicked.connect(lambda: self.selezionaTavoloUpdate(4))
        self.label_8.clicked.connect(lambda: self.selezionaTavoloUpdate(5))
        self.label_9.clicked.connect(lambda: self.selezionaTavoloUpdate(6))
        self.label_10.clicked.connect(lambda: self.selezionaTavoloUpdate(7))
        self.label_11.clicked.connect(lambda: self.selezionaTavoloUpdate(8))
        self.label_12.clicked.connect(lambda: self.selezionaTavoloUpdate(9))
        self.label_13.clicked.connect(lambda: self.selezionaTavoloUpdate(10))
        self.timeEdit.timeChanged.connect(lambda: self.sceltaOrarioUpdate())
        self.pushButton.clicked.connect(self.confermaButton)
        self.sceltaOrarioUpdate()


    def sceltaOrarioUpdate(self):

        with open(self.filePath, 'r') as o:
            self.orari = json.load(o)
            self.orario_scelto = self.timeEdit.time() #orario selezionato
            self.orario_str= self.orario_scelto.toString("HH:00") #converto in str per poter fare confronto
            for orario in self.orari:
                if orario['orario'] == self.orario_str:
                    tav_num = 0
                    for tavolo in orario['tavoli']:

                        if orario['tavoli'][tavolo]['email'] == self.login.getEmail():

                            self.labelTable[tav_num].setClickable(False)
                            if tav_num < 6:
                                self.labelTable[tav_num].setPixmap(QtGui.QPixmap("Pictures/TavoloI_c.png"))
                            else:
                                self.labelTable[tav_num].setPixmap(QtGui.QPixmap("Pictures/TavoloE_c.png"))

                        elif orario['tavoli'][tavolo]['email'] != None:

                            self.labelTable[tav_num].setClickable(False)
                            if tav_num < 6:
                                self.labelTable[tav_num].setPixmap(QtGui.QPixmap("Pictures/TavoloI_x.png"))
                            else:
                                self.labelTable[tav_num].setPixmap(QtGui.QPixmap("Pictures/TavoloE_x.png"))

                        else:
                            self.labelTable[tav_num].setClickable(True)
                            if tav_num < 6:
                                self.labelTable[tav_num].setPixmap(QtGui.QPixmap("Pictures/TavoloI.png"))
                            else:
                                self.labelTable[tav_num].setPixmap(QtGui.QPixmap("Pictures/TavoloE.png"))

                        tav_num += 1
        self.selezionaTavoloUpdate(20)


    def selezionaTavoloUpdate(self, lab_num):

        self.tavoloScelto = 0

        '''if not self.prenotabile:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("Hai già una prenotazione attiva.")
            self.msg.setWindowTitle("Info Message")
            self.msg.show()
            print("Non puoi più prenotare")
            return
        '''
        i = 1
        for lab in self.labelTable:

            if i == lab_num and lab.isClickable() and self.prenotabile:
                self.tavoloScelto = lab_num
                lab.setStyleSheet("border: 3px solid blue")
            else:
                lab.setStyleSheet("border: 0px solid blue;")

            i += 1

    def confermaButton(self):
        self.orario_scelto = self.timeEdit.time()
        self.orario_str = self.orario_scelto.toString("HH:00")
        tavoloScelto = "tavolo"+str(self.tavoloScelto)
        email = self.login.getEmail()

        if not self.prenotabile:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("Hai già una prenotazione attiva per le ore "+str(self.orario_Prenotazione)+":00.")
            self.msg.setWindowTitle("Info Message")
            self.msg.show()
            print("Non puoi più prenotare")
            return

        print("Sono nel pulsante", self.tavoloScelto, "at", self.orario_str, "for", email)

        with open(self.filePath, 'r') as o:
            self.orari = json.load(o)

            for orario in self.orari:
                if orario['orario'] == self.orario_str:
                    # print("Orario scelto:", orario['orario'], " - ", orario['tavoli'])
                    for tavolo in orario['tavoli']:
                        if tavolo == tavoloScelto:
                            # print(orario['tavoli'][tavolo])
                             orario['tavoli'][tavolo]['email'] = email
                             orario['tavoli'][tavolo]['ora'] = int(orario['orario'][:2])
                             self.orario_Prenotazione = int(orario['orario'][:2])

                    #print(orario['tavoli'])


        with open(self.filePath, 'w') as o:
            json.dump(self.orari, o, ensure_ascii=False, indent=4)

        self.prenotabile = False
        self.sceltaOrarioUpdate()
        self.selezionaTavoloUpdate(20)


    def retranslateUi(self, PrenotazioneView):
        _translate = QtCore.QCoreApplication.translate
        PrenotazioneView.setWindowTitle(_translate("PrenotazioneView", "Prenotazione"))
        self.timeEdit.setDisplayFormat(_translate("PrenotazioneView", "HH:00"))
        self.label.setText(_translate("PrenotazioneView", "  Seleziona tavolo:"))
        self.pushButton.setText(_translate("PrenotazioneView", "Conferma"))
        now = dt.datetime.now().hour+1

        if now > 17:
            self.label_7.setText(_translate("PrenotazioneView", "Seleziona orario:*"))
            self.label_15.setText(_translate("PrenotazioneView", "*la prenotazione si riferisce a domani"))

        else:
            self.label_7.setText(_translate("PrenotazioneView", "Seleziona orario:"))
            self.label_15.setText(_translate("PrenotazioneView", ""))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PrenotazioneView = QtWidgets.QDialog()
    ui = Ui_PrenotazioneView()
    ui.setupUi(PrenotazioneView)
    PrenotazioneView.show()
    sys.exit(app.exec_())