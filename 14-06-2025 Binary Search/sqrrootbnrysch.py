
'''
Square Root (Floor) Using Binary Search
Problem:
Return the integer part (floor) of the square root of a non-negative number.

Input: x = 10  
Output: 3 (because 3² = 9 and 4² = 16)
'''

def floor_sqrt(x):
    if x < 2:
        return x
    
    low, high = 1, x
    answer = 0

    while low <= high:
        mid = (low + high) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer

print(floor_sqrt(16))
print(floor_sqrt(10))
print(floor_sqrt(0))
print(floor_sqrt(99))
