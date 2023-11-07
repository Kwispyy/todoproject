# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'todo.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(506, 683)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u"appIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(103, 61, 255, 255), stop:0.505682 rgba(0, 147, 246, 255), stop:1 rgba(49, 58, 255, 255));\n"
"font-family: Ruda Regular;")
        self.mainFrame = QWidget(MainWindow)
        self.mainFrame.setObjectName(u"mainFrame")
        self.verticalLayout = QVBoxLayout(self.mainFrame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.nameLable = QLabel(self.mainFrame)
        self.nameLable.setObjectName(u"nameLable")
        self.nameLable.setCursor(QCursor(Qt.ArrowCursor))
        self.nameLable.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-size: 25px;")
        self.nameLable.setFrameShape(QFrame.NoFrame)
        self.nameLable.setTextFormat(Qt.AutoText)
        self.nameLable.setScaledContents(False)
        self.nameLable.setWordWrap(False)
        self.nameLable.setMargin(0)

        self.verticalLayout.addWidget(self.nameLable)

        self.reminderList = QListView(self.mainFrame)
        self.reminderList.setObjectName(u"reminderList")
        self.reminderList.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-size: 25px;")

        self.verticalLayout.addWidget(self.reminderList)

        self.buttonsFrame = QFrame(self.mainFrame)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setStyleSheet(u"background-color: rgba(255,255,255,0)")
        self.horizontalLayout = QHBoxLayout(self.buttonsFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, -1, -1)
        self.changeButton = QPushButton(self.buttonsFrame)
        self.changeButton.setObjectName(u"changeButton")
        self.changeButton.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 120px;\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/edit_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.changeButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.changeButton)

        self.completeButton = QPushButton(self.buttonsFrame)
        self.completeButton.setObjectName(u"completeButton")
        self.completeButton.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.completeButton)

        self.addButton = QPushButton(self.buttonsFrame)
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/add_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon2)

        self.horizontalLayout.addWidget(self.addButton)

        self.deleteButton = QPushButton(self.buttonsFrame)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 120px;\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/delete_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteButton.setIcon(icon3)

        self.horizontalLayout.addWidget(self.deleteButton)


        self.verticalLayout.addWidget(self.buttonsFrame)

        self.shareButton = QPushButton(self.mainFrame)
        self.shareButton.setObjectName(u"shareButton")
        self.shareButton.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 30px;\n"
"height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,40)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70)\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/share_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.shareButton.setIcon(icon4)

        self.verticalLayout.addWidget(self.shareButton)

        MainWindow.setCentralWidget(self.mainFrame)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ToDo List", None))
        self.nameLable.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0434\u0435\u043b", None))
        self.changeButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.completeButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.shareButton.setText(QCoreApplication.translate("MainWindow", u"LiveShare", None))
    # retranslateUi

