# This Python file uses the following encoding: utf-8
# Senior Design Embedded GUI file
import sys
from PyQt5 import *
from UIbasemainwindow import *



class SDMainWindow(Ui_MainWindow):
    def __init__(self):
        super().setupUi(MainWindow)



    def WelcomePage(self): #first widget
        #setting up page
        self.stackedWidget.setCurrentIndex(0)
        self.pb_TLeft.setEnabled(False)
        self.ScreenTitle.setText("Welcome")

        #actions
        self.pb_BarcodeTrue.clicked.connect(self.BarcodeScanningPage)
        self.pb_TRight.clicked.connect(self.LoginPage)



    def BarcodeScanningPage(self): #second widget
        #setting up page
        self.stackedWidget.setCurrentIndex(1)
        self.pb_TLeft.setEnabled(True)
        self.ScreenTitle.setText("Scanner")

        #actions
        self.pb_TLeft.clicked.connect(self.WelcomePage)
        self.pb_notworking.clicked.connect(self.KeyInTrackNumPage)
        self.pb_TRight.clicked.connect(self.LoginPage)

    def KeyInTrackNumPage(self): #third widget
        #actions
        def keypadinput( num): #Define logic for keypad input
            #print(num, ' pressed')
            self.TrackinglineEdit.setFocus()
            if num == '0':
                self.keybuffer = self.keybuffer[0:self.index] + '0' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 1:
                self.keybuffer = self.keybuffer[0:self.index] + '1' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 2:
                self.keybuffer = self.keybuffer[0:self.index] + '2' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 3:
                self.keybuffer = self.keybuffer[0:self.index] + '3' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 4:
                self.keybuffer = self.keybuffer[0:self.index] + '4' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 5:
                self.keybuffer = self.keybuffer[0:self.index] + '5' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 6:
                self.keybuffer = self.keybuffer[0:self.index] + '6' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 7:
                self.keybuffer = self.keybuffer[0:self.index] + '7' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 8:
                self.keybuffer = self.keybuffer[0:self.index] + '8' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 9:
                self.keybuffer = self.keybuffer[0:self.index] + '9' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1

            elif num == 'moveback':
                if self.index != 0:
                    self.index = self.index - 1

            elif num == 'moveforward':
                if not self.index >= len(self.keybuffer):
                    self.index = self.index + 1

            elif num == 'backspace':
                if self.index != 0:
                    self.index = self.index - 1
                    self.keybuffer = self.keybuffer[0:self.index] + self.keybuffer[self.index+1:len(self.keybuffer)]

            elif num == 'A':
                self.keybuffer = self.keybuffer[0:self.index] + 'A' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'B':
                self.keybuffer = self.keybuffer[0:self.index] + 'B' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'C':
                self.keybuffer = self.keybuffer[0:self.index] + 'C' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'D':
                self.keybuffer = self.keybuffer[0:self.index] + 'D' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'E':
                self.keybuffer = self.keybuffer[0:self.index] + 'E' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'F':
                self.keybuffer = self.keybuffer[0:self.index] + 'F' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'G':
                self.keybuffer = self.keybuffer[0:self.index] + 'G' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'H':
                self.keybuffer = self.keybuffer[0:self.index] + 'H' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'I':
                self.keybuffer = self.keybuffer[0:self.index] + 'I' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'J':
                self.keybuffer = self.keybuffer[0:self.index] + 'J' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'K':
                self.keybuffer = self.keybuffer[0:self.index] + 'K' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'L':
                self.keybuffer = self.keybuffer[0:self.index] + 'L' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'M':
                self.keybuffer = self.keybuffer[0:self.index] + 'M' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'N':
                self.keybuffer = self.keybuffer[0:self.index] + 'N' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'O':
                self.keybuffer = self.keybuffer[0:self.index] + 'O' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'P':
                self.keybuffer = self.keybuffer[0:self.index] + 'P' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'Q':
                self.keybuffer = self.keybuffer[0:self.index] + 'Q' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'R':
                self.keybuffer = self.keybuffer[0:self.index] + 'R' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'S':
                self.keybuffer = self.keybuffer[0:self.index] + 'S' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'T':
                self.keybuffer = self.keybuffer[0:self.index] + 'T' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'U':
                self.keybuffer = self.keybuffer[0:self.index] + 'U' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'V':
                self.keybuffer = self.keybuffer[0:self.index] + 'V' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'W':
                self.keybuffer = self.keybuffer[0:self.index] + 'W' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'X':
                self.keybuffer = self.keybuffer[0:self.index] + 'X' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            elif num == 'Y':
                self.keybuffer = self.keybuffer[0:self.index] + 'Y' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            else:
                self.keybuffer = self.keybuffer[0:self.index] + 'Z' + self.keybuffer[self.index:len(self.keybuffer)]
                self.index = self.index + 1
            self.TrackinglineEdit.setText(self.keybuffer)
            self.TrackinglineEdit.setCursorPosition(self.index)
        def ResetAndGoBack(): #reset buffer and index before returning to second widget
            self.keybuffer = ''
            self.index = 0
            self.BarcodeScanningPage()
        def getTrackingNumber(): #to return tracking number to core
            print(self.TrackinglineEdit.text())
            #return self.TrackinglineEdit.text()
        #setup
        def setup(): #setup third widget after functions are defined
            #connect all the pushbuttons to keypadinput()'s logic
            self.pb_num1.clicked.connect(lambda: keypadinput(1))
            self.pb_num2.clicked.connect(lambda: keypadinput(2))
            self.pb_num3.clicked.connect(lambda: keypadinput(3))
            self.pb_num4.clicked.connect(lambda: keypadinput(4))
            self.pb_num5.clicked.connect(lambda: keypadinput(5))
            self.pb_num6.clicked.connect(lambda: keypadinput(6))
            self.pb_num7.clicked.connect(lambda: keypadinput(7))
            self.pb_num8.clicked.connect(lambda: keypadinput(8))
            self.pb_num9.clicked.connect(lambda: keypadinput(9))
            self.pb_num0.clicked.connect(lambda: keypadinput('0'))
            self.pb_DEL.clicked.connect(lambda: keypadinput('backspace'))
            self.pb_movecursorforward.clicked.connect(lambda: keypadinput('moveforward'))
            self.pb_movecursorbackward.clicked.connect(lambda: keypadinput('moveback'))
            self.pb_A.clicked.connect(lambda: keypadinput('A'))
            self.pb_B.clicked.connect(lambda: keypadinput('B'))
            self.pb_C.clicked.connect(lambda: keypadinput('C'))
            self.pb_D.clicked.connect(lambda: keypadinput('D'))
            self.pb_E.clicked.connect(lambda: keypadinput('E'))
            self.pb_F.clicked.connect(lambda: keypadinput('F'))
            self.pb_G.clicked.connect(lambda: keypadinput('G'))
            self.pb_H.clicked.connect(lambda: keypadinput('H'))
            self.pb_I.clicked.connect(lambda: keypadinput('I'))
            self.pb_J.clicked.connect(lambda: keypadinput('J'))
            self.pb_K.clicked.connect(lambda: keypadinput('K'))
            self.pb_L.clicked.connect(lambda: keypadinput('L'))
            self.pb_M.clicked.connect(lambda: keypadinput('M'))
            self.pb_N.clicked.connect(lambda: keypadinput('N'))
            self.pb_O.clicked.connect(lambda: keypadinput('O'))
            self.pb_P.clicked.connect(lambda: keypadinput('P'))
            self.pb_Q.clicked.connect(lambda: keypadinput('Q'))
            self.pb_R.clicked.connect(lambda: keypadinput('R'))
            self.pb_S.clicked.connect(lambda: keypadinput('S'))
            self.pb_T.clicked.connect(lambda: keypadinput('T'))
            self.pb_U.clicked.connect(lambda: keypadinput('U'))
            self.pb_V.clicked.connect(lambda: keypadinput('V'))
            self.pb_W.clicked.connect(lambda: keypadinput('W'))
            self.pb_X.clicked.connect(lambda: keypadinput('X'))
            self.pb_Y.clicked.connect(lambda: keypadinput('Y'))
            self.pb_Z.clicked.connect(lambda: keypadinput('Z'))
            self.pb_TLeft.clicked.connect(ResetAndGoBack)
            self.pb_TRight.clicked.connect(self.LoginPage)
            self.pb_numEnter.clicked.connect(getTrackingNumber)
            #setting up page
            self.stackedWidget.setCurrentIndex(2)
            self.pb_TLeft.setEnabled(True)
            self.ScreenTitle.setText("Key in Tracking Number")
            self.TrackinglineEdit.setFocus()
            self.TrackinglineEdit.clear()
            self.keybuffer = ""
            self.index = 0
        setup() #setup call


    def LoginPage(self): #fourth widget
        #setup
        def setup():
            self.stackedWidget.setCurrentIndex(3)
            self.pb_TLeft.setEnabled(True)
            self.ScreenTitle.setText("Login")
            self.pb_TLeft.clicked.connect(self.WelcomePage)
        setup()




if __name__ == "__main__":  #execute application from class python file
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SDMainWindow()
    ui.WelcomePage()
    MainWindow.show()

    sys.exit(app.exec_())
