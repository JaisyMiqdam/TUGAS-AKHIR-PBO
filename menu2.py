# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SEMUA(object):
    def setupUi(self, SEMUA):
        SEMUA.setObjectName("SEMUA")
        SEMUA.resize(713, 586)
        SEMUA.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(80, 80, 122);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(157, 0, 0);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(157, 0, 0);\n"
"\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(157, 0, 0);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(SEMUA)
        self.centralwidget.setStyleSheet("background-color: black;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setStyleSheet(" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(56, 56, 85);\n"
" }")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -691, 681, 1218))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(600, 1200))
        self.frame.setStyleSheet("background-color: rgb(90, 90, 90);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(-20, -10, 751, 91))
        self.label_4.setStyleSheet("background-color: black;\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QPushButton#searchButton {\n"
"    padding: 10px 20px;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#searchButton:hover {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QPushButton#searchButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QPushButton#searchButton:focus {\n"
"    outline: none;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(-30, 80, 770, 31))
        self.label_14.setStyleSheet("background-color: red")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 110, 671, 1091))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.HD1 = QtWidgets.QLabel(self.frame)
        self.HD1.setGeometry(QtCore.QRect(135, 165, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD1.setFont(font)
        self.HD1.setAutoFillBackground(False)
        self.HD1.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD1.setObjectName("HD1")
        self.HD2 = QtWidgets.QLabel(self.frame)
        self.HD2.setGeometry(QtCore.QRect(285, 165, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD2.setFont(font)
        self.HD2.setAutoFillBackground(False)
        self.HD2.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD2.setObjectName("HD2")
        self.HD3 = QtWidgets.QLabel(self.frame)
        self.HD3.setGeometry(QtCore.QRect(435, 165, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD3.setFont(font)
        self.HD3.setAutoFillBackground(False)
        self.HD3.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD3.setObjectName("HD3")
        self.FILM2 = QtWidgets.QLabel(self.frame)
        self.FILM2.setGeometry(QtCore.QRect(185, 158, 131, 181))
        self.FILM2.setText("")
        self.FILM2.setPixmap(QtGui.QPixmap(":/images/film2.png"))
        self.FILM2.setScaledContents(True)
        self.FILM2.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM2.setObjectName("FILM2")
        self.FILM3 = QtWidgets.QLabel(self.frame)
        self.FILM3.setGeometry(QtCore.QRect(335, 158, 131, 181))
        self.FILM3.setText("")
        self.FILM3.setPixmap(QtGui.QPixmap(":/images/film3.png"))
        self.FILM3.setScaledContents(True)
        self.FILM3.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM3.setObjectName("FILM3")
        self.ABU1 = QtWidgets.QLabel(self.frame)
        self.ABU1.setGeometry(QtCore.QRect(10, 125, 630, 800))
        self.ABU1.setAutoFillBackground(False)
        self.ABU1.setStyleSheet("background-color: rgba(255, 255, 255, 0.2);\n"
"    color: #000000;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    border-radius: 10px;")
        self.ABU1.setText("")
        self.ABU1.setObjectName("ABU1")
        self.JUDUL1 = QtWidgets.QLabel(self.frame)
        self.JUDUL1.setEnabled(True)
        self.JUDUL1.setGeometry(QtCore.QRect(40, 343, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL1.setFont(font)
        self.JUDUL1.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL1.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL1.setObjectName("JUDUL1")
        self.JUDUL2 = QtWidgets.QLabel(self.frame)
        self.JUDUL2.setGeometry(QtCore.QRect(190, 343, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL2.setFont(font)
        self.JUDUL2.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL2.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL2.setObjectName("JUDUL2")
        self.JUDUL3 = QtWidgets.QLabel(self.frame)
        self.JUDUL3.setGeometry(QtCore.QRect(349, 343, 105, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL3.setFont(font)
        self.JUDUL3.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL3.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL3.setObjectName("JUDUL3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(286, 933, 90, 15))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: red;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.GARIS_6 = QtWidgets.QLabel(self.frame)
        self.GARIS_6.setGeometry(QtCore.QRect(-60, 956, 751, 5))
        self.GARIS_6.setAutoFillBackground(False)
        self.GARIS_6.setStyleSheet("background-color: red;\n"
"    border-radius: 10px;\n"
"    padding: 5px;")
        self.GARIS_6.setText("")
        self.GARIS_6.setObjectName("GARIS_6")
        self.CR = QtWidgets.QLabel(self.frame)
        self.CR.setGeometry(QtCore.QRect(0, 1140, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.CR.setFont(font)
        self.CR.setStyleSheet("color: white; background-color: rgba(0, 0, 0, 0);\n"
"")
        self.CR.setAlignment(QtCore.Qt.AlignCenter)
        self.CR.setObjectName("CR")
        self.JUDUL4 = QtWidgets.QLabel(self.frame)
        self.JUDUL4.setGeometry(QtCore.QRect(499, 343, 105, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL4.setFont(font)
        self.JUDUL4.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL4.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL4.setObjectName("JUDUL4")
        self.HD5 = QtWidgets.QLabel(self.frame)
        self.HD5.setGeometry(QtCore.QRect(135, 415, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD5.setFont(font)
        self.HD5.setAutoFillBackground(False)
        self.HD5.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD5.setObjectName("HD5")
        self.HD6 = QtWidgets.QLabel(self.frame)
        self.HD6.setGeometry(QtCore.QRect(285, 415, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD6.setFont(font)
        self.HD6.setAutoFillBackground(False)
        self.HD6.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD6.setObjectName("HD6")
        self.FILM4 = QtWidgets.QLabel(self.frame)
        self.FILM4.setGeometry(QtCore.QRect(485, 158, 131, 181))
        self.FILM4.setText("")
        self.FILM4.setPixmap(QtGui.QPixmap(":/images/blacknight.png"))
        self.FILM4.setScaledContents(True)
        self.FILM4.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM4.setObjectName("FILM4")
        self.HD4 = QtWidgets.QLabel(self.frame)
        self.HD4.setGeometry(QtCore.QRect(585, 165, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD4.setFont(font)
        self.HD4.setAutoFillBackground(False)
        self.HD4.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD4.setObjectName("HD4")
        self.JUDUL5 = QtWidgets.QLabel(self.frame)
        self.JUDUL5.setGeometry(QtCore.QRect(40, 595, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL5.setFont(font)
        self.JUDUL5.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL5.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL5.setObjectName("JUDUL5")
        self.JUDUL6 = QtWidgets.QLabel(self.frame)
        self.JUDUL6.setGeometry(QtCore.QRect(198, 595, 105, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL6.setFont(font)
        self.JUDUL6.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL6.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL6.setObjectName("JUDUL6")
        self.FILM6 = QtWidgets.QLabel(self.frame)
        self.FILM6.setGeometry(QtCore.QRect(185, 410, 131, 181))
        self.FILM6.setText("")
        self.FILM6.setPixmap(QtGui.QPixmap(":/images/thegoblin.png"))
        self.FILM6.setScaledContents(True)
        self.FILM6.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM6.setObjectName("FILM6")
        self.FILM5 = QtWidgets.QLabel(self.frame)
        self.FILM5.setGeometry(QtCore.QRect(35, 410, 131, 181))
        self.FILM5.setText("")
        self.FILM5.setPixmap(QtGui.QPixmap(":/images/theguardian.png"))
        self.FILM5.setScaledContents(True)
        self.FILM5.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM5.setObjectName("FILM5")
        self.DESK = QtWidgets.QLabel(self.frame)
        self.DESK.setGeometry(QtCore.QRect(10, 990, 631, 141))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.DESK.setFont(font)
        self.DESK.setStyleSheet("color: white; background-color: rgba(0, 0, 0, 0);\n"
"")
        self.DESK.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DESK.setWordWrap(False)
        self.DESK.setObjectName("DESK")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(40, 85, 51, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAutoFillBackground(False)
        self.label_20.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);")
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(160, 85, 61, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(423, 85, 51, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_21.setAutoFillBackground(False)
        self.label_21.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(530, 85, 101, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_22.setAutoFillBackground(False)
        self.label_22.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(290, 85, 81, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.FILM7 = QtWidgets.QLabel(self.frame)
        self.FILM7.setGeometry(QtCore.QRect(335, 410, 131, 181))
        self.FILM7.setText("")
        self.FILM7.setPixmap(QtGui.QPixmap(":/images/ride On.png"))
        self.FILM7.setScaledContents(True)
        self.FILM7.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM7.setObjectName("FILM7")
        self.FILM8 = QtWidgets.QLabel(self.frame)
        self.FILM8.setGeometry(QtCore.QRect(485, 410, 131, 181))
        self.FILM8.setText("")
        self.FILM8.setPixmap(QtGui.QPixmap(":/images/Demon Slayer new.png"))
        self.FILM8.setScaledContents(True)
        self.FILM8.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM8.setObjectName("FILM8")
        self.FILM9 = QtWidgets.QLabel(self.frame)
        self.FILM9.setGeometry(QtCore.QRect(35, 660, 131, 181))
        self.FILM9.setText("")
        self.FILM9.setPixmap(QtGui.QPixmap(":/images/The God Of High School.png"))
        self.FILM9.setScaledContents(True)
        self.FILM9.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM9.setObjectName("FILM9")
        self.FILM10 = QtWidgets.QLabel(self.frame)
        self.FILM10.setGeometry(QtCore.QRect(185, 660, 131, 181))
        self.FILM10.setText("")
        self.FILM10.setPixmap(QtGui.QPixmap(":/images/Secret Invasion.png"))
        self.FILM10.setScaledContents(True)
        self.FILM10.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM10.setObjectName("FILM10")
        self.FILM11 = QtWidgets.QLabel(self.frame)
        self.FILM11.setGeometry(QtCore.QRect(335, 660, 131, 181))
        self.FILM11.setText("")
        self.FILM11.setPixmap(QtGui.QPixmap(":/images/skull island new.png"))
        self.FILM11.setScaledContents(True)
        self.FILM11.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM11.setObjectName("FILM11")
        self.FILM12 = QtWidgets.QLabel(self.frame)
        self.FILM12.setGeometry(QtCore.QRect(485, 660, 131, 181))
        self.FILM12.setText("")
        self.FILM12.setPixmap(QtGui.QPixmap(":/images/Manifest.png"))
        self.FILM12.setScaledContents(True)
        self.FILM12.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM12.setObjectName("FILM12")
        self.JUDUL9 = QtWidgets.QLabel(self.frame)
        self.JUDUL9.setEnabled(True)
        self.JUDUL9.setGeometry(QtCore.QRect(48, 845, 105, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL9.setFont(font)
        self.JUDUL9.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL9.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL9.setObjectName("JUDUL9")
        self.JUDUL7 = QtWidgets.QLabel(self.frame)
        self.JUDUL7.setEnabled(True)
        self.JUDUL7.setGeometry(QtCore.QRect(348, 595, 105, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL7.setFont(font)
        self.JUDUL7.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL7.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL7.setObjectName("JUDUL7")
        self.JUDUL8 = QtWidgets.QLabel(self.frame)
        self.JUDUL8.setEnabled(True)
        self.JUDUL8.setGeometry(QtCore.QRect(490, 595, 121, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL8.setFont(font)
        self.JUDUL8.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL8.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL8.setObjectName("JUDUL8")
        self.JUDUL10 = QtWidgets.QLabel(self.frame)
        self.JUDUL10.setEnabled(True)
        self.JUDUL10.setGeometry(QtCore.QRect(184, 845, 131, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL10.setFont(font)
        self.JUDUL10.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL10.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL10.setObjectName("JUDUL10")
        self.JUDUL11 = QtWidgets.QLabel(self.frame)
        self.JUDUL11.setEnabled(True)
        self.JUDUL11.setGeometry(QtCore.QRect(348, 845, 105, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL11.setFont(font)
        self.JUDUL11.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL11.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL11.setObjectName("JUDUL11")
        self.JUDUL12 = QtWidgets.QLabel(self.frame)
        self.JUDUL12.setEnabled(True)
        self.JUDUL12.setGeometry(QtCore.QRect(498, 845, 105, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL12.setFont(font)
        self.JUDUL12.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL12.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL12.setObjectName("JUDUL12")
        self.HD7 = QtWidgets.QLabel(self.frame)
        self.HD7.setGeometry(QtCore.QRect(435, 415, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD7.setFont(font)
        self.HD7.setAutoFillBackground(False)
        self.HD7.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD7.setObjectName("HD7")
        self.HD8 = QtWidgets.QLabel(self.frame)
        self.HD8.setGeometry(QtCore.QRect(585, 415, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD8.setFont(font)
        self.HD8.setAutoFillBackground(False)
        self.HD8.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD8.setObjectName("HD8")
        self.HD9 = QtWidgets.QLabel(self.frame)
        self.HD9.setGeometry(QtCore.QRect(135, 665, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD9.setFont(font)
        self.HD9.setAutoFillBackground(False)
        self.HD9.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD9.setObjectName("HD9")
        self.HD10 = QtWidgets.QLabel(self.frame)
        self.HD10.setGeometry(QtCore.QRect(285, 665, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD10.setFont(font)
        self.HD10.setAutoFillBackground(False)
        self.HD10.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD10.setObjectName("HD10")
        self.HD12 = QtWidgets.QLabel(self.frame)
        self.HD12.setGeometry(QtCore.QRect(585, 665, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD12.setFont(font)
        self.HD12.setAutoFillBackground(False)
        self.HD12.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD12.setObjectName("HD12")
        self.HD11 = QtWidgets.QLabel(self.frame)
        self.HD11.setGeometry(QtCore.QRect(435, 665, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD11.setFont(font)
        self.HD11.setAutoFillBackground(False)
        self.HD11.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD11.setObjectName("HD11")
        self.LOGOUT = QtWidgets.QPushButton(self.frame)
        self.LOGOUT.setGeometry(QtCore.QRect(625, 25, 30, 25))
        self.LOGOUT.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.LOGOUT.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LOGOUT.setIcon(icon)
        self.LOGOUT.setIconSize(QtCore.QSize(20, 20))
        self.LOGOUT.setObjectName("LOGOUT")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(371, 28, 25, 15))
        self.label_13.setStyleSheet("color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/images/faq.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.FAQ_2 = QtWidgets.QLabel(self.frame)
        self.FAQ_2.setGeometry(QtCore.QRect(401, 22, 31, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.FAQ_2.setFont(font)
        self.FAQ_2.setAutoFillBackground(False)
        self.FAQ_2.setStyleSheet("color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.FAQ_2.setObjectName("FAQ_2")
        self.FAQ_3 = QtWidgets.QLabel(self.frame)
        self.FAQ_3.setGeometry(QtCore.QRect(470, 23, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.FAQ_3.setFont(font)
        self.FAQ_3.setAutoFillBackground(False)
        self.FAQ_3.setStyleSheet("color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.FAQ_3.setObjectName("FAQ_3")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(444, 27, 24, 16))
        self.label_16.setStyleSheet("color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(":/images/gembok.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(522, 29, 25, 15))
        self.label_15.setStyleSheet("color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap(":/images/list.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.FAQ_4 = QtWidgets.QLabel(self.frame)
        self.FAQ_4.setGeometry(QtCore.QRect(550, 23, 71, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.FAQ_4.setFont(font)
        self.FAQ_4.setAutoFillBackground(False)
        self.FAQ_4.setStyleSheet("color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.FAQ_4.setObjectName("FAQ_4")
        self.LOGO_2 = QtWidgets.QPushButton(self.frame)
        self.LOGO_2.setGeometry(QtCore.QRect(1, -10, 111, 91))
        self.LOGO_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"")
        self.LOGO_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LOGO_2.setIcon(icon1)
        self.LOGO_2.setIconSize(QtCore.QSize(100, 100))
        self.LOGO_2.setObjectName("LOGO_2")
        self.FILM1 = QtWidgets.QPushButton(self.frame)
        self.FILM1.setGeometry(QtCore.QRect(30, 160, 141, 181))
        self.FILM1.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.FILM1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/film1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FILM1.setIcon(icon2)
        self.FILM1.setIconSize(QtCore.QSize(200, 200))
        self.FILM1.setObjectName("FILM1")
        self.label_14.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.lineEdit_2.raise_()
        self.label_2.raise_()
        self.GARIS_6.raise_()
        self.CR.raise_()
        self.DESK.raise_()
        self.label_20.raise_()
        self.label_7.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_8.raise_()
        self.ABU1.raise_()
        self.FILM2.raise_()
        self.FILM3.raise_()
        self.HD2.raise_()
        self.HD3.raise_()
        self.FILM7.raise_()
        self.FILM8.raise_()
        self.FILM9.raise_()
        self.FILM10.raise_()
        self.FILM11.raise_()
        self.FILM12.raise_()
        self.HD7.raise_()
        self.HD8.raise_()
        self.HD9.raise_()
        self.HD10.raise_()
        self.HD12.raise_()
        self.HD11.raise_()
        self.FILM5.raise_()
        self.FILM6.raise_()
        self.HD5.raise_()
        self.HD6.raise_()
        self.FILM4.raise_()
        self.HD4.raise_()
        self.LOGOUT.raise_()
        self.label_13.raise_()
        self.FAQ_2.raise_()
        self.FAQ_3.raise_()
        self.label_16.raise_()
        self.label_15.raise_()
        self.FAQ_4.raise_()
        self.JUDUL3.raise_()
        self.JUDUL2.raise_()
        self.JUDUL12.raise_()
        self.JUDUL11.raise_()
        self.JUDUL10.raise_()
        self.JUDUL1.raise_()
        self.JUDUL4.raise_()
        self.JUDUL5.raise_()
        self.JUDUL6.raise_()
        self.JUDUL7.raise_()
        self.JUDUL8.raise_()
        self.JUDUL9.raise_()
        self.LOGO_2.raise_()
        self.FILM1.raise_()
        self.HD1.raise_()
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        SEMUA.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SEMUA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 21))
        self.menubar.setObjectName("menubar")
        SEMUA.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SEMUA)
        self.statusbar.setObjectName("statusbar")
        SEMUA.setStatusBar(self.statusbar)

        self.retranslateUi(SEMUA)
        QtCore.QMetaObject.connectSlotsByName(SEMUA)

    def retranslateUi(self, SEMUA):
        _translate = QtCore.QCoreApplication.translate
        SEMUA.setWindowTitle(_translate("SEMUA", "MainWindow"))
        self.lineEdit_2.setPlaceholderText(_translate("SEMUA", "  Search Movies"))
        self.HD1.setText(_translate("SEMUA", "HD"))
        self.HD2.setText(_translate("SEMUA", "HD"))
        self.HD3.setText(_translate("SEMUA", "HD"))
        self.JUDUL1.setText(_translate("SEMUA", "Black Clover:\n"
"Sword of the\n"
"Wizard King"))
        self.JUDUL2.setText(_translate("SEMUA", "Transformers:\n"
"Rise of the\n"
"Beasts (2023)"))
        self.JUDUL3.setText(_translate("SEMUA", "Fast X\n"
" (2023)"))
        self.label_2.setText(_translate("SEMUA", "1  2  ...  362 >>"))
        self.CR.setText(_translate("SEMUA", "Copyright @2021 YOUPET - All Rights Reserved Disclaimer: This site does not store any files\n"
" on its server. All contents are provided by non-affiliated third parties and make money online"))
        self.JUDUL4.setText(_translate("SEMUA", "Black Knight"))
        self.HD5.setText(_translate("SEMUA", "HD"))
        self.HD6.setText(_translate("SEMUA", "HD"))
        self.HD4.setText(_translate("SEMUA", "HD"))
        self.JUDUL5.setText(_translate("SEMUA", "Guardians of\n"
" the Galaxy Volume 3"))
        self.JUDUL6.setText(_translate("SEMUA", "The Goblin\n"
"(2022)"))
        self.DESK.setText(_translate("SEMUA", "YOUPET Streaming Film dan TV Series Subtitle Indonesia\n"
"YOUPET adalah situs web nonton streaming online download film terbaru film asia\n"
"terbaru, film barat terbaru secara gratis dan lengkap. Disini tersedia banyak\n"
"kualitas video seperti bluray, web-dl, hd, dvdrip, hdrip dan hdcam. Format video\n"
"yang kami sediakan ada mp4 mkv serta berbagai macam resolusi seperti 360p, 480p,\n"
"720p dan 1080p. Semua film yang tersedia di situs ini hanya untuk review saja.\n"
"Jika anda ingin menonton filmdengan kualitas yang lebih baik, silahkan beli DVD\n"
"resminya."))
        self.label_20.setText(_translate("SEMUA", "HOME"))
        self.label_7.setText(_translate("SEMUA", "GENRE"))
        self.label_21.setText(_translate("SEMUA", "YEAR"))
        self.label_22.setText(_translate("SEMUA", "BOX OFFICE"))
        self.label_8.setText(_translate("SEMUA", "COUNTRY"))
        self.JUDUL9.setText(_translate("SEMUA", "The God of High\n"
"School"))
        self.JUDUL7.setText(_translate("SEMUA", "Ride On"))
        self.JUDUL8.setText(_translate("SEMUA", "Demon Slayer"))
        self.JUDUL10.setText(_translate("SEMUA", "Secret Invasion"))
        self.JUDUL11.setText(_translate("SEMUA", "Skull Island"))
        self.JUDUL12.setText(_translate("SEMUA", "Manifest"))
        self.HD7.setText(_translate("SEMUA", "HD"))
        self.HD8.setText(_translate("SEMUA", "HD"))
        self.HD9.setText(_translate("SEMUA", "HD"))
        self.HD10.setText(_translate("SEMUA", "HD"))
        self.HD12.setText(_translate("SEMUA", "HD"))
        self.HD11.setText(_translate("SEMUA", "HD"))
        self.FAQ_2.setText(_translate("SEMUA", "FAQ"))
        self.FAQ_3.setText(_translate("SEMUA", "DMCA"))
        self.FAQ_4.setText(_translate("SEMUA", "SITEMAP"))
import res_rc
