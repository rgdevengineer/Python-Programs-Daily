
# Sort User Input
'''
Take input from the user as a comma-separated string of numbers, convert them to integers, and then sort using selection sort.

Example Input: "34,12,5,66,1"
Expected Output: [1, 5, 12, 34, 66]
'''
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_indx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_indx]:
                min_indx = j

        arr[i], arr[min_indx] = arr[min_indx], arr[i]

    return arr
'''
arr = list(map(int, input("Enter number one by one seperated by space: ").split()))
print("Your Array = ", arr)
'''
input_str = input("Enter numbers seperated by commas: ")

arr = [int(num) for num in input_str.split(',')]

print("Array = ",arr)

sorted_array = selection_sort(arr)

print("Sorted Array = ",sorted_array)
