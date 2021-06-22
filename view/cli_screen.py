from students.student_manager import ManageStudent
import getpass


class CliScreen:

    def __init__(self, db):
        self.db = db

    # Signup Screen
    def register_view(self):
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
        if admit:
            print("\n   Student has been admitted.\n")
        else:
            print("\n   Student not admitted.\n")

    # Login Screen
    def login_view(self):
        print("\nLogin:\n")
        email = input("\n Email: ")
        password = getpass.getpass(prompt="\n Password: ")

        manage_student = ManageStudent(
            email=email,
            password=password
        )
        student_id = manage_student.login_student(self.db)
        if student_id:
            print("\n   logged in\n")
            self.home_view(student_id)

    # Home Screen
    def home_view(self, student_id):
        print('''
         What do you want to do?
        1. View your profile
        2. View other students
        3. Update your profile
        4. Delete this account
        5. Logout
        ''')
        choices = {
            "1": self.profile_view,
            "2": self.view_all_student,
            "3": self.update_student,
            "4": self.delete_student_account,
            "5": self.log_out
        }
        choice = input("Please choose: ")
        action = choices.get(choice)
        if action:
            action(student_id)
        else:
            print("\n   Please choose the right choice\n")
            self.home_view(student_id)

    # View Profile
    def profile_view(self, student_id):
        print('\n   Your Profile:')
        manage_student = ManageStudent(s_id=student_id)
        profile = manage_student.get_my_profile(self.db)
        print('''
        <---------------------------------------->
            First Name  :   {}
            Last Name   :   {}
            Address     :   {}
            Phone Number:   {}
            Email       :   {}
        <---------------------------------------->
        '''.format(profile['first_name'], profile['last_name'], profile['address'], profile['phone'], profile['email']))
        return self.home_view(student_id)

    # View list of all Students
    def view_all_student(self, student_id):
        print("\n   All students:")
        manage_student = ManageStudent(s_id=student_id)
        all_students = manage_student.get_all_profile_to_view_only(self.db)
        for student in all_students:
            print('''
            <---------------------------------------->
            Name        :   {}
            Address     :   {}
            Phone       :   {}
            Email       :   {}
            <---------------------------------------->
            '''.format(student[0], student[1], student[2], student[3]))
        return self.home_view(student_id)

    # Update Student and choose what to update
    def update_student(self, student_id):
        manage_student = ManageStudent(s_id=student_id)
        print('''
            What do you want to update?
            1. Change Name
            2. Change Password
            3. Change Address
            4. Change Phone
            5. Change Email
        ''')
        choices = {
            "1": manage_student.update_name,
            "2": manage_student.update_password,
            "3": manage_student.update_address,
            "4": manage_student.update_phone,
            "5": manage_student.update_email
        }
        choice = input("Enter choice: ")
        action = choices.get(choice)
        if action:
            action(self.db)
            self.home_view(student_id)

    # Delete student with confirmation
    def delete_student_account(self, student_id):
        manage_student = ManageStudent(s_id=student_id)
        print('''
               Do you really wish to delete this account?
                   1. Yes
                   2. No
               ''')
        choice = input("Yes or no (1 or 2): ")
        if choice == "1":
            manage_student.delete_student(self.db)
            print("\nStudent has been deleted\n")
        else:
            print("\nStudent not deleted\n")
            self.home_view(student_id)

    # log out
    def log_out(self, student_id):
        db = self.db
        student_id = None
        print("logged out")



