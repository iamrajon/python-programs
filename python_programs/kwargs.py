"""
**kwargs =
-> parameter that will pack all arguments into a dictionary
-> useful so that a function can accept varying amount of keyword arguments
"""


def showName(**kwargs):
    print("Welcome", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


showName(first="Rajon", middle="veng", last="Chaudhary")
