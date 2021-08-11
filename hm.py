from PyQt5 import QtWidgets
from hesapmakinesiui import Ui_Dialog

class Arayuz(QtWidgets.QMainWindow, Ui_Dialog):
    firstNumber = None
    secondNumber = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        # Toplama vb
        self.buttonArti.clicked.connect(self.aritmetik)
        self.buttonEksi.clicked.connect(self.aritmetik)
        self.buttonCarp.clicked.connect(self.aritmetik)
        self.buttonBol.clicked.connect(self.aritmetik)
        self.buttonArti.setCheckable(True)
        self.buttonEksi.setCheckable(True)
        self.buttonCarp.setCheckable(True)
        self.buttonBol.setCheckable(True)
        # Sayılar
        self.buttonSifir.clicked.connect(self.rakambasma)
        self.buttonBir.clicked.connect(self.rakambasma)
        self.buttonIki.clicked.connect(self.rakambasma)
        self.buttonUc.clicked.connect(self.rakambasma)
        self.buttonDort.clicked.connect(self.rakambasma)
        self.buttonBes.clicked.connect(self.rakambasma)
        self.buttonAlti.clicked.connect(self.rakambasma)
        self.buttonYedi.clicked.connect(self.rakambasma)
        self.buttonSekiz.clicked.connect(self.rakambasma)
        self.buttonDokuz.clicked.connect(self.rakambasma)
        # Hesapla
        self.buttonHesapla.clicked.connect(self.sonuc)
        # Sıfırla vb
        self.buttonSifirla.clicked.connect(self.sifirla) 
        self.buttonSifirla.setCheckable(True) 

    # Herhangi bir rakam butonuna basıldığında çalışacak fonksiyon
    def rakambasma(self):
        sender = self.sender()

        if (self.buttonArti.isChecked() or self.buttonEksi.isChecked() or self.buttonCarp.isChecked() or self.buttonBol.isChecked()) and (not self.secondNumber):
            self.label.setText(format(float(sender.text()), ".15g")) 
            self.secondNumber = True
        else:
            if (('.' in self.label.text()) and sender.text() == "0"):
                self.label.setText(format(float(self.label.text() + sender.text()), ".15"))
            else:
                self.label.setText(format(float(self.label.text() + sender.text()), ".15g")) 
     
    def aritmetik(self):
        sender = self.sender()
        self.firstNumber = float(self.label.text())
        sender.setChecked(True) 
    
    def sonuc(self):
        second = float(self.label.text())

        if self.buttonArti.isChecked():
            first = self.firstNumber + second
            self.label.setText(format(first, ".15g"))
            self.buttonArti.setChecked(False)
        elif self.buttonEksi.isChecked():
            first = self.firstNumber - second
            self.label.setText(format(first, ".15g"))
            self.buttonEksi.setChecked(False)
        elif self.buttonCarp.isChecked():
            first = self.firstNumber * second
            self.label.setText(format(first, ".15g"))
            self.buttonCarp.setChecked(False)
        elif self.buttonBol.isChecked():
            first = self.firstNumber / second
            self.label.setText(format(first, ".15g"))
            self.buttonBol.setChecked(False)  
    def sifirla(self):
        self.firstNumber = 0
        self.secondNumber = False
        self.buttonSifirla.setChecked(False)
        self.label.setText("0")