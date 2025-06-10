
'''
Quick Sort on Even and Odd Partition
Input: [7, 2, 9, 4, 6, 3]
Output: Sort even and odd parts separately.

Even: [2, 4, 6] → [2, 4, 6]
Odd: [7, 9, 3] → [3, 7, 9]
Final: [2, 4, 6, 3, 7, 9]
'''

lst = [7, 2, 9, 4, 6, 3]

even_lst = [item for item in lst if item % 2 == 0]
odd_lst = [item for item in lst if item % 2 != 0]

print("Even = ", even_lst)
print("Odd = ", odd_lst)

def quick_sort(even_lst):
    if len(even_lst) <= 1:
        return even_lst
    else:
        pivot = even_lst[0]
        lesser = [item for item in even_lst[1:] if item <= pivot]
        greater = [item for item in even_lst[1:] if item > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)
    
new_even = quick_sort(even_lst)
#print(new_even)

def quick_sort(odd_lst):
    if len(odd_lst) <= 1:
        return odd_lst
    else:
        pivot = odd_lst[0]
        lesser = [item for item in odd_lst[1:] if item <= pivot]
        greater = [item for item in odd_lst[1:] if item > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

new_odd = quick_sort(odd_lst)
#print(new_odd)

new_lst = new_even + new_odd

print("Final = ", new_lst)