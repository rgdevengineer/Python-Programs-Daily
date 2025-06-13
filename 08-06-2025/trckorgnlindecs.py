
'''
Track Original Indices After Selection Sort
Problem:
Sort the array using Selection Sort and return the original indices of the sorted elements.

Input: [40, 10, 20]
Sorted: [10, 20, 40]
Original indices: [1, 2, 0]
'''

def selection_sort_with_indices(arr):
    indexed = list(enumerate(arr))  # [(0, 40), (1, 10), (2, 20)]
    n = len(indexed)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if indexed[j][1] < indexed[min_idx][1]:
                min_idx = j
        indexed[i], indexed[min_idx] = indexed[min_idx], indexed[i]

    sorted_arr = [x[1] for x in indexed]
    original_indices = [x[0] for x in indexed]
    return sorted_arr, original_indices

print(selection_sort_with_indices([40, 10, 20]))
