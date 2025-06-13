
# Implement the binary search with an proper example 

def binary_search(arr, target):
    size = len(arr)

    start = 0
    end = size - 1

    while(start <= end):
        mid = (start + end)//2

        if(arr[mid]==target):
            return mid
        elif(arr[mid] > target):
            end = mid-1
        elif(arr[mid] < target):
            end = mid+1
    
    return -1

sorted_list = [10,22,37,49,54,68,75,81,99]
target = 54

result = binary_search(sorted_list, target)
print("The index of the target is = ",result)