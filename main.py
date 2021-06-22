from db_config import DBConfigClass
from database import DbClass


class Main:

    def __init__(self):

        # Config file 
        db_config = DBConfigClass()

        # database config from config file is return in python dictionary
        db_data = db_config.get_db_config()

        # initiate DbClass 
        self.db =  DbClass(db_data['db'], db_data['user'], db_data['passwd'], db_data['host'])
        
     
if __name__== "__main__":
    Main()
