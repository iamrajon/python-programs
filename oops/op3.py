
# instance variable: a variable created within constructor and for every instance there is seperate copy of instance variable and when changed one particular instance variable it doesnot affect the vaiable assigned to another instance


# class Mobile():
#     def __init__(self, title, price = 50000):
#         self.name = title
#         self.price = price  


#     def disp(self):
#         print(f'Name: {self.name} -- price: {self.price}')


# if __name__ == "__main__":
#     redmi = Mobile("Redmi Note 9", 21000)
#     print(redmi.name)

#     redmi.name = "Redmi Note 11"
#     print(redmi.name)

#     print()

#     iphone = Mobile("Iphone 15 pro max")
#     print(iphone.name)


"""
class variable and class method
"""

class Mobile():
    name = "Iphone 15 Pro Max"    # class variable

    @classmethod
    def disp(cls):                # class Method to access class variable inside the class
        print(f"Name of phone: {cls.name}")

if __name__ == "__main__":
    # print(Mobile.name)
    # # Mobile.disp()

    ob1 = Mobile()
    print(ob1.name)

    # ob1.name = "Redmi"
    Mobile.name = "Redmi"   # when changed class variable then it will change for all instances


    ob2 = Mobile()
    print(ob2.name)
