class SubjectQueries:
    def __init__(self, db):
        self.db = db

    def insert(self, subject):
        subject_code = subject.get_subject_code
        subject_name = subject.get_subject_name
        grade = subject.get_grade
        query = """
            INSERT INTO subjects(subject_code, subject_name, grade_id)
            VALUES (%s, %s, %s)
            RETURNING id
        """
        self.db.execute(
            query,
            (subject_code, subject_name, grade),
        )
        return self.db.fetchone()

    def get_all(self):
        query = """
            SELECT * FROM subjects ORDER BY id
        """
        self.db.execute(query)
        return self.db.fetchall()

    def get_all_by_grade(self, grade):
        query = """
            SELECT * FROM subjects s
            INNER JOIN grades g ON s.grade_id = g.id
            WHERE g.grade=%s
        """
        self.db.execute(query, (grade,))
        return self.db.fetchall()

    def get_subject_by_subject_code(self, subject_code):
        query = """
            SELECT * FROM subjects s
            INNER JOIN grades g ON s.grade_id = g.id
            WHERE subject_code=%s
        """
        self.db.execute(query, (subject_code,))
        return self.db.fetchone()
