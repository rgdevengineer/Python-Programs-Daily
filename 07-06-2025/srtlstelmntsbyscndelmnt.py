
'''
Given a list of tuples, sort it using Bubble Sort based on the second element of each tuple.

Input: [(1, 3), (2, 2), (3, 1)]  
Output: [(3, 1), (2, 2), (1, 3)]
'''

def bubble_sort_by_second_element(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort_by_second_element([(1, 3), (2, 2), (3, 1)]))
