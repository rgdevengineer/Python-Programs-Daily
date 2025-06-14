
'''
Search for all occurrences of a number in a list, and replace them with another number using recursion.
'''
def search_and_replae(arr, old, new, index=0):
    if index == len(arr):
        return arr
    if arr[index] == old:
        arr[index] = new
    return search_and_replae(arr, old, new, index + 1)

print(search_and_replae([1, 2, 2, 3, 2], 2, 10))