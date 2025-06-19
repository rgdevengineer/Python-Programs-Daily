
'''
Check if an Array is Sorted
Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.
Note: Two consecutive equal values are considered to be sorted.
'''

def isSorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i-1]:  # checking if the array element has smaller value than its previous one
            return False
    return True

# Manual Testing

arr1 = [1, 2, 3, 4, 5]   # Test Case 1: Sorted in ascending order
print("Test Case 1:", isSorted(arr1, len(arr1)))  

arr2 = [1, 2, 2, 2, 3]  # Test Case 2: Sorted with equal elements (non-decreasing)
print("Test Case 2:", isSorted(arr2, len(arr2)))  

arr3 = [5, 3, 4, 2]    # Test Case 3: Not sorted
print("Test Case 3:", isSorted(arr3, len(arr3)))  

arr4 = [10]            # Test Case 4: Single element
print("Test Case 4:", isSorted(arr4, len(arr4)))  

arr5 = []              # Test Case 5: Empty array
print("Test Case 5:", isSorted(arr5, len(arr5)))  

arr6 = [7, 7, 7, 7]     # Test Case 6: All elements same
print("Test Case 6:", isSorted(arr6, len(arr6)))  

arr7 = [1, 2, 3, 2]     # Test Case 7: Last element smaller
print("Test Case 7:", isSorted(arr7, len(arr7)))  


