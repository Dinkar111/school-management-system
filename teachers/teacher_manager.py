from .teacher import Teacher
from helpers.validations import email_validation, phone_validation, password_validation
from subjects.subject import Subject
from simple_term_menu import TerminalMenu


class TeacherManager(Teacher):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subject_obj = Subject()

    # Register Teacher
    def register_teacher(self, db):
        if password_validation(self.password) and phone_validation(self.phone) and email_validation(self.email):
            check_email = self.check_email_exist(db)
            check_phone = self.check_phone_exist(db)
            if check_phone:
                return {
                    "status": 409,
                    "message": "Phone number already exist."
                }
            elif check_email:
                return {
                    "status": 409,
                    "message": "Email already Exist."
                }
            else:
                teacher = self.insert(db)
                self.user_id = teacher['teacher_id']
                self.add_teachers_subjects(db)
                return {
                    "status": 200,
                    "message": "Teacher has been added."
                }

    # Login Teacher
    def login_teacher(self, db):
        teacher = self.get_by_email_password(db)
        if not teacher:
            return {
                "status": 401,
                "message": "Email or password must have been incorrect. Please Try again"
            }
        else:
            self.user_id = teacher['teacher_id']
            return {
                "status": 200,
                "teacher_id": self.user_id,
                "message": "Logged in"
            }

    # Get profile
    def get_my_profile(self, db):
        profile = self.get_user_by_id(db)
        if not profile:
            return {
                "status": 404,
                "message": "No profile found"
            }
        else:
            return {
                "status": 200,
                "full_name": profile['full_name'],
                "address": profile['address'],
                "phone": profile['phone'],
                "email": profile['email'],
                "subject_name": profile['subject_name']
            }

    # Get all student profile
    def get_all_profile(self, db):
        all_profiles = self.get_all_profile_to_view(db)
        return all_profiles

    # Update name
    def update_teacher_name(self, db):
        first_name = input("Update First Name: ")
        last_name = input("Update Last Name: ")
        self.first_name = first_name
        self.last_name = last_name
        self.update_name(db)
        return {
            "status": 200,
            "message": "Name has been updated to {} {} ".format(self.first_name, self.last_name)
        }

    # Update password
    def update_teacher_password(self, db):
        password = input("Update Password: ")
        if not password_validation(password):
            return {
                "status": 400,
                "message": "Bad Request"
            }
        else:
            self.password = password
            self.update_password(db)
            return {
                "status": 200,
                "message": "Password has been updated"
            }

    # Update address
    def update_teacher_address(self, db):
        address = input("Update Address: ")
        self.address = address
        self.update_address(db)
        return {
            "status": 200,
            "message": "Address has been updated to {}".format(self.address)
        }

    # Update phone
    def update_teacher_phone(self, db):
        phone = input("Update Phone Number: ")
        if not phone_validation(phone):
            return {
                "status": 400,
                "message": "Bad Request"
            }
        else:
            self.phone = phone
            self.update_phone(db)
            return {
                "status": 200,
                "message": "Phone number has been updated to {}".format(self.phone)
            }

    # Update email
    def update_teacher_email(self, db):
        email = input("Update Email: ")
        if not email_validation(email):
            return {
                "status": 400,
                "message": "Bad Request"
            }
        else:
            self.email = email
            check_email = self.check_email_exist(db)
            if check_email:
                print("\n   Email already exist\n")
                self.update_email(db)
            else:
                self.update_teacher_email(db)
                return {
                    "status": 200,
                    "message": "Email has been updated to {}".format(self.email)
                }

    # Delete Teacher
    def delete_teacher(self, db):
        self.delete(db)
        return {
            "status": 200,
            "message": "Teacher deleted"
        }

    # Add subject to teachers
    def add_teachers_subjects(self, db):
        print("\n Select subject you teach: ")
        subjects = self.subject_obj.view_all_subject(db)
        subject_name = [subject['subject_name'] for subject in subjects]
        terminal = TerminalMenu(subject_name)
        show = terminal.show()
        self.subject_obj.subject_name = subject_name[show]
        check = self.subject_obj.check_subject_exist(db)
        subject_id = check['subject_id']
        added_subject = self.add_teacher_and_subject(db, subject_id)
        if not added_subject:
            return {
                "status": 500,
                "message": "Something is wrong"
            }
        else:
            return {
                "status": 200,
                "message": "Subject has been added to your profile"
            }

