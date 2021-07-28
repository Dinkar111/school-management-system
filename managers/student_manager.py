from repositories.student_queries import StudentQueries
from .user_manager import UserManager
from models.student import Student
from models.subject import Subject
from models.teacher import Teacher
from helpers.validations import (
    email_validation,
    password_validation,
    phone_validation,
)
from helpers.password_hash import make_pw_hash


class StudentManager(UserManager):
    def __init__(self, db):
        super().__init__(db)
        self.student_queries = StudentQueries(db)

    def show_all_students(self, grade_name):
        students = self.student_queries.get_all()
        if not students:
            return {"status": 404, "message": "There are no students"}
        else:
            student_objects = [
                Student(
                    first_name=student["first_name"],
                    last_name=student["last_name"],
                    password=student["password"],
                    address=student["address"],
                    email=student["email"],
                    phone=student["phone"],
                    roll_no=student["roll_no"],
                    grade=student["grade"],
                )
                for student in students
                if student["grade"] == grade_name
            ]
            if len(student_objects) < 1:
                return {
                    "status": 404,
                    "message": "There are no students in this class",
                }
            else:
                return {"status": 200, "students": student_objects}

    # Register Student
    def register_student(
        self,
        first_name=None,
        last_name=None,
        password=None,
        address=None,
        phone=None,
        email=None,
        grade=None,
        roll_no=None,
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
                    is_student=True,
                    is_teacher=False,
                )
                if user["id"]:
                    user_id = user["id"]
                    grade_id = grade.get_id
                    self.student_queries.insert(
                        user_id=user_id, roll_no=roll_no, grade_id=grade_id
                    )
                    return {
                        "status": 200,
                        "message": "Student has been admitted.",
                    }
                else:
                    return {"status": 500, "message": "Something is wrong."}
        else:
            return {"status": 400, "message": "Bad Request"}

    def student_profile(self, user):
        user_id = user.get_id
        student = self.student_queries.get_student_by_user_id(user_id)
        if not student:
            return {"status": 404, "message": "No Student found"}
        else:
            student_object = Student(
                user_id=student["user_id"],
                first_name=student["first_name"],
                last_name=student["last_name"],
                address=student["address"],
                phone=student["phone"],
                email=student["email"],
                roll_no=student["roll_no"],
                grade=student["grade"],
            )

            return {"status": 200, "student": student_object}

    def show_student_subjects(self, user):
        user_id = user.get_id
        subjects = self.student_queries.get_subjects_by_user_id(user_id)
        if not subjects:
            return {
                "status": 404,
                "message": "No Subject has been assigned to you class yet",
            }
        else:
            subject_objects = [
                Subject(
                    subject_name=subject["subject_name"],
                    subject_code=subject["subject_code"],
                )
                for subject in subjects
            ]
            return {"status": 200, "subjects": subject_objects}

    def show_student_teachers(self, user):
        user_id = user.get_id
        student = self.student_queries.get_student_by_user_id(user_id)
        if not student:
            return {"status": 404, "message": "Student not found"}
        else:
            grade_name = student["grade"]
            teachers = self.student_queries.get_teachers_related_to_students(
                grade_name
            )
            if not teachers:
                return {
                    "status": 404,
                    "message": "No Teachers are assigned to your class",
                }
            else:
                teacher_objects = [
                    Teacher(
                        user_id=teacher["user_id"],
                        first_name=teacher["first_name"],
                        last_name=teacher["last_name"],
                        address=teacher["address"],
                        phone=teacher["phone"],
                        email=teacher["email"],
                        subjects=teacher["subject_name"],
                        grades=teacher["grade"],
                    )
                    for teacher in teachers
                ]
                return {"status": 200, "teachers": teacher_objects}
