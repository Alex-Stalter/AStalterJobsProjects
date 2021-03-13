from PySide6.QtWidgets import *
from typing import List, Dict
import plotly.graph_objects as maps_plotly
# import jobs


class JobsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.quit_button = QPushButton("Quit", self)
        self.update_button = QPushButton("Update Data", self)
        self.data_button = QPushButton("Run Data Visualization", self)
        self.back_button = QPushButton("Back", self)
        self.data_visualization_label = QLabel("Welcome to data visualization!", self)
        self.welcome_label = QLabel("Welcome to Jobs Data Visualization", self)
        self.us_map = maps_plotly.Figure(maps_plotly.Scattergeo())
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
        self.welcome_label.move(150, 150)
        self.us_map.update_geos(visible=False, resolution=110, scope="usa",
                                showcountries=True, countrycolor="Black",
                                showsubunits=True, subunitcolor="Grey")
        self.us_map.update_layout()

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

    def run_data_visualization(self):
        self.update_button.hide()
        self.data_button.hide()
        self.data_visualization_label.show()
        self.back_button.show()
        self.setGeometry(50, 50, 800, 800)
        self.back_button.move(25, 750)
        self.quit_button.move(715, 750)
        self.welcome_label.hide()
        self.us_map.show()

    def go_back(self):
        self.back_button.hide()
        self.update_button.show()
        self.data_button.show()
        self.data_visualization_label.hide()
        self.setGeometry(100, 100, 500, 500)
        self.back_button.move(25, 450)
        self.quit_button.move(415, 450)
        self.welcome_label.show()
