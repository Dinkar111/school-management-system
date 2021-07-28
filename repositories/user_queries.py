class UserQueries:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        query = """
            SELECT * FROM users
        """
        self.db.execute(query)
        return self.db.fetchall()

    def get_user_by_email(self, email):
        query = """
            SELECT * FROM users WHERE email=%s
        """
        self.db.execute(query, (email,))
        return self.db.fetchone()

    def insert(
        self,
        first_name,
        last_name,
        password,
        address,
        email,
        phone,
        is_teacher,
        is_student,
    ):
        query = """
            INSERT INTO users(first_name, last_name, password, address, phone, email, is_student, is_teacher)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """
        self.db.execute(
            query,
            (
                first_name,
                last_name,
                password,
                address,
                phone,
                email,
                is_student,
                is_teacher,
            ),
        )
        return self.db.fetchone()
