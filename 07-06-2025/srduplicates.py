
#  Sort a list with duplicates
# Sort this list using Bubble Sort: [4, 2, 4, 3, 1]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort(4,2,4,3,1))