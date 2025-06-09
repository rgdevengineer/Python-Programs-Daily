
'''
Sort a given list of integers in ascending order
Input: [7, 2, 5, 3, 8]

Output: [2, 3, 5, 7, 8]
'''
def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        temp = lst[i]

        j = i-1
        while j >= 0 and temp < lst[j]:
            lst[j+1] = lst[j]
            j = j-1

        lst[j+1] = temp

    return lst

lst = [7, 2, 5, 3, 8]
sorted_lst_ascndng = insertion_sort(lst)
print(lst)