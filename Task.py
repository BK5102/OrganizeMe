"""
    methods: createTask(), removeTask()
"""
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey
from .DBBase import DBBase
from .Student import StudentInfo

class Tasks(DBBase):
    __tablename__ = "task"

    taskID= Column("taskID", Integer, autoincrement=True, primary_key=True)
    stuIDT = Column("studentID", Integer, ForeignKey("student.studentID"), primary_key=True)
    task = Column("user_task", VARCHAR)       
    
    def __init__(self, id, task):
        self.stuIDT = id
        self.task = task
        
    def __repr__(self):
        return f"({self.task})"