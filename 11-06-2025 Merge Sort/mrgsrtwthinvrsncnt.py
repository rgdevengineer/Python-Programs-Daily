
'''
Count Inversions in an Array
Input: [2, 4, 1, 3, 5]
Output: 3
(Inversions: (2,1), (4,1), (4,3))
Goal: Count how many pairs (i, j) exist such that i < j and arr[i] > arr[j].
'''

def merge_sort_and_count(lst):
    return _merge_sort(lst, 0, len(lst)-1)

def _merge_sort(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += _merge_sort(arr, left, mid)
        inv_count += _merge_sort(arr, mid + 1, right)
        inv_count += merge_and_count(arr, left, mid, right)
    return inv_count

def merge_and_count(arr, left, mid, right):
    left_part = arr[left:mid+1]
    right_part = arr[mid+1:right+1]
    i = j = 0
    k = left
    inv_count = 0

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
            inv_count += len(left_part) - i
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

    return inv_count
