from PyQt6.QtWidgets import QPushButton, QLineEdit
from dsa import Stack
from utils.slots import pushMathStack, calculate


# Button element
def pushButton(title: str, lineEdit: QLineEdit, mathStack: Stack):
  button = QPushButton(title)

  if title.lower() == "c":
    button.clicked.connect(lambda: (lineEdit.clear(), mathStack.stack.clear()))
  elif title.lower() == "=":
    button.clicked.connect(lambda: calculate(mathStack, lineEdit))
  else:
    button.clicked.connect(lambda: pushMathStack(title, lineEdit, mathStack))

  return button

# Advance math operation
def advanceMathButton(title: str, lineEdit: QLineEdit, mathStack: Stack):
  button = QPushButton(title)
  button.clicked.connect(lambda: print("Advance clicked"))
  return button


# Line Edit element
def lineEdit():
  lineEdit = QLineEdit()
  lineEdit.setFixedHeight(75)
  return lineEdit