import uuid
import requests
from datetime import date, datetime, timedelta
from pydantic import BaseModel, confloat, validator
from enum import Enum

# fetch the raw JSON data from Github
url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v2.json'
data = requests.get(url).json()


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


# Iterate over each student record
for student in data:
    # create Pydantic model object by unpacking key/val pairs from our JSON dict as arguments 
    model = Student(**student)
    print(model)