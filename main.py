"""
Main file
"""
import sys

from simple_term_menu import TerminalMenu
from decouple import config

from database import DbClass
from view.login_screen import LoginScreen


class Main:
    def __init__(self):

        # initiate DbClass
        self.db = DbClass(
            db_name=config("DB_NAME"),
            user_name=config("USER"),
            password=config("PASSWORD"),
            host_name=config("HOST"),
        )
        self.db.connect()
        self.db.create_all_tables()

        # initiate screen class object
        self.login_screen = LoginScreen(self.db)

        # choices to select in interface which action to run
        self.choices = {"Login": self.login_screen.login, "Exit": sys.exit}

    def main(self):
        try:
            main_menu = ["Login", "Exit"]
            menu = TerminalMenu(
                main_menu,
                title="""
            <------------------------->
            SCHOOL MANAGEMENT SYSTEM
            <------------------------->
            """,
            )
            display = menu.show()
            choice = main_menu[display]
            action = self.choices.get(choice)
            if action:
                action()
                self.main()
            else:
                print("\n   Please choose to login or exit\n")
                self.main()
        except TypeError:
            self.main()
        except KeyboardInterrupt:
            print("\n   Thank you, Goodbye\n")


if __name__ == "__main__":
    run = Main()
    run.main()
