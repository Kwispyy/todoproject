# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'changeUi.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 299)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(103, 61, 255, 255), stop:0.505682 rgba(0, 147, 246, 255), stop:1 rgba(49, 58, 255, 255));\n"
"font-family: Ruda Regular;")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 381, 281))
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-size: 25px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 361, 261))
        self.frame_2.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-size: 25px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 10, 341, 241))
        self.frame_3.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-size: 25px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 321, 221))
        self.frame_4.setStyleSheet(u"font-weight: bold;\n"
"font-size: 18pt;\n"
"background-color: none;\n"
"border: none;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 301, 81))
        self.newTextReminder = QLineEdit(self.frame_4)
        self.newTextReminder.setObjectName(u"newTextReminder")
        self.newTextReminder.setGeometry(QRect(10, 120, 301, 41))
        self.newTextReminder.setStyleSheet(u"background-color: rgba(255,255,255,40);\n"
"font-size: 20px;\n"
"font-weight: normal;")
        self.changeButton = QPushButton(self.frame_4)
        self.changeButton.setObjectName(u"changeButton")
        self.changeButton.setGeometry(QRect(10, 170, 301, 51))
        font = QFont()
        font.setFamilies([u"Ruda Regular"])
        font.setPointSize(18)
        font.setBold(False)
        self.changeButton.setFont(font)
        self.changeButton.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"font-weight: normal;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 100px;\n"
"height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,40)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70)\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u0435", None))
        self.newTextReminder.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u044f", None))
        self.changeButton.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

