
# Implement the Insertion Sorting

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]

        j = i-1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j- 1
        
        arr[j+1] = temp

    return arr

arr = [12,23,45,10,33,21] 
sorted_arr = insertion_sort(arr)
print(sorted_arr) 




        