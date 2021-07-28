from .user import User


class Student(User):
    def __init__(self, student_id=None, roll_no=None, grade=None, **kwargs):
        super().__init__(**kwargs)
        self.__student_id = student_id
        self.__roll_no = roll_no
        self.__grade = grade

    @property
    def get_student_id(self):
        return self.__student_id

    @property
    def get_roll_no(self):
        return self.__roll_no

    @property
    def get_grade(self):
        return self.__grade
