
'''
Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.
Examples:
Input: nums = [0, 2, 3, 1, 4]
Output: 5
Explanation: nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]
Input: nums = [0, 1, 2, 4, 5, 6]
Output: 3
Explanation: nums contains 0, 1, 2, 4, 5, 6 thus leaving 3 as the only missing number in the range [0, 6]
'''

class Solution:
    def missingNumber(self, nums):
        n = len(nums)  # Get the number of elements
        xor1 = 0
        xor2 = 0
        
        for i in range(n):      # XOR all array elements
            xor1 ^= nums[i]
                               
        for i in range(n + 1):    # XOR all numbers from 0 to n
            xor2 ^= i

        return xor1 ^ xor2    # The missing number is the XOR of xor1 and xor2

solution = Solution()

# Test Case 1
nums1 = [0, 2, 3, 1, 4]
print("Test 1 Expected: 5 | Got:", solution.missingNumber(nums1))

# Test Case 2
nums2 = [0, 1, 2, 4, 5, 6]
print("Test 2 Expected: 3 | Got:", solution.missingNumber(nums2))

# Test Case 3
nums3 = [1, 2, 3, 4, 5, 6]
print("Test 3 Expected: 0 | Got:", solution.missingNumber(nums3))

# Test Case 4
nums4 = [0, 1, 2, 3, 5, 6]
print("Test 4 Expected: 4 | Got:", solution.missingNumber(nums4))

# Test Case 5
nums5 = [0]
print("Test 5 Expected: 1 | Got:", solution.missingNumber(nums5))

# Test Case 6
nums6 = [1]
print("Test 6 Expected: 0 | Got:", solution.missingNumber(nums6))

# Test Case 7
nums7 = [0, 1, 3]
print("Test 7 Expected: 2 | Got:", solution.missingNumber(nums7))
