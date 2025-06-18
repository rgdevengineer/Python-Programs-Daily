
'''
Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.
Examples:
Input: nums = [8, 8, 7, 6, 5]
Output: 7
Explanation: The largest value in nums is 8, the second largest is 7
Input: nums = [10, 10, 10, 10, 10]
Output: -1
Explanation: The only value in nums is 10, so there is no second largest value, thus -1 is returned
'''

class Solution:        # defines a class named Solution
    def secondLargestElement(self, arr):  # defines a method called largestElement inside the Solution class
        if not arr:        # This line checks if the array is empty
            raise ValueError("Array is Empty")   ## If the array is empty, raise a ValueError with a custom message
        
        largest = max(arr)
        second_largest = float('-inf')  ## Initialize second_largest to negative infinity.

        for num in arr:
            if num != largest and num > second_largest:
                second_largest = num
        
        return second_largest if second_largest != float('-inf') else -1  # If second_largest was never updated, return -1

# Manual Testing

if __name__ == "__main__":
    sol = Solution()
    print(sol.secondLargestElement([3, 3, 6, 1]))
    print(sol.secondLargestElement([3, 3, 0, 99, -40]))
    print(sol.secondLargestElement([-5, -1, -10]))
    print(sol.secondLargestElement([10, 10, 10]))         
    print(sol.secondLargestElement([-2, -2, -2]))