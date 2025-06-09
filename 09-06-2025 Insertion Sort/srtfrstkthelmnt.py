
'''
Sort the first k elements of an array using insertion sort
Input: arr = [9, 8, 7, 5, 2, 10], k = 4

Output: [5, 7, 8, 9, 2, 10]
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

lst = [9, 8, 7, 5, 2, 10]

# lst1 = lst[:4] # because k = 4
# lst2 = lst[4:]

new_lst = insertion_sort(lst[:4])

print(new_lst)

sorted_list = new_lst + lst[4:]

print(sorted_list)

