"""
creating thread without inheriting the Thread class
"""

from threading import Thread


class MyThread:
    def disp(self, x , y):
        print(f"The sum is: {x+y}")



if __name__ == "__main__":
    t = MyThread()
    thread = Thread(target=t.disp, args=(12, 14), name="sumthread")
    thread.start()
    print("Name of thread is: ", thread.name)