
'''
Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.
Examples:
Input: nums = [1, 2, 3, 4, 5, 6], k = 2
Output: nums = [3, 4, 5, 6, 1, 2]
Explanation: rotate 1 step to the left: [2, 3, 4, 5, 6, 1]
rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]
Input: nums = [3, 4, 1, 5, 3, -5], k = 8
Output: nums = [1, 5, 3, -5, 3, 4]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
0 <= k <= 105
'''

class Rotator:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def rotate_left(self, k):
        k = k % self.n

        for _ in range(k):
            first = self.arr[0]
            for i in range(self.n - 1):
                self.arr[i] = self.arr[i+1]
            self.arr[self.n - 1] = first

    def print_array(self):
        for num in self.arr:
            print(num, end=" ")
        print()

arr = [1, 2, 3, 4, 5]
k = 2
# Create object
r = Rotator(arr)
# Rotate the array to the left by k
r.rotate_left(k)
# Print the final array
r.print_array()




