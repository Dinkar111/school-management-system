from simple_term_menu import TerminalMenu

from .base_screen import BaseScreen
from models.grade import Grade


class TeacherScreen(BaseScreen):
    def __init__(self, db, user):
        super().__init__(db)
        self.user = user

    # Home Screen
    def home_teacher_screen(self):
        choices = {
            "View your profile": self.your_profile_screen,
            "View my students": self.view_my_students_screen,
            "Choose your subject": self.choose_subject_screen,
            "Logout": self.log_out,
        }
        teacher_menu = [
            "View your profile",
            "View my students",
            "Choose your subject",
            "Logout",
        ]
        menu = TerminalMenu(
            teacher_menu,
            title="""
        <------------------------->
            TEACHER HOME
        <------------------------->
        """,
        )
        display = menu.show()
        choice = teacher_menu[display]
        action = choices.get(choice)
        if action:
            action()
        else:
            print("\n   Please choose the right choice\n")
            self.home_teacher_screen()

    # View Profile
    def your_profile_screen(self):
        res = self.teacher_manager.teacher_profile(self.user)
        if res["status"] == 404:
            print("\n -------> " + res["message"] + "\n")
        else:
            teacher = res["teacher"]
            print(
                """
            Your Profile
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
        return self.home_teacher_screen()

    # choose teachers subject
    def choose_subject_screen(self):
        teacher = self.teacher_manager.teacher_profile(self.user)
        if teacher["status"] == 404:
            print("\n -------> " + teacher["message"] + "\n")
        else:
            teacher_obj = teacher["teacher"]
            grade_name = teacher_obj.get_grades
            grade_object = Grade(grade=grade_name)
            subjects = self.subject_manager.get_all_subjects_by_grade(
                grade_object
            )
            if subjects["status"] == 404:
                print("\n -------> " + subjects["message"] + "\n")
            else:
                subject_codes = [
                    subject.get_subject_code
                    for subject in subjects["subjects"]
                ]
                terminal = TerminalMenu(
                    subject_codes,
                    title="""
                Choose Subject:
                """,
                )
                show = terminal.show()
                subject_code = subject_codes[show]
                subject = self.subject_manager.get_subject_by_code(
                    subject_code
                )
                if subject["status"] == 404:
                    print("\n -------> " + subjects["message"] + "\n")
                else:
                    subject_obj = subject["subject"]
                    res = self.teacher_manager.choose_subject(
                        teacher_obj, subject_obj
                    )
                    if res["status"] == 200:
                        print("\n -------> " + res["message"] + "\n")
        return self.home_teacher_screen()

    def view_my_students_screen(self):
        res = self.teacher_manager.show_teacher_students(self.user)
        if res["status"] == 404:
            print("\n -------> " + res["message"] + "\n")
        else:
            print("\n My Students :- ")
            for student in res["students"]:
                print(
                    """
                    <---------------------------------------->
                    Name        :   {}
                    Address     :   {}
                    Phone       :   {}
                    Email       :   {}
                    Roll        :   {}
                    Grade       :   {}
                    <---------------------------------------->
                    """.format(
                        student.get_name,
                        student.get_address,
                        student.get_phone,
                        student.get_email,
                        student.get_roll_no,
                        student.get_grade,
                    )
                )
        return self.home_teacher_screen()

    # log out
    def log_out(self):
        print("\n   logged out\n")
