import jobs


# makes sure there are over 1000 entries of data being accessed.


def test_get_data():
    data = jobs.get_data(jobs.format_url())
    assert len(data) > 1000


# test_db_creation90 creates an empty database and inserts a test entry
# the test then uses query_run() to get a query which should return the data entered and then tests it
# against the test_data list.


def test_db_creation():
    test_data = [{'school.name': 'Test School', '2017.student.size': 5, '2018.student.size': 1, 'school.state': 'NJ',
                  'id': 1, '2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 1,
                  '2016.repayment.3_yr_repayment.overall': 1},
                 {'school.name': 'Test School 1', '2017.student.size': 4, '2018.student.size': 6, 'school.state': 'MA',
                  'id': 2, '2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 1,
                  '2016.repayment.3_yr_repayment.overall': 1}]
    conn, cursor = jobs.open_db("test_db.sqlite")
    jobs.setup_db(cursor)
    jobs.insert_data(test_data, "school", cursor)
    jobs.close_db(conn)
    conn, cursor = jobs.open_db("test_db.sqlite")
    test_query = jobs.query_run("SELECT * FROM" + " SCHOOL;", cursor)
    for (row, element) in zip(test_query, test_data):
        assert row[0] == element['id']
        assert row[1] == element['school.name']
        assert row[2] == element['school.state']
        assert row[3] == element['2017.student.size']
        assert row[4] == element['2018.student.size']
        assert row[5] == element['2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line']
        assert row[6] == element['2016.repayment.3_yr_repayment.overall']
    jobs.close_db(conn)
