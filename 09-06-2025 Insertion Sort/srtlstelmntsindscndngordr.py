
'''
 Sort a list in descending order using insertion sort
Input: [4, 9, 1, 7]

Output: [9, 7, 4, 1]
'''
def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        temp = lst[i]

        j = i-1
        while j >= 0 and temp > lst[j]:
            lst[j+1] = lst[j]
            j = j-1

        lst[j+1] = temp

    return lst

lst = [4, 9, 1, 7]
sorted_lst_dscndng = insertion_sort(lst)
print(lst)