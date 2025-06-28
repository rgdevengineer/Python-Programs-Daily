
from collections import defaultdict
from typing import List

def group_anagrams(words: List[str]) -> List[List[str]]:
    """
    Groups anagrams together from a list of strings.

    Args:
    words: List[str] - A list of words.

    Returns:
    List[List[str]] - A list where each sublist contains words that are anagrams.
    """
    anagram_map = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())
