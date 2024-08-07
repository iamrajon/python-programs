"""
math functions and string slicing in python
->slicing = creating a substring by extracting elements from another stirng.
-> indexing[], and slice()
-> [start:stop:step]
"""

import math

pi = 3.14
num = 4

# print(round(pi))
# print(math.ceil(pi)) # prints upper bound value
# print(math.floor(pi)) # prints the lower bound value
# print(abs(pi))
# print(pow(num, 2))
# print(math.sqrt(num))
# print(max(2, 3, 4))
# print(min(4, 5, 6))

# via indexing
name = "Miles Chaudhary"
# print(name[::-1])
# first_name = name[:5]
# last_name = name[6:]
# funky_name = name[::2]  # it prints string by removing every second char after printing and also includes the first character
# reversed_name = name[::-1]
# print(reversed_name)

# via slice() function
link1 = 'https://google.com'
link2 = 'https://wikipedia.com'

domain = slice(8, -4)
print(link1[domain])
print(link2[domain])

