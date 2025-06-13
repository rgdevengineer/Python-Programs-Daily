
'''
Find the smallest element greater than or equal to target.

arr = [1, 2, 8, 10, 10, 12, 19]
target = 5
Output: 8
'''

def find_ceiling(arr, target):
    low, high = 0, len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            ans = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ans

print(find_ceiling([1, 2, 8, 10, 10, 12, 19], 5))  
