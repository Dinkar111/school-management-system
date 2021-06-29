from .admin import Admin
from subjects.subject import Subject


class AdminManager(Admin):
    def __init__(self, admin_id=None, admin_username=None, admin_email=None, admin_password=None):
        super().__init__(
            admin_id=admin_id,
            admin_username=admin_username,
            admin_email=admin_email,
            admin_password=admin_password,
        )
        self.subject_obj = Subject()

    def admin_login(self, db):
        admin = self.get_admin_by_username_password(db)
        if not admin:
            return {
                "status": 401,
                "message": "\n  Admin credentials are not correct. No admin user found."
            }
        else:
            return {
                "status": 200,
                "admin_id": admin['admin_id'],
                "admin_fullname": admin['admin_username'],
                "message": "logged in as admin"
            }

    def admin_profile(self, db):
        admin_profile = self.get_admin_by_id(db)
        if not admin_profile:
            return {
                "status": 404,
                "message": "No profile found"
            }
        else:
            return {
                "status": 200,
                "admin_username": admin_profile['admin_username'],
                "admin_email": admin_profile['admin_email']
            }

    def add_subject(self, db):
        subject_name = input("\n Subject Name: ")
        self.subject_obj.subject_name = subject_name
        check = self.subject_obj.check_subject_exist(db)
        if check:
            return {
                "status": 409,
                "message": "Subject already exists"
            }
        else:
            self.subject_obj.add(db)
            return {
                "status": 200,
                "message": "{} has been added to subject.".format(subject_name)
            }

    def view_subject(self, db):
        return self.subject_obj.view_all_subject(db)
