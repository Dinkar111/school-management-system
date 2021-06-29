
class Subject:

    def __init__(self, subject_id=None, subject_name=None):
        self.subject_id = subject_id
        self.subject_name = subject_name

    def add(self, db):
        add_query = '''
            INSERT INTO subjects(subject_name) VALUES (%s)
        '''
        db.execute(add_query, (self.subject_name,))
        return True

    def check_subject_exist(self, db):
        check_query = '''
            SELECT subject_id, subject_name FROM subjects WHERE subject_name=%s
        '''
        db.execute(check_query, (self.subject_name, ))
        return db.fetchone()

    def view_all_subject(self, db):
        all_subjects = '''
            SELECT * FROM subjects
        '''
        db.execute(all_subjects)
        return db.fetchall()
