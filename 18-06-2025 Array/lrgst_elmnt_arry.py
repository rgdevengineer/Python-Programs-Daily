
'''
Given an array of integers nums, return the value of the largest element in the array
Examples:
Input: nums = [3, 3, 6, 1]
Output: 6
Explanation: The largest element in array is 6
Input: nums = [3, 3, 0, 99, -40]
Output: 99
Explanation: The largest element in array is 99
'''

'''
class Solution:
    def largestElement(self, arr):
        largest = arr[0]
        for num in arr:
            if num > largest:
                largest = num
        return largest
    
Sol = Solution()
print(Sol.largestElement([3, 3, 6, 1]))
print(Sol.largestElement([3, 3, 0, 99, -40]))
'''

# The previous one was better but if I want to add testing then

# Adding Basic Manual Testing Now

class Solution:     # defines a class named Solution
    def largestElement(self, arr):   # defines a method called largestElement inside the Solution class
        if not arr:   # This line checks if the array is empty
            raise ValueError("Array is Empty")   # If the array is empty, raise a ValueError with a custom message
        largest = arr[0]
        for num in arr:
            if num > largest:
                largest = num
        return largest
        
# Manual Testing

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestElement([3, 3, 6, 1]))
    print(sol.largestElement([3, 3, 0, 99, -40]))
    print(sol.largestElement([-5, -1, -10]))
