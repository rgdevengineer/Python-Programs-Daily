
# Sort List in Descending Order

'''
Modify selection sort to sort an array of integers in descending order.

Example Input: [10, 40, 20, 5]
Expected Output: [40, 20, 10, 5]
'''

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_indx = i
        
        for j in range(i + 1, n):
            if arr[j] > arr[min_indx]:
                min_indx = j

        arr[i], arr[min_indx] = arr[min_indx], arr[i]

    return arr

arr = [10, 40, 20, 5]

sorted_arr = selection_sort(arr)

print("Sorted Array: ", sorted_arr)