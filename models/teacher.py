from .user import User


class Teacher(User):
    def __init__(self, teacher_id=None, subjects=None, grades=None, **kwargs):
        super().__init__(**kwargs)
        self.__teacher_id = teacher_id
        self.__subjects = subjects
        self.__grades = grades

    @property
    def get_teacher_id(self):
        return self.__teacher_id

    @property
    def get_subjects(self):
        return self.__subjects

    @property
    def get_grades(self):
        return self.__grades
