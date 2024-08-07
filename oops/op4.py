# Accesser method and Mutator method ie. (gettet/setter) method
# class method


class Student():
    def __init__(self):
        self.name = "Rajon"
        self.age = 22

    def get_student_data(self):
        return f"Name: {self.name} -- Age: {self.age}"
    
    def set_student_data(self, name, age):
        self.name = name
        self.age = age


class Mobile(object):

    model = "Samsung"   # class variable

    def __init__(self):
        print("I am constructor..")

    @classmethod
    def show_model(cls):
        print("I am class method")
        print(f"model is: {cls.model}")

class Developer:
    def __init__(self):
        print("I am constructor of Developer class.")

    salary = 100000

    @staticmethod
    def show_data(name):
        name = name
        salary = Developer.salary

        print(f"Name of Dev: {name} -- salary: {salary}")



if __name__ == "__main__":
    student1 = Student()

    # res = student1.get_student_data()
    # print(res)


    # student1.set_student_data("Hailee", 24)

    # res = student1.get_student_data()
    # print(res)


    # mobile1 = Mobile()
    # mobile1.show_model()
    # Mobile.show_model()

    name = input("Enter Your Name:  ")
    developer1 = Developer()
    Developer.show_data(name)




    

