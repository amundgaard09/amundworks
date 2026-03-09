"""The main ANVIL GUI program for the FUTUREFORGE IA System"""

from foundry import toolsteel
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(panel):
        super().__init__()
        panel.setWindowTitle("FUTUREFORGE v0.1")
        panel.setMinimumSize(QSize(400, 300))
        button = QPushButton("Test")
        panel.setCentralWidget(button)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

if __name__ == "__main__":
    app.exec()
