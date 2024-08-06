""" 
    class: course
        methods: createCourse(), removeCourse(), getCourse()
    class: assignment 
        methods: createAssignment(), removeAssignment(),
        getAssignment(), 
        
    [FRONTEND] --- sortAssignment(), checkDueDate() [to check whether entered assignment has a due date], 
        sortByDueDate()
"""

from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from datetime import date
from .Organizer import ClassOrganizer
from .DBBase import DBBase
from typing import List

router = APIRouter()

class Organizer_SerializerAssign(BaseModel):
    stuIDCO: str
    stuAssign: str
    stuCourse: str
    stuAssign: str
    date: date

    class Config:
        orm_mode = True

class Organizer_SerializerCourse(BaseModel):
    stuIDCO: str
    stuAssign: str
    stuCourse: str
    stuAssign: str
    date: date

    class Config:
        orm_mode = True

class Organizer_SerializerDD(BaseModel):
    stuIDCO: str
    stuAssign: str
    stuCourse: str
    stuAssign: str
    date: date

    class Config:
        orm_mode = True

class Organizer_Serializer(BaseModel):
    organizerID: int
    stuIDCO: int
    stuCourse: str
    stuAssign: str
    date: date

    class Config:
        orm_mode = True

db = DBBase.session

#                                           Assignments

@router.post("/assignment", response_model=Organizer_Serializer,status_code=status.HTTP_201_CREATED)
def create_new_Assignment(assignment:Organizer_SerializerAssign):
    db_assignment = db.query(ClassOrganizer).filter(ClassOrganizer.stuAssign == assignment.stuAssign).first()

    if db_assignment is not None:
        raise HTTPException(status_code=400, detail="Assignment already exists.")
    
    new_assignment = ClassOrganizer(int(assignment.stuIDCO),assignment.stuCourse,assignment.stuAssign,assignment.date)

    try:
        db.add(new_assignment)
    except:
        db.rollback()
        raise
    else:
        db.commit()
        
    return new_assignment

""" @router.get("/assignment/{stu_Assign}", response_model=Organizer_Serializer, status_code=status.HTTP_200_OK)
def get_Assignment(stu_Assign:str):
    assignment = db.query(ClassOrganizer).filter(ClassOrganizer.stuAssign == stu_Assign).first()
    if assignment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")
    
    return assignment """

@router.get("/assignments", response_model=List[Organizer_Serializer], status_code=200)
def get_all_Assignments():
    assignments = db.query(ClassOrganizer).all()
    return assignments

@router.delete("/assignment/{organizerID}")
def remove_Assignment(organizerID: int):
    assignment_to_del = db.query(ClassOrganizer).filter(ClassOrganizer.organizerID == organizerID).first()

    if assignment_to_del is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

    try:
        db.delete(assignment_to_del)
    except:
        db.rollback()
        raise
    else:
        db.commit()
     
    return assignment_to_del

#                                            Courses
@router.post("/course", response_model=Organizer_Serializer,status_code=status.HTTP_201_CREATED)
def create_new_Course(course:Organizer_SerializerCourse):
    db_course = db.query(ClassOrganizer).filter(ClassOrganizer.stuCourse == course.stuCourse).first()

    if db_course is not None:
        raise HTTPException(status_code=400, detail="Course already exists.")
    
    new_course = ClassOrganizer(int(course.stuIDCO),course.stuCourse,course.stuAssign,course.date)
    
    try:
        db.add(new_course)
    except:
        db.rollback()
        raise
    else:
        db.commit()
        
    return new_course

@router.delete("/course/{organizerID}")
def remove_Course(organizerID: int):
    course_to_del = db.query(ClassOrganizer).filter(ClassOrganizer.organizerID == organizerID).first()

    if course_to_del is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

    try:
        db.delete(course_to_del)
    except:
        db.rollback()
        raise
    else:
        db.commit()
     
    return course_to_del

                                                # Due Date

@router.post("/dueDate", response_model=Organizer_Serializer,status_code=status.HTTP_201_CREATED)
def add_DueDate(dueDate:Organizer_SerializerDD):
    db_date = db.query(ClassOrganizer).filter(ClassOrganizer.date == dueDate.date).first()

    if db_date is not None:
        raise HTTPException(status_code=400, detail="Date already provided.")
    
    new_date = ClassOrganizer(int(dueDate.stuIDCO),dueDate.stuCourse,dueDate.stuAssign,dueDate.date)
    
    try:
        db.add(new_date)
    except:
        db.rollback()
        raise
    else:
        db.commit()
        
    return new_date