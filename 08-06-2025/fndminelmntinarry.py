
# Find Minimum Using Selection Sort Logic
'''
Without using the min() function, find the smallest element in a list by modifying selection sort logic.

Example Input: [8, 4, 6, 2, 7]
Expected Output: 2
'''
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_indx = i

        for j in range(i+1, n):
            if arr[j] < arr[min_indx]:
                min_indx = j

        arr[i], arr[min_indx] = arr[min_indx], arr[i]

    return arr

arr = [8, 4, 6, 2, 7]

sorted_arr = selection_sort(arr)

print("Sorted Array: ", sorted_arr)

print("Smallest element = ", sorted_arr[0])