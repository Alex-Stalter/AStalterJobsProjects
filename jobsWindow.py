from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QLabel, QApplication, QWidget, \
    QListWidget, QListWidgetItem, QLineEdit, QComboBox
# import pandas
import plotly.graph_objects as px
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
        self.order_selector_text = QComboBox(self)
        self.data_selector_map = QComboBox(self)
        self.data_visualization_label = QLabel("Welcome to data visualization!", self)
        self.welcome_label = QLabel("Welcome to Jobs data Visualization.", self)
        self.list_control = None
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
        display_list = QListWidget(self)
        self.list_control = display_list
        display_list.resize(500, 350)
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
        self.text_visualization_button.move(400 - self.text_visualization_button.width(), 600)
        self.order_selector_text.move(self.text_visualization_button.x(),
                                      self.text_visualization_button.y()+self.text_visualization_button.height()+10)
        self.text_visualization_button.clicked.connect(self.text_visualization)
        self.map_visualization.move(self.text_visualization_button.x() + self.text_visualization_button.width(),
                                    self.text_visualization_button.y())
        self.data_selector_map.move(self.map_visualization.x(),
                                    self.map_visualization.y()+self.map_visualization.height()+10)
        self.map_visualization.clicked.connect(self.run_map_visualization)
        self.welcome_label.move(150, 150)
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
        self.order_selector_text.addItem("---")
        self.order_selector_text.addItem("ASC")
        self.order_selector_text.addItem("DESC")
        self.data_selector_map.addItem("---")
        self.data_selector_map.addItem("Graduates to Employment")
        self.data_selector_map.addItem("Average Declining Balance Percent to Average Salar")
        self.data_selector_map.addItem("Average Salary")
        self.table_selection.currentIndexChanged.connect(self.update_selection)
        self.hidden_at_start()

        self.show()

    def hidden_at_start(self):
        self.hide_update_boxes()
        self.list_control.hide()
        self.update_information.hide()
        self.map_visualization.hide()
        self.text_visualization_button.hide()
        self.data_visualization_label.hide()
        self.back_button.hide()
        self.table_selection.hide()
        self.enter_data.hide()
        self.update_excel_selection.hide()
        self.excel_label.hide()
        self.data_selector_map.hide()
        self.order_selector_text.hide()

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
                jobs.update_data_from_list(information_to_update, "Jobs", "jobs_db.sqlite")
            elif self.table_selection.currentText() == "Schools":
                information_to_update = [self.update_box_01.text(), self.update_box_02.text(),
                                         self.update_box_03.text(), self.update_box_04.text(),
                                         self.update_box_05.text(), self.update_box_06.text(),
                                         self.update_box_07.text(), self.update_box_08.text()]
                jobs.update_data_from_list(information_to_update, "Schools", "jobs_db.sqlite")
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
        self.data_selector_map.show()
        self.order_selector_text.show()

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
        self.list_control.clear()
        conn, cursor = jobs.open_db("jobs_db.sqlite")
        if self.order_selector_text.currentText() == "ASC":
            data_visualization_per_state = jobs.query_run('''SELECT state_abrev, state_name, ''' + '''
            total(jobs.employment) as employment,
            total(school.size_2018/4),
            round(avg(school.repayment_cohort),3) as repayment_cohort,
            round(avg(jobs.salary_25th_percentile)) as averge_entry_salary
            FROM school
            JOIN states using(state_abrev)
            JOIN jobs using(state_name)
            GROUP BY state_name
            ORDER BY employment DESC;''', cursor)
        elif self.order_selector_text.currentText() == "DESC":
            data_visualization_per_state = jobs.query_run('''SELECT state_abrev, state_name, ''' + '''
                        total(jobs.employment) as employment,
                        total(school.size_2018/4),
                        round(avg(school.repayment_cohort),3) as repayment_cohort,
                        round(avg(jobs.salary_25th_percentile)) as averge_entry_salary
                        FROM school
                        JOIN states using(state_abrev)
                        JOIN jobs using(state_name)
                        GROUP BY state_name
                        ORDER BY employment;''', cursor)
        else:
            data_visualization_per_state = jobs.query_run('''SELECT state_abrev, state_name, ''' + '''
                                    total(jobs.employment) as employment,
                                    total(school.size_2018/4),
                                    round(avg(school.repayment_cohort),3) as repayment_cohort,
                                    round(avg(jobs.salary_25th_percentile)) as averge_entry_salary
                                    FROM school
                                    JOIN states using(state_abrev)
                                    JOIN jobs using(state_name)
                                    GROUP BY state_name
                                    ;''', cursor)
        QListWidgetItem("State", listview=self.list_control)
        for state in data_visualization_per_state:
            state_display_data = f"{state[0]}, {state[1]}"
            grad_employ_data = f"2019 graduates: {state[3]} to Total employment: {state[2]}"
            repayment_data = f"Average Declining Balance Percent: {state[4]} to Entry Salary Average: {state[5]}"
            state_item = QListWidgetItem(state_display_data, listview=self.list_control)
            grad_item = QListWidgetItem(grad_employ_data, listview=self.list_control)
            repayment_item = QListWidgetItem(repayment_data, listview=self.list_control)
            grad_item.setForeground(Qt.darkGreen)
            repayment_item.setForeground(Qt.blue)
            state_item.setForeground(Qt.white)
            state_item.setBackground(Qt.black)
        self.list_control.show()
        jobs.close_db(conn)

    def run_map_visualization(self):
        conn, cursor = jobs.open_db("jobs_db.sqlite")
        data_visualization_per_state = jobs.query_run('''SELECT state_abrev, state_name, ''' + '''
                total(jobs.employment) as employment,
                total(school.size_2018/4),
                round(avg(school.repayment_cohort),3) as repayment_cohort,
                round(avg(jobs.salary_25th_percentile)) as averge_entry_salary
                FROM school
                JOIN states using(state_abrev)
                JOIN jobs using(state_name)
                GROUP BY state_name
                ;''', cursor)
        state_abrev = []
        state_grads = []
        state_repayment = []
        state_employment = []
        state_salary = []

        for state in data_visualization_per_state:
            state_abrev.append(state[0])
            state_grads.append(state[3]/state[2])
            state_repayment.append(state[4])
            state_employment.append(state[2])
            state_salary.append(state[5])

        if self.data_selector_map.currentText() == "Graduates to Employment":
            us_map = px.Figure(data=px.Choropleth(locations=state_abrev, z=state_grads,
                                                  locationmode='USA-states', colorbar_title="Graduates/Employment"
                                                  ))
            us_map.update_layout(geo_scope='usa', title_text='Graduates to Employment By State')
            us_map.show()
        elif self.data_selector_map.currentText() == "Average Declining Balance Percent":
            us_map = px.Figure(data=px.Choropleth(locations=state_abrev, z=state_repayment,
                                                  locationmode='USA-states', colorbar_title="Average Percent"
                                                  ))
            us_map.update_layout(geo_scope='usa', title_text='Average Percent of People with Declining Loans')
            us_map.show()
        elif self.data_selector_map.currentText() == "Average Salary":
            us_map = px.Figure(data=px.Choropleth(locations=state_abrev, z=state_salary,
                                                  locationmode='USA-states', colorbar_title="Salary"
                                                  ))
            us_map.update_layout(geo_scope='usa', title_text='Entry Level Salary by State')
            us_map.show()
        else:
            us_map = px.Figure(data=px.Choropleth(locations=state_abrev, z=state_grads,
                                                  locationmode='USA-states', colorbar_title="Graduates"
                                                  ))
            us_map.update_layout(geo_scope='usa', title_text='Graduates By State')
            us_map.show()
        jobs.close_db(conn)
        self.list_control.hide()
