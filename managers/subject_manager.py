from repositories.subject_queries import SubjectQueries
from models.subject import Subject


class SubjectManager:
    def __init__(self, db):
        self.subject_queries = SubjectQueries(db)

    # add subjects
    def add_subject(self, subject_code=None, subject_name=None, grade_id=None):
        subject_object = Subject(
            subject_code=subject_code,
            subject_name=subject_name,
            grade_id=grade_id,
        )
        subject_exist = self.subject_queries.get_subject_by_subject_code(
            subject_code
        )
        if subject_exist:
            return {
                "status": 409,
                "message": "Subject code - {} already exists".format(
                    subject_code
                ),
            }
        else:
            subject = self.subject_queries.insert(subject_object)
            if not subject:
                return {
                    "status": 500,
                    "message": "Subject not added, something wrong.",
                }
            else:
                return {
                    "status": 200,
                    "message": "{} Subject has been admitted.".format(
                        subject_name
                    ),
                }

    def get_all_subjects_by_grade(self, grade):
        grade = grade.get_grade
        subjects = self.subject_queries.get_all_by_grade(grade)
        if not subjects:
            return {"status": 404, "message": " NO subject Found "}
        else:
            subject_objects = [
                Subject(
                    subject_id=subject["id"],
                    subject_code=subject["subject_code"],
                    subject_name=subject["subject_name"],
                    grade_id=subject["grade"],
                )
                for subject in subjects
            ]
            return {"status": 200, "subjects": subject_objects}

    def get_subject_by_code(self, subject_code):
        subject = self.subject_queries.get_subject_by_subject_code(
            subject_code
        )
        if not subject:
            return {"status": 404, "message": " NO subject Found "}
        else:
            subject_object = Subject(
                subject_id=subject["id"],
                subject_code=subject["subject_code"],
                subject_name=subject["subject_name"],
                grade_id=subject["grade"],
            )
            return {"status": 200, "subject": subject_object}
