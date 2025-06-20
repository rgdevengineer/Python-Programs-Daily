
# Using Hash Map (for any character)

str = "aaabbccddeeaafffgg"

char_freq = {}

for char in str:
    char_freq[char] = char_freq.get(char, 0) + 1

for char in char_freq:
    print(f"'{char}' appears = {char_freq[char]} times")