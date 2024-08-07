""""
creating thread by inheriting Thread class
"""


from threading import Thread, current_thread


class MySecondThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("I am contructor in MySecondThread class..")

    def run(self):
        for _ in range(5):
            print("I am child Thread..")


class MyThread(Thread):
    def run(self):
        # print("I am overriden run method in MyThread class..")
        for _ in range(5):
            print("I am child Thread..")



if __name__ == "__main__":
    # t1 = MyThread()
    # t1.start()
    # print(t.name)
    # t1.name = "MyOwnThread"
    # print(t.name)
    # t1.join()

    # Main Thread
    # print(current_thread().name)  

    t2 = MySecondThread()
    t2.start()
    print(t2.name)

    for _ in range(5):
        print("I am Main Thread..")



