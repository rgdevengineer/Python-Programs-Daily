
'''
Test if tuple is distinct

Given a tuple arr , print "True" if all elements of tuple are different otherwise print "False".

A tuple is a collection of items that are ordered and unchangeable.

Examples:

Input:
arr = (1, 2, 3, 4, 5, 4)
Output: False
Input:
arr = (1, 2, 3, 4, 5)
Output: True
'''

'''
# Submission - 1

#User function Template for python3
arr = tuple(map(int, input().split()))

########### Write your code below ###############
# Print "True" if all elements of tuple are different, otherwise print "False"

########### Write your code above ###############
if len(arr) == len(set(arr)):
    print(True)
else:
    print(False)
'''

# Submission - 2

#User function Template for python3
arr = tuple(map(int, input().split()))

########### Write your code below ###############
# Print "True" if all elements of tuple are different, otherwise print "False"

########### Write your code above ###############

seen = set()
flag = True

for num in arr:
    if num in seen:
        flag = False
        break
    seen.add(num)

print(flag)