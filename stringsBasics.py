myName = "His name is {name} and he is {age} years old. {name} likes to code ".format(
    name="Aravind", age=28)
totalNumber = []


def general():
    for i in myName:
        print(i.isspace())
        if not i.isspace():
            totalNumber.append(i)
            try:
                int(i)
                print(f"im a integrer {i}")
            except:
                print(f"im a string {i}")
    print(len(totalNumber))
    print(totalNumber)


def new():
    myList = ["aravind", "abilash", "w"]
    print("Hi".join(myList))


def stripeSplit():
    print(myName.strip()+"o")
    array = myName.split()
    print(array)
    print(array[-3:-1])
    array[3] = "Jeni"


stripeSplit()

print(myName.capitalize()+"o")
# print(myName.casefold())
# print(myName.count("A"))
# print(myName.encode('utf-8'))
# print(myName.find("Aravind"))
# print(myName.upper())
# print(myName.lower())
# print(myName.replace("Aravind", "Abilash"))
