import uuid


def Unique_Name():
    username = uuid.uuid4().hex[:7].upper()
    print(username)
    return username


def Unique_Password():
    password = uuid.uuid4().hex[:7].upper()
    print(password)
    return password