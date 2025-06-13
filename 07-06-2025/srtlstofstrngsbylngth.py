
'''
ort a list of strings based on length instead of lexicographical order.

Input: ["banana", "kiwi", "apple", "fig"]
Output: ["fig", "kiwi", "apple", "banana"]
'''

def bubble_sort_by_length(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort_by_length(["banana", "kiwi", "apple", "fig"]))
