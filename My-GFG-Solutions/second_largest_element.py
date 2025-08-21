
'''
Second Largest

Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.
Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.
Constraints:
2 ≤ arr.size() ≤ 10^5
1 ≤ arr[i] ≤ 10^5
'''

class Solution:
    def getSecondLargest(self, arr):
        #arr_new = sorted(set(arr))
        #set_arr = set(arr)
        
        #n = len(arr)
        #for i in range(n):
        # arr.sort()
        # largest = arr[-1]
        
        # for num in reversed(arr[:-1]):
        #     if num != largest:
        #         return num
        
        # raise ValueError("No second largest element exists")
        
        sorted_arr = sorted(arr, reverse=True)
        largest = sorted_arr[0]
        for num in sorted_arr[1:]:
            if num != largest:
                return num
        return -1
                