from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
"    background-color: rgb(229,228,226);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-1, 0, 801, 600))
        self.tabWidget.setMaximumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane\n"
"{\n"
"    border: 1px;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab\n"
"{\n"
"    min-width: 26ex;\n"
"    min-height: 16ex;\n"
"    margin-left: 1px;\n"
"    left: -2px;\n"
"    color: black;    \n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    background: rgb(130,130,130)\n"
"}\n"
"\n"
"QTabBar::tab:hover\n"
"{\n"
"    background: rgb(156,156,156)\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setStyleSheet("")
        self.tab_1.setObjectName("tab_1")
        self.tab_1_btn_telegram = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_btn_telegram.setGeometry(QtCore.QRect(60, 30, 201, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_1_btn_telegram.sizePolicy().hasHeightForWidth())
        self.tab_1_btn_telegram.setSizePolicy(sizePolicy)
        self.tab_1_btn_telegram.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Air America")
        font.setPointSize(42)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tab_1_btn_telegram.setFont(font)
        self.tab_1_btn_telegram.setStyleSheet("QPushButton \n"
"{\n"
"    border-radius: 25px;\n"
"    color: white;\n"
"    background: #90c6f9\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background: rgb(156,156,156)\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background: rgb(0, 0, 0)\n"
"}")
        self.tab_1_btn_telegram.setObjectName("tab_1_btn_telegram")
        self.tab_1_btn_youtube = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_btn_youtube.setGeometry(QtCore.QRect(530, 30, 201, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_1_btn_youtube.sizePolicy().hasHeightForWidth())
        self.tab_1_btn_youtube.setSizePolicy(sizePolicy)
        self.tab_1_btn_youtube.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Air America")
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_btn_youtube.setFont(font)
        self.tab_1_btn_youtube.setStyleSheet("QPushButton \n"
"{\n"
"    border-radius: 25px;\n"
"    color: white;\n"
"    background: #ff0000\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background: rgb(156,156,156)\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background: rgb(0, 0, 0)\n"
"}")
        self.tab_1_btn_youtube.setObjectName("tab_1_btn_youtube")
        self.tab_1_btn_vk = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_btn_vk.setGeometry(QtCore.QRect(60, 320, 201, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_1_btn_vk.sizePolicy().hasHeightForWidth())
        self.tab_1_btn_vk.setSizePolicy(sizePolicy)
        self.tab_1_btn_vk.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Air America")
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_btn_vk.setFont(font)
        self.tab_1_btn_vk.setStyleSheet("QPushButton \n"
"{\n"
"    border-radius: 25px;\n"
"    color: white;\n"
"    background: #3d61ff\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background: rgb(156,156,156)\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background: rgb(0, 0, 0)\n"
"}")
        self.tab_1_btn_vk.setObjectName("tab_1_btn_vk")
        self.tab_1_btn_all = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_btn_all.setGeometry(QtCore.QRect(530, 320, 201, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_1_btn_all.sizePolicy().hasHeightForWidth())
        self.tab_1_btn_all.setSizePolicy(sizePolicy)
        self.tab_1_btn_all.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Air America")
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_btn_all.setFont(font)
        self.tab_1_btn_all.setStyleSheet("QPushButton \n"
"{\n"
"    border-radius: 25px;\n"
"    color: white;\n"
"    background: rgb(244,0,161)\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background: rgb(156,156,156)\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background: rgb(0, 0, 0)\n"
"}")
        self.tab_1_btn_all.setObjectName("tab_1_btn_all")
        self.tab_1_btn_blind_typing_invisible = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_btn_blind_typing_invisible.setGeometry(QtCore.QRect(433, 250, 31, 27))
        self.tab_1_btn_blind_typing_invisible.setStyleSheet("QPushButton:pressed\n"
"{\n"
"    background: red\n"
"}")
        self.tab_1_btn_blind_typing_invisible.setText("")
        self.tab_1_btn_blind_typing_invisible.setFlat(True)
        self.tab_1_btn_blind_typing_invisible.setObjectName("tab_1_btn_blind_typing_invisible")
        self.tab_1_btn_unotalone_invisible = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_btn_unotalone_invisible.setGeometry(QtCore.QRect(335, 250, 31, 27))
        self.tab_1_btn_unotalone_invisible.setStyleSheet("QPushButton:pressed\n"
"{\n"
"    background: red\n"
"}")
        self.tab_1_btn_unotalone_invisible.setText("")
        self.tab_1_btn_unotalone_invisible.setFlat(True)
        self.tab_1_btn_unotalone_invisible.setObjectName("tab_1_btn_unotalone_invisible")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.tab_2.setObjectName("tab_2")
        self.tab_2_off_pc = QtWidgets.QLabel(self.tab_2)
        self.tab_2_off_pc.setGeometry(QtCore.QRect(10, 10, 425, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_off_pc.setFont(font)
        self.tab_2_off_pc.setStyleSheet("color: rgb(255, 255, 255);")
        self.tab_2_off_pc.setObjectName("tab_2_off_pc")
        self.tab_2_btn_off_pc = QtWidgets.QPushButton(self.tab_2)
        self.tab_2_btn_off_pc.setGeometry(QtCore.QRect(590, 10, 60, 60))
        self.tab_2_btn_off_pc.setStyleSheet("QPushButton \n"
"{\n"
"    color: white\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background: rgb(156,156,156)\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background: rgb(0, 0, 0)\n"
"}")
        self.tab_2_btn_off_pc.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/shutdown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_2_btn_off_pc.setIcon(icon)
        self.tab_2_btn_off_pc.setIconSize(QtCore.QSize(54, 54))
        self.tab_2_btn_off_pc.setObjectName("tab_2_btn_off_pc")
        self.tab_2_time_to_shutdown = QtWidgets.QLineEdit(self.tab_2)
        self.tab_2_time_to_shutdown.setGeometry(QtCore.QRect(443, 30, 41, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_2_time_to_shutdown.sizePolicy().hasHeightForWidth())
        self.tab_2_time_to_shutdown.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_time_to_shutdown.setFont(font)
        self.tab_2_time_to_shutdown.setAutoFillBackground(False)
        self.tab_2_time_to_shutdown.setStyleSheet("QLineEdit\n"
"{\n"
"    border-radius: 3px;\n"
"}")
        self.tab_2_time_to_shutdown.setMaxLength(3)
        self.tab_2_time_to_shutdown.setObjectName("tab_2_time_to_shutdown")
        self.tab_2_minutes = QtWidgets.QLabel(self.tab_2)
        self.tab_2_minutes.setGeometry(QtCore.QRect(492, 10, 87, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat Alternates")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_minutes.setFont(font)
        self.tab_2_minutes.setStyleSheet("color: rgb(255, 255, 255);")
        self.tab_2_minutes.setObjectName("tab_2_minutes")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setStyleSheet("")
        self.tab_5.setObjectName("tab_5")
        self.tab_5_fanat_skiLLa1 = QtWidgets.QLabel(self.tab_5)
        self.tab_5_fanat_skiLLa1.setGeometry(QtCore.QRect(260, 20, 301, 83))
        font = QtGui.QFont()
        font.setFamily("Air America")
        font.setPointSize(52)
        font.setBold(False)
        font.setWeight(50)
        self.tab_5_fanat_skiLLa1.setFont(font)
        self.tab_5_fanat_skiLLa1.setAutoFillBackground(False)
        self.tab_5_fanat_skiLLa1.setStyleSheet("color: rgb(255, 255, 255);")
        self.tab_5_fanat_skiLLa1.setTextFormat(QtCore.Qt.AutoText)
        self.tab_5_fanat_skiLLa1.setObjectName("tab_5_fanat_skiLLa1")
        self.tab_5_btn_telegram = QtWidgets.QPushButton(self.tab_5)
        self.tab_5_btn_telegram.setGeometry(QtCore.QRect(60, 180, 191, 191))
        self.tab_5_btn_telegram.setStyleSheet("QPushButton \n"
"{\n"
"    color: white\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background: rgb(156,156,156)\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background: rgb(0, 0, 0)\n"
"}")
        self.tab_5_btn_telegram.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/tg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("Icons/tg.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tab_5_btn_telegram.setIcon(icon1)
        self.tab_5_btn_telegram.setIconSize(QtCore.QSize(296, 296))
        self.tab_5_btn_telegram.setObjectName("tab_5_btn_telegram")
        self.tab_5_btn_vk = QtWidgets.QPushButton(self.tab_5)
        self.tab_5_btn_vk.setGeometry(QtCore.QRect(550, 180, 191, 191))
        self.tab_5_btn_vk.setStyleSheet("QPushButton \n"
"{\n"
"    color: white\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background: rgb(156,156,156)\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background: rgb(0, 0, 0)\n"
"}")
        self.tab_5_btn_vk.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/vk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("Icons/vk.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tab_5_btn_vk.setIcon(icon2)
        self.tab_5_btn_vk.setIconSize(QtCore.QSize(185, 185))
        self.tab_5_btn_vk.setObjectName("tab_5_btn_vk")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "facilitating life"))
        self.tab_1_btn_telegram.setText(_translate("MainWindow", "Telegram"))
        self.tab_1_btn_youtube.setText(_translate("MainWindow", "YouTube"))
        self.tab_1_btn_vk.setText(_translate("MainWindow", "VK"))
        self.tab_1_btn_all.setText(_translate("MainWindow", "Open all"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Открыть сайты"))
        self.tab_2_off_pc.setText(_translate("MainWindow", "Выключить пк через"))
        self.tab_2_minutes.setText(_translate("MainWindow", "мин."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Системные скрипты"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Отключение служб"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Полезные программы"))
        self.tab_5_fanat_skiLLa1.setText(_translate("MainWindow", "fanat skiLLa1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Автор"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
