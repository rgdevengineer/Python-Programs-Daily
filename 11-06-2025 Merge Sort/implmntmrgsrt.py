
# Implement the merge sort algorithm

def merge_sort(lst):
    if len(lst)>1:
        mid=len(lst)//2 # floor division because we always need a integer value after dividing the list length
        leftlst = lst[:mid]
        rightlst = lst[mid:]

        merge_sort(leftlst)
        merge_sort(rightlst)

        i=j=k=0
        while i<len(leftlst) and j<len(rightlst):
            if leftlst[i]<rightlst[j]:
                lst[k]=leftlst[i]
                i+=1
            else:
                lst[k]=rightlst[j]
                j+=1
            k+=1
        while i<len(leftlst):
            lst[k]=leftlst[i]
            i+=1
            k+=1
        while j<len(rightlst):
            lst[k]=rightlst[j]
            j+=1
            k+=1

my_list = [75,29,83,42,16,90,56,34,20,71,88,92,7]
merge_sort(my_list)
print(my_list)