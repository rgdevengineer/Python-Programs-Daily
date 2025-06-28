
import re

def extract_numbers(s: str) -> list[int]:
  
    return list(map(int, re.findall(r'\d+', s)))


def extract_words(s: str) -> list[str]:
    
    return re.findall(r'\b\w+\b', s)


def is_valid_email(email: str) -> bool:
    
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None
