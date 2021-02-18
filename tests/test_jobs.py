import jobs


def test_get_data():
    data = jobs.get_data(jobs.format_url())
    assert len(data) > 1000


def test_db_creation():
    test_data = [{'school.name': 'Test School', '2017.student.size': 5, '2018.student.size': 1, 'school.state': 'NJ',
                  'id': 1, '2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line': 1,
                  '2016.repayment.3_yr_repayment.overall': 1}]

    conn, cursor = jobs.open_db("test_db.sqlite")
    jobs.setup_db(cursor)
    jobs.insert_data(test_data, cursor)
    jobs.close_db(conn)
    conn, cursor = jobs.open_db("test_db.sqlite")
    test_query = jobs.query_run("SELECT * FROM" + " SCHOOL;", cursor)
    for row in test_query:
        pass
    jobs.close_db(conn)
