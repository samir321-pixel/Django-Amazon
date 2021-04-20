import uuid


def Unique_Name():
    username = uuid.uuid4().hex[:7].upper()
<<<<<<< Updated upstream
    username = "{}{}".format("ADS", username)
    print(username)
    return username


def Unique_Password():
    password = uuid.uuid4().hex[:7].upper()
    password = "{}{}".format("ADS", password)
    print(password)
    return password


def Delivery_Boy_Unique_Name():
    username = uuid.uuid4().hex[:6].upper()
    username = "{}{}".format("ADB", username)
=======
>>>>>>> Stashed changes
    print(username)
    return username


<<<<<<< Updated upstream
def Delivery_Boy_Unique_Password():
    password = uuid.uuid4().hex[:6].upper()
    password = "{}{}".format("ADB", password)
    print(password)
    return password
=======
def Unique_Password():
    password = uuid.uuid4().hex[:7].upper()
    print(password)
    return password
>>>>>>> Stashed changes
