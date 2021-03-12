from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem, QLabel, QComboBox
from typing import List, Dict
# import jobs


class JobsWindow(QWidget):
    def __init__(self, data_to_show):
        super().__init__()
        self.table_selection = QComboBox(self)
        self.combo_label = QLabel("Hello", self)
        self.data = data_to_show
        self.list_control = None
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Jobs Window")
        display_list = QListWidget(self)
        self.list_control = display_list
        self.put_data_in_list(self.data)
        display_list.resize(700, 350)
        self.setGeometry(100, 100, 700, 500)
        quit_button = QPushButton("Quit", self)
        quit_button.clicked.connect(QApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        quit_button.move(615, 450)
        update_button = QPushButton("Update", self)
        update_button.clicked.connect(self.update_data)
        update_button.move(50, 450)
        self.combo_label.move(350, 450)
        self.combo_label.hide()
        self.table_selection.addItem("---")
        self.table_selection.addItem("School Table")
        self.table_selection.addItem("Jobs Table")
        self.table_selection.move(50, 400)
        self.show()

    def put_data_in_list(self, data: List[Dict]):
        for item in data:
            display_text = f"{item['state']}, {item['title']}, {item['salary']}"
            QListWidgetItem(display_text, listview=self.list_control)

    def update_data(self):
        table_to_update = self.table_selection.itemText(self.table_selection.currentIndex())
        table_to_update += "ok"
