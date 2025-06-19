
'''
Move Zeros to End
Given an integer array nums, move all the 0's to the end of the array. The relative order of the other elements must remain the same. This must be done in place, without making a copy of the array.
Examples:
Input: nums = [0, 1, 4, 0, 5, 2]
Output: [1, 4, 5, 2, 0, 0]
Explanation: Both the zeroes are moved to the end and the order of the other elements stay the same
Input: nums = [0, 0, 0, 1, 3, -2]
Output: [1, 3, -2, 0, 0, 0]
Explanation: All 3 zeroes are moved to the end and the order of the other elements stay the same
'''

def moveZeroes(nums):
    non_zero_index = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1

    for i in range(non_zero_index, len(nums)):
        nums[i] = 0

    return nums


# 🔍 Manual Tests (simple & clear)

# Test 1
nums1 = [0, 1, 4, 0, 5, 2]
print("Before:", nums1)
print("After: ", moveZeroes(nums1))
print("Expected: [1, 4, 5, 2, 0, 0]\n")

# Test 2
nums2 = [0, 0, 0, 1, 3, -2]
print("Before:", nums2)
print("After: ", moveZeroes(nums2))
print("Expected: [1, 3, -2, 0, 0, 0]\n")

# Test 3
nums3 = [1, 2, 3]
print("Before:", nums3)
print("After: ", moveZeroes(nums3))
print("Expected: [1, 2, 3]\n")

# Test 4
nums4 = [0, 0, 0]
print("Before:", nums4)
print("After: ", moveZeroes(nums4))
print("Expected: [0, 0, 0]\n")

# Test 5
nums5 = [0, 1, 0, 3, 12]
print("Before:", nums5)
print("After: ", moveZeroes(nums5))
print("Expected: [1, 3, 12, 0, 0]\n")