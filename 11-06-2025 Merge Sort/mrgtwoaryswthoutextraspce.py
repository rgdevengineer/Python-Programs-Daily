
'''
Merge Two Sorted Arrays Without Using Extra Space
Input: A = [1, 3, 5], B = [2, 4, 6]
Output: A = [1, 2, 3], B = [4, 5, 6]
'''

def merge(A, B):
    i = 0

    while i < len(A):
        if A[i] > B[0]:
            A[i], B[0] = B[0], A[i]

            temp = B[0]
            K = 1

            while K < len(B) and B[K] < temp:
                B[K - 1] = B[K]
                K += 1
            B[K - 1] = temp
        i += 1

A = [1, 3, 5]
B = [2, 4, 6]

print("Input:")
print("A =", A)
print("B =", B)

merge(A, B)

print("\nOutput:")
print("A =", A)
print("B =", B)