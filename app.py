import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout
from layouts import CombinationLayout, GridLayout
from dsa import Stack
from utils.slots import squared, multiplicativeInverse, squareRoot
from utils.widgets import lineEdit

# Create a main class from PyQT for main app
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("PyQt6 - Calculator")

    # Satu line edit dan satu math stack yang dipakai bersama oleh semua layout
    self.lineEdit = lineEdit()
    self.mathStack = Stack()

    # Set Tabs Widget
    self.tabs = QTabWidget()
    self.tabs.setTabPosition(QTabWidget.TabPosition.North)
    self.tabs.setMovable(True)

    # Add tab
    self.tabs.addTab(GridLayout(self.lineEdit, self.mathStack).getLayout(), "Grid Layout")
    self.tabs.addTab(CombinationLayout(self.lineEdit, self.mathStack).getLayout(), "Combination Layout")

    # Line edit berada di atas tab, sehingga selalu tampil di kedua layout
    self.central = QWidget()
    self.centralLayout = QVBoxLayout()
    self.centralLayout.addWidget(self.lineEdit)
    self.centralLayout.addWidget(self.tabs)
    self.central.setLayout(self.centralLayout)
    self.setCentralWidget(self.central)

    # Set Menu
    self.menu = self.menuBar()

    # Squared Operation
    self.squaredButton = QAction("x²", self)
    self.squaredButton.setStatusTip("Squared operation")
    self.squaredButton.triggered.connect(lambda: squared(self.lineEdit))

    # MultiplicativeInverse Operation
    self.multiplicativeInverseOperationButton = QAction("1/x", self)
    self.multiplicativeInverseOperationButton.setStatusTip("MultiplicativeInverse Operation")
    self.multiplicativeInverseOperationButton.triggered.connect(lambda: multiplicativeInverse(self.lineEdit))

    # SquareRoot Operation
    self.squareRootButton = QAction("√x", self)
    self.squareRootButton.setStatusTip("SquareRoot Operation")
    self.squareRootButton.triggered.connect(lambda: squareRoot(self.lineEdit))

    self.fileMenu = self.menu.addMenu("&Operasi Matematika")
    self.fileMenu.addAction(self.squaredButton)
    self.fileMenu.addSeparator()
    self.fileMenu.addAction(self.multiplicativeInverseOperationButton)
    self.fileMenu.addSeparator()
    self.fileMenu.addAction(self.squareRootButton)



# Create QApplication instance per application.
app = QApplication(sys.argv)

# Create an instance of MainWindow class
window = MainWindow()
window.show()

app.exec()
