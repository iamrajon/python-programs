

nums = [1, 2, 3, 4, 5]
squared_nums = []

# for num in nums:
#     square = (num**2)
#     if square > 10:
#         squared_nums.append(square)

# print(f"Squared list is: {squared_nums}")


# using walrus operator

# for num in nums:
#     if(square := num**2) >10:
#         squared_nums.append(square)
#
# print(f"Squared list is: {squared_nums}")

"""
list comprehension
"""
# new_list = [square for num in nums if(square := num**2) > 10]
# print(f"new list: {new_list}")