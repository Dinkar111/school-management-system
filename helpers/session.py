
class Session:
    def __init__(self):
        self.sessions = {}

    def set_session(self, logged_in=False, student_id=None, first_name=None):
        self.sessions['logged_in'] = logged_in
        self.sessions['student_id'] = student_id
        self.sessions['first_name'] = first_name

    def clear_session(self):
        self.sessions['logged_in'] = False
        self.sessions['student_id'] = None
        self.sessions['first_name'] = None

