
# Check if a given number x exists in the list.

def exists_recursively(arr, x, index):
    if index == len(arr):
        return False
    return arr[index] == x or exists_recursively(arr, x, index + 1)

print(exists_recursively([1, 3, 5, 7, 9], 5, 0))
print(exists_recursively([1, 3, 5, 7, 9], 2, 0))