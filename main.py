from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QStandardItem, QStandardItemModel, QIcon
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()

        uic.loadUi("todo.ui", self)
        self.show()

        self.setFixedSize(442, 683)
        

        self.setWindowTitle("Dementiev Dmitriy Todo v0.1")
        self.model = QStandardItemModel()
        self.reminderList.setModel(self.model)

        self.addButton.clicked.connect(self.showAddDialog)
        self.deleteButton.clicked.connect(self.del_reminder)
        self.shareButton.clicked.connect(self.share)
        self.changeButton.clicked.connect(self.showChangeDialog)
        self.completeButton.clicked.connect(self.complete_reminder)

    def showAddDialog(self):
        showAddDialog = AddReminderWindow()
        showAddDialog.inputTextSignal.connect(self.add_reminder)
        showAddDialog.exec_()

    def showChangeDialog(self):
        if len(self.reminderList.selectedIndexes()) != 0:
            selected = self.reminderList.selectedIndexes()[0]
            item = self.model.itemFromIndex(selected)
            showChangeDialog = ChangeReminderWindow(item)
            showChangeDialog.inputTextSignal.connect(self.change_reminder)
            showChangeDialog.exec_()
        else:
            dialog = QMessageBox()
            dialog.setWindowTitle("Ой!")
            dialog.setWindowIcon(QIcon("appIcon.png"))
            dialog.setText("Напоминание не выбрано!")
            if dialog.exec_() == 0:
                self.show()

    def add_reminder(self, text):
        if text != "":
            item = QStandardItem(text)
            self.model.appendRow(item)

    def complete_reminder(self):
        if len(self.reminderList.selectedIndexes()) != 0:
            selected = self.reminderList.selectedIndexes()[0]
            
            dialog = QMessageBox()
            dialog.setWindowIcon(QIcon("appIcon.png"))
            dialog.setText(f"Вы выполнили напоминание '{selected.data()}'?")
            dialog.addButton(QPushButton("Да"), QMessageBox.YesRole)
            dialog.addButton(QPushButton("Нет"), QMessageBox.NoRole)

            if dialog.exec_() == 0:
                item = self.model.itemFromIndex(selected)
                font = item.font()
                font.setStrikeOut(True)
                item.setFont(font)

    def change_reminder(self, newText):
        selected = self.reminderList.selectedIndexes()[0]
        item = self.model.itemFromIndex(selected)
        item.setText(newText)


    def del_reminder(self):
        if len(self.reminderList.selectedIndexes()) != 0:
            selected = self.reminderList.selectedIndexes()[0]

            dialog = QMessageBox()
            dialog.setWindowIcon(QIcon("appIcon.png"))
            dialog.setText(f"Вы точно желаете удалить напоминание '{selected.data()}'?")
            dialog.addButton(QPushButton("Да"), QMessageBox.YesRole)
            dialog.addButton(QPushButton("Нет"), QMessageBox.NoRole)

            if dialog.exec_() == 0:
                self.model.removeRow(selected.row())


    def share(self):
        dialog = QMessageBox()
        dialog.setWindowTitle("LiveShare")
        dialog.setWindowIcon(QIcon("appIcon.png"))
        dialog.setText("Функция LiveShare ещё в разработке")
        if dialog.exec_() == 0:
            self.show()

class AddReminderWindow(QDialog):
    inputTextSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        uic.loadUi("addUi.ui", self)
        self.setWindowTitle("Add reminder")
        self.setWindowIcon(QIcon("appIcon.png"))
        self.setFixedSize(438, 366)

        self.addButton.clicked.connect(self.clickAdd)
    
    def clickAdd(self):
        text = self.textReminder.text()
        self.inputTextSignal.emit(text)

class ChangeReminderWindow(QDialog):
    inputTextSignal = pyqtSignal(str)
    
    def __init__(self, item):
        super().__init__()
        uic.loadUi("changeUi.ui", self)
        self.setWindowTitle("Change reminder")
        self.setWindowIcon(QIcon("appIcon.png"))
        self.setFixedSize(400, 299)
        
        self.item = item
        self.newTextReminder.setText(self.item.text())

        self.changeButton.clicked.connect(self.clickChange)

    def clickChange(self):
        newText = self.newTextReminder.text()
        self.inputTextSignal.emit(newText)

app = QApplication([])
window = MyGUI()
app.exec_()
