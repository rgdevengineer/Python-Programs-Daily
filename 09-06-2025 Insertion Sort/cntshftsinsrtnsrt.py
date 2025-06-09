
'''
Count how many shifts are made during insertion sort
Input: [2, 1, 3, 1, 2]
Output: 4 (number of element movements)
'''

def insertion_sort_count_shift(arr):
    shifts = 0
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1

        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            shifts += 1
            j -= 1

        arr[j+1] = temp

    return shifts

arr = [2, 1, 3, 1, 2]

print("Number of element movements = ", insertion_sort_count_shift(arr))


