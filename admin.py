import argparse
import sys
from decouple import config

from database import DbClass
from helpers.password_hash import make_pw_hash


def create_admin(database, arguments):
    email = arguments.email
    hashed_password = make_pw_hash(arguments.password)
    insert_admin_query = """
    INSERT INTO users(email, password, is_admin, first_name, last_name) VALUES (%s, %s, %s, %s, %s)
    """
    admin_created = database.execute(
        insert_admin_query,
        (
            email,
            hashed_password,
            True,
            "admin",
            "admin",
        ),
    )
    if admin_created:
        return "Admin created successfully"
    else:
        return "Something went wrong"


# initiate DbClass
db = DbClass(
    db_name=config("DB_NAME"),
    user_name=config("USER"),
    password=config("PASSWORD"),
    host_name=config("HOST"),
)
db.connect()
db.create_all_tables()

parser = argparse.ArgumentParser()
parser.add_argument("-email", type=str)
parser.add_argument("-password", type=str)
args = parser.parse_args()
sys.stdout.write(str(create_admin(db, args)))
