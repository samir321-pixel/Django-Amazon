import uuid


def Unique_Name():
    username = uuid.uuid4().hex[:6].upper()
    return username


def Unique_Password():
    password = uuid.uuid4().hex[:6].upper()
    return password
