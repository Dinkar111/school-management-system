from .student import Student
from helpers.session import Session


class ManageStudent(Student):
    def __init__(self, s_id=None, first_name=None, last_name=None, password=None, address=None, phone=None, email=None):
        super().__init__(
            s_id=s_id,
            first_name=first_name,
            last_name=last_name,
            password=password,
            address=address,
            phone=phone,
            email=email
        )
        self.session = Session()

    # Register Student
    def register_student(self, db):
        # If table not exist create table
        db.create_student_table()
        check_email = self.check_email_exist(db)
        check_phone = self.check_phone_exist(db)
        if check_email:
            print("\n   Email already exist.")
        elif check_phone:
            print("\n   Phone already exist.")
        else:
            return self.insert_student(db)

    # Login Student
    def login_student(self, db):
        student = self.get_student_by_email_password(db)
        if not student:
            print("\n   email or password must have been incorrect. Please Try again\n")
        else:
            self.s_id = student[0]
            return self.s_id

    # Get profile
    def get_my_profile(self, db):
        profile = self.get_user_by_id(db)
        self.first_name = profile[1]
        self.last_name = profile[2]
        self.address = profile[4]
        self.phone = profile[5]
        self.email = profile[6]
        if not profile:
            print("No profile found")
        else:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "address": self.address,
                "phone": self.phone,
                "email": self.email
            }

    # Get all student profile
    def get_all_profile(self, db):
        all_profiles = self.get_all_profile_to_view_only(db)
        return all_profiles

    # Update name
    def update_name(self, db):
        first_name = input("Update First Name: ")
        last_name = input("Update Last Name: ")
        self.first_name = first_name
        self.last_name = first_name
        updated = self.update_student_name(db)
        print("\n   Name has been updated to {} {}\n ".format(self.first_name, self.last_name))
        return updated

    # Update password
    def update_password(self, db):
        password = input("Update Password: ")
        self.password = password
        updated = self.update_student_password(db)
        print("\n   Password has been updated\n")
        return updated

    # Update address
    def update_address(self, db):
        address = input("Update Address: ")
        self.address = address
        updated = self.update_student_address(db)
        print("\n   Address has been updated to {}\n".format(self.address))
        return updated

    # Update phone
    def update_phone(self, db):
        phone = input("Update Phone Number: ")
        self.phone = phone
        updated = self.update_student_phone(db)
        print("\n   Phone number has been updated to {}\n".format(self.phone))
        return updated

    # Update email
    def update_email(self, db):
        email = input("Update Email: ")
        self.email = email
        check_email = self.check_email_exist(db)
        if check_email:
            print("\n   Email already exist\n")
            self.update_email(db)
        else:
            updated = self.update_student_email(db)
            print("\n   Email has been updated to {}\n".format(self.email))
            return updated

    # Delete Student
    def delete_student(self, db):
        return self.delete(db)

