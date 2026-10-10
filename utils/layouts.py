from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit

from utils.widgets import pushButton, advanceMathButton, lineEdit
from utils.dsa import Stack


# Create Grid Display
class GridLayout(QMainWindow):
  def __init__(self, lineEdit: QLineEdit, mathStack: Stack):
    super().__init__()

    # Line edit dan math stack dipakai bersama (dibuat di MainWindow)
    self.lineEdit = lineEdit
    self.mathStack = mathStack

    # Create grid box and cointainer
    self.gridLayout = QGridLayout()
    self.container = QWidget()
    self.container.setLayout(self.gridLayout)
    
    # Row 1 ada di MainWindow (line edit bersama)

    # Row 2
    self.gridLayout.addWidget(advanceMathButton("x²", self.lineEdit), 1, 0)
    self.gridLayout.addWidget(advanceMathButton("1/x", self.lineEdit), 1, 1)
    self.gridLayout.addWidget(advanceMathButton("√x", self.lineEdit), 1, 2)
    self.gridLayout.addWidget(pushButton("+", self.lineEdit, self.mathStack), 1, 3)

    # Row 3 / HLayout
    self.gridLayout.addWidget(pushButton("8", self.lineEdit, self.mathStack))
    self.gridLayout.addWidget(pushButton("9", self.lineEdit, self.mathStack))
    self.gridLayout.addWidget(pushButton("C", self.lineEdit, self.mathStack))
    self.gridLayout.addWidget(pushButton("-", self.lineEdit, self.mathStack))
    
    # Row 4 / HLayout
    self.gridLayout.addWidget(pushButton("3", self.lineEdit, self.mathStack))
    self.gridLayout.addWidget(pushButton("6", self.lineEdit, self.mathStack))
    self.gridLayout.addWidget(pushButton("7", self.lineEdit, self.mathStack))
    self.gridLayout.addWidget(pushButton("×", self.lineEdit, self.mathStack))
    
    # Row 5 / HLayout
    self.gridLayout.addWidget(pushButton("0", self.lineEdit, self.mathStack))
    self.gridLayout.addWidget(pushButton("1", self.lineEdit, self.mathStack))
    self.gridLayout.addWidget(pushButton("2", self.lineEdit, self.mathStack))
    self.gridLayout.addWidget(pushButton("÷", self.lineEdit, self.mathStack))
    
    # Row 6 / HLayout
    self.gridLayout.addWidget(pushButton("=", self.lineEdit, self.mathStack))

  def getLayout(self):
    return self.container


# Create Combination Display
class CombinationLayout(QMainWindow):
  def __init__(self, lineEdit: QLineEdit, mathStack: Stack):
    super().__init__()

    # Line edit dan math stack dipakai bersama (dibuat di MainWindow)
    self.lineEdit = lineEdit
    self.mathStack = mathStack

    # Create Cntainer / VLayout
    self.vlayout = QVBoxLayout()
    self.container = QWidget()
    self.container.setLayout(self.vlayout)

    # Row 1 ada di MainWindow (line edit bersama)

    # Row 2 / HLayout
    self.row2 = QHBoxLayout()
    self.row2.addWidget(advanceMathButton("x²", self.lineEdit))
    self.row2.addWidget(advanceMathButton("1/x", self.lineEdit))
    self.row2.addWidget(advanceMathButton("√x", self.lineEdit))
    self.row2.addWidget(pushButton("+", self.lineEdit, self.mathStack))
    self.vlayout.addLayout(self.row2)
    
    # Row 3 / HLayout
    self.row3 = QHBoxLayout()
    self.row3.addWidget(pushButton("8", self.lineEdit, self.mathStack))
    self.row3.addWidget(pushButton("9", self.lineEdit, self.mathStack))
    self.row3.addWidget(pushButton("C", self.lineEdit, self.mathStack))
    self.row3.addWidget(pushButton("-", self.lineEdit, self.mathStack))
    self.vlayout.addLayout(self.row3)
    
    # Row 4 / HLayout
    self.row4 = QHBoxLayout()
    self.row4.addWidget(pushButton("3", self.lineEdit, self.mathStack))
    self.row4.addWidget(pushButton("6", self.lineEdit, self.mathStack))
    self.row4.addWidget(pushButton("7", self.lineEdit, self.mathStack))
    self.row4.addWidget(pushButton("×", self.lineEdit, self.mathStack))
    self.vlayout.addLayout(self.row4)
    
    # Row 5 / HLayout
    self.row5 = QHBoxLayout()
    self.row5.addWidget(pushButton("0", self.lineEdit, self.mathStack))
    self.row5.addWidget(pushButton("1", self.lineEdit, self.mathStack))
    self.row5.addWidget(pushButton("2", self.lineEdit, self.mathStack))
    self.row5.addWidget(pushButton("÷", self.lineEdit, self.mathStack))
    self.vlayout.addLayout(self.row5)
    
    # Row 6 / HLayout
    self.row6 = QHBoxLayout()
    self.row6.addWidget(pushButton("=", self.lineEdit, self.mathStack))
    self.vlayout.addLayout(self.row6)

  def getLayout(self):
    return self.container