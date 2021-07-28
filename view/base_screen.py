from managers.user_manager import UserManager
from managers.student_manager import StudentManager
from managers.teacher_manager import TeacherManager
from managers.grade_manager import GradeManager
from managers.subject_manager import SubjectManager


class BaseScreen:
    def __init__(self, db):
        self.db = db
        self.user_manager = UserManager(db=self.db)
        self.student_manager = StudentManager(db=self.db)
        self.teacher_manager = TeacherManager(db=self.db)
        self.subject_manager = SubjectManager(db=self.db)
        self.grade_manager = GradeManager(db=self.db)
