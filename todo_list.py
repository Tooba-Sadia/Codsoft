import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TodoApp(QWidget):    
    def __init__(self):
        super().__init__() 
        self.initializeUI()
  
    def initializeUI(self):
        # Main widget properties
        self.setWindowTitle('My Todo List')
        self.setFixedSize(400, 500)
        self.setStyleSheet("""
            background-color: #f0f0f0;
            font-size: 16px;
        """)

        # Title Label
        self.titleLabel = QLabel('My Todo List')
        self.titleLabel.setFont(QFont('Arial', 24, QFont.Bold))
        self.titleLabel.setAlignment(Qt.AlignCenter)

        # Input Box
        self.inputBox = QLineEdit()
        self.inputBox.setStyleSheet('QLineEdit {background: white;}')
        self.inputBox.setMinimumHeight(40)

        # Add Button
        self.addButton = QPushButton('Add')
        self.addButton.setStyleSheet('QPushButton {background: #4CAF50; color: white;}')
        self.addButton.clicked.connect(self.addTodo)

        # Update Button
        self.updateButton = QPushButton('Update')
        self.updateButton.setStyleSheet('QPushButton {background: #2196f3; color: white;}')
        self.updateButton.clicked.connect(self.updateTodo)

        # Delete Button
        self.deleteButton = QPushButton('Delete')
        self.deleteButton.setStyleSheet('QPushButton {background: #FF6347; color: white;}')
        self.deleteButton.clicked.connect(self.deleteTodo)

        # Todo List
        self.todoList = QListWidget()
        self.todoList.setStyleSheet('QListWidget {background: white;}')
        self.todoList.setSelectionMode(QAbstractItemView.SingleSelection)

        # Main Layout
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.titleLabel)
        self.mainLayout.addWidget(self.inputBox)
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.addButton)
        self.buttonLayout.addWidget(self.updateButton)
        self.buttonLayout.addWidget(self.deleteButton)
        self.mainLayout.addLayout(self.buttonLayout)
        self.mainLayout.addWidget(self.todoList)
        self.setLayout(self.mainLayout)

    def addTodo(self):
        item_text = self.inputBox.text().strip()
        if item_text:
            item = QListWidgetItem(item_text)
            item.setCheckState(Qt.Unchecked)
            self.todoList.addItem(item)
            self.inputBox.clear()

    def updateTodo(self):
        currentItem = self.todoList.currentItem()
        if currentItem:
            itemText = self.inputBox.text()  
            currentItem.setText(itemText)
            self.inputBox.clear()

    def deleteTodo(self):
        currentItem = self.todoList.currentItem()
        if currentItem:
            confirm = QMessageBox.question(self, 'Delete Item', 'Are you sure you want to delete this item?',
                                           QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                self.todoList.takeItem(self.todoList.currentRow())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Dark theme
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    window = TodoApp()
    window.show() 
    sys.exit(app.exec_())
