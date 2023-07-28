# Import necessary libraries
from typing import Optional, List
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
import base64
from ..assignments.assignment_model import Assignment

# We'll reuse the Status and Assignment classes from the previous code snippet.
# If this code is in a different file, you might need to import these classes.

# Define a Pydantic model for Student
class Student(BaseModel):
    # Each attribute represents a field in the Student model.
    # The type hints indicate the data type of each field.
    # The Field function is used to add extra information about each field.
    # The '...' indicates that the field is required.
    id: str = Field(...)
    name: str = Field(...)
    all_assignments: Optional[List[Assignment]] = Field(None)
    completed_assignments: Optional[List[Assignment]] = Field(None)

    # The Config class is a nested class where you can define model configuration.
    class Config:
        # The schema_extra attribute allows you to add extra information to the JSON Schema for this model.
        # Here, we're adding an example.
        schema_extra = {
            "example": {
                "id": "1",
                "name": "John Doe",
                "all_assignments": [
                    {
                        "id": "1",
                        "title": "Assignment 1",
                        "status": "status1",
                        "due_date": "2023-07-13T00:00:00",
                        "description": "This is an assignment",
                        "student_answer": "This is a student answer",
                        "student_handwriting_img_path": "/path/to/image",
                        "student_handwriting_img": base64.b64encode(b'Your Image data'),
                        "teacher_answer": "This is a teacher answer",
                    }
                ],
                "completed_assignments": [],
            }
        }
