
'''
Print Elements of Array
Given an array arr[], print all its elements space-separated.

Note: You don't need to move to the next line after printing all elements of the array (space-separated)

Examples:
Input: arr[] = [1, 2, 3, 4, 5]
Output: 1 2 3 4 5
Input: arr[] = [2, 3, 5, 5]
Output: 2 3 5 5
Constraints:
1 <= arr.size <= 10^6
1 <= arr[i] <= 10^8
'''

#User function Template for python3
class Solution:
    # Just print the space seperated array elements
	def printArray(self, arr):
	    for i in arr:
	        print(i, end =" ")