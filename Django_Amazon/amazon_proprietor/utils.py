import uuid


def Unique_Name():
    username = uuid.uuid4().hex[:7].upper()
    username = "{}{}".format("AP", username)
    print(username)
    return username


def Unique_Password():
    password = uuid.uuid4().hex[:7].upper()
    password = "{}{}".format("AP", password)
    print(password)
    return password