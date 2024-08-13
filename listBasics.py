def list():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    thislist[5] = "Raspberry"
    thislist[1:4] = ["blackcurrant", "watermelon"]
    thislist.insert(3, "asd")
    print(thislist)


list()
