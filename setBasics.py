mySet = {"Aravind", "is", 28, "years",
         "old", "and", "he", "is", "into", "tech"}
newMySet = mySet.copy()
newSet = {"Monish", "is", 27, "years",
          "old", "and", "he", "is", "into", "cars"}
newNewSet = newSet.copy()
# mySet.difference(newSet)
# print(mySet)

mySet.difference_update(newSet)
print(mySet)

newMySet.discard("Monish")
print(newMySet)

newMySet.issubset(newNewSet)
print(newMySet)
