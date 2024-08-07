
"""
demo of multiple inheritance in python programming language

"""


class Father(object):
    f_money = 50000
    def __init__(self):
        super().__init__()
        self.money = 50000
        print("Father class constructor..")

    def check(self):
        print("I am father..")

    @classmethod
    def show_father(cls):
        print(f"Father has total balance: {cls.f_money}")


class Mother(object):
    m_money = 30000
    def __init__(self):
        super().__init__()
        self.money = 30000
        print("Mother class Constructor..")

    def check(self):
        super().check()
        print("I am mother..")

    @classmethod
    def show_mother(cls):
        print(f"Mother has total balance: {cls.m_money}")


class Child(Mother, Father):
    def __init__(self):
        super().__init__()
        self.money = 10000
        print("child calss constructor..")

    def check(self):
        super().check()
        print("I am child")

    def show_child(self):
        print(f"child has total balance of : {self.money}")


if __name__ == "__main__":
    child = Child()
    child.check()
    print(Child.mro())
    # child.show_child()
    # child.show_father()
    # child.show_mother()
