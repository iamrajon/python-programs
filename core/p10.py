"""
tuple = collection which is ordered and unchangeable used to group together related data
-> tuple is immutable
"""

# student = ("Rajon", 22, "male")
# count = student.count("Rajon")
# index = student.index("male")
# print(f"count of 'Rajon' in tuple is {count} and index of 'male' in tuple is {index}")
#
# for x in student:
#     print(x)
#
# if "Rajon" in student:
#     print("Rajon is inside tuple")


job = ("web development", "cloud computing")
# print(job.count("web development"))
# print(job)
# job[0] = "app development"  # it gives error which proves tuple is immutable
# print(job[0])


"""
set = collection which is unordered, un-indexed.
-> it does not allow duplicate values

"""

utensils = {"fork", "spoon", "knife", "knife", "Knife"}
dishes = {"bowl", "plate", "cup", "fork"}

# for x in utensils:
#     print(x)

# utensils.add("napkin")
# print(utensils)

# utensils.remove("Knife")
# print(utensils)

# utensils.clear()
#
# if len(utensils) == 0:
#     print("set is empty")
# else:
#     print(utensils)

# utensils.update(dishes)
# dishes.update(utensils)

# print(utensils)
# print(dishes)

# dinner_table = utensils.union(dishes)
# for x in dinner_table:
#     print(x)

# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))