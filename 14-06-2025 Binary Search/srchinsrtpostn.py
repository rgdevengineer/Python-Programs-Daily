
'''
Search Insert Position
Description: Return the index 
where the target should be inserted to keep the array sorted.

Input: arr = [1, 3, 5, 6], target = 2  
Output: 1
'''
def binary_search_insert_position(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low

print(binary_search_insert_position([1, 3, 5, 7, 9], 2))