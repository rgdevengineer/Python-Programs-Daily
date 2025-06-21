
'''
Given a binary array nums, return the maximum number of consecutive 1s in the array.
A binary array is an array that contains only 0s and 1s.
Examples:
Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]
Output: 3
Explanation: The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s
Input: nums = [0, 0, 0, 0, 0, 0, 0, 0]
Output: 0
Explanation: No 1s are present in nums, thus we return 0
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        current_count = 0

        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0

        return max_count

solution = Solution()

nums1 = [1, 1, 0, 0, 1, 1, 1, 0]
print("Test 1 Expected: 3 | Got:", solution.findMaxConsecutiveOnes(nums1))

nums2 = [0, 0, 0, 0, 0]
print("Test 2 Expected: 0 | Got:", solution.findMaxConsecutiveOnes(nums2))

nums3 = [1, 1, 1, 1]
print("Test 3 Expected: 4 | Got:", solution.findMaxConsecutiveOnes(nums3))

nums4 = [1, 0, 1, 1, 0, 1]
print("Test 4 Expected: 2 | Got:", solution.findMaxConsecutiveOnes(nums4))

nums5 = []
print("Test 5 Expected: 0 | Got:", solution.findMaxConsecutiveOnes(nums5))
