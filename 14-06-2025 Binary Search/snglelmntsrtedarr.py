
'''
In a sorted array where every element appears twice except one, find that one.

Input: arr = [1,1,2,2,3,4,4,5,5]  
Output: 3
'''

def single_element(num):
    low, high = 0, len(num) - 1
    
    while low < high:
        mid = (low + high) // 2

        if mid % 2 == 1:
            mid = mid -1

        if num[mid] == num[mid + 1]:
            low = mid + 2

        else:
            high = mid

    return num[low]

Signle_Element = single_element([1,1,2,2,3,3,4,5,5,6,6,7,7])

print(Signle_Element)