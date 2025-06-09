
'''
Check if a list is already sorted using insertion sort logic
Input: [1, 2, 3, 4, 5]

Output: True (No shifts needed)
'''

def insertion_sort_check(lst):
    for i in range(1, len(lst)):
        check = lst[i]
        j = i - 1

        if check < lst[j]:
            return False
        
        else:
            return True
        
lst = [1, 2, 3, 4, 5]
print(insertion_sort_check(lst))