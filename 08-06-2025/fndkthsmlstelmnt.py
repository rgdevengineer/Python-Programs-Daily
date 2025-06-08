
# Find the Kth Smallest Element
'''
Use selection sort to find the Kth smallest element in a list.

Example Input: arr = [7, 10, 4, 3, 20, 15], k = 3
Expected Output: 7 (3rd smallest)
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

arr = [7, 10, 4, 3, 20, 15]

sorted_arr = selection_sort(arr)

print("Sorted Array: ", sorted_arr)

print("kth element = ", sorted_arr[2])
