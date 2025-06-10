
'''
Find the Kth Smallest Element
Input: arr = [7, 10, 4, 3, 20, 15], k = 3
Output: 7
'''

def quick_sort(list1):
    if len(list1) <= 1:
        return list1
    else:
        pivot = list1[0]
        lesser = [x for x in list1[1:] if x <= pivot]
        greater = [x for x in list1[1:] if x > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)
    
my_list = [7, 10, 4, 3, 20, 15]
my_list = quick_sort(my_list)
print(my_list)
print("Kth element = ", my_list[2])