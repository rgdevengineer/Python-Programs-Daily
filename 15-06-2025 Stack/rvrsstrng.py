
def reverse_string(s):
    stack = []

    for char in s:
        stack.append(char)

    reverse_str = ''
    while stack:
        reverse_str += stack.pop()

    return reverse_str

str = "Python"

print("Original:", str)

print("Reversed:", reverse_string(str))
