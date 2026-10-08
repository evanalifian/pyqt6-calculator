import sys

# Impoert PyQt6 Classes and Modules
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget

from layouts import GridLayout

# Create a main class from PyQT for main app
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("PyQt6 - Calculator")
    self.setFixedSize(QSize(320, 500))

    self.gridLayout = GridLayout()

    self.setCentralWidget(self.gridLayout.getGridLayout())



# Create QApplication instance per application.
app = QApplication(sys.argv)

# Create an instance of MainWindow class
window = MainWindow()
window.show()

app.exec()
