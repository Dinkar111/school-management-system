class Grade:
    def __init__(self, grade_id=None, grade=None, no_of_students=None):
        self.__id = grade_id
        self.__grade = grade
        self.__no_of_students = no_of_students

    def __str__(self):
        return self.__grade

    @property
    def get_id(self):
        return self.__id

    @property
    def get_grade(self):
        return self.__grade

    @property
    def get_no_of_students(self):
        return self.__no_of_students
