

# key = lambda x : x

# first approack
def quick_sort(numlist):
    if len(numlist) <=1:
        return numlist
    else:
        pivot = numlist[0]
        lesser = [x for x in numlist[1:] if x < pivot]
        greater = [x for x in numlist[1:] if x > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)
    
# second approach
def quick_sort_two(datalist):
    if len(datalist) <=1:
        return datalist;
    else:
        pivot = datalist[len(datalist) // 2]
        left = [x for x in datalist if x > pivot]
        middle = [x for x in datalist if x == pivot]
        right = [x for x in datalist if x < pivot]
        return quick_sort_two(left) + middle + quick_sort_two(right)
    

if __name__ == "__main__":
    numlist = [53, 12, 34, 76, 41, 18, 80, 75, 99, 100]
    print(f"Unsorted List: {numlist}")

    # sorted_list = quick_sort(numlist)
    # print(f"Sorted List: {sorted_list}")

    # print(key(5))

    res = quick_sort_two(numlist)
    print("sorted list: ", res)

