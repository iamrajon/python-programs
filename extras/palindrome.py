"""
To check the given number is palindrome is or not
"""

def is_palindrome(num):

    num_str = str(num)
    num_str_rev = num_str[::-1]

    return num_str == num_str_rev
    

def is_palindrome_number(num):
    
    num_str = str(num)
    
    left = 0
    right = len(num_str) - 1
    
    while left < right:
        if num_str[left] != num_str[right]:
            return False
            
        left += 1
        right -= 1
        
    return True
    
    
if __name__ == "__main__":
    num = int(input("Enter a Number: "))
    
    # res = is_palindrome_number(num)
    res = is_palindrome(num)
    if res:
        print(f"The number {num} is a palindrome.")
    else:
        print("The number ", num , " is not a palindrome.")




