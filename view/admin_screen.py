import getpass
from simple_term_menu import TerminalMenu

from .base_screen import BaseScreen
from helpers.helper_func import select_grade


class AdminScreen(BaseScreen):
    def __init__(self, db, user):
        super().__init__(db)
        self.user = user

    # Admin Home Screen
    def home_admin_screen(self):
        choices = {
            "View your profile": self.admin_profile_screen,
            "View all students": self.view_all_students_screen,
            "View all teachers": self.view_all_teachers_screen,
            "Add Student": self.student_register_screen,
            "Add Teacher": self.teacher_register_screen,
            "Add Subject": self.add_subjects_screen,
            "View Subjects": self.view_subjects_screen,
            "Add Grades": self.add_grade_screen,
            "View Grades": self.view_grades_screen,
            "Log Out": self.log_out,
        }
        admin_menu = [
            "View your profile",
            "View all students",
            "View all teachers",
            "Add Student",
            "Add Teacher",
            "Add Subject",
            "View Subjects",
            "Add Grades",
            "View Grades",
            "Log Out",
        ]
        menu = TerminalMenu(
            admin_menu,
            title="""
        <------------------------->
            ADMIN HOME
        <------------------------->
        """,
        )
        display = menu.show()
        choice = admin_menu[display]
        action = choices.get(choice)
        if action:
            action()
        else:
            print("\n   Please choose the right choice\n")
            self.home_admin_screen()

    # profile of admin
    def admin_profile_screen(self):
        print(
            """
        Admin Profile
        <---------------------------------------->
            Admin Name  :   {}
            Email       :   {}
        <---------------------------------------->
        """.format(
                self.user.get_name, self.user.get_email
            )
        )
        return self.home_admin_screen()

    # view all students
    def view_all_students_screen(self):
        grade_name = select_grade(self.grade_manager)
        if grade_name:
            res = self.student_manager.show_all_students(grade_name)
            if res["status"] == 404:
                print("\n -------> " + res["message"] + "\n")
            else:
                print("\n All Students of {}:- ".format(grade_name))
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
        return self.home_admin_screen()

    # view all teachers
    def view_all_teachers_screen(self):
        grade_name = select_grade(self.grade_manager)
        if grade_name:
            res = self.teacher_manager.show_all_teachers(grade_name)
            if res["status"] == 404:
                print("\n -------> " + res["message"] + "\n")
            else:
                print("\n All Teachers of {}:- ".format(grade_name))
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
        return self.home_admin_screen()

    # Student Signup Screen
    def student_register_screen(self):
        print("\nPlease Register New Student:\n")
        first_name = input("\n Enter First Name: ")
        last_name = input("\n Enter Last Name: ")
        password = getpass.getpass(prompt="\n Password: ")
        address = input("\n Enter Address: ")
        phone = input("\n Enter Phone: ")
        email = input("\n Enter Email: ")

        grade_name = select_grade(self.grade_manager)
        if grade_name:
            grade = self.grade_manager.get_grade_by_name(grade_name)
            roll_no = grade.get_no_of_students + 1

            res = self.student_manager.register_student(
                first_name=first_name,
                last_name=last_name,
                password=password,
                address=address,
                phone=phone,
                email=email,
                grade=grade,
                roll_no=roll_no,
            )

            if res["status"] == 409:
                print("\n -------> " + res["message"] + "\n")
            elif res["status"] == 500:
                print("\n -------> " + res["message"] + "\n")
            elif res["status"] == 400:
                print("\n -------> " + res["message"] + "\n")
            else:
                self.grade_manager.add_no_of_students(grade)
                print("\n -------> " + res["message"] + "\n")
        else:
            return self.home_admin_screen()
        return self.home_admin_screen()

    # Student Signup Screen
    def teacher_register_screen(self):
        print("\nPlease Register New Teacher:\n")
        first_name = input("\n Enter First Name: ")
        last_name = input("\n Enter Last Name: ")
        password = getpass.getpass(prompt="\n Password: ")
        address = input("\n Enter Address: ")
        phone = input("\n Enter Phone: ")
        email = input("\n Enter Email: ")

        grade_name = select_grade(self.grade_manager)
        if grade_name:
            grade = self.grade_manager.get_grade_by_name(grade_name)

            res = self.teacher_manager.register_teacher(
                first_name=first_name,
                last_name=last_name,
                password=password,
                address=address,
                phone=phone,
                email=email,
                grade=grade,
            )

            if res["status"] == 409:
                print("\n -------> " + res["message"] + "\n")
            elif res["status"] == 500:
                print("\n -------> " + res["message"] + "\n")
            elif res["status"] == 400:
                print("\n -------> " + res["message"] + "\n")
            else:
                print("\n -------> " + res["message"] + "\n")
        else:
            return self.home_admin_screen()
        return self.home_admin_screen()

    # Add subject Screen
    def add_subjects_screen(self):
        print("\nPlease Add New Subject:\n")
        subject_code = input("\n Enter Subject Code: ")
        subject_name = input("\n Enter Subject Name: ")
        grade_name = select_grade(self.grade_manager)
        if grade_name:
            grade = self.grade_manager.get_grade_by_name(grade_name)
            grade_id = grade.get_id
            res = self.subject_manager.add_subject(
                subject_code=subject_code,
                subject_name=subject_name,
                grade_id=grade_id,
            )
            if res["status"] == 409:
                print("\n ------->" + res["message"] + "\n")
                self.add_subjects_screen()
            elif res["status"] == 500:
                print("\n -------> " + res["message"] + "\n")
            else:
                print("\n -------> " + res["message"] + "\n")
        return self.home_admin_screen()

    # View all subject
    def view_subjects_screen(self):
        grade_name = select_grade(self.grade_manager)
        if grade_name:
            grade = self.grade_manager.get_grade_by_name(grade_name)
            if grade:
                res = self.subject_manager.get_all_subjects_by_grade(grade)
                if res["status"] == 404:
                    print("\n -------> " + res["message"] + "\n")
                else:
                    print("\n All Subjects:- ")
                    for subject in res["subjects"]:
                        print(
                            """
                        <---------------------------------------->
                        Subject Code:   {}
                        Subject Name:   {}
                        Grade       :   {}
                        <---------------------------------------->
                        """.format(
                                subject.get_subject_code,
                                subject.get_subject_name,
                                subject.get_grade,
                            )
                        )
        return self.home_admin_screen()

    # Add Grades Screen
    def add_grade_screen(self):
        grade = input("Enter Grade? <eg. Class 1> :")
        res = self.grade_manager.add_grades(grade)
        if res["status"] == 400:
            print("\n -------> " + res["message"] + "\n")
            print("Add Another Grade\n")
            return self.add_grade_screen()
        else:
            print("\n -------> " + res["message"] + "\n")
        return self.home_admin_screen()

    # View all grades
    def view_grades_screen(self):
        res = self.grade_manager.show_all_grades()
        if res["status"] == 404:
            print("\n -------> " + res["message"] + "\n")
        else:
            print("\n All Grades:- ")
            for grade in res["grades"]:
                print(
                    """
                <---------------------------------------->
                Grade         :   {}
                No of Students:   {}
                <---------------------------------------->
                """.format(
                        grade.get_grade,
                        grade.get_no_of_students,
                    )
                )
        return self.home_admin_screen()

    # log out
    def log_out(self):
        print("\n   logged out\n")
