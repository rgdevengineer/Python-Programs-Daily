
# Use a stack to check if a given string is a palindrome.

def is_palindrome(str):
    stack = []

    for char in str:
        stack.append(char)

    reversed_str = ""

    while stack:
        reversed_str += stack.pop()

    return str == reversed_str

print(is_palindrome("madam"))
print(is_palindrome("stack"))
print(is_palindrome("python"))
print(is_palindrome("a"))
print(is_palindrome(""))