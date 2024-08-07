# Normal Function
def add_two_nums(x, y):
    return x + y


add_nums = lambda x, y: x + y  # lambda function

idials = [12, 14, 16, 18, 20]

# def square(x):
#     return x**2


if __name__ == "__main__":
    # result = add_nums(12, 10)
    # result = add_two_nums(10, 12)
    # print(f"The sum of two numbers is: {result}")

    # suared_idials = list(map(square, idials))
    suared_idials = list(map(lambda x: x**2, idials))

    print(suared_idials)
