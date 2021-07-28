from models.grade import Grade
from repositories.grade_queries import GradeQueries


class GradeManager:
    def __init__(self, db):
        self.grade_queries = GradeQueries(db)

    def add_grades(self, grade_name):
        grade_obj = Grade(grade=grade_name, no_of_students=0)
        grade_exists = self.grade_queries.get_grade(grade_name)
        if grade_exists:
            return {
                "status": 400,
                "message": "{} already exists".format(grade_obj.get_grade),
            }
        else:
            grade = self.grade_queries.insert(grade_obj)
            if grade["id"]:
                return {
                    "status": 200,
                    "message": "{} has been added".format(grade_obj.get_grade),
                }
            else:
                return {
                    "status": 500,
                    "message": "Something went wrong while adding grade",
                }

    def show_all_grades(self):
        grades = self.grade_queries.get_all()
        if not grades:
            return {"status": 404, "message": "There are no grades"}
        else:
            grade_objects = [
                Grade(
                    grade_id=grade["id"],
                    grade=grade["grade"],
                    no_of_students=grade["no_of_students"],
                )
                for grade in grades
            ]
            return {"status": 200, "grades": grade_objects}

    def get_grade_by_name(self, grade_name):
        grade = self.grade_queries.get_grade(grade_name)
        if not grade:
            return {"status": 404, "message": "grade not found"}
        else:
            grade_obj = Grade(
                grade_id=grade["id"],
                grade=grade["grade"],
                no_of_students=grade["no_of_students"],
            )
            return grade_obj

    def add_no_of_students(self, grade):
        grade_name = grade.get_grade
        no_of_students = grade.get_no_of_students + 1
        update = self.grade_queries.update_no_of_students(
            grade=grade_name, no_of_students=no_of_students
        )
        if not update:
            return {"status": 500, "message": "Something is wrong"}
        else:
            return {"status": 200, "message": "No of students changed"}
