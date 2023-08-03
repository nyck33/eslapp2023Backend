# Import necessary libraries
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
import base64


# Define an Enum class for Status
class Status(str, Enum):
    # Define your status values here. For example:
    status1 = "status1"
    status2 = "status2"
    status3 = "status3"


# Define a Pydantic model for Assignment
class Assignment(BaseModel):
    # Each attribute represents a field in the Assignment model.
    # The type hints indicate the data type of each field.
    # The Field function is used to add extra information about each field.
    # The '...' indicates that the field is required.
    id: str = Field(...)
    title: str = Field(...)
    status: Optional[Status] = Field(None)
    due_date: Optional[datetime] = Field(None)
    description: str = Field(...)
    student_answer: Optional[str] = Field(None)
    student_handwriting_img_path: Optional[str] = Field(None)
    student_handwriting_img: Optional[bytes] = Field(None)
    teacher_answer: Optional[str] = Field(None)

    # The Config class is a nested class where you can define model configuration.
    class Config:
        # The schema_extra attribute allows you to add extra information to the JSON Schema for this model.
        # Here, we're adding an example.
        schema_extra = {
            "example": {
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
        }

    # The from_orm method is a class method that allows you to create a model object from an arbitrary class.
    # Here, we're using it to handle the conversion of the student_handwriting_img field to a base64 string.
    @classmethod
    def from_orm(cls, obj):
        data = obj.__dict__.copy()
        if data.get('student_handwriting_img') is not None:
            data['student_handwriting_img'] = base64.b64encode(data['student_handwriting_img']).decode('utf-8')
        return cls(**data)

    # The to_orm method is used to convert the model object back to an arbitrary class.
    # Here, we're using it to handle the conversion of the student_handwriting_img field from a base64 string.
    def to_orm(self):
        data = self.dict()
        if data.get('student_handwriting_img') is not None:
            data['student_handwriting_img'] = base64.b64decode(data['student_handwriting_img'])
        return data
