from psycopg2 import InternalError


class Student:

    def __init__(self, s_id=None, first_name=None, last_name=None, password=None, address=None, phone=None, email=None):
        self.s_id = s_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.address = address
        self.phone = phone
        self.email = email

    # Insert student query
    def insert_student(self, db):
        insert_student_query = '''
        INSERT INTO students(s_first_name, s_last_name, s_password, s_address, s_phone, s_email)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
        return db.execute(insert_student_query, (self.first_name, self.last_name, self.password, self.address, self.phone, self.email ))

    # Check if Email already exist in the student table
    def check_email_exist(self, db):
        try:
            query = "SELECT * FROM students WHERE s_email=%s"
            query_obj = db.execute(query, (self.email,))
            return query_obj.fetchone()
        except InternalError as error:
            print(error)

    # Check if phone already exist in the student table
    def check_phone_exist(self, db):
        try:
            query = "SELECT * FROM students WHERE s_phone=%s"
            query_obj = db.execute(query, (self.phone,))
            return query_obj.fetchone()
        except InternalError as error:
            print(error)

    # get Student by email and password for login the student
    def get_student_by_email_password(self, db):
        try:
            login_query = "SELECT * FROM students WHERE s_email=%s AND s_password=%s"
            query_obj = db.execute(login_query, (self.email, self.password,))
            return query_obj.fetchone()
        except InternalError as error:
            print(error)

    # get Student by id after login and use id as a token
    def get_user_by_id(self, db):
        try:
            query = "SELECT * FROM students WHERE s_id=%s"
            student_obj = db.execute(query, (self.s_id,))
            return student_obj.fetchone()
        except InternalError as error:
            print(error)

    # get all student profile without student id and password
    def get_all_profile_to_view_only(self, db):
        try:
            s_id = self.s_id
            query = '''
            SELECT CONCAT(s_first_name, ' ', s_last_name) as full_name, s_address, s_phone, s_email FROM students;
            '''
            students_obj = db.execute(query)
            return students_obj.fetchall()
        except InternalError as error:
            print(error)

    # Update student name
    def update_student_name(self, db):
        try:
            query = """
            UPDATE students
            SET s_first_name=%s,s_last_name=%s
            WHERE s_id=%s
            """
            return db.execute(query, (self.first_name, self.last_name, self.s_id,))
        except InternalError as error:
            print(error)

    # Update student password
    def update_student_password(self, db):
        try:
            query = '''
            UPDATE students
            SET s_password=%s
            WHERE s_id=%s
            '''
            return db.execute(query, (self.password, self.s_id,))
        except InternalError as error:
            print(error)

    # Update student address
    def update_student_address(self, db):
        try:
            query = '''
            UPDATE students
            SET s_address=%s
            WHERE s_id=%s
            '''
            return db.execute(query, (self.address, self.s_id,))
        except InternalError as error:
            print(error)

    # Update student phone
    def update_student_phone(self, db):
        try:
            query = '''
            UPDATE students
            SET s_phone=%s
            WHERE s_id=%s
            '''
            return db.execute(query, (self.phone, self.s_id,))
        except InternalError as error:
            print(error)

    # Update student email
    def update_student_email(self, db):
        try:
            query = '''
            UPDATE students
            SET s_email=%s
            WHERE s_id=%s
            '''
            return db.execute(query, (self.email, self.s_id,))
        except InternalError as error:
            print(error)

    # Delete this student
    def delete(self, db):
        try:
            query = "DELETE FROM students WHERE s_id=%s"
            return db.execute(query, (self.s_id,))
        except InternalError as error:
            print(error)