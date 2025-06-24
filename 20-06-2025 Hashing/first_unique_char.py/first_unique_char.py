
'''
 Find First Non-Repeating Character
Given a string, return the first non-repeating character.
Example: "aabbcd" → 'c'
'''

def get_input():
    return "aabbcd"

def first_non_repeating_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None

def main():
    s = get_input()
    result = first_non_repeating_char(s)
    print(f"First non-repeating character: {result}" if result else "No unique character found.")

if __name__ == "__main__":
    main()
