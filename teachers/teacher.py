from abstract.person import Person


class Teacher(Person):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.role = 2

    # Insert Teacher query
    def insert(self, db):
        insert_teacher_query = '''
        INSERT INTO teachers(first_name, last_name, password, address, phone, email, role_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        db.execute(insert_teacher_query, (self.first_name, self.last_name, self.password,
                                          self.address, self.phone, self.email, self.role))
        db.execute("SELECT teacher_id FROM teachers WHERE email=%s", (self.email, ))
        return db.fetchone()

    # get Teacher by email and password for login the student
    def get_by_email_password(self, db):
        login_query = "SELECT teacher_id FROM teachers WHERE email=%s AND password=%s"
        db.execute(login_query, (self.email, self.password,))
        return db.fetchone()

    # get Teacher by id after login and use id as a token
    def get_user_by_id(self, db):
        query = '''
        SELECT T.teacher_id, CONCAT(T.first_name, ' ', T.last_name) AS full_name, T.address, T.phone, 
        T.email, STRING_AGG(S.subject_name,', ') AS subject_name from teachers T
        INNER JOIN teachers_subjects TS
        on TS.teacher_id = T.teacher_id
        INNER JOIN subjects S 
        ON TS.subject_id = S.subject_id
        WHERE T.teacher_id = %s
        GROUP BY 1, 2, 3, 4, 5;  
        '''
        db.execute(query, (self.user_id,))
        return db.fetchone()

    # get all student profile
    def get_all_profile_to_view(self, db):
        query = '''
        SELECT T.teacher_id, CONCAT(T.first_name, ' ', T.last_name) AS full_name, T.address, T.phone, 
        T.email, STRING_AGG(S.subject_name,', ') AS subject_name from teachers T
        INNER JOIN teachers_subjects TS
        on TS.teacher_id = T.teacher_id
        INNER JOIN subjects S 
        ON TS.subject_id = S.subject_id
        GROUP BY 1, 2, 3, 4, 5;   
        '''
        db.execute(query)
        return db.fetchall()

    # Update teacher name
    def update_name(self, db):
        query = """
        UPDATE teachers
        SET first_name=%s,last_name=%s
        WHERE teacher_id=%s
        """
        db.execute(query, (self.first_name, self.last_name, self.user_id,))

    # Update teacher password
    def update_password(self, db):
        query = '''
        UPDATE teachers
        SET password=%s
        WHERE teacher_id=%s
        '''
        db.execute(query, (self.password, self.user_id,))

    # Update teacher address
    def update_address(self, db):
        query = '''
        UPDATE teachers
        SET address=%s
        WHERE teacher_id=%s
        '''
        db.execute(query, (self.address, self.user_id,))

    # Update teacher phone
    def update_phone(self, db):
        query = '''
        UPDATE teachers
        SET phone=%s
        WHERE teacher_id=%s
        '''
        db.execute(query, (self.phone, self.user_id,))

    # Update teacher email
    def update_email(self, db):
        query = '''
        UPDATE teachers
        SET email=%s
        WHERE teacher_id=%s
        '''
        db.execute(query, (self.email, self.user_id,))

    # Delete this student
    def delete(self, db):
        query = "DELETE FROM teachers WHERE teacher_id=%s"
        db.execute(query, (self.user_id,))

    # Add subject to teachers
    def add_teacher_and_subject(self, db, subject_id):
        teacher_and_subject = '''
            INSERT INTO teachers_subjects(subject_id, teacher_id) VALUES (%s, %s)
        '''
        db.execute(teacher_and_subject, (subject_id, self.user_id, ))
        return True
