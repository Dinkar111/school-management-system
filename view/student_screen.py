from students.student_manager import ManageStudent
import getpass
from simple_term_menu import TerminalMenu


class StudentScreen:

    def __init__(self, db):
        self.db = db

    # Student Signup Screen
    def student_register_view(self):
        print("\nPlease Register New Student:\n")
        first_name = input("\n Enter First Name: ")
        last_name = input("\n Enter Last Name: ")
        password = input("\n Enter Password: ")
        address = input("\n Enter Address: ")
        phone = input("\n Enter Phone: ")
        email = input("\n Enter Email: ")

        manage_student = ManageStudent(
            first_name=first_name,
            last_name=last_name,
            password=password,
            address=address,
            phone=phone,
            email=email
        )
        admit = manage_student.register_student(self.db)
        if not admit:
            print("\n   Student not admitted\n")
        elif admit['status'] == 404:
            print("\n   "+admit['message']+"\n")
        else:
            print("\n   "+admit['message']+"\n")

    # Login Screen
    def student_login_view(self):
        print("\nLogin:\n")
        email = input("\n Email: ")
        password = getpass.getpass(prompt="\n Password: ")

        manage_student = ManageStudent(
            email=email,
            password=password
        )
        student = manage_student.login_student(self.db)
        if student['status'] == 401:
            print("\n   "+student["message"]+"\n")
        else:
            print("\n   "+student["message"]+"\n")
            self.home_view(student["student_id"])

    # Home Screen
    def home_view(self, student_id):
        print("\n WELCOME !!")
        choices = {
            "1": self.profile_view,
            "2": self.view_all_student,
            "3": self.choose_other_subject,
            "4": self.update_student,
            "5": self.delete_student_account,
            "6": self.log_out
        }
        student_menu = ["1. View your profile", "2. View all students", "3. Choose other Subject",
                        "4. Update your profile", "5. Delete this account", "6. Logout"]
        menu = TerminalMenu(student_menu)
        display = menu.show()
        choice = student_menu[display][0]
        action = choices.get(choice)
        if action:
            action(student_id)
        else:
            print("\n   Please choose the right choice\n")
            self.home_view(student_id)

    # View Profile
    def profile_view(self, student_id):
        print('\n   Your Profile:')
        manage_student = ManageStudent(user_id=student_id)
        profile = manage_student.get_my_profile(self.db)
        if profile['status'] == 404:
            print("\n   "+profile["message"]+"\n")
        else:
            print('''
            <-------------------------------------------------------->
                Name            :   {}
                Address         :   {}
                Phone Number    :   {}
                Email           :   {}
                Chosen Subject  :   {}          Teacher Name : {}
            <-------------------------------------------------------->
            '''.format(profile['student_name'], profile['address'], profile['phone'],
                       profile['email'], profile['subject_name'], profile['teacher_name']))
        return self.home_view(student_id)

    # View list of all Students
    def view_all_student(self, student_id):
        manage_student = ManageStudent(user_id=student_id)
        all_students = manage_student.get_all_profile_to_view(self.db)
        print("\n   All students:")
        for student in all_students:
            print('''
            <---------------------------------------->
                Name        :   {} {}
                Address     :   {}
                Phone       :   {}
                Email       :   {}
            <---------------------------------------->
            '''.format(student['first_name'], student['last_name'], student['address'],
                       student['phone'], student['email']))
        return self.home_view(student_id)

    # Update Student and choose what to update
    def update_student(self, student_id):
        manage_student = ManageStudent(user_id=student_id)
        print('''
        <----------------><---------------->
            What do you want to update?
            1. Change Name
            2. Change Password
            3. Change Address
            4. Change Phone
            5. Change Email
        <----------------><---------------->
        ''')
        choices = {
            "1": manage_student.update_student_name,
            "2": manage_student.update_student_password,
            "3": manage_student.update_student_address,
            "4": manage_student.update_student_phone,
            "5": manage_student.update_student_email
        }
        choice = input("Enter choice: ")
        action = choices.get(choice)
        if action:
            update = action(self.db)
            if not update:
                print("")
                self.update_student(student_id)
            elif update['status'] == 400:
                print("\n   "+update['message']+"\n")
                self.update_student(student_id)
            else:
                print("\n   "+update['message']+"\n")
                self.home_view(student_id)
        else:
            print("Please choose the correct choice")
            self.update_student(student_id)

    # Delete student with confirmation
    def delete_student_account(self, student_id):
        manage_student = ManageStudent(user_id=student_id)
        delete_choices = ["1. Yes", "2. No"]
        menu = TerminalMenu(delete_choices, title="Do you really wish to delete this account?")
        display = menu.show()
        choice = delete_choices[display][0]
        if choice == "1":
            delete = manage_student.delete_student(self.db)
            print("\n   "+delete["message"]+"\n")
        else:
            print("\nStudent not deleted\n")
        self.home_view(student_id)

    def choose_other_subject(self, student_id):
        manage_student = ManageStudent(user_id=student_id)
        added_subject = manage_student.add_students_subjects(self.db)
        if added_subject['status'] == 500:
            print("\n   "+added_subject["message"]+"\n")
        else:
            print("\n   "+added_subject["message"]+"\n")
        self.home_view(student_id)

    # log out
    def log_out(self, student_id):
        db = self.db
        student_id = None
        print("\n   logged out\n")



