import uuid


def Unique_Name():
    username = uuid.uuid4().hex[:6].upper()
    username = "{}{}".format("AE", username)
    print(username)
    return username


def Unique_Password():
    password = uuid.uuid4().hex[:6].upper()
    password = "{}{}".format("AE", password)
    print(password)
    return password
