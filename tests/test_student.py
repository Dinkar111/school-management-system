def test_login(user_manager):
    email = "ram@s.com"
    password = "Password@123"
    login = user_manager.login_user(email, password)
    assert login["status"] == 200
    assert login["message"] == "Logged in"


def test_student_register(student_manager):
    register = student_manager.register_student(
        first_name="Ram",
        last_name="Laxman",
        email="ram@s.com",
        password="Password@123",
        address="Janakpur",
        phone="9841707744",
        grade=1,
    )
    assert register["status"] == 200
    assert register["message"] == "Student has been admitted."
