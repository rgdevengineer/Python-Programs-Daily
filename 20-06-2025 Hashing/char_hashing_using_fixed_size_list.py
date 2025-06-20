
# Using Fixed-Size List (Only lowercase letters 'a' to 'z')

s = "aabbcddcaa"

# Fixed-size list for 26 lowercase English letters
freq = [0] * 26

# Count frequencies
for char in s:
    index = ord(char) - ord('a')  # a=0, b=1, ..., z=25
    freq[index] += 1

# Print frequencies
for i in range(26):
    if freq[i] > 0:
        print(f"{chr(i + ord('a'))} appears = {freq[i]} times")
