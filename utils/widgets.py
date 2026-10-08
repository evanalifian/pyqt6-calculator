from PyQt6.QtWidgets import QPushButton, QLineEdit

def pushButton(title, lineEdit = None):
  button = QPushButton(title)

  button.clicked.connect(lambda: lineEdit.setText(str(title)))

  return button

def lineEdit():
  lineEdit = QLineEdit()

  lineEdit.textChanged.connect(lambda: print("typing"))

  return lineEdit