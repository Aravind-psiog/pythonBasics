def dictoperation():
    myDict = {"name": "Aravind", "age": 28,
              "location": "Kodaikanal", "temp": 98.45, "unit": "celsius"}
    newDict = myDict.copy()
    print(myDict.get("location"))
    myDict.pop("name")
    print(myDict)
    print(myDict.values())
    print(myDict.keys())
    print(newDict.items())
    newDict.update({"weight": 86})
    newDict.update({"temp": 98})
    print(newDict)
    newDict.popitem()
    del newDict["age"]
    print(newDict)
    newDict.setdefault("remote", "Chennai")

    for k, v in newDict.items():
        print(k, v)


def fromkey():
    i = ("name", "age", "location")
    j = None
    newDict = dict.fromkeys(i, j)
    print(newDict)


dictoperation()
