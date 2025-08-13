
'''
Find index

Given a tuple arr with distinct elements and an integer x, find the index position of x. Assume to have x in the tuple always. Print the index (0-based).

Examples:

Input: arr = (1, 2, 3, 4, 5), x = 3
Output: 2
Input: arr = (3, 2, 1, 5, 4), x = 5
Output: 3
'''

'''
# Submission - 1

#User function Template for python3

arr = tuple(map(int, input().split()))
x = int(input())

print(arr.index(x))

'''

# Submission - 2

#User function Template for python3

arr = tuple(map(int, input().split()))
x = int(input())

for i in range(len(arr)):
    if arr[i] == x:
        print(i)
        break
