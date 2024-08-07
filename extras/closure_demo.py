"""
A closure in Python is a function object that has access to variables in its lexical scope, even when the function is called outside that scope. This means that a closure "remembers" the environment in which it was created.

In simpler terms, it's a function that has access to variables from its outer scope, even after the outer function has finished executing.

"""

def outer_function(num1):
    def inner_function(num2):
        return num1 + num2
    return inner_function



if __name__ == "__main__":
    my_closure = outer_function(10)  # here my_closure is a closure which has access of num1 from the outer function.
    # print(my_closure)
    print(type(my_closure))


    res = my_closure(5)
    print(f"sum is: {res}")