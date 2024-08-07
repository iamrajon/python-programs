"""
In Python, a thread is a separate flow of execution. This means that your program will have two things happening at once. Threads are a lighter form of multiprocessing and are used to perform multiple operations concurrently in a single process.
"""


import threading


print("Thread in python part one")


# t = threading.current_thread().getName()
t = threading.current_thread()

print(f"Current Thread is: {t} -- type({t})")  # instance of Main Thread
print(f"Current Thread Name is: {t.name}")