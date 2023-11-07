# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addUi.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(438, 366)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(103, 61, 255, 255), stop:0.505682 rgba(0, 147, 246, 255), stop:1 rgba(49, 58, 255, 255));\n"
"font-family: Ruda Regular;")
        self.EffectGlass3_withFrame = QFrame(Dialog)
        self.EffectGlass3_withFrame.setObjectName(u"EffectGlass3_withFrame")
        self.EffectGlass3_withFrame.setGeometry(QRect(30, 30, 381, 301))
        self.EffectGlass3_withFrame.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-size: 25px;")
        self.EffectGlass3_withFrame.setFrameShape(QFrame.StyledPanel)
        self.EffectGlass3_withFrame.setFrameShadow(QFrame.Raised)
        self.action_box_new_reminder = QFrame(self.EffectGlass3_withFrame)
        self.action_box_new_reminder.setObjectName(u"action_box_new_reminder")
        self.action_box_new_reminder.setGeometry(QRect(10, 10, 361, 281))
        self.action_box_new_reminder.setStyleSheet(u"border: none;\n"
"background-color: none;")
        self.verticalLayout = QVBoxLayout(self.action_box_new_reminder)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.action_box_new_reminder)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label)

        self.textReminder = QLineEdit(self.action_box_new_reminder)
        self.textReminder.setObjectName(u"textReminder")
        self.textReminder.setStyleSheet(u"background-color: rgba(255,255,255,40)")

        self.verticalLayout.addWidget(self.textReminder)

        self.addButton = QPushButton(self.action_box_new_reminder)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
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
        icon = QIcon()
        icon.addFile(u":/icons/icons/add_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon)

        self.verticalLayout.addWidget(self.addButton)

        self.EffectGlass2 = QFrame(Dialog)
        self.EffectGlass2.setObjectName(u"EffectGlass2")
        self.EffectGlass2.setGeometry(QRect(20, 20, 401, 321))
        self.EffectGlass2.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-size: 25px;")
        self.EffectGlass2.setFrameShape(QFrame.StyledPanel)
        self.EffectGlass2.setFrameShadow(QFrame.Raised)
        self.EffectGlass1 = QFrame(Dialog)
        self.EffectGlass1.setObjectName(u"EffectGlass1")
        self.EffectGlass1.setGeometry(QRect(10, 10, 421, 341))
        self.EffectGlass1.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-size: 25px;")
        self.EffectGlass1.setFrameShape(QFrame.StyledPanel)
        self.EffectGlass1.setFrameShadow(QFrame.Raised)
        self.EffectGlass2.raise_()
        self.EffectGlass1.raise_()
        self.EffectGlass3_withFrame.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u043e\u0435 \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u0435", None))
        self.textReminder.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u044f", None))
        self.addButton.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

