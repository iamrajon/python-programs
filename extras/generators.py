"""
A generator is a special type of function that returns an iterator. Unlike regular functions that return a single value and then terminate, generators can yield multiple values over time. This means that the generator function can pause its execution and resume it later, allowing for efficient memory usage and lazy evaluation.

"""


def count_generator(max):
    count = 1
    while count <= max:
        yield count
        count += 1



# creating a generator object
gen_obj = count_generator(10)
# print(next(gen_obj))  # output: 1
# print(next(gen_obj))  # output: 2
# print(next(gen_obj))  # output 3


# iterating over loop
# for num in count_generator(10):
#     print(num)


"""
Generators can also be created using generator expressions, which are similar to list comprehensions but with parentheses instead of square brackets:
- Generators return an object generator class
"""

table = (10 * x for x in range(1, 11))
# print(table)
print(type(table))

for num in table:
    print(num)


"""
list comprehension
-List Comprehension returns a new list
"""
print("-----")
table2 = [2*x for x in range(1, 11)]
# print(table2)
for num in table2:
    print(num)
