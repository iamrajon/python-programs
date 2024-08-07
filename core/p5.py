"""
string methods in python
"""

# name = "Rajon chaudhary"

# print(len(name))
# print(name.find("C"))
# print(name.capitalize())   # it capitalize first letter of words
# print(name.upper())          # it converts the whole string in upper case
# print(name.lower())
# print(name.isdigit())  # it checks the datatype of variable and return true or false
# print(name.isalpha())  # it checks the white space between words
# print(name.count("a"))
# print(name.replace("o", "a"))
# print(name*2)

name = input("What is your name?: ")
age = int(input("How old are you?: "))

age = age+1

print("Hello, " + name + f" you are {age} years old from today coz today is your birthday!")
