
from spiral_matrix_traversal import spiralOrder

test_cases = [
    {
        "input": [],
        "expected": []
    },
    {
        "input": [[]],
        "expected": []
    },
    {
        "input": [[42]],
        "expected": [42]
    },
    {
        "input": [[1, 2, 3, 4]],
        "expected": [1, 2, 3, 4]
    },
    {
        "input": [[1], [2], [3], [4]],
        "expected": [1, 2, 3, 4]
    },
    {
        "input": [
            [1, 2, 3],
            [4, 5, 6]
        ],
        "expected": [1, 2, 3, 6, 5, 4]
    },
    {
        "input": [
            [1, 2],
            [3, 4],
            [5, 6]
        ],
        "expected": [1, 2, 4, 6, 5, 3]
    },
    {
        "input": [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        "expected": [1, 2, 3, 6, 9, 8, 7, 4, 5]
    },
    {
        "input": [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9,10,11,12],
            [13,14,15,16]
        ],
        "expected": [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    }
]

for i, test in enumerate(test_cases):
    actual = spiralOrder(test["input"])
    print(f"Test Case {i+1}: {'PASS' if actual == test['expected'] else 'FAIL'}")
    print(f"Input: {test['input']}")
    print(f"Expected: {test['expected']}")
    print(f"Got: {actual}\n")
