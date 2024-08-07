
class Animal(object):
    def __init__(self, name):
        self.fname = name
        self.animal_code = 12
        print("I am Animal class constructor..")

    def show(self):
        print("I am Animal Calss instance method..")


class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.speak = "whoo"
        self.name = name
        # self.name = "wild Animal"

    def disp(self):
        # animal_name = self.name
        print("I am Elephant class Instance method..")
        print(f"Name: {self.fname} - Name2: {self.name} Speak: {self.speak} - Animal_code: {self.animal_code}")


if __name__ == "__main__":
    e = Elephant("elephant")
    e.show()
    e.disp()