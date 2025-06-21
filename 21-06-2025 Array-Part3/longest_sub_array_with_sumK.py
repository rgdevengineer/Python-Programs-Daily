
'''
Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
Examples:
Input: nums = [10, 5, 2, 7, 1, 9],  k=15
Output: 4
Explanation: The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.
Input: nums = [-3, 2, 1], k=6
Output: 0
Explanation: There is no sub-array in the array that sums to 6. Therefore, the output is 0.
'''

class Solution:
    def maxSubArrayLen(self, nums, k):
        prefix_sum_map = {}
        curr_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            curr_sum += num

            # Case 1: subarray from index 0 to i
            if curr_sum == k:
                max_len = i + 1

            # Case 2: check if there is a prefix sum that makes curr_sum - k
            if (curr_sum - k) in prefix_sum_map:
                max_len = max(max_len, i - prefix_sum_map[curr_sum - k])

            # Store the first occurrence of a prefix sum
            if curr_sum not in prefix_sum_map:
                prefix_sum_map[curr_sum] = i

        return max_len

# ----------- Manual Testing -----------
solution = Solution()

# Test Case 1
nums1 = [10, 5, 2, 7, 1, 9]
k1 = 15
print("Test 1 Expected: 4 | Got:", solution.maxSubArrayLen(nums1, k1))

# Test Case 2
nums2 = [-3, 2, 1]
k2 = 6
print("Test 2 Expected: 0 | Got:", solution.maxSubArrayLen(nums2, k2))

# Test Case 3
nums3 = [1, 2, 3, 4, 5]
k3 = 9
print("Test 3 Expected: 3 | Got:", solution.maxSubArrayLen(nums3, k3))  # [2, 3, 4]

# Test Case 4
nums4 = [1, -1, 5, -2, 3]
k4 = 3
print("Test 4 Expected: 4 | Got:", solution.maxSubArrayLen(nums4, k4))  # [1, -1, 5, -2]

# Test Case 5
nums5 = [5]
k5 = 5
print("Test 5 Expected: 1 | Got:", solution.maxSubArrayLen(nums5, k5))

# Test Case 6
nums6 = [1, 2, 3]
k6 = 6
print("Test 6 Expected: 3 | Got:", solution.maxSubArrayLen(nums6, k6))  # entire array

# Test Case 7
nums7 = [1, -1, 1, -1, 1, -1, 1]
k7 = 0
print("Test 7 Expected: 6 | Got:", solution.maxSubArrayLen(nums7, k7))  # [1, -1, ..., -1] (index 0 to 5)

# Test Case 8
nums8 = []
k8 = 0
print("Test 8 Expected: 0 | Got:", solution.maxSubArrayLen(nums8, k8))

# Test Case 9
nums9 = [1, 2, 3, -3, 4]
k9 = 7
print("Test 9 Expected: 4 | Got:", solution.maxSubArrayLen(nums9, k9))  # [2, 3, -3, 4]

# Test Case 10
nums10 = [3, 1, -1, 2, 4, 1]
k10 = 6
print("Test 10 Expected: 4 | Got:", solution.maxSubArrayLen(nums10, k10))  # [1, -1, 2, 4]
