import psycopg2
from psycopg2 import (
    DataError,
    InternalError,
    OperationalError,
    ProgrammingError,
)
from psycopg2.extras import DictCursor


class DbClass:
    def __init__(
        self, db_name=None, user_name=None, password=None, host_name=None
    ):
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
                database=self.db_name,
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
        self.create_grade_table()
        self.create_user_table()
        self.create_student_table()
        self.create_teacher_table()
        self.create_subject_table()
        self.create_teacher_and_subject_table()
        self.create_teacher_and_grade_table()

    # creates grade table if not exist
    def create_grade_table(self):
        create_grade_table_query = """
            CREATE TABLE IF NOT EXISTS grades(
                id SERIAL PRIMARY KEY NOT NULL,
                grade VARCHAR(255) NOT NULL UNIQUE,
                no_of_students INT DEFAULT 0
            );
        """
        self.execute(create_grade_table_query)

    # Creates users table if not exist
    def create_user_table(self):
        create_user_table_query = """
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY NOT NULL,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                address VARCHAR(255),
                phone VARCHAR(255),
                is_admin BOOL NOT NULL DEFAULT FALSE,
                is_teacher BOOL NOT NULL DEFAULT FALSE,
                is_student BOOL NOT NULL DEFAULT FALSE
            );
        """
        self.execute(create_user_table_query)

    # Creates students table if not exist
    def create_student_table(self):
        create_student_table_query = """
            CREATE TABLE IF NOT EXISTS students(
                id SERIAL PRIMARY KEY NOT NULL,
                user_id INT NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE,
                roll_no INT NOT NULL,
                grade_id INT NOT NULL REFERENCES grades(id)
            );
        """
        self.execute(create_student_table_query)

    # Creates teachers table if not exist
    def create_teacher_table(self):
        create_teacher_table_query = """
            CREATE TABLE IF NOT EXISTS teachers(
                id SERIAL PRIMARY KEY NOT NULL,
                user_id INT NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE
            )
        """
        self.execute(create_teacher_table_query)

    # creates subjects table if not exist
    def create_subject_table(self):
        create_subject_table_query = """
            CREATE TABLE IF NOT EXISTS subjects(
                id SERIAL PRIMARY KEY NOT NULL,
                subject_code VARCHAR(255) NOT NULL UNIQUE,
                subject_name VARCHAR(255) NOT NULL,
                grade_id INT NOT NULL references grades(id) ON DELETE CASCADE
            )
        """
        self.execute(create_subject_table_query)

    # creates many to many teacher and subject table if not exist
    def create_teacher_and_subject_table(self):
        teacher_and_subject_table = """
            CREATE TABLE IF NOT EXISTS teachers_subjects(
                teacher_id INT NOT NULL references teachers(id) ON DELETE CASCADE,
                subject_id INT NOT NULL references subjects(id) ON DELETE CASCADE
            )
        """
        self.execute(teacher_and_subject_table)

    # creates many to many teacher and grades table if not exist
    def create_teacher_and_grade_table(self):
        teacher_and_grade_table = """
            CREATE TABLE IF NOT EXISTS teachers_grades(
                teacher_id INT NOT NULL references teachers(id) ON DELETE CASCADE,
                grade_id INT NOT NULL references grades(id) ON DELETE CASCADE
            )
        """
        self.execute(teacher_and_grade_table)
