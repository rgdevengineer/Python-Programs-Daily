
'''
Find any one peak element (greater than its neighbors) in an array.
Array may not be sorted.
arr = [1, 3, 20, 4, 1, 0]
Output: 20 (index 2)
'''

def find_peak(arr):
    n = len(arr)
    for i in range(n):
        if (i == 0 or arr[i] >= arr[i-1]) and (i == n-1 or arr[i] >= arr[i+1]):
            return arr[i]
    return -1

print(find_peak([1, 3, 20, 4, 1, 0]))  
