
'''
String Builder / Manual Construction
Use list and ''.join() for efficient string construction (strings are immutable in Python).

Examples:

Compress String (Run-Length Encoding)
"aaabbcc" → "a3b2c2"

Remove characters, modify selectively
→ e.g. Remove vowels from a string
'''
def compress_string(s: str) -> str:

    if not s:
        return ""

    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
                                        # Append the last character and count
    result.append(s[-1] + str(count))
    return ''.join(result)


def remove_vowels(s: str) -> str:
    """
    Removes all vowels (a, e, i, o, u) from the input string.
    Example: "beautiful" -> "btfl"
    """
    vowels = set("aeiouAEIOU")
    return ''.join([ch for ch in s if ch not in vowels])
