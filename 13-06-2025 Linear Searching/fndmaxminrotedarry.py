
'''
Find Maximum in Rotated Sorted Array (No Duplicates)
Input:  [4, 5, 6, 7, 0, 1, 2]
Output: 7
'''

def find_max_in_rotated(arr):
    low, high = 0, len(arr) - 1
    
    if arr[low] < arr[high]:
        return arr[high]
    
    while low <= high:
        mid = (low + high) // 2
        
        if mid < high and arr[mid] > arr[mid + 1]:
            return arr[mid]
        if mid > low and arr[mid] < arr[mid - 1]:
            return arr[mid - 1]
        
        if arr[mid] > arr[low]:
            low = mid + 1
        else:
            high = mid - 1

    return arr[0]  


print(find_max_in_rotated([4, 5, 6, 7, 0, 1, 2]))  
print(find_max_in_rotated([6, 7, 1, 2, 3, 4, 5]))  
print(find_max_in_rotated([1, 2, 3, 4, 5]))       