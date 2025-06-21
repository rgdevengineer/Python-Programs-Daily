
'''
Given an array of nums of n integers. Every integer in the array appears twice except one integer. Find the number that appeared once in the array.
Examples:
Input : nums = [1, 2, 2, 4, 3, 1, 4]
Output : 3
Explanation : The integer 3 has appeared only once.
Input : nums = [5]
Output : 5
Explanation : The integer 5 has appeared only once.
'''

class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result

# ----------- Manual Testing -----------
solution = Solution()

# Test Case 1: Only one element appears once
nums1 = [1, 2, 2, 4, 3, 1, 4]
print("Test 1 Expected: 3 | Got:", solution.singleNumber(nums1))

# Test Case 2: Single element in array
nums2 = [5]
print("Test 2 Expected: 5 | Got:", solution.singleNumber(nums2))

# Test Case 3: Negative numbers
nums3 = [7, -1, 7]
print("Test 3 Expected: -1 | Got:", solution.singleNumber(nums3))

# Test Case 4: Element at the end is unique
nums4 = [9, 8, 8, 9, 11]
print("Test 4 Expected: 11 | Got:", solution.singleNumber(nums4))

# Test Case 5: Element at the beginning is unique
nums5 = [15, 4, 4, 5, 5]
print("Test 5 Expected: 15 | Got:", solution.singleNumber(nums5))

# Test Case 6: All numbers large
nums6 = [99999, 88888, 99999]
print("Test 6 Expected: 88888 | Got:", solution.singleNumber(nums6))

# Test Case 7: Multiple duplicate pairs
nums7 = [6, 1, 1, 2, 2, 3, 3, 6, 7]
print("Test 7 Expected: 7 | Got:", solution.singleNumber(nums7))
