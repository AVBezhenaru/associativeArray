from associativeArray import *

def putTest():
    print("Put test")
    count = 0
    aa = NativeDictionary(4)

    aa.put("1", 1)
    if aa.slots[1] == 1:
        count += 1

    aa.put("1", 2)
    if aa.slots[1] == 2:
        count += 1

    if count == 2:
        print("OK")

    else:
        print("ERROR")

putTest()


def isKeyTest():
    print("is key test")
    count = 0
    aa = NativeDictionary(4)

    aa.put("1", 1)
    a = aa.is_key("1")
    if a == True:
        count += 1

    a = aa.is_key("2")
    if a == False:
        count += 1

    if count == 2:
        print("OK")

    else:
        print("ERROR")

isKeyTest()


def getTest():
    print("get test")
    count = 0
    aa = NativeDictionary(4)

    aa.put("1", 1)
    a = aa.get("1")
    if a == 1:
        count += 1

    a = aa.get("2")
    if a == None:
        count += 1

    if count == 2:
        print("OK")

    else:
        print("ERROR")

getTest()
