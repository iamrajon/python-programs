"""
index operator [] = gives access to a sequence's element (string, list, tuples)
"""

name = "miles chaudhay"
# print(f"Before: {name}")

# if name[0].islower():
#     name = name.capitalize()
#
# print(f"After: {name}")

# first_name = name[0:5].upper()
# print(f"first name: {first_name}")
#
# last_name = name[6:].lower()
# print(f"last name: {last_name}")

# last_character = name[-1]
# print(last_character)


"""
Function in python = a block of code which is executed only when it is called
"""


# def hello(name):
#     print("Hello " + name)
#     print("Learning function in python")
#
#
# hello("Rajon")  # function calling

"""
return statement = Functions send python values/objects back to the callers.
                    These values/objects are known as the function's return value
"""


# def multiply(num1, num2):
#     result = num1 * num2
#     return result
#
#
# value = multiply(2, 4)
# print(value)


# use of keyword arguments in python
# def showName(first, middle, last):
#     print(f"Hello {first} {middle} {last}")
#
#
# showName(last="Chaudhary", middle="Veng", first="Rajon")


"""
nested function calls = function call inside other function call
                        innermost function calls are resolved first
                        returned value is used as  argument for the next outer function
"""

# this task can be done simply using neted function calls
# num = input("Enter a whole positive number?: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(f"The number is: {num}")

print(round(abs(float(input("Enter a whole positive number?: ")))))

