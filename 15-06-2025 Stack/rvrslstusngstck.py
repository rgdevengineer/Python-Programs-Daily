
'''
Reverse a List using Stack
Use a stack (list) to reverse a list.

# Input: [1, 2, 3, 4]
# Output: [4, 3, 2, 1]
'''

def reverse_list(arr):
    stack = []

    for item in arr:
        stack.append(item)

    reversed_arr = []

    while stack:
        reversed_arr.append(stack.pop())

    return reversed_arr

original = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original)

print("Original List:", original)

print("Reversed List:", reversed_list)