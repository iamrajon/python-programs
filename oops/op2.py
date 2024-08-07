
# constructor with parameters


class Mobile():
    def __init__(self, name, price=50000):
        self.name = name
        self.price = price

    def disp(self):
        print(f"Mobile: {self.name} -- Price = {self.price} ")


if __name__ == "__main__":
    redmi = Mobile("Redmi Note 10 Pro", 25000)
    redmi.disp()
    print(id(redmi))

    print()

    iphone = Mobile("Iphone 15 Pro")
    iphone.disp()
    print(id(iphone))