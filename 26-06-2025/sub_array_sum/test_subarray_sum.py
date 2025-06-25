

from subarray_sum import subarray_sum

def test_basic_case():
    assert subarray_sum([1, 1, 1], 2) == 2

def test_all_zero_k_zero():
    assert subarray_sum([0, 0, 0, 0], 0) == 10  # Many zero-sum subarrays

def test_negative_numbers():
    # Total 6 subarrays with sum 0
    assert subarray_sum([1, -1, 1, -1, 1], 0) == 6


def test_single_match():
    assert subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4

def test_no_subarray():
    assert subarray_sum([1, 2, 3], 7) == 0

def test_whole_array():
    assert subarray_sum([1, 2, 3], 6) == 1
