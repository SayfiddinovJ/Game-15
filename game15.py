from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300,350)

        self.lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,""]
        self.gr_lay = QGridLayout()
        self.h_lay = QHBoxLayout()
        self.true = QMessageBox()

        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        self.btn4 = QPushButton("4")
        self.btn5 = QPushButton("5")
        self.btn6 = QPushButton("6")
        self.btn7 = QPushButton("7")
        self.btn8 = QPushButton("8")
        self.btn9 = QPushButton("9")
        self.btn10 = QPushButton("10")
        self.btn11 = QPushButton("11")
        self.btn12 = QPushButton("12")
        self.btn13 = QPushButton("13")
        self.btn14 = QPushButton("14")
        self.btn15 = QPushButton("15")
        self.btn16 = QPushButton("")


        self.start = QPushButton("START")
        self.ochir = QPushButton("CLOSE")
        self.qayt = QPushButton("FIX")
        self.tek = QPushButton("CHECK")
        self.start.setFixedSize(70,50)
        self.ochir.setFixedSize(70,50)
        self.qayt.setFixedSize(70,50)
        self.tek.setFixedSize(70,50)

        self.lst_btn = [self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,self.btn11,self.btn12,self.btn13,self.btn14,self.btn15,self.btn16]
        
        k = 0
        for i in range(4):
            for j in range(4):
                self.gr_lay.addWidget(self.lst_btn[k],i,j)
                self.lst_btn[k].setFixedSize(70,70)
                k+=1
        
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1

        self.gr_lay.addWidget(self.start)
        self.gr_lay.addWidget(self.ochir)
        self.gr_lay.addWidget(self.qayt)
        self.gr_lay.addWidget(self.tek)
        self.setLayout(self.gr_lay)

        self.start.clicked.connect(self.boshla)
        self.ochir.clicked.connect(self.tugat)
        self.qayt.clicked.connect(self.qaytar)
        self.tek.clicked.connect(self.check_it)

        self.btn1.clicked.connect(self.bbtn1)
        self.btn2.clicked.connect(self.bbtn2)
        self.btn3.clicked.connect(self.bbtn3)
        self.btn4.clicked.connect(self.bbtn4)
        self.btn5.clicked.connect(self.bbtn5)
        self.btn6.clicked.connect(self.bbtn6)
        self.btn7.clicked.connect(self.bbtn7)
        self.btn8.clicked.connect(self.bbtn8)
        self.btn9.clicked.connect(self.bbtn9)
        self.btn10.clicked.connect(self.bbtn10)
        self.btn11.clicked.connect(self.bbtn11)
        self.btn12.clicked.connect(self.bbtn12)
        self.btn13.clicked.connect(self.bbtn13)
        self.btn14.clicked.connect(self.bbtn14)
        self.btn15.clicked.connect(self.bbtn15)
        self.btn16.clicked.connect(self.bbtn16)

    def bbtn1(self):
        a = ""
        b = ""
        if self.btn1.text()!="":
            if self.btn2.text()=="":
                a = self.btn1.text()
                self.btn1.setText(b)
                self.btn2.setText(a)
            elif self.btn5.text()=="":
                a = self.btn1.text()
                self.btn1.setText(b)
                self.btn5.setText(a)
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1
    def bbtn2(self):
        a = ""
        b = ""
        if self.btn2.text()!="":
            if self.btn1.text()=="":
                a = self.btn2.text()
                self.btn2.setText(b)
                self.btn1.setText(a)
            elif self.btn3.text()=="":
                a = self.btn2.text()
                self.btn2.setText(b)
                self.btn3.setText(a)
            elif self.btn6.text()=="":
                a = self.btn2.text()
                self.btn2.setText(b)
                self.btn6.setText(a)
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1
    def bbtn3(self):
        a = ""
        b = ""
        if self.btn3.text()!="":
            if self.btn2.text()=="":
                a = self.btn3.text()
                self.btn3.setText(b)
                self.btn2.setText(a)
            elif self.btn4.text()=="":
                a = self.btn3.text()
                self.btn3.setText(b)
                self.btn4.setText(a)
            elif self.btn7.text()=="":
                a = self.btn3.text()
                self.btn3.setText(b)
                self.btn7.setText(a)
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1
    def bbtn4(self):
        a = ""
        b = ""
        if self.btn4.text()!="":
            if self.btn3.text()=="":
                a = self.btn4.text()
                self.btn4.setText(b)
                self.btn3.setText(a)
            elif self.btn8.text()=="":
                a = self.btn4.text()
                self.btn4.setText(b)
                self.btn8.setText(a)
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1
    def bbtn5(self):
        a = ""
        b = ""
        if self.btn5.text()!="":
            if self.btn1.text()=="":
                a = self.btn5.text()
                self.btn5.setText(b)
                self.btn1.setText(a)
            elif self.btn6.text()=="":
                a = self.btn5.text()
                self.btn5.setText(b)
                self.btn6.setText(a)
            elif self.btn9.text()=="":
                a = self.btn5.text()
                self.btn5.setText(b)
                self.btn9.setText(a)
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1
    def bbtn6(self):
        a = ""
        b = ""
        if self.btn6.text()!="":
            if self.btn2.text()=="":
                a = self.btn6.text()
                self.btn6.setText(b)
                self.btn2.setText(a)
            elif self.btn7.text()=="":
                a = self.btn6.text()
                self.btn6.setText(b)
                self.btn7.setText(a)
            elif self.btn10.text()=="":
                a = self.btn6.text()
                self.btn6.setText(b)
                self.btn10.setText(a)
            elif self.btn5.text()=="":
                a = self.btn6.text()
                self.btn6.setText(b)
                self.btn5.setText(a)
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1
    def bbtn7(self):
        a = ""
        b = ""
        if self.btn7.text()!="":
            if self.btn3.text()=="":
                a = self.btn7.text()
                self.btn7.setText(b)
                self.btn3.setText(a)
            elif self.btn8.text()=="":
                a = self.btn7.text()
                self.btn7.setText(b)
                self.btn8.setText(a)
            elif self.btn11.text()=="":
                a = self.btn7.text()
                self.btn7.setText(b)
                self.btn11.setText(a)
            elif self.btn6.text()=="":
                a = self.btn7.text()
                self.btn7.setText(b)
                self.btn6.setText(a)
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1
    def bbtn8(self):
        a = ""
        b = ""
        if self.btn8.text()!="":
            if self.btn4.text()=="":
                a = self.btn8.text()
                self.btn8.setText(b)
                self.btn4.setText(a)
            elif self.btn7.text()=="":
                a = self.btn8.text()
                self.btn8.setText(b)
                self.btn7.setText(a)
            elif self.btn12.text()=="":
                a = self.btn8.text()
                self.btn8.setText(b)
                self.btn12.setText(a)
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1
    def bbtn9(self):
        a = ""
        b = ""
        if self.btn9.text()!="":
            if self.btn5.text()=="":
                a = self.btn9.text()
                self.btn9.setText(b)
                self.btn5.setText(a)
            elif self.btn10.text()=="":
                a = self.btn9.text()
                self.btn9.setText(b)
                self.btn10.setText(a)
            elif self.btn13.text()=="":
                a = self.btn9.text()
                self.btn9.setText(b)
                self.btn13.setText(a)
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1
    def bbtn10(self):
        a = ""
        b = ""
        if self.btn10.text()!="":
            if self.btn6.text()=="":
                a = self.btn10.text()
                self.btn10.setText(b)
                self.btn6.setText(a)
            elif self.btn11.text()=="":
                a = self.btn10.text()
                self.btn10.setText(b)
                self.btn11.setText(a)
            elif self.btn14.text()=="":
                a = self.btn10.text()
                self.btn10.setText(b)
                self.btn14.setText(a)
            elif self.btn9.text()=="":
                a = self.btn10.text()
                self.btn10.setText(b)
                self.btn9.setText(a)
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1
    def bbtn11(self):
        a = ""
        b = ""
        if self.btn11.text()!="":
            if self.btn7.text()=="":
                a = self.btn11.text()
                self.btn11.setText(b)
                self.btn7.setText(a)
            elif self.btn12.text()=="":
                a = self.btn11.text()
                self.btn11.setText(b)
                self.btn12.setText(a)
            elif self.btn15.text()=="":
                a = self.btn11.text()
                self.btn11.setText(b)
                self.btn15.setText(a)
            elif self.btn10.text()=="":
                a = self.btn11.text()
                self.btn11.setText(b)
                self.btn10.setText(a)
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1
    def bbtn12(self):
        a = ""
        b = ""
        if self.btn12.text()!="":
            if self.btn8.text()=="":
                a = self.btn12.text()
                self.btn12.setText(b)
                self.btn8.setText(a)
            elif self.btn16.text()=="":
                a = self.btn12.text()
                self.btn12.setText(b)
                self.btn16.setText(a)
            elif self.btn11.text()=="":
                a = self.btn12.text()
                self.btn12.setText(b)
                self.btn11.setText(a)
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1
    def bbtn13(self):
        a = ""
        b = ""
        if self.btn13.text()!="":
            if self.btn9.text()=="":
                a = self.btn13.text()
                self.btn13.setText(b)
                self.btn9.setText(a)
            elif self.btn14.text()=="":
                a = self.btn13.text()
                self.btn13.setText(b)
                self.btn14.setText(a)
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1
    def bbtn14(self):
        a = ""
        b = ""
        if self.btn14.text()!="":
            if self.btn13.text()=="":
                a = self.btn14.text()
                self.btn14.setText(b)
                self.btn13.setText(a)
            elif self.btn10.text()=="":
                a = self.btn14.text()
                self.btn14.setText(b)
                self.btn10.setText(a)
            elif self.btn15.text()=="":
                a = self.btn14.text()
                self.btn14.setText(b)
                self.btn15.setText(a)
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1
    def bbtn15(self):
        a = ""
        b = ""
        if self.btn15.text()!="":
            if self.btn14.text()=="":
                a = self.btn15.text()
                self.btn15.setText(b)
                self.btn14.setText(a)
            elif self.btn11.text()=="":
                a = self.btn15.text()
                self.btn15.setText(b)
                self.btn11.setText(a)
            elif self.btn16.text()=="":
                a = self.btn15.text()
                self.btn15.setText(b)
                self.btn16.setText(a)
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1
    def bbtn16(self):
        a = ""
        b = ""
        if self.btn16.text()!="":
            if self.btn15.text()=="":
                a = self.btn16.text()
                self.btn16.setText(b)
                self.btn15.setText(a)
            elif self.btn12.text()=="":
                a = self.btn16.text()
                self.btn16.setText(b)
                self.btn12.setText(a)
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1

    def check_it(self):
        self.lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,""]
        k = 0
        a = 0
        s = 0
        for i in self.lst:
            a = i
            if self.lst_btn[k].text()==str(a):
                s+=1
                if s==16:
                    self.true.setWindowTitle("Check")
                    self.true.setFixedSize(100,50)
                    self.true.setText("✅ You win!")
                else:
                    self.true.setWindowTitle("Check")
                    self.true.setFixedSize(100,50)
                    self.true.setText("❌ False")
            k+=1
        self.true.exec_()

    def qaytar(self):
        self.lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,""]
        k = 0
        a = 0
        for i in self.lst:
            a = i
            self.lst_btn[k].setText(str(a))
            k+=1
        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1
    
    def tugat(self):
        self.close()

    def boshla(self):
        random.shuffle(self.lst)
        k = 0
        a = 0
        for i in self.lst:
            a = i
            self.lst_btn[k].setText(str(a))
            k+=1

        a = 0
        for i in range(int(len(self.lst_btn))):
            if self.lst_btn[a].text()=="":
                self.lst_btn[a].setStyleSheet("background: white")
            else:
                self.lst_btn[a].setStyleSheet("background: black; color: white")
            a+=1

app = QApplication([])
win = MainWindow()
win.show()
app.exec_()