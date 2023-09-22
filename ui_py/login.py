# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QWidget)
from ui_py import lg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 400)
        MainWindow.setMinimumSize(QSize(819, 400))
        MainWindow.setMaximumSize(QSize(819, 400))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.name = QLabel(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(510, 110, 51, 31))
        self.name.setStyleSheet(u"font-size:20px;\n"
"")
        self.id = QTextEdit(self.centralwidget)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(560, 110, 251, 31))
        self.password = QLabel(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(510, 220, 51, 31))
        self.password.setStyleSheet(u"font-size:20px;")
        self.pwd = QTextEdit(self.centralwidget)
        self.pwd.setObjectName(u"pwd")
        self.pwd.setGeometry(QRect(560, 220, 251, 31))
        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(0, 0, 501, 401))
        self.img.setStyleSheet(u"image: url(:/\u767b\u5f55/login-l.6ef9d260_\u6781\u5149\u770b\u56fe.png);")
        self.img.setScaledContents(True)
        self.login = QPushButton(self.centralwidget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(630, 330, 93, 28))
        self.login.setStyleSheet(u"border-radius: 10px;\n"
"\n"
" border: 2px groove gray;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7\uff1a", None))
        self.password.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\uff1a", None))
        self.img.setText("")
        self.login.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
    # retranslateUi

