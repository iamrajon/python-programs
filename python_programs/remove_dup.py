# python program to remove duplicate number from given list

def remove_duplicate(numlist):
    new_numlist = []
    for number in numlist:
        if number not in new_numlist:
            new_numlist.append(number)
    return new_numlist


initial_list = [12, 10, 6, 7, 5, 14, 2, 10, 7, 10, 18, 20, 21, 14]
result_list = remove_duplicate(initial_list)
print(f"The initial list: {initial_list}")
print(f"The final list with dup removed: {result_list}")
