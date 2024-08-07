

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show_data(self):
        print(f"Hello, {self.name} Your roll is changed to {self.roll+1}")

    @classmethod
    def initiate_data(cls, name, roll):
        return cls(name, roll)


# creating instance of Student class using class method
obj = Student.initiate_data('Rajon', 18)

obj.show_data()




