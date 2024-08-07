
"""
method overriding in python

"""

# class Shape(object):
#     def __init__(self):
#         print("I am Shape class Constructor..")

#     def calculation(self, a, b):
#         print(f"Sum of two numbers is: {a + b}")

# class Size(Shape):
#     def __init__(self):
#         super().__init__()
#         print("I am Size class constructor..")

#     def calculation(self, a, b):
#         super().calculation(a, b)
#         mul = a * b
#         print(f"Product of two numbers is: {mul}")

# if __name__ == "__main__":
#     # size = Size()
#     # size.calculation(10, 20)
#     print(int.__add__(10, 20))



"""
operator overloading
"""

# print(int.__add__(12, 13))
# print(str.__add__("Rajon", "Hailee"))

# dunder repr method in python
# class Demo:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self) -> str:
#         return f"Sum is: {self.x + self.y}"
    

# if __name__ == "__main__":
#     d = Demo(10, 20)
#     print(d)
#     print(repr(d))


# operator overloading in python

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        #Point.__add__(p1, p2)
        X = self.x + other.x
        Y = self.y + other.y
        return Point(X, Y)
    
    def disp(self):
        print(f"x is: {self.x} -- y is: {self.y}")

    def __repr__(self) -> str:
        res = f"Point({self.x}, {self.y})"
        return res


if __name__ == "__main__":
    p1 = Point(10, 20)
    p2 = Point(30, 40)

    p3 = p1 + p2
    # print(type(p3))  # p3 is instance of Point

    # print(f"First Point: {p1} -- Second Point: {p2}")
    print(p3)
    
    p3.disp()


