from simple_term_menu import TerminalMenu

from .base_screen import BaseScreen


class StudentScreen(BaseScreen):
    def __init__(self, db, user):
        super().__init__(db)
        self.user = user

    # Home Screen
    def home_student_screen(self):
        choices = {
            "View your profile": self.your_profile_screen,
            "View your subjects": self.view_your_subjects,
            "View your teachers": self.view_your_teachers,
            "Logout": self.log_out,
        }
        student_menu = [
            "View your profile",
            "View your subjects",
            "View your teachers",
            "Logout",
        ]
        menu = TerminalMenu(
            student_menu,
            title="""
        <------------------------->
            STUDENT HOME
        <------------------------->
        """,
        )
        display = menu.show()
        choice = student_menu[display]
        action = choices.get(choice)
        if action:
            action()
        else:
            print("\n   Please choose the right choice\n")
            self.home_student_screen()

    # View Profile
    def your_profile_screen(self):
        res = self.student_manager.student_profile(self.user)
        if res["status"] == 404:
            print("\n -------> " + res["message"] + "\n")
        else:
            student = res["student"]
            print(
                """
                Your Profile
                <-------------------------------------------------------->
                    Name            :   {}
                    Address         :   {}
                    Phone Number    :   {}
                    Email           :   {}
                    Grade           :   {}
                    Roll no         :   {}
                <-------------------------------------------------------->
            """.format(
                    student.get_name,
                    student.get_address,
                    student.get_phone,
                    student.get_email,
                    student.get_grade,
                    student.get_roll_no,
                )
            )
        return self.home_student_screen()

    # View list of all Students
    def view_your_subjects(self):
        res = self.student_manager.show_student_subjects(self.user)
        if res["status"] == 404:
            print("\n -------> " + res["message"] + "\n")
        else:
            print("\n You must study these subjects in your class:")
            for subject in res["subjects"]:
                print(
                    """
                <---------------------------------------->
                    Subject Code:   {}
                    Subject Name:   {}
                <---------------------------------------->
                """.format(
                        subject.get_subject_code,
                        subject.get_subject_name,
                    )
                )
        return self.home_student_screen()

    def view_your_teachers(self):
        res = self.student_manager.show_student_teachers(self.user)
        if res["status"] == 404:
            print("\n -------> " + res["message"] + "\n")
        else:
            print("\n Teachers who teach me :- ")
            for teacher in res["teachers"]:
                print(
                    """
                    <---------------------------------------->
                    Name        :   {}
                    Address     :   {}
                    Phone       :   {}
                    Email       :   {}
                    Grade       :   {}
                    Subject     :   {}
                    <---------------------------------------->
                    """.format(
                        teacher.get_name,
                        teacher.get_address,
                        teacher.get_phone,
                        teacher.get_email,
                        teacher.get_grades,
                        teacher.get_subjects,
                    )
                )
        return self.home_student_screen()

    # log out
    def log_out(self):
        print("\n   logged out\n")
