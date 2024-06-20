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

router = APIRouter()

class Organizer_Serializer(BaseModel):
    organizerID: int
    stuIDCO: int
    stuCourse: str
    stuAssign: str
    date: date

    class Config:
        orm_mode = True

db = DBBase.session

@router.post("/new_assignment", response_model=Organizer_Serializer,status_code=status.HTTP_201_CREATED)
def create_new_Assignment(assignment:Organizer_Serializer):
    db_assignment = db.query(ClassOrganizer).filter(ClassOrganizer.stuAssign == assignment.stuAssign).first()

    if db_assignment is not None:
        raise HTTPException(status_code=400, detail="Assignment already exists.")
    
    new_assignment = ClassOrganizer(assignment.stuIDCO, assignment.stuCourse, assignment.stuAssign, assignment.date)
    
    try:
        db.add(new_assignment)
    except:
        db.rollback()
        raise
    else:
        db.commit()
        
    return new_assignment

@router.get("/assignment/{stu_Assign}", response_model=Organizer_Serializer, status_code=status.HTTP_200_OK)
def get_Assignment(stu_Assign:str):
    assignment = db.query(ClassOrganizer).filter(ClassOrganizer.stuAssign == stu_Assign).first()
    if assignment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")
    
    return assignment

@router.delete("/del_assignment/{stu_Assign}", response_model=Organizer_Serializer)
def remove_Assignment(stu_Assign: str):
    assignment_to_del = db.query(ClassOrganizer).filter(ClassOrganizer.stuAssign == stu_Assign).first()

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