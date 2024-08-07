"""
for loop = a statement that will execute it's block of code a limited amount of time
while loop = unlimited
for loop = limited
"""

# import  time

#
# for i in range(10):
#     print(i+1)

# for i in "I am vengeance":
#     print(i)

# for i in range(10, 20, 2):
#     print(i)

# for seconds in range(5, 0, -1):
#     print(seconds)
#     time.sleep(1)
#
# print("Happy Birthday Rajon")


"""
nested for loops = The "inner loop" will finish all it's iteration before finishing one iteration of the "outer loop"
"""
# program to print pattern

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?" ))
# symbol = input("Enter symbol to be used?: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()


"""
loop control statements = change a loop execution from it's normal sequence
break = used to terminate the loop entirely
continue = skips to the next iteration of loop.
pass = does nothing, acts as a placeholder
"""

# while True:
#     name = input("Enter Your Name?: ")
#     if name != "":
#         break
#
# print(f"welcome mr. {name}")


# phone_number = "123-456-7890"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")


# i want to print 1 to 10 except 6 then pass is used
for i in range(1, 11):
    if i == 6:
        pass
    else:
        print(i, end=",")
