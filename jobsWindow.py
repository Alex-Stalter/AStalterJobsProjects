from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem
from typing import List, Dict


class JobsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Jobs Project")
        self.setGeometry(0, 0, 500, 500)
        quit_button = QPushButton("Quit Now", self)
        quit_button.clicked.connect(QApplication.instance().quit)
        quit_button.move(225, 225)
        self.show()
