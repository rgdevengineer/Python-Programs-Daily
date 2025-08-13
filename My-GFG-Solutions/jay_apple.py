
'''
Jay's Apples
Given a queue of persons represented by an array of integers, where each person is identified by a specific integer, find the minimum kilograms of apples that need to be distributed, ensuring that each person receives 1 kilogram of apples only once.

Examples:
Input: arr[] = [1, 1, 1, 1, 1]
Output: 1
Explanation: The person identified by '1' appears multiple times but will only receive 1 kilogram of apples once. Therefore, the minimum apples required is 1 kg.
Input: arr[] = [1, 2, 3, 1, 2]
Output: 3
Explanation: There are three distinct persons in the queue, so 3 kilograms of apples need to be distributed.
Constraints:
1 ≤ arr.size() ≤ 10^6
1 ≤ arr[i] ≤ 10^6
'''

class Solution:
    def minimumApple(self, arr):
        return len(set(arr))
