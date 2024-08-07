"""
list = used to store multiple items of different data types in a single variable
-> list is mutable i.e items of list can be changed dynamically
"""

food = ["pizza", "burger", "hotdog", "momos"]
food[3] = "Biryani"

# print(food)
# print(type(food))
# print(food[0])
# print(food[3])

# iterating over list through loop
# for f in food:
#     print(f)


# some methods of list
# food.append("ice cream")
# food.remove("burger")
# food.pop()
# food.sort()
# food.clear()
# print(food)


"""
2D List = a list of lists 
multi dimension list
"""

drinks = ['coffee', 'soda', 'tea']
dinner = ['pizza', 'hamburger', 'hotdog']
dessert = ['cake', 'ice cream']

food = [drinks, dinner, dessert]
print(food)
print(type(food))
print(food[0][1])

# iterating through 2d list using for loop
for row in food:
    for element in row:
        print(element, end=",")


