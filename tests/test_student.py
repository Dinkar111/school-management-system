
def test_login(db_setup, student_manager):
    db = db_setup
    student = student_manager
    student.email = "rajeshhamal@gmail.com"
    student.password = "rajeshdai"
    login = student.login_student(db)
    assert login


def test_get_user_by_id(db_setup, student_manager):
    db = db_setup
    student = student_manager
    student.s_id = 3
    user = student.get_user_by_id(db)
    expected_return = [3, 'Rajesh', 'Hamal', 'rajeshdai', 'Lazimpat', 9841470814, 'rajeshhamal@gmail.com']
    assert user == expected_return


def test_check_email_exist(db_setup, student_manager):
    db = db_setup
    student = student_manager
    student.email = "dinkarmaharjan@gmail.com"
    check_student = student.check_email_exist(db)
    assert check_student
