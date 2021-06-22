
class StudentQuery:

    def __init__(self, db) -> None:
        self.db = db

    # Creates students table if not exist
    def create_student_table(self):
        try:
            create_stud_table_query = '''
                CREATE TABLE IF NOT EXISTS students(
                    s_id SERIAL PRIMARY KEY NOT NULL,
                    s_first_name VARCHAR(255) NOT NULL,
                    s_last_name VARCHAR(255) NOT NULL,
                    s_password VARCHAR(255) NOT NULL,
                    s_address VARCHAR(255) NOT NULL,
                    s_phone BIGINT NOT NULL,
                    s_email VARCHAR(255)
                );
            '''
            self.db.execute(create_stud_table_query)
        except Exception as e:
            print(e)

    # Check if Email already exist in the student table
    def check_email_exists(self, s_email):
        query = "SELECT * FROM students WHERE s_email=%s"
        query_obj = self.db.execute(query, (s_email,))
        student = query_obj.fetchone()
        if student:
            return True
        else:
            return False

    # Check if phone already exist in the student table
    def check_phone_exists(self, s_phone):
        query = "SELECT * FROM students WHERE s_phone=%s"
        query_obj = self.db.execute(query, (s_phone,))
        student = query_obj.fetchone()
        if student:
            return True
        else:
            return False

    # Get user if the id exist
    def get_user_by_id(self, student_id):
        query = "SELECT * FROM students WHERE s_id=%s"
        student_obj = self.db.execute(query, (student_id,))
        student = student_obj.fetchone()
        if student:
            return student
        else:
            return None

    # Insert student query
    def insert_query(self, student):
        insert_student_query = '''
            INSERT INTO students(s_first_name, s_last_name, s_password, s_address, s_phone, s_email)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''' 
        return self.db.execute(insert_student_query, student.get_details_with_password())

    # Get User by email and password for login
    def login_query(self, student):
        login_student_query = "SELECT * FROM students WHERE s_email=%s AND s_password=%s"
        student_obj = self.db.execute(login_student_query, (student.email, student.password))
        student = student_obj.fetchone()
        if student:
            return student

    # Returns list of tuples of each student
    def get_all_student_query(self):
        query = "SELECT * FROM students;"
        select_students = self.db.execute(query)
        return select_students.fetchall()

    # Update name
    def update_name(self, student):
        query = '''
            UPDATE students
            SET s_first_name=%s, s_last_name=%s
            WHERE s_id=%s
        '''
        return self.db.execute(query, (student.first_name, student.last_name, student.id,))

    # Update address
    def update_address(self, student):
        query = '''
            UPDATE students
            SET s_address=%s
            WHERE s_id=%s
        '''
        return self.db.execute(query, (student.address, student.id))

    # Update phone
    def update_phone(self, student):
        query = '''
            UPDATE students
            SET s_phone=%s
            WHERE s_id=%s
        '''
        return self.db.execute(query, (student.get_student_phone(), student.get_student_id()))

    # Update email
    def update_email(self, student):
        query = '''
            UPDATE students
            SET s_email=%s
            WHERE s_id=%s
        '''
        return self.db.execute(query, (student.get_student_email(), student.get_student_id()))

    # Delete student
    def delete_query(self, student):
        query = '''
            DELETE FROM students
            WHERE s_id=%s
        '''
        return self.db.execute(query, (student.get_student_id(),))
