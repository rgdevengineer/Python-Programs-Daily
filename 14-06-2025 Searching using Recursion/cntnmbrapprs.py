
# Count Number of Times an Element Appears

def count_occurences(arr, x, index):
    if index == len(arr):
        return 0
    count = 1 if arr[index] == x else 0
    return count + count_occurences(arr, x, index+1)

print(count_occurences([1, 2, 2, 3, 2, 4], 2, 0))
print(count_occurences([1, 2, 3, 4], 5, 0))