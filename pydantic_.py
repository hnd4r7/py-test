from dataclasses import Field
from typing import Literal, Optional, Union
import uuid
import requests
from datetime import date, datetime, timedelta
from pydantic import BaseModel, confloat, validator
from enum import Enum

# fetch the raw JSON data from Github
url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v2.json'
data = requests.get(url).json()
print(data)

# define an Enum of acceptable Department values
class DepartmentEnum(Enum):
    ARTS_AND_HUMANITIES = 'Arts and Humanities'
    LIFE_SCIENCES = 'Life Sciences'
    SCIENCE_AND_ENGINEERING = 'Science and Engineering'


# Pydantic model to outline structure/types of Modules
class Module(BaseModel):
    id: int
    name: str
    professor: str
    credits: int
    registration_code: str


# Pydantic model to outline structure/types of Students (including nested model)
class Student(BaseModel):
    id: uuid.UUID
    name: str
    date_of_birth: date
    GPA: confloat(ge=0, le=4)
    course: str | None
    department: DepartmentEnum
    fees_paid: bool
    modules: list[Module] = [] 

    @validator('date_of_birth')
    def ensure_16_or_over(cls, value):
        sixteen_years_ago = datetime.now() - timedelta(days=365*16)

        # convert datetime object -> date
        sixteen_years_ago = sixteen_years_ago.date()
        
        # raise error if DOB is more recent than 16 years past.
        if value > sixteen_years_ago:
            raise ValueError("Too young to enrol, sorry!")
        return value

# define an Enum of acceptable Department values
class DepartmentEnum(Enum):
    ARTS_AND_HUMANITIES = 'Arts and Humanities'
    LIFE_SCIENCES = 'Life Sciences'
    SCIENCE_AND_ENGINEERING = 'Science and Engineering'


# Pydantic model to outline structure/types of Modules
class Module(BaseModel):
    id: Union[uuid.UUID, int]
    name: str
    professor: str
    credits: Literal[10,20]
    registration_code: str


# Pydantic model to outline structure/types of Students (including nested model)
class Student(BaseModel):
    id: uuid.UUID
    student_name: str = Field(alias="name")
    date_of_birth: date = Field(default_factory=lambda: datetime.today().date())
    GPA: confloat(ge=0, le=4)
    course: Optional[str]
    department: DepartmentEnum
    modules: list[Module] = Field(default=[])

    class Config:
        use_enum_values = True

# Iterate over each student record
for student in data:
    # create Pydantic model object by unpacking key/val pairs from our JSON dict as arguments 
    model = Student(**student)
    model.modules[3]
    print(model)