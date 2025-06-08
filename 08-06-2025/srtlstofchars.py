
'''
Given a list of single lowercase characters, sort them alphabetically using selection sort.

Example Input: ['d', 'a', 'c', 'b']
Expected Output: ['a', 'b', 'c', 'd']
'''

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_indx = i

        for j in range(i + 1, n):
            if ord(arr[j]) < ord(arr[min_indx]):
                min_indx = j

        arr[i], arr[min_indx] = arr[min_indx], arr[i]

    return arr

arr = ['d', 'a', 'c', 'b']

sorted_arr = selection_sort(arr)

print("Sorted Array: ", sorted_arr)