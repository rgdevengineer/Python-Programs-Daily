
# Convert Decimal to Binary using Stack

def decimal_to_binary(n):
    stack = []

    while n > 0:
        stack.append(str(n%2))
        n = n // 2

    return ''.join(reversed(stack)) or "0"

print("Binary of 10 is:", decimal_to_binary(10))