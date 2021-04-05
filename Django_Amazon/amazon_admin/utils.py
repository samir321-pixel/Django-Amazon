import uuid


def Unique_Name():
    username = uuid.uuid4().hex[:6].upper()
    print(username)
    return username


def Unique_Password():
    password = uuid.uuid4().hex[:6].upper()
    print(password)
    return password


Unique_Name()
Unique_Password()
