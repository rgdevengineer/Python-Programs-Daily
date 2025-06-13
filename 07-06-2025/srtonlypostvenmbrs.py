
'''
Sort Only Positive Numbers in List, Keep Negatives in Place
Problem:
Sort only positive numbers in the list using Bubble Sort and leave negative numbers in their original positions.
Input: [3, -1, 2, -4, 1]  
Output: [1, -1, 2, -4, 3]
'''

def bubble_sort_positives_only(arr):
    indices = [i for i in range(len(arr)) if arr[i] >= 0]
    for i in range(len(indices)):
        for j in range(len(indices) - i - 1):
            if arr[indices[j]] > arr[indices[j + 1]]:
                arr[indices[j]], arr[indices[j + 1]] = arr[indices[j + 1]], arr[indices[j]]
    return arr

print(bubble_sort_positives_only([3, -1, 2, -4, 1]))
