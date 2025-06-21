
'''
Given an array of integers nums and an integer target. Return the indices(0 - indexed) of two elements in nums such that they add up to target.
Each input will have exactly one solution, and the same element cannot be used twice. Return the answer in non-decreasing order.
Examples:
Input: nums = [1, 6, 2, 10, 3], target = 7
Output: [0, 1]
Explanation: nums[0] + nums[1] = 1 + 6 = 7
Input: nums = [1, 3, 5, -7, 6, -3], target = 0
Output: [1, 5]
Explanation: nums[1] + nums[5] = 3 + (-3) = 0
'''

class Solution:
    def twoSum(self, nums, target):
        num_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                # Return indices in non-decreasing order
                return sorted([num_to_index[complement], i])
            num_to_index[num] = i

        return []  # Should never be reached if one solution is guaranteed

solution = Solution()

# Test Case 1
nums1 = [1, 6, 2, 10, 3]
target1 = 7
print("Test 1 Expected: [0, 1] | Got:", solution.twoSum(nums1, target1))

# Test Case 2
nums2 = [1, 3, 5, -7, 6, -3]
target2 = 0
print("Test 2 Expected: [1, 5] | Got:", solution.twoSum(nums2, target2))

# Test Case 3
nums3 = [2, 7, 11, 15]
target3 = 9
print("Test 3 Expected: [0, 1] | Got:", solution.twoSum(nums3, target3))

# Test Case 4
nums4 = [3, 2, 4]
target4 = 6
print("Test 4 Expected: [1, 2] | Got:", solution.twoSum(nums4, target4))

# Test Case 5
nums5 = [-1, -2, -3, -4, -5]
target5 = -8
print("Test 5 Expected: [2, 4] | Got:", solution.twoSum(nums5, target5))

# Test Case 6
nums6 = [0, 4, 3, 0]
target6 = 0
print("Test 6 Expected: [0, 3] | Got:", solution.twoSum(nums6, target6))
