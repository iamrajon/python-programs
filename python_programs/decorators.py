# decorators in python
"""
In Python, a decorator is a special type of function that is used to modify or extend the behavior of another function or method.
Decorators are often used to wrap or enhance the functionality of functions without modifying their actual code.
They are denoted by the "@" symbol followed by the decorator function's name.
"""

# example 1
# def my_decorator(func):
#     def modify_func():
#         print("first you have to learn any one programming language")
#         func()
#         print("Now your are a programmer.")
#
#     # return modify_func()   -> gives error
#     return modify_func
#
#
# @my_decorator
# def greet():
#     print("Welcome to world of programming!")
#
# greet()


# Example 2

def my_decorator(func):
    def modify(*args, **kwargs):
        print(f" what is inside **args:  {args}")
        print("The two numbers Provided are: ")
        for i in args:
            print(i, end=",")

        print()
        print("do you know how to add two numbers")
        func(*args, **kwargs)
        print("result of sum of two numbers is shown")

    return modify


@my_decorator
def add(x, y):
    result = x + y
    print(f"sum is: {result}")


add(10, 5)