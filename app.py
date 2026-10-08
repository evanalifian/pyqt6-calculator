import sys

# Impoert PyQt6 Classes and Modules
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

    # Initiate Layouts
    self.layouts = [
      {
        "name": "Grid Layout",
        "layout": GridLayout().getLayout()
      },
      {
        "name": "Combination Layout",
        "layout": CombinationLayout().getLayout()
      },
    ]

    # Add tab
    for l in self.layouts:
      self.tabs.addTab(l["layout"], l["name"])

    self.setCentralWidget(self.tabs)



# Create QApplication instance per application.
app = QApplication(sys.argv)

# Create an instance of MainWindow class
window = MainWindow()
window.show()

app.exec()
