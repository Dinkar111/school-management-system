from admins.admin_manager import AdminManager
from students.student import Student
from teachers.teacher import Teacher
import getpass
from simple_term_menu import TerminalMenu


class AdminScreen:

    def __init__(self, db):
        self.db = db

    def login_admin_view(self):
        print("\n Admin Login")
        name = input("\n     enter admin fullname: ")
        password = getpass.getpass(prompt="     enter admin password: ")

        admin_manager = AdminManager(admin_username=name, admin_password=password)
        admin = admin_manager.admin_login(self.db)
        if admin['status'] == 401:
            print(admin["message"])
        else:
            print(admin["message"])
            self.home_admin_view(admin['admin_id'])

    # Admin Home Screen
    def home_admin_view(self, admin_id):
        choices = {
            "1": self.admin_profile,
            "2": self.view_all_students,
            "3": self.view_all_teachers,
            "4": self.add_subjects,
            "5": self.view_subjects,
            "8": self.log_out
        }

        admin_menu = ["1. View your profile", "2. View all students", "3. View all teachers",
                      "4. Add Subject", "5. View Subjects", "8. Logout"]
        menu = TerminalMenu(admin_menu)
        display = menu.show()
        choice = admin_menu[display][0]
        action = choices.get(choice)
        if action:
            action(admin_id)
        else:
            print("\n   Please choose the right choice\n")
            self.home_admin_view(admin_id)

    # profile of admin
    def admin_profile(self, admin_id):
        admin_manager = AdminManager(admin_id=admin_id)
        admin_profile = admin_manager.admin_profile(self.db)
        if admin_profile['status'] == 404:
            print("\n   "+admin_profile["message"]+"\n")
        else:
            print('''
            <---------------------------------------->
                Admin Name  :   {}
                Email       :   {}
            <---------------------------------------->
            '''.format(admin_profile['admin_username'], admin_profile['admin_email']))
        return self.home_admin_view(admin_id)

    # view all students
    def view_all_students(self, admin_id):
        student = Student()
        students = student.get_all_profile_to_view(self.db)
        if not students:
            print("\n   No students\n")
        else:
            print("\n All Students:- ")
            for student in students:
                print('''
                <---------------------------------------->
                ID          :   {}
                Name        :   {} {}
                Address     :   {}
                Phone       :   {}
                Email       :   {}
                <---------------------------------------->
                '''.format(student['student_id'], student['first_name'], student['last_name'],
                           student['address'], student['phone'], student['email']))
        return self.home_admin_view(admin_id)

    # view all teachers
    def view_all_teachers(self, admin_id):
        teacher = Teacher()
        teachers = teacher.get_all_profile_to_view(self.db)
        if not teachers:
            print("\n   No teachers\n")
        else:
            print("\n All Teachers:- ")
            for teacher in teachers:
                print('''
                <---------------------------------------->
                ID          :   {}
                Name        :   {}
                Address     :   {}
                Phone       :   {}
                Email       :   {}
                Subject     :   {}
                <---------------------------------------->
                '''.format(teacher['teacher_id'], teacher['full_name'], teacher['address'], teacher['phone'],
                           teacher['email'], teacher['subject_name']))
        return self.home_admin_view(admin_id)

    # Add subject
    def add_subjects(self, admin_id):
        admin_manager = AdminManager(admin_id=admin_id)
        subject = admin_manager.add_subject(self.db)
        if subject['status'] == 409:
            print("\n   "+subject['message']+"\n")
            self.add_subjects(admin_id)
        else:
            print("\n   "+subject['message']+"\n")
            return self.home_admin_view(admin_id)

    # View all subject
    def view_subjects(self, admin_id):
        admin_manager = AdminManager(admin_id=admin_id)
        subjects = admin_manager.view_subject(self.db)
        if not subjects:
            print("\n   No subjects founds\n")
        else:
            print("\n All Subjects:- ")
            for subject in subjects:
                print('''
                <---------------------------------------->
                Subject ID  :   {}
                Subject Name:   {}
                <---------------------------------------->
                '''.format(subject['subject_id'], subject['subject_name'],))
        return self.home_admin_view(admin_id)

    # log out
    def log_out(self, teacher_id):
        db = self.db
        teacher_id = None
        print("\n   logged out\n")



