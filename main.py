from config import DBConfigClass
from database import DbClass
from view.cli_screen import CliScreen
import sys


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

        # initiate screen class object
        self.cli_screen = CliScreen(self.db)

        # choices to select in interface which action to run
        self.choices = {
            "1": self.cli_screen.login_view,
            "2": self.cli_screen.register_view,
            "3": sys.exit
        }

    def main(self):

        print("SCHOOL MANAGEMENT SYSTEM")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        try:
            choice = input("\nWhat would you like to do? Please choose: \n")
            action = self.choices.get(choice)
            if action:
                action()
                self.main()
            else:
                print("Thank you, Goodbye")
        except KeyboardInterrupt as e:
            print("\nThank you, Goodbye\n")

     
if __name__ == "__main__":
    run = Main()
    run.main()
