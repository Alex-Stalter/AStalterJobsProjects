import jobs
import openpyxl


# makes sure there are over 1000 entries of data being accessed.


def test_get_data():
    data = jobs.get_data(jobs.format_url())
    assert len(data) > 1000


# test_db_creation90 creates an empty database and inserts a test entry
# the test then uses query_run() to get a query which should return the data entered and then tests it
# against the test_data list.


def test_db_creation():
    school_test_data = [
        {'school.name': 'Test School', '2017.student.size': 5, '2018.student.size': 1, 'school.state': 'NJ',
         'id': 1, '2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 1,
         '2016.repayment.3_yr_repayment.overall': 1, '2016.repayment.repayment_cohort.3_year_declining_balance': 0.5},
        {'school.name': 'Test School 1', '2017.student.size': 4, '2018.student.size': 6, 'school.state': 'MA',
         'id': 2, '2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 1,
         '2016.repayment.3_yr_repayment.overall': 1, '2016.repayment.repayment_cohort.3_year_declining_balance': 0.5}]
    job_test_data = [{'state': 'Massachusetts', 'code': '00-0001', 'title': 'testttl', 'employment': 5, 'salary': 1000}]
    expected_tables = ['school', 'jobs']

    conn, cursor = jobs.open_db("test_db.sqlite")
    jobs.setup_db(cursor)
    jobs.insert_data(job_test_data, "jobs", cursor)
    jobs.insert_data(school_test_data, "school", cursor)
    jobs.close_db(conn)
    conn, cursor = jobs.open_db("test_db.sqlite")

    tables_query = jobs.query_run("SELECT name FROM " + "sqlite_master WHERE type='table' and name NOT LIKE 'sqlite_%';"
                                                        "", cursor)
    for (table, returned_tables) in zip(expected_tables, tables_query):
        assert table == returned_tables[0]
    school_query = jobs.query_run("SELECT * FROM" + " SCHOOL;", cursor)
    for (row, element) in zip(school_query, school_test_data):
        assert row[0] == element['id']
        assert row[1] == element['school.name']
        assert row[2] == element['school.state']
        assert row[3] == element['2017.student.size']
        assert row[4] == element['2018.student.size']
        assert row[5] == element['2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line']
        assert row[6] == element['2016.repayment.3_yr_repayment.overall']
        assert row[7] == element['2016.repayment.repayment_cohort.3_year_declining_balance']
    jobs_query = jobs.query_run("SELECT * FROM" + " JOBS;", cursor)
    for (row, element) in zip(jobs_query, job_test_data):
        assert row[0] == 1
        assert row[1] == element['state']
        assert row[2] == element['code']
        assert row[3] == element['title']
        assert row[4] == element['employment']
        assert row[5] == element['salary']

    jobs.close_db(conn)


def test_excel_import_jobs():
    jobs_data = jobs.excel_jobs_import("state_job_data.xlsx")
    assert len(jobs_data) > 1000
    conn, cursor = jobs.open_db("excel_import_test.sqlite")
    jobs.setup_db(cursor)
    jobs.insert_data(jobs_data, "jobs", cursor)
    jobs.close_db(conn)
    conn, cursor = jobs.open_db("excel_import_test.sqlite")
    state_query = jobs.query_run("SELECT count(DISTINCT state_name) from" + " jobs;", cursor)
    for element in state_query:
        assert element[0] > 50


def test_specific_excel_data():
    excel_test_data = ["massachusetts", 0, "test", "major", 5, 5]
    excel_book = openpyxl.load_workbook(filename="test_workbook.xlsx")
    test_sheet = excel_book.active
    test_sheet['B2'] = excel_test_data[0]
    test_sheet['H2'] = excel_test_data[1]
    test_sheet['I2'] = excel_test_data[2]
    test_sheet['J2'] = excel_test_data[3]
    test_sheet['K2'] = excel_test_data[4]
    test_sheet['Y2'] = excel_test_data[5]
    excel_book.save(filename="test_workbook.xlsx")
    test_dict = jobs.excel_jobs_import("test_workbook.xlsx")
    conn, cursor = jobs.open_db("test_specific_excel_data.sqlite")
    jobs.setup_db(cursor)
    jobs.insert_data(test_dict, "jobs", cursor)
    jobs.close_db(conn)
    conn, cursor = jobs.open_db("test_specific_excel_data.sqlite")
    specific_data_query = jobs.query_run("SELECT * FROM " + "JOBS;", cursor)
    for element in specific_data_query:
        assert element[1] == excel_test_data[0]
        assert element[2] == excel_test_data[1]
        assert element[3] == excel_test_data[2]
        assert element[4] == excel_test_data[4]
        assert element[5] == excel_test_data[5]
