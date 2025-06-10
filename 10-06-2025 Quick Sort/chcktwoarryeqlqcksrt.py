
'''
Check if Two Arrays are Equal After Sorting
Input: arr1 = [1, 2, 3], arr2 = [3, 2, 1]
Output: True
'''
def quick_sort(arr1):
    if len(arr1) <= 1:
        return arr1
    else:
        pivot1 = arr1[0]
        lesser1 = [x for x in arr1[1:] if x <= pivot1]
        greater1 = [x for x in arr1[1:] if x > pivot1]
        return quick_sort(lesser1) + [pivot1] + quick_sort(greater1)
    
def quick_sort(arr2):
    if len(arr2) <= 1:
        return arr2
    else:
        pivot2 = arr2[0]
        lesser2 = [x for x in arr2[1:] if x <= pivot2]
        greater2 = [x for x in arr2[1:] if x > pivot2]
        return quick_sort(lesser2) + [pivot2] + quick_sort(greater2)

arr1 = [1, 2, 3]
my_arr1 = quick_sort(arr1)
print(my_arr1)
arr2 = [3, 2, 1]
my_arr2 = quick_sort(arr2)
print(my_arr2)

if (my_arr1 == my_arr2):
    print("True")
else:
    print("False")