
'''
Index Tracking and Substring Slicing
Track character positions or slice substrings directly.

Examples:

Find first/last index of a character
→ s.find('a'), s.rfind('a')

Custom Substring Parsing
→ Like extracting domain from email: s.split('@')[1]
'''

def find_first_index(s: str, char: str) -> int:
    
    return s.find(char)


def find_last_index(s: str, char: str) -> int:
   
    return s.rfind(char)


def extract_email_domain(email: str) -> str:
    
    parts = email.split('@')
    if len(parts) != 2 or not parts[1]:
        raise ValueError("Invalid email format")
    return parts[1]


def extract_after(s: str, delimiter: str) -> str:
   
    index = s.find(delimiter)
    if index == -1:
        return ""
    return s[index + len(delimiter):]


def extract_before(s: str, delimiter: str) -> str:
  
    index = s.find(delimiter)
    if index == -1:
        return ""
    return s[:index]

