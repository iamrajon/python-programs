
# class Student:
#     def __init__(self):
#         self.name = "Rajan Chauhary"
#         print("I am Student Class constructor..")

#     def show(self):
#         print(f"Name of student is: {self.name}")

# class Teacher:
#     def __init__(self):
#         self.dep = "IT"
#         print("I am Teacher class constructor..")

#     def disp(self):
#         print(f"Department of Teacher is: {self.dep}")


# def make_call(obj):
#     if hasattr(obj, "disp"):
#         obj.disp()
#     else:
#         print(f"{obj} has no method disp()")

# if __name__ == "__main__":
#     student = Student()
#     make_call(student)

    # teacher = Teacher()
    # make_call(teacher)



"""
method overlading is not supported in python programming langauge but we can achuieve by using default values
"""

class Calculation:
    def sum(self, a = None , b = None, c = None):
        if a is not None and b is not None and c is not None:
            sum = a + b + c
            return sum
        elif a is not None and b is not None:
            return a + b
        else:
            return "Provide at least two numbers"
        sum = a + b + c
        return sum
    
    def sum(self, *args, **kwargs):
        # print(kwargs)
        # print(args)
        if args:
            sum = 0
            for num in args:
                sum += num
            return sum
        
        if kwargs:
            sum = 0
            for value in kwargs.values():
                sum += value
            return sum

        
    

calc = Calculation()
# print(f"Sum is: {calc.sum(10, 20, 30)}")
# print(f"Sum is: {calc.sum(10, 20)}")
# print(f"Sum is: {calc.sum(10)}")

res = calc.sum(10, 20, 12, 42, 432, 2342)
print(f"sum is: {res}")

# res = calc.sum(num1 = 10, num2 = 20)
# print(f"sum is : {res}")