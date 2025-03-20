from pydantic import BaseModel,field_validator
from utils.valid import valid_username,valid_mobile,valid_dob,valid_email

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    username: str
    email:str
    date_of_birth:str
    gender: str
    mobile: str

    @field_validator("username")
    @classmethod
    def validate_username(cls,value):
        valid_username(value)
        return value
    
    @field_validator("mobile")
    @classmethod
    def validate_mobile(cls,value):
        valid_mobile(value)
        return value
    
    @field_validator("email")
    @classmethod
    def validate_email(cls,value):
        valid_email(value)
        return value
    
    @field_validator("date_of_birth")
    @classmethod
    def validate_dob(cls,value):
        valid_dob(value)
        return value
