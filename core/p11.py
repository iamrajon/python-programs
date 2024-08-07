"""
dictionary = A changeable, unordered collection of unique key: value pairs.
-> it is fast because dictionary uses hashing, allow us to access a value quickly
"""

capitals = {
    'USA': 'washington DC',
    'India': 'New Delhi',
    'China': 'Beijing',
    'Nepal': 'Kathmandu',
}

# print(capitals)
# print(capitals['China'])

# for x in capitals:
#     print(x.upper())  # it prints all keys only not values

# for key,values in capitals.items():
#     print(key, values)

#
# print(f"The list of keys of capitals: {capitals.keys()}")
# print(f"The list of values of capitals: {capitals.values()}")
# print(capitals.items())

# print(capitals['Germany'])  # it will give error
# print(capitals.get('Germany'))
# print(capitals.get('Nepal'))

# capitals.update({'Germany': 'Berlin'})
# capitals.update({'USA': 'Las Vegas'})
# capitals.pop('China')
# capitals.clear()
print(capitals)