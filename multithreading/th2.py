
# creating thread without creating class

from threading import Thread


def test_thread(num):
    print("Starting thread..")
    for x in range(1, 11):
        print(f"{num} * {x} = {num*x}")


# def test_thread_two(num):
#     print("Thread Running..", num)


if __name__ == "__main__":
    t = Thread(target=test_thread, args=(10,))
    t.start()

    for _ in range(1, 11):
        print("Main Thread..")

    # for i in range(5):
    #     t = Thread(target=test_thread_two, args=(i,))
    #     t.start()