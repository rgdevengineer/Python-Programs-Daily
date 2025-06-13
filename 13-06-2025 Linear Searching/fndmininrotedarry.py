
'''
Given a rotated sorted array with no duplicates, find the minimum element.

Input: [4, 5, 6, 7, 0, 1, 2]
Output: 0
'''

def find_min(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return arr[low]

print(find_min([4, 5, 6, 7, 0, 1, 2]))
