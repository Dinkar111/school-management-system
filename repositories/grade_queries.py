class GradeQueries:
    def __init__(self, db):
        self.db = db

    def insert(self, grade):
        grade_name = grade.get_grade
        no_of_students = grade.get_no_of_students

        query = """
            INSERT INTO grades(grade, no_of_students)
            VALUES (%s, %s)
            RETURNING id
        """
        self.db.execute(
            query,
            (
                grade_name,
                no_of_students,
            ),
        )
        return self.db.fetchone()

    def get_all(self):
        query = """
            SELECT * FROM grades ORDER BY id
        """
        self.db.execute(query)
        return self.db.fetchall()

    def get_grade(self, grade_name):
        query = """
            SELECT * FROM grades WHERE grade=%s
        """
        self.db.execute(query, (grade_name,))
        return self.db.fetchone()

    def update_no_of_students(self, grade, no_of_students):
        query = """
            UPDATE grades
            SET no_of_students = %s
            WHERE grade=%s
        """
        return self.db.execute(
            query,
            (
                no_of_students,
                grade,
            ),
        )
