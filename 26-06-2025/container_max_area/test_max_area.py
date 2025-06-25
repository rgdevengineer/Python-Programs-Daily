


from max_area import max_area

def test_example_case():
    assert max_area([1,8,6,2,5,4,8,3,7]) == 49

def test_small_case():
    assert max_area([1,1]) == 1

def test_all_same_height():
    assert max_area([4,4,4,4]) == 12  # 4*(3-0)

def test_decreasing():
    assert max_area([9,8,7,6,5]) == 20  # 5*(1-0)

def test_peak_middle():
    assert max_area([1,2,100,2,1]) == 4  # min(2,2)*2

def test_single_element():
    assert max_area([5]) == 0

def test_two_elements():
    assert max_area([3,7]) == 3
