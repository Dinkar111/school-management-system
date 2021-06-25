import psycopg2
from psycopg2 import OperationalError, DatabaseError, ProgrammingError, DataError, InternalError


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
            self.cursor = self.connection.cursor()
        except (OperationalError, DatabaseError) as error:
            print(error)

    def execute(self, db_query, data=None):
        try:
            self.cursor.execute(db_query, data)
            self.connection.commit()
            return self.cursor
        except (DataError, ProgrammingError, OperationalError) as error:
            print(error)

    # Creates students table if not exist
    def create_student_table(self):
        try:
            create_student_table_query = '''
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
            self.execute(create_student_table_query)
        except InternalError as error:
            print(error)
