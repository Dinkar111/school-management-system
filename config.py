from decouple import config


class DBConfigClass:

    def __init__(self):
        self.host = config('HOST')
        self.user = config('USER')
        self.password = config('PASSWORD')
        self.db_name = config('DB_NAME')

    def get_config(self):
        return {
            "host": self.host,
            "user": self.user,
            "password": self.password,
            "db": self.db_name
        }
