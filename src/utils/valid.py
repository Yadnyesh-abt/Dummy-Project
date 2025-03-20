import re

from fastapi import HTTPException


def valid_mobile(mobile:str):
    if not re.match(r"^91\d{10}",mobile):
        raise HTTPException(status_code=400,detail="Mobile number must be exactly 12 digits and should start with 91 ")
    
def valid_username(username:str):
    if not re.match(r"^[a-zA-Z0-9_]{3,32}$",username):
        raise HTTPException(status_code=400,detail="Username should be 32 characters long and should contain no special characters except '_' ") 

def valid_email(email:str):
    if not re.match(r"^[[\w\.-]+@[\w\.-]+\.\w{2,}$", email) or not email.endswith(".com"):
        raise HTTPException(status_code=400,detail="Invalid Format !!! Email should contain '@' and should end with '.com' ")

def valid_dob(date_of_birth:str):
    
        if not re.match(r"^(19|20)\d{2}/(0[1-9]|1[0-2])/([0-2][0-9]|3[0-1])$",date_of_birth):
            raise HTTPException(status_code=400,detail="Invalid Format !!! Date Should be in format YYYY/MM/DD. Month Should be below 12 and Date should be below 31")
        
   
    