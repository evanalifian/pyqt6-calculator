# Impoert PyQt6 Classes and Modules
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout

# Import widgets
from utils.widgets import pushButton, lineEdit

class GridLayout(QMainWindow):
  def __init__(self):
    super().__init__()

    # Create container / VLayout
    self.vlayout = QVBoxLayout()
    self.container = QWidget()
    self.container.setLayout(self.vlayout)

    # Row 1 / HLayout
    self.row1 = QHBoxLayout()
    self.lineEdit = lineEdit()
    self.lineEdit.setFixedHeight(75)
    self.row1.addWidget(self.lineEdit)
    self.vlayout.addLayout(self.row1)

    # Row 2 / HLayout
    self.row2 = QHBoxLayout()
    self.row2.addWidget(pushButton("x²"))
    self.row2.addWidget(pushButton("1/x"))
    self.row2.addWidget(pushButton("√x"))
    self.row2.addWidget(pushButton("+"))
    self.vlayout.addLayout(self.row2)
    
    # Row 3 / HLayout
    self.row3 = QHBoxLayout()
    self.row3.addWidget(pushButton("8"))
    self.row3.addWidget(pushButton("9"))
    self.row3.addWidget(pushButton("C"))
    self.row3.addWidget(pushButton("-"))
    self.vlayout.addLayout(self.row3)
    
    # Row 4 / HLayout
    self.row4 = QHBoxLayout()
    self.row4.addWidget(pushButton("3"))
    self.row4.addWidget(pushButton("6"))
    self.row4.addWidget(pushButton("7"))
    self.row4.addWidget(pushButton("×"))
    self.vlayout.addLayout(self.row4)
    
    # Row 5 / HLayout
    self.row5 = QHBoxLayout()
    self.row5.addWidget(pushButton("0"))
    self.row5.addWidget(pushButton("1"))
    self.row5.addWidget(pushButton("2"))
    self.row5.addWidget(pushButton("÷"))
    self.vlayout.addLayout(self.row5)
    
    # Row 6 / HLayout
    self.row6 = QHBoxLayout()
    self.row6.addWidget(pushButton("="))
    self.vlayout.addLayout(self.row6)

  def getGridLayout(self):
    return self.container