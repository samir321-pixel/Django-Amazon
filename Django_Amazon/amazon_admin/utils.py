import uuid


def Unique_Name():
    username = uuid.uuid4().hex[:8].upper()
    username = "{}{}".format("AD", username)
    return username


def Unique_Password():
    password = uuid.uuid4().hex[:8].upper()
    password = "{}{}".format("AD", password)
    return password
