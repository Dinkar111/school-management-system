class User:
    def __init__(
        self,
        user_id=None,
        first_name=None,
        last_name=None,
        password=None,
        address=None,
        phone=None,
        email=None,
        is_admin=False,
        is_teacher=False,
        is_student=False,
    ):
        self.__id = user_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__password = password
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__is_admin = is_admin
        self.__is_teacher = is_teacher
        self.__is_student = is_student

    def __str__(self):
        return self.__first_name, self.__last_name

    @property
    def get_id(self):
        return self.__id

    @property
    def get_name(self):
        return self.__first_name + " " + self.__last_name

    @property
    def get_address(self):
        return self.__address

    @property
    def get_phone(self):
        return self.__phone

    @property
    def get_email(self):
        return self.__email

    @property
    def is_admin(self):
        return self.__is_admin

    @property
    def is_teacher(self):
        return self.__is_teacher

    @property
    def is_student(self):
        return self.__is_student

    # check email exist
    def check_email_exist(self):
        query = """
        SELECT email FROM users WHERE email=%s;
        """
        self.db.execute(query, (self.email,))
        return self.db.fetchone()

    # get detail using email and password
    def get_user_by_email(self):
        query = "SELECT * FROM users WHERE email=%s"
        self.db.execute(
            query,
            (self.email,),
        )
        return self.db.fetchone()

    # insert new user
    def insert_new_user(self):
        insert_user_query = """
            INSERT INTO users(first_name, last_name, password, address, phone, email, is_student, is_teacher)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """
        self.db.execute(
            insert_user_query,
            (
                self.first_name,
                self.last_name,
                self.password,
                self.address,
                self.phone,
                self.email,
                self.is_student,
                self.is_teacher,
            ),
        )
        return self.db.fetchone()
