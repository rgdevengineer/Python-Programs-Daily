
'''
Minimum product pair

Given an array of positive integers. The task is to print the minimum product of any two numbers of the given array.

Examples:

Input : arr[] = [2, 7, 3, 4]
Output : 6
Explanation : The minimum product of any two numbers will be 2 * 3 = 6.
Input : arr[] = [198, 76, 544, 123, 154, 675]
Output :  9348
Explanation : The minimum product of any two numbers will be 76 * 123 = 9348.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
2<= arr.size() <=106
1<= arr[i] <=106
'''

class Solution:
    def printMinimumProduct(self, a):
        first = second = float('inf')

        for num in a:
            if num < first:
                second = first
                first = num
            elif num < second:
                second = num

        return first * second
    
    
    