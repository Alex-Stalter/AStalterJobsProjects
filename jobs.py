# Author: Alex Stalter

import requests
import secrets
# import os
import sqlite3
import openpyxl
from typing import Tuple
import jobsWindow
import sys


# import PySide6.QtWidgets


# open_db() creates a database based on the name that is inputted and then returns the cursor and connection so that
# the data can be accessed and edited through python code.


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


# closes and commits changes to the database using the connection created by the open_db() function.


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


# format_url() uses a hardcoded url and adds the queries to it so that it is easier to manage and to read.


def format_url():
    query = ["school.name", "school.state", "2018.student.size", "2017.student.size",
             "2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line",
             "2016.repayment.3_yr_repayment.overall", "2016.repayment.repayment_cohort.3_year_declining_balance"]
    sort = query[4]
    degree_type = "school.degrees_awarded.predominant=2,3"
    url = "https://api.data.gov/ed/collegescorecard/v1/schools.json?" + degree_type + "&fields=id"
    for query_element in query:
        url += "," + query_element
    url += "&sort=" + sort

    return url


# Drops the table school so that no conflicts are created and a clean table can be worked in.
# Once table has been dropped teh school table is created and all the columns created.


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute(''' DROP TABLE IF EXISTS school;''')
    cursor.execute('''DROP TABLE if EXISTS jobs;''')
    cursor.execute('''DROP TABLE if EXISTS states;''')
    cursor.execute('''CREATE TABLE if NOT EXISTS school(
    school_id INTEGER PRIMARY KEY,
    name TEXT,
    state_abrev TEXT,
    size_2017 INTEGER,
    size_2018 INTEGER,
    earnings INTEGER,
    repayment_overall INTEGER,
    repayment_cohort FLOAT);''')
    cursor.execute('''CREATE TABLE if NOT EXISTS jobs(
    job_id INTEGER PRIMARY KEY,
    state_name TEXT,
    occupation_code INTEGER,
    title TEXT,
    employment INTEGER,
    salary_25th_percentile INTEGER);''')


def excel_import(excel_file: str):
    excel = openpyxl.load_workbook(filename=excel_file)
    job_worksheet = excel.active
    occupation_groups = job_worksheet['J']
    rows_to_read = []
    excel_dict = []
    for group in occupation_groups:
        if group.value == "major":
            rows_to_read.append(group.row)

    for row in rows_to_read:
        excel_dict.append({'state': job_worksheet['B' + str(row)].value, 'code': str(job_worksheet['H' + str(row)].value)[:2],
                           'title': job_worksheet['I' + str(row)].value,
                           'employment': job_worksheet['K' + str(row)].value,
                           'salary': job_worksheet['Y' + str(row)].value})
    print("excel_import() has finished...sending data...")
    return excel_dict


# get_data takes the inputted URL and adds the api_key from secrets.py to the end of the url.
# the function then loops through all of the pages given the information from the metadata.
# looks good demo comment for checking actions


def get_data(url: str):
    # TODO: general clean up to make code more readable.
    all_data = []
    full_url = f"{url}&api_key={secrets.api_key}"
    response = requests.get(full_url)
    if response.status_code != 200:
        print(response.text)
        return []
    json_data = response.json()
    metadata = json_data['metadata']
    total_data = metadata['total']
    per_page = metadata['per_page']
    pages = round(total_data / per_page)

    for x in range(pages + 1):
        response = requests.get(full_url)
        if response.status_code != 200:
            print(response.text)
            return []
        json_data = response.json()
        results = json_data['results']
        all_data.extend(results)
        full_url = f"{url}&api_key={secrets.api_key}&page={x + 1}"
    print("get_data() has finished...sending data...")
    return all_data
    # write_to_file(all_data, "raw_results.txt")
    # write_to_file(clean_data(all_data), "clean_results.txt")


# clean_data() takes in the raw data taken from the results and formats it to be more readable.


def insert_data(table_data, table: str, cursor: sqlite3.Cursor):
    for data_element in table_data:
        if table == "school":
            name = data_element['school.name']
            state = data_element['school.state']
            school_id = data_element['id']
            size_2017 = data_element['2017.student.size']
            size_2018 = data_element['2018.student.size']
            earnings = data_element['2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line']
            repayment_overall = data_element['2016.repayment.3_yr_repayment.overall']
            repayment_cohort = data_element['2016.repayment.repayment_cohort.3_year_declining_balance']
            cursor.execute('''INSERT INTO SCHOOL (school_id, name, state_abrev, size_2017, size_2018, earnings,
            repayment_overall, repayment_cohort) VALUES (?, ?, ?, ?, ?, ?, ?,?)''',
                           (school_id, name, state, size_2017, size_2018, earnings,
                            repayment_overall, repayment_cohort))
        elif table == "jobs":
            occupation_id = data_element['code']
            state = data_element['state']
            occupation_title = data_element['title']
            employment = data_element['employment']
            salary = data_element['salary']
            cursor.execute('''INSERT INTO JOBS (job_id, state_name, occupation_code,title, employment, salary_25th_percentile)
                        VALUES (?,?, ?, ?, ?, ?)''',
                           (None, state, occupation_id, occupation_title, employment, salary))
        elif table == "states":
            cursor.execute('''INSERT INTO STATES (state_id, state_name, state_arbev)
                        VALUES(?,?,?)''', (None, data_element['state_name'], data_element['state.abrev']))


# query_run makes running queries easier so that a cursor and string can be provided
# and the results will be returned instead of rewriting execute statements everywhere.


def query_run(query: str, cursor: sqlite3.Cursor):
    finished_query = cursor.execute(query)
    return finished_query


def create_window():
    qt_app = jobsWindow.QApplication(sys.argv)
    my_window = jobsWindow.JobsWindow()
    my_window.repaint()
    sys.exit(qt_app.exec_())


def main():
    #school_data = get_data(format_url())
    #jobs_data = excel_import("state_job_data.xlsx")
    #conn, cursor = open_db("jobs_db.sqlite")
    #setup_db(cursor)
    #insert_data(school_data, "school", cursor)
    #insert_data(jobs_data, "jobs", cursor)
    #close_db(conn)
    create_window()


if __name__ == '__main__':
    main()
