def make():

    user=Info(Fname=fname,Lname=lname,username=Username,gender=Gender,mobile=Mobile)



    session.add(user)
    session.commit()

    return {"Registered"}

def update(value,coloumn,change):
    users=session.query(Info).filter_by(coloumn=value).all()
    
    users.Fname=change

    session.commit()

    return "Database Updated"

def delete(col,value):
    users=session.query(Info).filter_by(col=value).one_or_none()
    user=users.fname

    session.delete(users)

    session.commit()

    return user

def read():
    users=session.query(Info).all()
    for user in users:
       print(f"First Name:{user.Fname} Last Name:{user.Lname} Username:{user.username} Gender:{user.gender} mobile:{user.mobile}")
    return "Fetch From Database"