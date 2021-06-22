from configparser import ConfigParser

class DBConfigClass:

    def __init__(self):
        self.config = ConfigParser()

    def get_db_config(self):
        self.config.read("config.ini")
        return {
            "host": self.config['dev_DB']['HOST'],
            "user": self.config['dev_DB']['USER'],
            "passwd": self.config['dev_DB']['PASSWORD'],
            "db": self.config['dev_DB']['DB']
        }