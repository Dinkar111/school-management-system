class StudentQueries:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        query = """
            SELECT *
            FROM users u
            INNER JOIN students s ON u.id = s.user_id
            INNER JOIN grades g ON s.grade_id = g.id
            WHERE is_student = true ;
        """
        self.db.execute(query)
        return self.db.fetchall()

    def insert(self, user_id, roll_no, grade_id):
        query = """
            INSERT INTO students(user_id, roll_no, grade_id)
            VALUES (%s, %s, %s)
        """
        self.db.execute(query, (user_id, roll_no, grade_id))

    def get_student_by_user_id(self, user_id):
        query = """
            SELECT *
            FROM users u
            INNER JOIN students s ON u.id = s.user_id
            INNER JOIN grades g ON s.grade_id = g.id
            WHERE s.user_id=%s
        """
        self.db.execute(query, (user_id,))
        return self.db.fetchone()

    def get_subjects_by_user_id(self, user_id):
        query = """
            SELECT subject_code, subject_name FROM students s
            INNER JOIN grades g ON s.grade_id = g.id
            INNER JOIN subjects s2 ON g.id = s2.grade_id
            WHERE s.user_id=%s
        """
        self.db.execute(query, (user_id,))
        return self.db.fetchall()

    def get_teachers_related_to_students(self, grade_name):
        query = """
            SELECT first_name, last_name, email, address, phone, grade, user_id,
            string_agg(subject_name, ',') AS subject_name
            FROM users u
            INNER JOIN teachers t ON u.id = t.user_id
            INNER JOIN teachers_grades tg ON t.id = tg.teacher_id
            INNER JOIN grades g ON tg.grade_id = g.id
            LEFT JOIN teachers_subjects ts ON t.id = ts.teacher_id
            LEFT JOIN subjects s ON ts.subject_id = s.id
            WHERE is_teacher = true AND grade=%s
            group by 1, 2, 3, 4, 5, 6, 7;
        """
        self.db.execute(query, (grade_name,))
        return self.db.fetchall()
