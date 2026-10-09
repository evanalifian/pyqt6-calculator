import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget

from layouts import CombinationLayout, GridLayout

# Create a main class from PyQT for main app
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("PyQt6 - Calculator")
    self.setFixedSize(QSize(320, 500))

    # Set Tabs Widget
    self.tabs = QTabWidget()
    self.tabs.setTabPosition(QTabWidget.TabPosition.North)
    self.tabs.setMovable(True)

    # Add tab
    self.tabs.addTab(GridLayout().getLayout(), "Grid Layout")
    self.tabs.addTab(CombinationLayout().getLayout(), "Combination Layout")

    self.setCentralWidget(self.tabs)



# Create QApplication instance per application.
app = QApplication(sys.argv)

# Create an instance of MainWindow class
window = MainWindow()
window.show()

app.exec()
