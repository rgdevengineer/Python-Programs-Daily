
from group_anagrams import group_anagrams

def test_basic_case():
    input_data = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = group_anagrams(input_data)

    expected_groups = [
        sorted(["eat", "tea", "ate"]),
        sorted(["tan", "nat"]),
        sorted(["bat"])
    ]

    output_sorted = [sorted(group) for group in output]

    assert sorted(output_sorted) == sorted(expected_groups)

def test_empty_list():
    assert group_anagrams([]) == []

def test_single_word():
    assert group_anagrams(["hello"]) == [["hello"]]

def test_all_anagrams():
    input_data = ["abc", "bca", "cab", "cba", "bac"]
    output = group_anagrams(input_data)
    assert len(output) == 1
    assert sorted(output[0]) == sorted(input_data)

def test_no_anagrams():
    input_data = ["a", "b", "c"]
    result = group_anagrams(input_data)
    assert sorted([sorted(group) for group in result]) == [['a'], ['b'], ['c']]
