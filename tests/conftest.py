import pytest
from database import DbClass
from students.student_manager import ManageStudent

@pytest.fixture
def db_setup():
    db = DbClass(db_name='school', user_name='dinkar', password='password', host_name='localhost')
    db.connect()
    return db

@pytest.fixture
def student_manager():
    student_manager = ManageStudent()
    return student_manager
