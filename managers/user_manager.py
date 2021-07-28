from repositories.user_queries import UserQueries
from models.user import User
from helpers.password_hash import check_pw_hash


class UserManager:
    def __init__(self, db):
        self.user_queries = UserQueries(db)

    # Login Student
    def login_user(self, email, password):
        user = self.user_queries.get_user_by_email(email)
        if user and check_pw_hash(password, user["password"]):
            user_obj = User(
                user_id=user["id"],
                first_name=user["first_name"],
                last_name=user["last_name"],
                address=user["address"],
                phone=user["phone"],
                email=user["email"],
                is_admin=user["is_admin"],
                is_teacher=user["is_teacher"],
                is_student=user["is_student"],
                password=user["password"],
            )
            return {"status": 200, "user": user_obj, "message": "Logged in"}
        else:
            return {
                "status": 401,
                "message": "Email or password must have been incorrect. Please Try again",
            }

    def show_all_users(self):
        users = self.user_queries.get_all()
        if not users:
            return {"status": 404, "message": "There are no grades"}
        else:
            user_objects = [
                User(
                    user_id=user["id"],
                    first_name=user["first_name"],
                    last_name=user["last_name"],
                    password=user["password"],
                    address=user["address"],
                    email=user["email"],
                    phone=user["phone"],
                    is_admin=user["is_admin"],
                    is_teacher=user["is_teacher"],
                    is_student=user["is_student"],
                )
                for user in users
            ]
            return {"status": 200, "users": user_objects}
