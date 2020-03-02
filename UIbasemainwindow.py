# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Benbo/Desktop/Python QT/rpi_app1 PyQT5/basemainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        MainWindow.setStyleSheet("QLabel {\n"
"    font: bold 28px Arial;\n"
"    background: transparent;\n"
"    color: #0055ff;\n"
"}\n"
"QLabel#Title {\n"
"    font: bold italic 36px Arial;\n"
"    color: #0055ff; /*Blue to use*/\n"
"}\n"
"\n"
"QWidget {\n"
"    background: #d4d4d4;\n"
"}\n"
"\n"
"/*****Pushbutton****/\n"
"\n"
"QPushButton {\n"
"    font: bold 22px Arial;\n"
"    color: black;\n"
"    border: 3px solid #8f8f91;\n"
"    border-radius: 8px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 74px;   /* 6 less because of the padding*/\n"
"    min-height: 44px; /* 6 less because of the padding*/\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:focus {\n"
"    color: black;\n"
"    border: 3px solid red;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: white;\n"
"    border: 3px solid #8f8f91;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0055ff, stop: 1 #003cb6);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #d4d4d4;\n"
"    border: 3px solid #d4d4d4;\n"
"}\n"
"\n"
"/****Spinbox*****/\n"
"QAbstractSpinBox {\n"
"    font: bold 28px Arial;\n"
"    background-color: white;\n"
"    border: 3px solid #bdc3c7;\n"
"    padding: 3px 3px;\n"
"    border-radius: 6px;\n"
"}\n"
"QAbstractSpinBox::up-button { width: 0px; }\n"
"QAbstractSpinBox::down-button { width: 0px; }\n"
"\n"
"QAbstractSpinBox:focus, QAbstractSpinBox:hover {\n"
"    border: 4px solid red;\n"
"}\n"
"\n"
"QAbstractSpinBox:read-only, QAbstractSpinBox:disabled {\n"
"    background-color: Gainsboro !important;\n"
"    color: black;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.gridLayout_2.addWidget(self.Title, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(50, 50))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Benbo/Desktop/Python QT/rpi_app1 PyQT5\\sd edit.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/Benbo/Desktop/Python QT/rpi_app1 PyQT5\\sd edit.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(10, 1, 10, 1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ScreenTitle = QtWidgets.QLabel(self.centralwidget)
        self.ScreenTitle.setMinimumSize(QtCore.QSize(400, 0))
        self.ScreenTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.ScreenTitle.setObjectName("ScreenTitle")
        self.gridLayout_3.addWidget(self.ScreenTitle, 0, 2, 1, 1)
        self.pb_TLeft = QtWidgets.QPushButton(self.centralwidget)
        self.pb_TLeft.setEnabled(True)
        self.pb_TLeft.setMinimumSize(QtCore.QSize(100, 50))
        self.pb_TLeft.setObjectName("pb_TLeft")
        self.gridLayout_3.addWidget(self.pb_TLeft, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 3, 1, 1)
        self.pb_TRight = QtWidgets.QPushButton(self.centralwidget)
        self.pb_TRight.setMinimumSize(QtCore.QSize(100, 50))
        self.pb_TRight.setObjectName("pb_TRight")
        self.gridLayout_3.addWidget(self.pb_TRight, 0, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.FirstPage = QtWidgets.QWidget()
        self.FirstPage.setStyleSheet("QPushButton {\n"
"    font: bold 22px Arial;\n"
"    color: black;\n"
"    border: 3px solid #8f8f91;\n"
"    border-radius: 8px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 74px;   /* 6 less because of the padding*/\n"
"    min-height: 144px; /* 6 less because of the padding*/\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:focus {\n"
"    color: black;\n"
"    border: 3px solid red;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: white;\n"
"    border: 3px solid #8f8f91;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0055ff, stop: 1 #003cb6);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #d4d4d4;\n"
"    border: 3px solid #d4d4d4;\n"
"}\n"
"")
        self.FirstPage.setObjectName("FirstPage")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.FirstPage)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_BarcodeTrue = QtWidgets.QPushButton(self.FirstPage)
        self.pb_BarcodeTrue.setMinimumSize(QtCore.QSize(100, 150))
        self.pb_BarcodeTrue.setObjectName("pb_BarcodeTrue")
        self.horizontalLayout.addWidget(self.pb_BarcodeTrue)
        self.pb_BarcodeFalse = QtWidgets.QPushButton(self.FirstPage)
        self.pb_BarcodeFalse.setMinimumSize(QtCore.QSize(100, 150))
        self.pb_BarcodeFalse.setObjectName("pb_BarcodeFalse")
        self.horizontalLayout.addWidget(self.pb_BarcodeFalse)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.FirstPage)
        self.ScanBarcode = QtWidgets.QWidget()
        self.ScanBarcode.setObjectName("ScanBarcode")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.ScanBarcode)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_Instruct1 = QtWidgets.QLabel(self.ScanBarcode)
        self.lbl_Instruct1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Instruct1.setObjectName("lbl_Instruct1")
        self.verticalLayout_2.addWidget(self.lbl_Instruct1)
        self.pb_notworking = QtWidgets.QPushButton(self.ScanBarcode)
        self.pb_notworking.setObjectName("pb_notworking")
        self.verticalLayout_2.addWidget(self.pb_notworking)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.frame = QtWidgets.QFrame(self.ScanBarcode)
        self.frame.setMinimumSize(QtCore.QSize(550, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2.addWidget(self.frame)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.ScanBarcode)
        self.KeyInTrackNum = QtWidgets.QWidget()
        self.KeyInTrackNum.setStyleSheet("QPushButton {\n"
"    font: bold 22px Arial;\n"
"    color: black;\n"
"    border: 3px solid #8f8f91;\n"
"    border-radius: 8px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 44px;   /* 6 less because of the padding*/\n"
"    min-height: 44px; /* 6 less because of the padding*/\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:focus {\n"
"    color: black;\n"
"    border: 3px solid red;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: white;\n"
"    border: 3px solid #8f8f91;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0055ff, stop: 1 #003cb6);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #d4d4d4;\n"
"    border: 3px solid #d4d4d4;\n"
"}\n"
"\n"
"/********Line Edit*********/\n"
"\n"
"QLineEdit {\n"
"  font: bold 16pt \"Liberation Sans Narrow\";\n"
"  color: black;\n"
"  border: 1px solid #ccc;\n"
"  padding: 3px 6px;\n"
"  border-radius: 8px;\n"
"  margin: 1%;\n"
"  background:white;\n"
"  /*background-color:transparent;*/\n"
"  border:4px solid #0055ff;\n"
"  min-height: 30px;\n"
"  max-height: 30px;\n"
"}\n"
"\n"
"QLineEdit:hover, QLineEdit:focus{background:none; border:4px solid red}\n"
"\n"
"QLineEdit:disabled{\n"
"  background:grey;\n"
"  border-right:4px solid #bbb;\n"
"  border-left:4px solid #bbb;\n"
"}\n"
"QLineEdit:read-only,QLineEdit:hover:read-only {\n"
"  background:url(:/images/ControlButtons/txbx_readonly.png) no-repeat center;\n"
"  border:3px solid #eee;  \n"
"  border-left: 4px solid #ddd;  \n"
"  border-right: 4px solid #ddd; \n"
"}\n"
"")
        self.KeyInTrackNum.setObjectName("KeyInTrackNum")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.KeyInTrackNum)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pb_movecursorbackward = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_movecursorbackward.setObjectName("pb_movecursorbackward")
        self.horizontalLayout_3.addWidget(self.pb_movecursorbackward)
        self.TrackinglineEdit = QtWidgets.QLineEdit(self.KeyInTrackNum)
        self.TrackinglineEdit.setMouseTracking(True)
        self.TrackinglineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.TrackinglineEdit.setText("")
        self.TrackinglineEdit.setDragEnabled(True)
        self.TrackinglineEdit.setObjectName("TrackinglineEdit")
        self.horizontalLayout_3.addWidget(self.TrackinglineEdit)
        self.pb_movecursorforward = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_movecursorforward.setObjectName("pb_movecursorforward")
        self.horizontalLayout_3.addWidget(self.pb_movecursorforward)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pb_num3 = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_num3.setObjectName("pb_num3")
        self.gridLayout_4.addWidget(self.pb_num3, 0, 2, 1, 1)
        self.pb_T = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_T.setObjectName("pb_T")
        self.gridLayout_4.addWidget(self.pb_T, 1, 4, 1, 1)
        self.pb_Y = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_Y.setObjectName("pb_Y")
        self.gridLayout_4.addWidget(self.pb_Y, 1, 5, 1, 1)
        self.pb_num2 = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_num2.setObjectName("pb_num2")
        self.gridLayout_4.addWidget(self.pb_num2, 0, 1, 1, 1)
        self.pb_E = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_E.setObjectName("pb_E")
        self.gridLayout_4.addWidget(self.pb_E, 1, 2, 1, 1)
        self.pb_num9 = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_num9.setObjectName("pb_num9")
        self.gridLayout_4.addWidget(self.pb_num9, 0, 8, 1, 1)
        self.pb_num7 = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_num7.setObjectName("pb_num7")
        self.gridLayout_4.addWidget(self.pb_num7, 0, 6, 1, 1)
        self.pb_A = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_A.setObjectName("pb_A")
        self.gridLayout_4.addWidget(self.pb_A, 2, 0, 1, 1)
        self.pb_W = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_W.setObjectName("pb_W")
        self.gridLayout_4.addWidget(self.pb_W, 1, 1, 1, 1)
        self.pb_num1 = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_num1.setObjectName("pb_num1")
        self.gridLayout_4.addWidget(self.pb_num1, 0, 0, 1, 1)
        self.pb_R = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_R.setObjectName("pb_R")
        self.gridLayout_4.addWidget(self.pb_R, 1, 3, 1, 1)
        self.pb_num6 = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_num6.setObjectName("pb_num6")
        self.gridLayout_4.addWidget(self.pb_num6, 0, 5, 1, 1)
        self.pb_Q = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_Q.setObjectName("pb_Q")
        self.gridLayout_4.addWidget(self.pb_Q, 1, 0, 1, 1)
        self.pb_num5 = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_num5.setObjectName("pb_num5")
        self.gridLayout_4.addWidget(self.pb_num5, 0, 4, 1, 1)
        self.pb_num8 = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_num8.setObjectName("pb_num8")
        self.gridLayout_4.addWidget(self.pb_num8, 0, 7, 1, 1)
        self.pb_num4 = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_num4.setObjectName("pb_num4")
        self.gridLayout_4.addWidget(self.pb_num4, 0, 3, 1, 1)
        self.pb_num0 = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_num0.setObjectName("pb_num0")
        self.gridLayout_4.addWidget(self.pb_num0, 0, 9, 1, 1)
        self.pb_U = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_U.setObjectName("pb_U")
        self.gridLayout_4.addWidget(self.pb_U, 1, 6, 1, 1)
        self.pb_I = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_I.setObjectName("pb_I")
        self.gridLayout_4.addWidget(self.pb_I, 1, 7, 1, 1)
        self.pb_K = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_K.setObjectName("pb_K")
        self.gridLayout_4.addWidget(self.pb_K, 2, 7, 1, 1)
        self.pb_O = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_O.setObjectName("pb_O")
        self.gridLayout_4.addWidget(self.pb_O, 1, 8, 1, 1)
        self.pb_P = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_P.setObjectName("pb_P")
        self.gridLayout_4.addWidget(self.pb_P, 1, 9, 1, 1)
        self.pb_S = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_S.setObjectName("pb_S")
        self.gridLayout_4.addWidget(self.pb_S, 2, 1, 1, 1)
        self.pb_D = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_D.setObjectName("pb_D")
        self.gridLayout_4.addWidget(self.pb_D, 2, 2, 1, 1)
        self.pb_F = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_F.setObjectName("pb_F")
        self.gridLayout_4.addWidget(self.pb_F, 2, 3, 1, 1)
        self.pb_G = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_G.setObjectName("pb_G")
        self.gridLayout_4.addWidget(self.pb_G, 2, 4, 1, 1)
        self.pb_H = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_H.setObjectName("pb_H")
        self.gridLayout_4.addWidget(self.pb_H, 2, 5, 1, 1)
        self.pb_J = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_J.setObjectName("pb_J")
        self.gridLayout_4.addWidget(self.pb_J, 2, 6, 1, 1)
        self.pb_L = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_L.setObjectName("pb_L")
        self.gridLayout_4.addWidget(self.pb_L, 2, 8, 1, 1)
        self.pb_M = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_M.setObjectName("pb_M")
        self.gridLayout_4.addWidget(self.pb_M, 3, 7, 1, 1)
        self.pb_N = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_N.setObjectName("pb_N")
        self.gridLayout_4.addWidget(self.pb_N, 3, 6, 1, 1)
        self.pb_B = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_B.setObjectName("pb_B")
        self.gridLayout_4.addWidget(self.pb_B, 3, 5, 1, 1)
        self.pb_V = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_V.setObjectName("pb_V")
        self.gridLayout_4.addWidget(self.pb_V, 3, 4, 1, 1)
        self.pb_C = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_C.setObjectName("pb_C")
        self.gridLayout_4.addWidget(self.pb_C, 3, 3, 1, 1)
        self.pb_X = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_X.setObjectName("pb_X")
        self.gridLayout_4.addWidget(self.pb_X, 3, 2, 1, 1)
        self.pb_Z = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_Z.setObjectName("pb_Z")
        self.gridLayout_4.addWidget(self.pb_Z, 3, 1, 1, 1)
        self.pb_numEnter = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_numEnter.setMinimumSize(QtCore.QSize(70, 50))
        self.pb_numEnter.setMaximumSize(QtCore.QSize(150, 150))
        self.pb_numEnter.setObjectName("pb_numEnter")
        self.gridLayout_4.addWidget(self.pb_numEnter, 3, 8, 1, 2)
        self.pb_DEL = QtWidgets.QPushButton(self.KeyInTrackNum)
        self.pb_DEL.setObjectName("pb_DEL")
        self.gridLayout_4.addWidget(self.pb_DEL, 2, 9, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.KeyInTrackNum)
        self.Login = QtWidgets.QWidget()
        self.Login.setStyleSheet("QPushButton {\n"
"    font: bold 22px Arial;\n"
"    color: black;\n"
"    border: 3px solid #8f8f91;\n"
"    border-radius: 8px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 44px;   /* 6 less because of the padding*/\n"
"    min-height: 44px; /* 6 less because of the padding*/\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:focus {\n"
"    color: black;\n"
"    border: 3px solid red;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: white;\n"
"    border: 3px solid #8f8f91;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0055ff, stop: 1 #003cb6);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #d4d4d4;\n"
"    border: 3px solid #d4d4d4;\n"
"}\n"
"\n"
"/********Line Edit*********/\n"
"\n"
"QLineEdit {\n"
"  font: bold 16pt \"Liberation Sans Narrow\";\n"
"  color: black;\n"
"  border: 1px solid #ccc;\n"
"  padding: 3px 6px;\n"
"  border-radius: 8px;\n"
"  margin: 1%;\n"
"  background:white;\n"
"  /*background-color:transparent;*/\n"
"  border:4px solid #0055ff;\n"
"  min-height: 30px;\n"
"  max-height: 30px;\n"
"}\n"
"\n"
"QLineEdit:hover, QLineEdit:focus{background:none; border:4px solid red}\n"
"\n"
"QLineEdit:disabled{\n"
"  background:grey;\n"
"  border-right:4px solid #bbb;\n"
"  border-left:4px solid #bbb;\n"
"}\n"
"QLineEdit:read-only,QLineEdit:hover:read-only {\n"
"  background:url(:/images/ControlButtons/txbx_readonly.png) no-repeat center;\n"
"  border:3px solid #eee;  \n"
"  border-left: 4px solid #ddd;  \n"
"  border-right: 4px solid #ddd; \n"
"}\n"
"")
        self.Login.setObjectName("Login")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Login)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.Login)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pb2_num8 = QtWidgets.QPushButton(self.Login)
        self.pb2_num8.setObjectName("pb2_num8")
        self.gridLayout_5.addWidget(self.pb2_num8, 7, 1, 1, 1)
        self.pb2_num2 = QtWidgets.QPushButton(self.Login)
        self.pb2_num2.setObjectName("pb2_num2")
        self.gridLayout_5.addWidget(self.pb2_num2, 0, 1, 1, 1)
        self.pb2_num5 = QtWidgets.QPushButton(self.Login)
        self.pb2_num5.setObjectName("pb2_num5")
        self.gridLayout_5.addWidget(self.pb2_num5, 3, 1, 1, 1)
        self.pb2_num4 = QtWidgets.QPushButton(self.Login)
        self.pb2_num4.setObjectName("pb2_num4")
        self.gridLayout_5.addWidget(self.pb2_num4, 3, 0, 1, 1)
        self.pb2_num9 = QtWidgets.QPushButton(self.Login)
        self.pb2_num9.setObjectName("pb2_num9")
        self.gridLayout_5.addWidget(self.pb2_num9, 7, 2, 1, 1)
        self.pb2_num7 = QtWidgets.QPushButton(self.Login)
        self.pb2_num7.setObjectName("pb2_num7")
        self.gridLayout_5.addWidget(self.pb2_num7, 7, 0, 1, 1)
        self.pb2_num1 = QtWidgets.QPushButton(self.Login)
        self.pb2_num1.setObjectName("pb2_num1")
        self.gridLayout_5.addWidget(self.pb2_num1, 0, 0, 1, 1)
        self.pb2_num = QtWidgets.QPushButton(self.Login)
        self.pb2_num.setObjectName("pb2_num")
        self.gridLayout_5.addWidget(self.pb2_num, 3, 2, 1, 1)
        self.pb2_num3 = QtWidgets.QPushButton(self.Login)
        self.pb2_num3.setObjectName("pb2_num3")
        self.gridLayout_5.addWidget(self.pb2_num3, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.stackedWidget.addWidget(self.Login)
        self.gridLayout.addWidget(self.stackedWidget, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Intelli-Parse"))
        self.Title.setText(_translate("MainWindow", "Intelli-Parse"))
        self.ScreenTitle.setText(_translate("MainWindow", "Title of Screen"))
        self.pb_TLeft.setText(_translate("MainWindow", "Go Back"))
        self.pb_TRight.setText(_translate("MainWindow", "Owner"))
        self.pb_BarcodeTrue.setText(_translate("MainWindow", "I have Tracking Barcode"))
        self.pb_BarcodeFalse.setText(_translate("MainWindow", "No Barcode"))
        self.lbl_Instruct1.setText(_translate("MainWindow", "Scan Here ->"))
        self.pb_notworking.setText(_translate("MainWindow", "Not Working?"))
        self.pb_movecursorbackward.setText(_translate("MainWindow", "<"))
        self.TrackinglineEdit.setPlaceholderText(_translate("MainWindow", "Enter Tracking Number Here"))
        self.pb_movecursorforward.setText(_translate("MainWindow", ">"))
        self.pb_num3.setText(_translate("MainWindow", "3"))
        self.pb_T.setText(_translate("MainWindow", "T"))
        self.pb_Y.setText(_translate("MainWindow", "Y"))
        self.pb_num2.setText(_translate("MainWindow", "2"))
        self.pb_E.setText(_translate("MainWindow", "E"))
        self.pb_num9.setText(_translate("MainWindow", "9"))
        self.pb_num7.setText(_translate("MainWindow", "7"))
        self.pb_A.setText(_translate("MainWindow", "A"))
        self.pb_W.setText(_translate("MainWindow", "W"))
        self.pb_num1.setText(_translate("MainWindow", "1"))
        self.pb_R.setText(_translate("MainWindow", "R"))
        self.pb_num6.setText(_translate("MainWindow", "6"))
        self.pb_Q.setText(_translate("MainWindow", "Q"))
        self.pb_num5.setText(_translate("MainWindow", "5"))
        self.pb_num8.setText(_translate("MainWindow", "8"))
        self.pb_num4.setText(_translate("MainWindow", "4"))
        self.pb_num0.setText(_translate("MainWindow", "0"))
        self.pb_U.setText(_translate("MainWindow", "U"))
        self.pb_I.setText(_translate("MainWindow", "I"))
        self.pb_K.setText(_translate("MainWindow", "K"))
        self.pb_O.setText(_translate("MainWindow", "O"))
        self.pb_P.setText(_translate("MainWindow", "P"))
        self.pb_S.setText(_translate("MainWindow", "S"))
        self.pb_D.setText(_translate("MainWindow", "D"))
        self.pb_F.setText(_translate("MainWindow", "F"))
        self.pb_G.setText(_translate("MainWindow", "G"))
        self.pb_H.setText(_translate("MainWindow", "H"))
        self.pb_J.setText(_translate("MainWindow", "J"))
        self.pb_L.setText(_translate("MainWindow", "L"))
        self.pb_M.setText(_translate("MainWindow", "M"))
        self.pb_N.setText(_translate("MainWindow", "N"))
        self.pb_B.setText(_translate("MainWindow", "B"))
        self.pb_V.setText(_translate("MainWindow", "V"))
        self.pb_C.setText(_translate("MainWindow", "C"))
        self.pb_X.setText(_translate("MainWindow", "X"))
        self.pb_Z.setText(_translate("MainWindow", "Z"))
        self.pb_numEnter.setText(_translate("MainWindow", "Enter"))
        self.pb_DEL.setText(_translate("MainWindow", "DEL"))
        self.pb2_num8.setText(_translate("MainWindow", "8"))
        self.pb2_num2.setText(_translate("MainWindow", "2"))
        self.pb2_num5.setText(_translate("MainWindow", "5"))
        self.pb2_num4.setText(_translate("MainWindow", "4"))
        self.pb2_num9.setText(_translate("MainWindow", "9"))
        self.pb2_num7.setText(_translate("MainWindow", "7"))
        self.pb2_num1.setText(_translate("MainWindow", "1"))
        self.pb2_num.setText(_translate("MainWindow", "6"))
        self.pb2_num3.setText(_translate("MainWindow", "3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
