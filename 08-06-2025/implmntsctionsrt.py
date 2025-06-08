
# Implement the selection sort

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_indx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_indx]:
                min_indx = j

        arr[i], arr[min_indx] = arr[min_indx], arr[i]

    return arr

arr = [29, 10, 14, 37, 13]

sorted_arr = selection_sort(arr)

print("Sorted Array: ", sorted_arr)