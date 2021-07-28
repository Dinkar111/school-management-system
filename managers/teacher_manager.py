from repositories.teacher_queries import TeacherQueries
from repositories.student_queries import StudentQueries
from .user_manager import UserManager
from models.teacher import Teacher
from models.student import Student
from helpers.validations import (
    email_validation,
    password_validation,
    phone_validation,
)
from helpers.password_hash import make_pw_hash


class TeacherManager(UserManager):
    def __init__(self, db):
        super().__init__(db)
        self.teacher_queries = TeacherQueries(db)
        self.student_queries = StudentQueries(db)

    def show_all_teachers(self, grade_name):
        teachers = self.teacher_queries.get_all()
        if not teachers:
            return {"status": 404, "message": "There are no Teacher"}
        else:
            teacher_objects = [
                Teacher(
                    first_name=teacher["first_name"],
                    last_name=teacher["last_name"],
                    password=teacher["password"],
                    address=teacher["address"],
                    email=teacher["email"],
                    phone=teacher["phone"],
                    is_admin=teacher["is_admin"],
                    is_teacher=teacher["is_teacher"],
                    is_student=teacher["is_student"],
                    subjects=teacher["subject_names"],
                    grades=teacher["grade"],
                )
                for teacher in teachers
                if teacher["grade"] == grade_name
            ]
            if len(teacher_objects) < 1:
                return {"status": 404, "message": "There are no teachers"}
            else:
                return {"status": 200, "teachers": teacher_objects}

    # Register Student
    def register_teacher(
        self,
        first_name=None,
        last_name=None,
        password=None,
        address=None,
        phone=None,
        email=None,
        grade=None,
    ):
        if (
            password_validation(password)
            and phone_validation(phone)
            and email_validation(email)
        ):
            user = self.user_queries.get_user_by_email(email)
            if user:
                return {"status": 409, "message": "Email already Exist."}
            else:
                hashed_password = make_pw_hash(password)
                user = self.user_queries.insert(
                    first_name=first_name,
                    last_name=last_name,
                    password=hashed_password,
                    address=address,
                    email=email,
                    phone=phone,
                    is_student=False,
                    is_teacher=True,
                )
                if user["id"]:
                    user_id = user["id"]
                    teacher = self.teacher_queries.insert(user_id=user_id)
                    if teacher["id"]:
                        teacher_id = teacher["id"]
                        grade_id = grade.get_id
                        self.teacher_queries.insert_teacher_and_grade(
                            teacher_id, grade_id
                        )
                        return {
                            "status": 200,
                            "message": "Teacher has been admitted.",
                        }
                    else:
                        return {
                            "status": 500,
                            "message": "Teacher not added, something wrong.",
                        }
                else:
                    return {"status": 500, "message": "Something is wrong."}
        else:
            return {"status": 400, "message": "Bad Request"}

    def teacher_profile(self, user):
        user_id = user.get_id
        teacher = self.teacher_queries.get_teacher_by_user_id(user_id)
        if not teacher:
            return {"status": 404, "message": "No Teacher found"}
        else:
            teacher_object = Teacher(
                user_id=teacher["user_id"],
                first_name=teacher["first_name"],
                last_name=teacher["last_name"],
                address=teacher["address"],
                phone=teacher["phone"],
                email=teacher["email"],
                teacher_id=teacher["id"],
                subjects=teacher["subject_names"],
                grades=teacher["grade"],
            )
            return {"status": 200, "teacher": teacher_object}

    def show_teacher_students(self, user):
        user_id = user.get_id
        teacher = self.teacher_queries.get_teacher_by_user_id(user_id)
        if not teacher:
            return {"status": 404, "message": "No Teacher found"}
        else:
            grade_name = teacher["grade"]
            students = self.student_queries.get_all()
            if not students:
                return {"status": 404, "message": "No Teachers"}
            else:
                student_objects = [
                    Student(
                        user_id=student["user_id"],
                        first_name=student["first_name"],
                        last_name=student["last_name"],
                        address=student["address"],
                        phone=student["phone"],
                        email=student["email"],
                        roll_no=student["roll_no"],
                        grade=student["grade"],
                    )
                    for student in students
                    if student["grade"] == grade_name
                ]
                return {"status": 200, "students": student_objects}

    def choose_subject(self, teacher, subject):
        teacher_id = teacher.get_teacher_id
        subject_id = subject.get_subject_id
        self.teacher_queries.insert_teacher_and_subject(teacher_id, subject_id)
        return {
            "status": 200,
            "message": "You have chosen {}.".format(subject.get_subject_name),
        }
