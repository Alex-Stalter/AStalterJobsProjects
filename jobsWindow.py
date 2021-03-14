from PySide6.QtWidgets import QPushButton, QLabel, QApplication, QListWidgetItem, QWidget, \
    QTableWidgetItem, QTableWidget, QAbstractItemView, QLineEdit
from typing import List, Dict
import plotly.graph_objects as maps_plotly
import jobs


class JobsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.quit_button = QPushButton("Quit", self)
        self.update_button = QPushButton("Update Data", self)
        self.data_button = QPushButton("Run Data Visualization", self)
        self.back_button = QPushButton("Back", self)
        self.text_visualization_button = QPushButton("Text Visualization", self)
        self.map_visualization = QPushButton("Map Visualization", self)
        self.data_visualization_label = QLabel("Welcome to data visualization!", self)
        self.welcome_label = QLabel("Welcome to Jobs Data Visualization", self)
        self.text_data_visualization = QTableWidget(self)
        self.us_map = maps_plotly.Figure(maps_plotly.Scattergeo())
        self.update_box_01 = QLineEdit(self)
        self.list_control = None
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Jobs Window")
        self.setGeometry(50, 50, 500, 500)
        self.quit_button.clicked.connect(QApplication.instance().quit)
        self.quit_button.resize(self.quit_button.sizeHint())
        self.quit_button.move(415, 450)
        self.update_button.clicked.connect(self.update_data)
        self.update_button.move(200, 200)
        self.data_button.clicked.connect(self.run_data_visualization)
        self.data_button.move(175, 250)
        self.back_button.clicked.connect(self.go_back)
        self.back_button.move(25, 450)
        self.back_button.hide()
        self.data_visualization_label.hide()
        self.data_visualization_label.move(20, 400)
        self.text_visualization_button.move(400 - self.text_data_visualization.width(), 750)
        self.text_visualization_button.clicked.connect(self.text_visualization)
        self.text_visualization_button.hide()
        self.map_visualization.move(self.text_visualization_button.x()+self.text_visualization_button.width(),
                                    self.text_visualization_button.y())
        self.map_visualization.clicked.connect(self.run_map_visualization)
        self.map_visualization.hide()
        self.welcome_label.move(150, 150)
        self.us_map.update_geos(visible=False, resolution=110, scope="usa",
                                showcountries=True, countrycolor="Black",
                                showsubunits=True, subunitcolor="Grey")
        self.us_map.update_layout()
        self.text_data_visualization.setRowCount(5)
        self.text_data_visualization.setColumnCount(5)
        self.text_data_visualization.hide()
        self.text_data_visualization.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.text_data_visualization.resize(self.text_data_visualization.size().width() *
                                            self.text_data_visualization.columnCount() + 25, 300)
        self.text_data_visualization.setItem(0, 1, QTableWidgetItem("Data Entered"))
        self.update_box_01.move(230, 240)
        self.update_box_01.hide()

        self.show()

    def put_data_in_list(self, data: List[Dict]):
        for item in data:
            display_text = f"{item['state']}, {item['title']}, {item['salary']}"
            QListWidgetItem(display_text, listview=self.list_control)

    def update_data(self):
        self.update_button.hide()
        self.data_button.hide()
        self.back_button.show()
        self.welcome_label.hide()
        self.update_box_01.show()

    def run_data_visualization(self):
        self.update_button.hide()
        self.data_button.hide()
        self.data_visualization_label.show()
        self.back_button.show()
        self.setGeometry(50, 50, 800, 800)
        self.back_button.move(25, 750)
        self.quit_button.move(715, 750)
        self.welcome_label.hide()
        self.map_visualization.show()
        self.text_visualization_button.show()

    def go_back(self):
        self.back_button.hide()
        self.update_button.show()
        self.data_button.show()
        self.data_visualization_label.hide()
        self.setGeometry(50, 50, 500, 500)
        self.back_button.move(25, 450)
        self.quit_button.move(415, 450)
        self.welcome_label.show()
        self.text_data_visualization.hide()
        print(self.update_box_01.text())
        self.update_box_01.hide()
        self.map_visualization.hide()
        self.text_visualization_button.hide()

    def text_visualization(self):
        self.text_data_visualization.show()
        self.text_data_visualization.setItem(0, 0, QTableWidgetItem("Hello World!"))

    def run_map_visualization(self):
        self.text_data_visualization.hide()
        self.us_map.show()
