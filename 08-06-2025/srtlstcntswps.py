
# Sort and Count Swaps
'''
Use selection sort to sort a list and also count how many swaps it took.

Example Input: [5, 3, 4, 1]
Expected Output: Sorted List + Number of swaps
'''

def selection_sort_with_swaps(arr):
    n = len(arr)
    swap_count = 0

    for i in range(n):
        min_indx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_indx]:
                min_indx = j

        if min_indx != i:
            arr[i], arr[min_indx] = arr[min_indx], arr[i]
            swap_count += 1

    return arr,swap_count

arr = [5, 4, 3, 2, 1]

sorted_arr, swaps = selection_sort_with_swaps(arr)

print("Sorted Array = ", sorted_arr)
print("Total Number of swaps = ", swaps)


