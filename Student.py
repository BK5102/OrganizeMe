"""
    methods: signUp(), signIn()
"""
from sqlalchemy import Column, Integer, VARCHAR, CHAR
from .DBBase import DBBase

class StudentInfo(DBBase):
    __tablename__ = "student"

    stuID = Column("studentID", Integer, autoincrement=True, primary_key=True)
    firstName = Column("firstName", VARCHAR)
    lastName = Column("lastName", VARCHAR)
    email = Column("email", VARCHAR)
    password = Column("pass", CHAR)

    def __init__(self, first, last, email, password):
        self.firstName = first
        self.lastName = last
        self.email = email
        self.password = password

    def __repr__(self):
        return f"({self.firstName}, {self.lastName}, {self.email}, {self.password})"



