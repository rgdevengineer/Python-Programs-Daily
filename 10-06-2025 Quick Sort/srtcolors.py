
'''
Sort Colors (Dutch National Flag Problem)
Input: arr = [2, 0, 2, 1, 1, 0] (0: red, 1: white, 2: blue)
Output: [0, 0, 1, 1, 2, 2]
'''
'''
def quick_sort(arr1):
    if len(arr1) <= 1:
        return arr1
    else:
        pivot = arr1[0]
        lesser = [x for x in arr1[1:] if x <= pivot]
        greater = [x for x in arr1[1:] if x > pivot]
        return quick_sort(arr1) + [pivot] + quick_sort(arr1)

arr = [2, 0, 2, 1, 1, 0]
updated_arr = quick_sort(arr)
print(updated_arr)
'''

def sort_colors(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

arr = [2, 0, 2, 1, 1, 0]

output = sort_colors(arr)

print("Output:", arr)