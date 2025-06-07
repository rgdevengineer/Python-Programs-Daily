
# Optimize Bubble Sort to stop early if the list is already sorted.

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        flag = False
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            break
    return arr
print(optimized_bubble_sort([1,2,3,4,5]))
