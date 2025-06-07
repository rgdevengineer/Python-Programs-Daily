
# Bubble Sort in Descending Order
# Modify Bubble Sort to sort in descending order

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j+1] > arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort_desc([10,19,23,76,12]))
