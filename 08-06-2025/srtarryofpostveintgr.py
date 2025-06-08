
'''
Write a function that takes a list of positive integers and returns it sorted in ascending order using selection sort.

Example Input: [7, 3, 5, 2, 9]
Expected Output: [2, 3, 5, 7, 9]
'''

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_indx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_indx]:
                min_indx = j

        arr[i], arr[min_indx] = arr[min_indx], arr[i]

    return arr

arr = [7, 3, 5, 2, 9]

sorted_arr = selection_sort(arr)

print("Sorted Array: ", sorted_arr)