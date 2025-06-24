

from frequency_counter import count_frequency

def test_basic_case():
    assert count_frequency([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}

def test_empty_list():
    assert count_frequency([]) == {}

def test_all_same():
    assert count_frequency([4, 4, 4, 4]) == {4: 4}

def test_negative_numbers():
    assert count_frequency([-1, -1, -2]) == {-1: 2, -2: 1}

def test_mixed_numbers():
    assert count_frequency([0, 1, 0, -1, 1]) == {0: 2, 1: 2, -1: 1}
