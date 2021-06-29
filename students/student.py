from abstract.person import Person


class Student(Person):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.role = 1

    # Insert student query
    def insert(self, db):
        insert_student_query = '''
        INSERT INTO students(first_name, last_name, password, address, phone, email, role_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        db.execute(insert_student_query, (self.first_name, self.last_name, self.password,
                                          self.address, self.phone, self.email, self.role))
        db.execute("SELECT student_id FROM students WHERE email=%s", (self.email,))
        return db.fetchone()

    # get Student by email and password to login the student
    def get_by_email_password(self, db):
        login_query = "SELECT student_id FROM students WHERE email=%s AND password=%s"
        db.execute(login_query, (self.email, self.password,))
        return db.fetchone()

    # get Student by id after login and use id as a token
    def get_user_by_id(self, db):
        query = '''
        select s.student_id, CONCAT(s.first_name,' ',s.last_name) AS student_name, s.address, s.phone, s.email,
        sub.subject_name, CONCAT(t.first_name,' ',t.last_name) AS teacher_name FROM students_subjects SS
        INNER JOIN students s
            ON  SS.student_id = S.student_id
        INNER JOIN subjects Sub
            ON SS.subject_id = Sub.subject_id
        LEFT JOIN teachers_subjects TS
            ON TS.subject_id = Sub.subject_id
        LEFT JOIN teachers t  
            ON TS.teacher_id = T.teacher_id
        where s.student_id = %s
        '''
        db.execute(query, (self.user_id,))
        return db.fetchone()

    # get all student profile
    def get_all_profile_to_view(self, db):
        query = '''
        SELECT student_id, first_name, last_name, address, email, phone FROM students
        INNER JOIN roles
        ON students.role_id = roles.role_id
        '''
        db.execute(query)
        return db.fetchall()

    # Update student name
    def update_name(self, db):
        query = """
        UPDATE students
        SET first_name=%s,last_name=%s
        WHERE student_id=%s
        """
        db.execute(query, (self.first_name, self.last_name, self.user_id,))

    # Update student password
    def update_password(self, db):
        query = '''
        UPDATE students
        SET password=%s
        WHERE student_id=%s
        '''
        db.execute(query, (self.password, self.user_id,))

    # Update student address
    def update_address(self, db):
        query = '''
        UPDATE students
        SET address=%s
        WHERE student_id=%s
        '''
        db.execute(query, (self.address, self.user_id,))

    # Update student phone
    def update_phone(self, db):
        query = '''
        UPDATE students
        SET phone=%s
        WHERE student_id=%s
        '''
        db.execute(query, (self.phone, self.user_id,))

    # Update student email
    def update_email(self, db):
        query = '''
        UPDATE students
        SET email=%s
        WHERE student_id=%s
        '''
        db.execute(query, (self.email, self.user_id,))

    # Delete this student
    def delete(self, db):
        query = "DELETE FROM students WHERE student_id=%s"
        db.execute(query, (self.user_id,))

    def add_student_and_subject(self, db, subject_id):
        student_and_subject = '''
            INSERT INTO students_subjects(subject_id, student_id) VALUES (%s, %s)
        '''
        db.execute(student_and_subject, (subject_id, self.user_id, ))
        return True
