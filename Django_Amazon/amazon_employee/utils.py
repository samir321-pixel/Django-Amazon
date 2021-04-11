import uuid


def Unique_Name():
    username = uuid.uuid4().hex[:6].upper()
    print(username)
    return username
