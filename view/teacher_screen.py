from teachers.teacher_manager import TeacherManager
import getpass
from simple_term_menu import TerminalMenu


class TeacherScreen:

    def __init__(self, db):
        self.db = db

    # Teacher Signup Screen
    def teacher_register_view(self):
        print("\nPlease Register New Teacher:\n")
        first_name = input("\n Enter First Name: ")
        last_name = input("\n Enter Last Name: ")
        password = input("\n Enter Password: ")
        address = input("\n Enter Address: ")
        phone = input("\n Enter Phone: ")
        email = input("\n Enter Email: ")

        manage_teacher = TeacherManager(
            first_name=first_name,
            last_name=last_name,
            password=password,
            address=address,
            phone=phone,
            email=email
        )
        admit = manage_teacher.register_teacher(self.db)
        if not admit:
            print("\n   Teacher not admitted\n")
        elif admit['status'] == 409:
            print("\n   "+admit['message']+"\n")
        else:
            print("\n   "+admit['message']+"\n")

    # Login Screen
    def teacher_login_view(self):
        print("\nLogin:\n")
        email = input("\n Email: ")
        password = getpass.getpass(prompt="\n Password: ")

        manage_teacher = TeacherManager(
            email=email,
            password=password
        )
        teacher = manage_teacher.login_teacher(self.db)
        if teacher['status'] == 401:
            print("\n   "+teacher["message"]+"\n")
        else:
            print("\n   "+teacher["message"]+"\n")
            self.teacher_home_view(teacher["teacher_id"])

    # Home Screen
    def teacher_home_view(self, teacher_id):
        print("\n WELCOME !!")
        choices = {
            "1": self.profile_view,
            "2": self.view_all_teachers,
            "3": self.update_teacher,
            "4": self.choose_other_subject,
            "5": self.delete_teacher_account,
            "6": self.log_out
        }
        teacher_menu = ["1. View your profile", "2. View Teachers", "3. Update your profile",
                        "4. Select your subject", "5. Delete this account", "6. Logout"]
        menu = TerminalMenu(teacher_menu)
        display = menu.show()
        choice = teacher_menu[display][0]
        action = choices.get(choice)
        if action:
            action(teacher_id)
        else:
            print("\n   Please choose the right choice\n")
            self.teacher_home_view(teacher_id)

    # View Profile
    def profile_view(self, teacher_id):
        print('\n   Your Profile:')
        manage_teacher = TeacherManager(user_id=teacher_id)
        profile = manage_teacher.get_my_profile(self.db)
        if profile['status'] == 404:
            print("\n   "+profile["message"]+"\n")
        else:
            print('''
            <---------------------------------------->
                Name        :   {}
                Address     :   {}
                Phone Number:   {}
                Email       :   {}
                Subject     :   {}
            <---------------------------------------->
            '''.format(profile['full_name'], profile['address'], profile['phone'],
                       profile['email'], profile['subject_name']))
            return self.teacher_home_view(teacher_id)

    # View list of all Students
    def view_all_teachers(self, teacher_id):
        print("\n   All teachers:")
        manage_teacher = TeacherManager(user_id=teacher_id)
        all_teachers = manage_teacher.get_all_profile_to_view(self.db)
        for teacher in all_teachers:
            print('''
            <---------------------------------------->
                Name        :   {}
                Address     :   {}
                Phone Number:   {}
                Email       :   {}
                Subject     :   {}
            <---------------------------------------->
            '''.format(teacher['full_name'], teacher['address'], teacher['phone'],
                       teacher['email'], teacher['subject_name']))
        return self.teacher_home_view(teacher_id)

    # Update Teacher and choose what to update
    def update_teacher(self, teacher_id):
        manage_teacher = TeacherManager(user_id=teacher_id)
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
            "1": manage_teacher.update_teacher_name,
            "2": manage_teacher.update_teacher_password,
            "3": manage_teacher.update_teacher_address,
            "4": manage_teacher.update_teacher_phone,
            "5": manage_teacher.update_teacher_email,
        }
        choice = input("Enter choice: ")
        action = choices.get(choice)
        if action:
            update = action(self.db)
            if not update:
                print("")
                self.update_teacher(teacher_id)
            elif update['status'] == 400:
                print("\n   "+update['message']+"\n")
                self.update_teacher(teacher_id)
            else:
                print("\n   "+update['message']+"\n")
                self.teacher_home_view(teacher_id)
        else:
            print("Please choose the correct choice")
            self.update_teacher(teacher_id)

    # Delete teacher with confirmation
    def delete_teacher_account(self, teacher_id):
        manage_teacher = TeacherManager(user_id=teacher_id)
        delete_choices = ["1. Yes", "2. No"]
        menu = TerminalMenu(delete_choices, title="Do you really wish to delete this account?")
        display = menu.show()
        choice = delete_choices[display][0]
        if choice == "1":
            delete = manage_teacher.delete_teacher(self.db)
            print("\n   "+delete["message"]+"\n")
        else:
            print("\nTeacher not deleted\n")
            self.teacher_home_view(teacher_id)

    def choose_other_subject(self, teacher_id):
        teacher_obj = TeacherManager(user_id=teacher_id)
        added_subject = teacher_obj.add_teachers_subjects(self.db)
        if added_subject['status'] == 500:
            print("\n   "+added_subject["message"]+"\n")
        else:
            print("\n   "+added_subject["message"]+"\n")
        self.teacher_home_view(teacher_id)

    # log out
    def log_out(self, teacher_id):
        db = self.db
        teacher_id = None
        print("\n   logged out\n")



