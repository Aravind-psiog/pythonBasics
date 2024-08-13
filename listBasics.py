def list():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    newList = thislist.copy()
    print(thislist[1:4])
    thislist[5] = "Raspberry"
    thislist[1:4] = ["blackcurrant", "watermelon"]
    thislist.insert(3, "asd")
    print(thislist)
    if thislist.count("watermelon") == 1:
        print(thislist.index("watermelon"))
    newList.pop(1)
    newList.remove("cherry")
    print(newList)
    newList.reverse()
    print(newList)
    newList.sort()
    print(newList)


list()
