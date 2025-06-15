
'''
Check for Balanced Parentheses
Given a string of parentheses, check if it is balanced using a stack.

# Input: "((()))"
# Output: True

# Input: "(()))("
# Output: False
'''

def is_balanced(expression):
    stack = []
    matching = {')':'(', ']':'[', '}':'{'}

    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()

    return len(stack) == 0

print(is_balanced("((()))"))
print(is_balanced("(())))"))
print(is_balanced("[[{}(]]"))
print(is_balanced("[({[){[}]})]"))
print(is_balanced(""))