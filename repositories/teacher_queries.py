class TeacherQueries:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        query = """
            SELECT  u.id, t.id, u.first_name, u.last_name, u.email, u.password, u.address, u.phone,
            u.is_admin, u.is_teacher, u.is_student, g.grade, string_agg(subject_name, ',') AS subject_names
            FROM teachers t
            INNER JOIN users u ON t.user_id = u.id
            INNER JOIN teachers_grades tg ON t.id = tg.teacher_id
            INNER JOIN grades g ON tg.grade_id = g.id
            LEFT JOIN teachers_subjects ts ON t.id = ts.teacher_id
            LEFT JOIN subjects s ON  ts.subject_id = s.id
            WHERE is_teacher = true
            group by t.id, u.id, g.grade
        """
        self.db.execute(query)
        return self.db.fetchall()

    def insert(self, user_id):
        query = """
            INSERT INTO teachers(user_id) VALUES (%s)
            RETURNING id
        """
        self.db.execute(query, (user_id,))
        return self.db.fetchone()

    # Insert teacher and grade relation
    def insert_teacher_and_grade(self, teacher_id, grade_id):
        insert_teacher_grade_query = """
            INSERT INTO teachers_grades(teacher_id, grade_id) VALUES (%s, %s)
        """
        self.db.execute(
            insert_teacher_grade_query,
            (
                teacher_id,
                grade_id,
            ),
        )

    # Insert teacher and subject relation
    def insert_teacher_and_subject(self, teacher_id, subject_id):
        query = """
             INSERT INTO teachers_subjects(teacher_id, subject_id) VALUES (%s, %s)
         """
        self.db.execute(
            query,
            (
                teacher_id,
                subject_id,
            ),
        )

    def get_teacher_by_user_id(self, user_id):
        query = """
            SELECT first_name, last_name, email, user_id , t.id,
            address, phone, grade, string_agg(subject_name, ',') AS subject_names
            FROM teachers t
            INNER JOIN users u ON t.user_id = u.id
            INNER JOIN teachers_grades tg ON t.id = tg.teacher_id
            INNER JOIN grades g ON tg.grade_id = g.id
            LEFT JOIN teachers_subjects ts ON t.id = ts.teacher_id
            LEFT JOIN subjects s ON  ts.subject_id = s.id
            WHERE t.user_id=%s
            group by 1, 2, 3, 4, 5, 6, 7, 8;
        """
        self.db.execute(query, (user_id,))
        return self.db.fetchone()
