import psycopg2

class DbClass:

    def __init__(self, db_name, user, password, host):
        try:
            self.conn = psycopg2.connect(
                host = host,
                user = user,
                password = password,
                database = db_name
            )
            print("Database is connected successfully")
        except Exception as err:
            raise err


        
