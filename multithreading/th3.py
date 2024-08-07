"""

set and get thread name
"""

from threading import Thread, current_thread

def custom_thread():
    pass

def thread_demo(x):
    print(f"The number is : {x}")
    # print(current_thread().name)
    # current_thread().setName("New_Thread") # dpricated
    current_thread().name = "new_thread"
    print(current_thread().name)


if __name__ == "__main__":
    print("Starting current thread..")
    # t = Thread(target=thread_demo, args=(10,))
    # print(t.name)
    # t.name = "changed_thread"
    # print(t.name)
    # t.start()

    t2 = Thread(target=custom_thread, name="Rajon_Thread")
    print(t2.name)
    t2.start()

    print("Main Thread..")
    print(current_thread().name)

