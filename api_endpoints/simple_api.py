from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

from models.assignments.assignment_model import Assignment
from models.person.student_model import Student

app = FastAPI()

# Mock databases
assignments_db = {}
students_db = {}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/assignments/")
async def create_assignment(assignment: Assignment):
    if assignment.id in assignments_db:
        raise HTTPException(status_code=400, detail="Assignment already exists")
    assignments_db[assignment.id] = assignment
    return assignment

@app.get("/assignments/{assignment_id}")
async def read_assignment(assignment_id: str):
    if assignment_id not in assignments_db:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return assignments_db[assignment_id]

@app.post("/students/")
async def create_student(student: Student):
    if student.id in students_db:
        raise HTTPException(status_code=400, detail="Student already registered")
    students_db[student.id] = student
    return student

@app.get("/students/{student_id}")
async def read_student(student_id: str):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    return students_db[student_id]

@app.get("/students/{student_id}/assignments")
async def read_student_assignments(student_id: str):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    student = students_db[student_id]
    return student.allAssignments

@app.get("/students/{student_id}/assignments/{assignment_id}")
async def read_student_assignment(student_id: str, assignment_id: str):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    student = students_db[student_id]
    for assignment in student.allAssignments:
        if assignment.id == assignment_id:
            return assignment
    raise HTTPException(status_code=404, detail="Assignment not found")
