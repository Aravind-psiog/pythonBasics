class Humans:

    def __init__(self) -> None:
        self.name = "hello"

    def read_data(self):
        # print(self.name)
        return self.name

    def __privateclass(self):

        print("im private")

    def access(self):
        return self.__privateclass()


class Super(Humans):
    def __init__(self) -> None:
        self.name = "supes"


class head:
    def __init__(self) -> None:
        self.name = "supes"


read = Humans()

print(read.access())
