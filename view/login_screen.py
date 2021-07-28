import getpass

from .base_screen import BaseScreen
from .admin_screen import AdminScreen
from .student_screen import StudentScreen
from .teacher_screen import TeacherScreen


class LoginScreen(BaseScreen):
    def __init__(self, db):
        super().__init__(db)

    def login(self):
        print("\nLogin:\n")
        email = input("\n Email: ")
        password = getpass.getpass(prompt="\n Password: ")
        res = self.user_manager.login_user(email, password)
        if res["status"] == 401:
            print("\n   " + res["message"] + "\n")
        else:
            print("\n   " + res["message"] + "\n")
            if res["user"].is_teacher:
                teacher_screen = TeacherScreen(self.db, res["user"])
                teacher_screen.home_teacher_screen()
            elif res["user"].is_student:
                student_screen = StudentScreen(self.db, res["user"])
                student_screen.home_student_screen()
            else:
                admin_screen = AdminScreen(self.db, res["user"])
                admin_screen.home_admin_screen()
