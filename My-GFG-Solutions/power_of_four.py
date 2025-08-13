
'''
Power of Four

Given a number N, check if N is power of 4 or not.

Example 1:
Input: 
N = 64
Output: 1
Explanation:
43= 64
Example 2:
Input: 
N = 75
Output : 0
Explanation :
75 is not a power of 4.
Your task:
You don't have to read input or print anything. Your task is to complete the function isPowerOfFour() which takes an integer N and returns 1 if the number is a power of four else returns 0.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space : O(1)

Constraints:
1<=N<=10^5
'''

class Solution():
    def isPowerofFour(self, n):
         if n < 0:
             return 0
         while n % 4 == 0:
             n //= 4
         return 1 if n == 1 else 0