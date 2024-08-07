

class Father:
    money = 50000

    def disp(self):
        print("I am Father class Instance Method..")

    @classmethod
    def show_money(cls):
        print("I am classmethod of Father class", cls.money)

    @staticmethod
    def stat():
        print("I am Father class static method")


class Son(Father):
    def __init__(self):
        self.money = 10000

    def show_son_money(self):
        print("I am Son class Instance method.", self.money)



if __name__ == "__main__":
    son1 = Son()
    
    # Accessing Father class properties through son class instance
    print(super(Son, son1).money)
    # son1.disp()
    # son1.show_money()
    # son1.stat()

    # Accessing son class properties through son class instance
    # print(son1.show_son_money())
    print(son1.money)

    # Accessing Father class static method through son class
    # Son.stat()

    # Accessing Father class variable via father class
    print(Father.money)