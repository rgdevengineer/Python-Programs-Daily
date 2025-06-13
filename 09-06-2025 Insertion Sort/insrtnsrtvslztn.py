
'''
Print the list after each pass of the insertion sort to visualize how it changes step by step.

Input: [8, 5, 3]
Output:
Pass 1: [5, 8, 3]
Pass 2: [3, 5, 8]
'''

def insertion_sort_visual(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Pass {i}: {arr}")

insertion_sort_visual([8, 5, 3])
