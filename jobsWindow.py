from PySide6.QtWidgets import QPushButton, QLabel, QApplication, QWidget, \
    QTableWidget, QAbstractItemView, QLineEdit, QComboBox
# for later QTableWidgetItem
import plotly.graph_objects as maps_plotly
import jobs


class JobsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.quit_button = QPushButton("Quit", self)
        self.update_button = QPushButton("Update Data", self)
        self.enter_data = QPushButton("Enter Data", self)
        self.data_button = QPushButton("Run Data Visualization", self)
        self.back_button = QPushButton("Back", self)
        self.text_visualization_button = QPushButton("Text Visualization", self)
        self.map_visualization = QPushButton("Map Visualization", self)
        self.data_visualization_label = QLabel("Welcome to data visualization!", self)
        self.welcome_label = QLabel("Welcome to Jobs data Visualization.", self)
        self.update_label_01 = QLabel("", self)
        self.update_label_02 = QLabel("", self)
        self.update_label_03 = QLabel("", self)
        self.update_label_04 = QLabel("", self)
        self.update_label_05 = QLabel("", self)
        self.update_label_06 = QLabel("", self)
        self.update_label_07 = QLabel("", self)
        self.update_label_08 = QLabel("", self)
        self.excel_label = QLabel("Excel Spreadsheet:", self)
        self.update_information = QLabel(
            "If you would like to update a single entry please select the table and enter all of its information.\n"
            "If you would like to import from a spreadsheet type it into the box on the right and select the table.\n"
            "When you are ready with which ever function press Enter Data.\n"
            "For any data you want to append make sure the id is None.\n"
            "Also only work from one method at a time and make sure he other is empty.", self)
        self.text_data_visualization = QTableWidget(self)
        self.us_map = maps_plotly.Figure(maps_plotly.Scattergeo())
        self.table_selection = QComboBox(self)
        self.update_box_01 = QLineEdit(self)
        self.update_box_02 = QLineEdit(self)
        self.update_box_03 = QLineEdit(self)
        self.update_box_04 = QLineEdit(self)
        self.update_box_05 = QLineEdit(self)
        self.update_box_06 = QLineEdit(self)
        self.update_box_07 = QLineEdit(self)
        self.update_box_08 = QLineEdit(self)
        self.update_excel_selection = QLineEdit(self)
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
        self.data_visualization_label.move(20, 400)
        self.text_visualization_button.move(400 - self.text_data_visualization.width(), 750)
        self.text_visualization_button.clicked.connect(self.text_visualization)
        self.map_visualization.move(self.text_visualization_button.x() + self.text_visualization_button.width(),
                                    self.text_visualization_button.y())
        self.map_visualization.clicked.connect(self.run_map_visualization)
        self.welcome_label.move(150, 150)
        self.us_map.update_geos(visible=False, resolution=110, scope="usa",
                                showcountries=True, countrycolor="Black",
                                showsubunits=True, subunitcolor="Grey")
        self.us_map.update_layout()
        self.text_data_visualization.setRowCount(5)
        self.text_data_visualization.setColumnCount(5)
        self.text_data_visualization.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.text_data_visualization.resize(self.text_data_visualization.size().width() *
                                            self.text_data_visualization.columnCount() + 25, 300)
        self.update_box_01.move(150, 30)
        self.update_box_02.move(150, 60)
        self.update_box_03.move(150, 90)
        self.update_box_04.move(150, 120)
        self.update_box_05.move(150, 150)
        self.update_box_06.move(150, 180)
        self.update_box_07.move(150, 210)
        self.update_box_08.move(150, 240)
        self.excel_label.move(340, 70)
        self.update_excel_selection.move(340, 90)
        self.update_information.move(25, 325)
        self.update_label_01.setGeometry(5, 30, 145, 20)
        self.update_label_02.setGeometry(5, 60, 145, 20)
        self.update_label_03.setGeometry(5, 90, 145, 20)
        self.update_label_04.setGeometry(5, 120, 145, 20)
        self.update_label_05.setGeometry(5, 150, 145, 20)
        self.update_label_06.setGeometry(5, 180, 145, 20)
        self.update_label_07.setGeometry(5, 210, 145, 20)
        self.update_label_08.setGeometry(5, 240, 145, 20)
        self.table_selection.setGeometry(10, 10, 145, 20)
        self.enter_data.move(10, 260)
        self.enter_data.clicked.connect(self.import_data)
        self.table_selection.addItem("---")
        self.table_selection.addItem("Schools")
        self.table_selection.addItem("Jobs")
        self.table_selection.currentIndexChanged.connect(self.update_selection)
        self.hidden_at_start()

        self.show()

    def hidden_at_start(self):
        self.hide_update_boxes()
        self.update_information.hide()
        self.text_data_visualization.hide()
        self.map_visualization.hide()
        self.text_visualization_button.hide()
        self.data_visualization_label.hide()
        self.back_button.hide()
        self.table_selection.hide()
        self.enter_data.hide()
        self.update_excel_selection.hide()
        self.excel_label.hide()

    def hide_update_boxes(self):
        self.update_box_01.hide()
        self.update_box_02.hide()
        self.update_box_03.hide()
        self.update_box_04.hide()
        self.update_box_05.hide()
        self.update_box_06.hide()
        self.update_box_07.hide()
        self.update_box_08.hide()
        self.update_label_01.setText("")
        self.update_label_02.setText("")
        self.update_label_03.setText("")
        self.update_label_04.setText("")
        self.update_label_05.setText("")
        self.update_label_06.setText("")
        self.update_label_07.setText("")
        self.update_label_08.setText("")

    def update_data(self):
        self.update_button.hide()
        self.data_button.hide()
        self.back_button.show()
        self.welcome_label.hide()
        self.table_selection.show()
        self.enter_data.show()
        self.update_information.show()
        self.update_excel_selection.show()
        self.excel_label.show()

    def update_selection(self):
        self.hide_update_boxes()
        if self.table_selection.currentText() == "Jobs":
            self.update_box_01.show()
            self.update_label_01.setText("jobs_id")
            self.update_box_02.show()
            self.update_label_02.setText("state_name")
            self.update_box_03.show()
            self.update_label_03.setText("occupation_code")
            self.update_box_04.show()
            self.update_label_04.setText("tittle")
            self.update_box_05.show()
            self.update_label_05.setText("employment")
            self.update_box_06.show()
            self.update_label_06.setText("salary_25th_percentile")
        elif self.table_selection.currentText() == "Schools":
            self.update_box_01.show()
            self.update_label_01.setText("school_id")
            self.update_box_02.show()
            self.update_label_02.setText("name")
            self.update_box_03.show()
            self.update_label_03.setText("state_abrev")
            self.update_box_04.show()
            self.update_label_04.setText("size_2017")
            self.update_box_05.show()
            self.update_label_05.setText("size_2018")
            self.update_box_06.show()
            self.update_label_06.setText("earnings")
            self.update_box_07.show()
            self.update_label_07.setText("repayment_overall")
            self.update_box_08.show()
            self.update_label_08.setText("repayment_cohort")

    def import_data(self):
        if self.update_excel_selection.text() == "":
            if self.table_selection.currentText() == "Jobs":
                information_to_update = [self.update_box_01.text(), self.update_box_02.text(),
                                         self.update_box_03.text(), self.update_box_04.text(),
                                         self.update_box_05.text(), self.update_box_06.text()]
                jobs.update_data_from_list(information_to_update, "Jobs")
            elif self.table_selection.currentText() == "Schools":
                information_to_update = [self.update_box_01.text(), self.update_box_02.text(),
                                         self.update_box_03.text(), self.update_box_04.text(),
                                         self.update_box_05.text(), self.update_box_06.text(),
                                         self.update_box_07.text(), self.update_box_08.text()]
                jobs.update_data_from_list(information_to_update, "Schools")
        else:
            if self.table_selection.currentText() == "Jobs":
                jobs.update_data_from_excel(self.update_excel_selection.text(), "Jobs")
            elif self.table_selection.currentText() == "Schools":
                jobs.update_data_from_excel(self.update_excel_selection.text(), "Jobs")

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
        self.hidden_at_start()

    def text_visualization(self):
        self.text_data_visualization.show()

    def run_map_visualization(self):
        self.text_data_visualization.hide()
        self.us_map.show()
