

"""

Abstract class in python
"""

# from abc import ABC, abstractmethod


# class Relationship(ABC):
#     @abstractmethod
#     def has_gf(self):
#         pass

#     def same(self):
#         print("I am concrete method")


# class Rajan(Relationship):
#     def has_gf(self):
#         print("Hailee is Gf of Rajon")
            


# if __name__ == "__main__":
#     r = Rajan()
#     r.same()
#     r.has_gf()



"""
Interface in Python
- There is no any concept of Interface in python
- But we generally call an Abstract class as Interface if it contains only abstract methods and no any concrete method
- If the child class inheriting Interface must have to define the each abstract methods
- If the child class Inheriting Interface doesn't define the abstract methods then that class is also considereda as abstract class
- We can't create instance of Interface or any Abstract class
"""

from abc import ABC, abstractmethod


class Father(ABC):   # Father class here is treated as Interface, since it doesnot contain any concrete method
    @abstractmethod
    def fun1(self):
        pass

    @abstractmethod
    def fun2(self):
        pass


class Son(Father):   # Son class is considered as Abstract class since it doesnot define the fun2 method
    def fun1(self):
        print("I am fun1 method..")

class GrandSon(Son):   # GrandSon is not Abstract class, it is simple class
    def fun2(self):
        print("I am fun2 method...")


if __name__ == "__main__":
    g = GrandSon()
    g.fun1()
    g.fun2()