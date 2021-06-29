import psycopg2
from psycopg2.extras import DictCursor
from psycopg2 import OperationalError, ProgrammingError, DataError, InternalError


class DbClass:

    def __init__(self, db_name=None, user_name=None, password=None, host_name=None):
        self.host_name = host_name
        self.user_name = user_name
        self.password = password
        self.db_name = db_name
        self.cursor = None
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host_name,
                user=self.user_name,
                password=self.password,
                database=self.db_name
            )
            self.cursor = self.connection.cursor(cursor_factory=DictCursor)
        except OperationalError as error:
            print(error)

    def execute(self, db_query, data=None):
        try:
            self.cursor.execute(db_query, data)
            self.connection.commit()
            return self.cursor
        except DataError:
            print("\n Something Wrong with Data")
            self.connection.rollback()
        except ProgrammingError:
            print("\n Something wrong with syntax")
            self.connection.rollback()
        except InternalError as error:
            self.connection.rollback()
            print(error)

    def fetchone(self):
        try:
            return self.cursor.fetchone()
        except (DataError, ProgrammingError) as error:
            print(error)

    def fetchall(self):
        try:
            return self.cursor.fetchall()
        except (DataError, ProgrammingError) as error:
            print(error)

    def create_all_tables(self):
        self.create_student_table()
        self.create_teacher_table()
        self.create_admin_table()
        self.create_subject_table()
        self.create_teacher_and_subject_table()
        self.create_student_and_subject_table()

    # Creates students table if not exist
    def create_student_table(self):
        create_student_table_query = '''
            CREATE TABLE IF NOT EXISTS students(
                student_id SERIAL PRIMARY KEY NOT NULL,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                email VARCHAR(255),
                password VARCHAR(255) NOT NULL,
                address VARCHAR(255) NOT NULL,
                phone VARCHAR(255) NOT NULL,
                role_id int NOT NULL references roles(role_id)
            );
        '''
        self.execute(create_student_table_query)

    # Creates teachers table if not exist
    def create_teacher_table(self):
        create_teacher_table_query = '''
            CREATE TABLE IF NOT EXISTS teachers(
                teacher_id SERIAL PRIMARY KEY NOT NULL,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                email VARCHAR(255),
                password VARCHAR(255) NOT NULL,
                address VARCHAR(255) NOT NULL,
                phone VARCHAR(255) NOT NULL,
                role_id int NOT NULL references roles(role_id)
            )
        '''
        self.execute(create_teacher_table_query)

    # Creates admin table if not exist
    def create_admin_table(self):
        create_admin_table_query = '''
            CREATE TABLE IF NOT EXISTS admins(
                admin_id SERIAL PRIMARY KEY NOT NULL,
                admin_name VARCHAR(255) NOT NULL,
                admin_email VARCHAR(255) NOT NULL,
                admin_password VARCHAR(255) NOT NULL
            )
        '''
        self.execute(create_admin_table_query)

    def create_subject_table(self):
        create_subject_table_query = '''
            CREATE TABLE IF NOT EXISTS subjects(
                subject_id SERIAL PRIMARY KEY NOT NULL,
                subject_name VARCHAR(255) NOT NULL
            )
        '''
        self.execute(create_subject_table_query)

    def create_teacher_and_subject_table(self):
        teacher_and_subject_table = '''
            CREATE TABLE IF NOT EXISTS teachers_subjects(
                teacher_id INT NOT NULL references teachers(teacher_id) ON DELETE CASCADE,
                subject_id INT NOT NULL references subjects(subject_id)
            )
        '''
        self.execute(teacher_and_subject_table)

    def create_student_and_subject_table(self):
        teacher_and_subject_table = '''
            CREATE TABLE IF NOT EXISTS students_subjects(
                student_id INT NOT NULL references students(student_id) ON DELETE CASCADE,
                subject_id INT NOT NULL references subjects(subject_id)
            )
        '''
        self.execute(teacher_and_subject_table)
