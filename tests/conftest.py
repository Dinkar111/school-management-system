import pytest
from decouple import config

from database import DbClass
from managers.user_manager import UserManager
from managers.student_manager import StudentManager
from managers.grade_manager import GradeManager


@pytest.fixture
def db_setup():
    db = DbClass(
        db_name=config("TEST_DB_NAME"),
        user_name=config("TEST_USER"),
        password=config("TEST_PASSWORD"),
        host_name=config("TEST_HOST"),
    )
    db.connect()
    db.create_all_tables()
    return db


@pytest.fixture
def user_manager(db_setup):
    return UserManager(db_setup)


@pytest.fixture
def student_manager(db_setup):
    return StudentManager(db_setup)


@pytest.fixture
def grade_manager(db_setup):
    return GradeManager(db_setup)
