class Subject:
    def __init__(
        self,
        subject_id=None,
        subject_code=None,
        subject_name=None,
        grade_id=None,
    ):
        self.__id = subject_id
        self.__subject_code = subject_code
        self.__subject_name = subject_name
        self.__grade_id = grade_id

    @property
    def get_subject_id(self):
        return self.__id

    @property
    def get_subject_code(self):
        return self.__subject_code

    @property
    def get_subject_name(self):
        return self.__subject_name

    @property
    def get_grade(self):
        return self.__grade_id
