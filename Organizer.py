""" 
        course methods: createCourse(), removeCourse(), getCourse()
 
        assignment methods: createAssignment(), removeAssignment(),
        getAssignment(), sortAssignment(), checkDueDate() [to check whether entered assignment has a due date], 
        sortByDueDate()
"""
from sqlalchemy import Column, Integer, VARCHAR, DATE, ForeignKey
from .DBBase import DBBase
from .Student import StudentInfo

class ClassOrganizer(DBBase):
    __tablename__ = "class_organizer"

    organizerID= Column("organizerID", Integer, autoincrement=True, primary_key=True)
    stuIDCO = Column("studentID", Integer, ForeignKey("student.studentID"), primary_key=True)
    stuCourse = Column("course", VARCHAR)
    stuAssign = Column("assignment", VARCHAR)
    date = Column("due_date", DATE)       #implement scheduler instead
    
    def __init__(self, id, course, assign, date): 
        self.stuIDCO = id
        self.stuCourse = course
        self.stuAssign = assign
        self.date = date
        
    def __repr__(self):
        return f"({self.stuIDCO} {self.stuCourse}, {self.stuAssign}, {self.date})"