import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("PyQt Calculator") # Memberikan title pada main window
    self.setFixedSize(QSize(360, 520)) # Mengatur ukuran window


if __name__ == "__main__":
  app = QApplication(sys.argv)

  window = MainWindow()
  window.show()

  app.exec()