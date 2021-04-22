import uuid


def Unique_Name():
    username = uuid.uuid4().hex[:7].upper()
    username = "{}{}".format("ADS", username)
    print(username)
    return username


def Unique_Password():
    password = uuid.uuid4().hex[:7].upper()
    password = "{}{}".format("ADS", password)
    print(password)
    return password