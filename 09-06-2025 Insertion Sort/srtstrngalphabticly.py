
'''
 Sort strings alphabetically using insertion sort
Input: ["banana", "apple", "grape"]

Output: ["apple", "banana", "grape"]
'''

def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]

        j = i-1
        while j >= 0 and temp < lst[j]:
            lst[j+1] = lst[j]
            j = j-1

        lst[j+1] = temp

    return lst

lst = ["banana", "apple", "grape"]

sorted_lst = insertion_sort(lst)

print(sorted_lst)
