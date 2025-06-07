
# Sort the characters of a string using Bubble Sort.

def bubble_sort(str):
    chars = list(str)
    n = len(chars)
    for i in range(n):
        for j in range(n-i-1):
            if ord(chars[j]) > ord(chars[j+1]):
                chars[j], chars[j+1] = chars[j+1], chars[j]

    return ''.join(chars)

print(bubble_sort("python"))