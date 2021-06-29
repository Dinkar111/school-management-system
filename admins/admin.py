
class Admin:

    def __init__(self, admin_id=None, admin_username=None, admin_email=None, admin_password=None, role=None):
        self.admin_id = admin_id
        self.admin_username = admin_username
        self.admin_email = admin_email
        self.admin_password = admin_password
        self.role = role

    def get_admin_by_username_password(self, db):
        query = '''
            SELECT * FROM admins WHERE admin_username=%s AND admin_password=%s
        '''
        db.execute(query, (self.admin_username, self.admin_password,))
        return db.fetchone()

    def get_admin_by_id(self, db):
        query = '''
            SELECT admin_username, admin_email FROM admins
        '''
        db.execute(query, (self.admin_id,))
        return db.fetchone()
