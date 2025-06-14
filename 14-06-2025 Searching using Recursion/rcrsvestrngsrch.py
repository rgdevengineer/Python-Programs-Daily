
# Check if a substring target is present in a string s recursively.

def search_substring(s, target):
   
   
    if len(s) < len(target):
        return False
    
    first_part = s[:len(target)]

    if first_part == target:
        return True
    
    next_part= s[1:]
    return search_substring(next_part, target)

print(search_substring("recursionfunction", 'on'))

print(search_substring("recursionfunction", 'off'))
    
