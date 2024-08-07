"""
Array in python: for using array in python we have to import array module
-> 'i' is unicode which specifies the type integer for elements of array
-> for array of float numbers we have to write f before array list
"""

# import array
from array import *

# stu_roll = array.array("i", [101, 102, 103, 104, 105, 106, 107, 108])
#
# print(type(stu_roll))
# print(stu_roll[3])

# stu_roll = array('i', [101, 102, 103, 104, 105, 106, 107, 108])
# print(type(stu_roll))
# print(stu_roll[3])
#
# stu_marks = array('f', [88.9, 76.23, 65.98, 92.12, 76.77, 79, 87])
# print(stu_marks[4])
# print(stu_marks[5])
"""
if unicode is 'f' then it converts all integer values into float if exist.
but if unicode is 'i' and contains float value then it cannot convert float values into integer
instead it gives error at that situation
"""


# Accessing array using for loop
product_id = array('i', [101, 102, 103, 104, 107, 109, 112, 124, 128])

# for element in product_id:
#     print(element)

# accessing array elements with index number
# n = len(product_id)
# print(f"The length of array is: {n}")
#
# for i in range(n):
#     # print(product_id[i])
#     print(i, "->", product_id[i])


# multiplication table in python

num = int(input("Enter number whose table you want:?"))

print(f"The multiplication table of {num} is:")
for i in range(1, 11):
    print(f"{num} * {i} = {num*i}")
