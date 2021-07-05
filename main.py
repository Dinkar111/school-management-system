from config import DBConfigClass
from database import DbClass
from view.student_screen import StudentScreen
from view.admin_screen import AdminScreen
from view.teacher_screen import TeacherScreen
import sys
from simple_term_menu import TerminalMenu
import pdb


class Main:

    def __init__(self):
        # Config file
        db_config = DBConfigClass()

        # get db config data from DBConfigClass() object
        db_data = db_config.get_config()

        # initiate DbClass
        self.db = DbClass(
            db_name=db_data["db"],
            user_name=db_data["user"],
            password=db_data["password"],
            host_name=db_data["host"]
        )
        self.db.connect()
        self.db.create_all_tables()

        # initiate screen class object
        self.student_screen = StudentScreen(self.db)
        self.teacher_screen = TeacherScreen(self.db)
        self.admin_screen = AdminScreen(self.db)

        # choices to select in interface which action to run
        self.choices = {
            "1": self.login,
            "2": self.register,
            "3": self.admin_screen.login_admin_view,
            "4": sys.exit
        }

    def login(self):
        login_choice = {
            "1": self.student_screen.student_login_view,
            "2": self.teacher_screen.teacher_login_view,
            "3": self.main
        }
        login_menu = ["1. Login as student", "2. Login as teacher", "3. Back"]
        menu = TerminalMenu(login_menu)
        display = menu.show()
        choice = login_menu[display][0]
        action = login_choice.get(choice)
        if action == "3":
            action()
        elif action:
            action()
            self.main()
        else:
            print("\n   Are you teacher or a student?\n")
            self.login()

    def register(self):
        register_choice = {
            "1": self.student_screen.student_register_view,
            "2": self.teacher_screen.teacher_register_view,
            "3": self.main
        }
        register_menu = ["1. Register as student", "2. Register as teacher", "3. Back"]
        menu = TerminalMenu(register_menu)
        display = menu.show()
        choice = register_menu[display][0]
        action = register_choice.get(choice)
        if action == "3":
            action()
        elif action:
            action()
            self.main()
        else:
            print("\n   Are you teacher or a student?\n")
            self.register()

    def main(self):
        try:
            main_menu = ["1. Login", "2. Register", "3. Login as admin", "4. Exit"]
            menu = TerminalMenu(main_menu, title="SCHOOL MANAGEMENT SYSTEM")
            display = menu.show()
            choice = main_menu[display][0]
            action = self.choices.get(choice)
            if action:
                action()
                self.main()
            else:
                print("\n   Please choose to login, signup or exit\n")
                self.main()
        except TypeError:
            self.main()
        except KeyboardInterrupt as e:
            print("\n   Thank you, Goodbye\n")

     
if __name__ == "__main__":
    run = Main()
    run.main()
