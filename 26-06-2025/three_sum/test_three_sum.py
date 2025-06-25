


from three_sum import three_sum

def sort_triplets(triplets):
    """Helper function to sort inner triplets and outer list for comparison"""
    return sorted([sorted(triplet) for triplet in triplets])

def test_basic_case():
    assert sort_triplets(three_sum([-1, 0, 1, 2, -1, -4])) == sort_triplets([[-1, -1, 2], [-1, 0, 1]])

def test_multiple_solutions():
    assert sort_triplets(three_sum([0, 0, 0, 0])) == sort_triplets([[0, 0, 0]])

def test_no_solution():
    assert sort_triplets(three_sum([1, 2, 3, 4])) == []

def test_negative_only():
    assert sort_triplets(three_sum([-5, -2, -1, -3])) == []

def test_positive_and_negative_mix():
    assert sort_triplets(three_sum([-2, 0, 1, 1, 2])) == sort_triplets([[-2, 0, 2], [-2, 1, 1]])
