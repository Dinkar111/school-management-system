
class Person:

    def __init__(self, user_id=None, first_name=None, last_name=None,
                 password=None, address=None, phone=None, email=None):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.address = address
        self.phone = phone
        self.email = email
        self.role = None

    # Insert query
    def insert(self, db):
        pass

    # Check if Email already exist e
    def check_email_exist(self, db):
        query = '''
        SELECT email FROM students WHERE email=%s
        UNION 
        SELECT email from teachers where email=%s
        '''
        db.execute(query, (self.email, self.email,))
        return db.fetchone()

    # Check if phone already exist
    def check_phone_exist(self, db):
        query = '''
        SELECT phone FROM students WHERE phone=%s
        UNION 
        SELECT phone from teachers where phone=%s
        '''
        db.execute(query, (self.phone, self.phone,))
        return db.fetchone()

    # get by email and password
    def get_by_email_password(self, db):
        pass

    # get by id after login and use id as a token
    def get_user_by_id(self, db):
        pass

    # get all profile
    def get_all_profile_to_view(self, db):
        pass

    # Update name
    def update_name(self, db):
        pass

    # Update password
    def update_password(self, db):
        pass

    # Update address
    def update_address(self, db):
        pass

    # Update phone
    def update_phone(self, db):
        pass

    # Update email
    def update_email(self, db):
        pass

    # Delete
    def delete(self, db):
        pass
