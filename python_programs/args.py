"""
*args =
-> It is a parameter given to any function that will pack all arguments into a tuple at time of function call
-> Useful so that a function can accept a varying amount of arguments
-> we can give any name of *args ie nums (it's optional)
"""


def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


result = add(1, 2, 3, 4, 5)
print(f"The sum of all numbers is: {result}")
