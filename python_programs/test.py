
# find the max and min and second max value from given list

def find_max(numbers):
    if not numbers:
        return None
    elif len(numbers) == 0:
        return "List is empty to no max value"
    else:
        max_value = max(numbers)
        return max_value

def find_min(numbers):
    if not numbers:
        return None
    elif len(numbers) == 0:
        return "List is empty so no min value to print"
    else:
        min_value = min(numbers)
        return min_value

def find_second_max(numbers):
    if len(numbers) < 2:
        return None
    max_value = max(numbers)
    numbers.remove(max_value)
    second_max = max(numbers)
    return second_max


l = [12, 13, 14, 15, 16, 17]
# l=[]
max_value = find_max(l)
min_value = find_min(l)
second_max = find_second_max(l)


print(f"max is: {max_value} min is: {min_value} second_max is: {second_max}")
# print(f"l: {l}")




