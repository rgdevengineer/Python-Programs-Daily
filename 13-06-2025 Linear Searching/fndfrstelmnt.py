
'''
Given an array of 0's followed by 1's, find the first index of 1.
Input: [0, 0, 0, 1, 1, 1]
Output: 3
'''

def first_one(arr):
    low, high = 0, len(arr)-1
    res = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == 1:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res

print(first_one([0, 0, 0, 1, 1, 1])) 
