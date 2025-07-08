

from set_matrix_zeroes import setZeroes
import copy

test_cases = [
    {
        "input": [],
        "expected": []
    },
    {
        "input": [[]],
        "expected": [[]]
    },
    {
        "input": [[0]],
        "expected": [[0]]
    },
    {
        "input": [[1, 0, 3]],
        "expected": [[0, 0, 0]]
    },
    {
        "input": [[1], [0], [3]],
        "expected": [[0], [0], [0]]
    },
    {
        "input": [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        "expected": [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]
    },
    {
        "input": [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ],
        "expected": [
            [0, 0, 0, 0],
            [0, 4, 5, 0],
            [0, 3, 1, 0]
        ]
    },
    {
        "input": [
            [1, 2],
            [3, 4]
        ],
        "expected": [
            [1, 2],
            [3, 4]
        ]
    }
]

for i, test in enumerate(test_cases):
    matrix = copy.deepcopy(test["input"])  
    setZeroes(matrix)
    passed = matrix == test["expected"]
    print(f"Test Case {i+1}: {'PASS' if passed else 'FAIL'}")
    print(f"Input: {test['input']}")
    print(f"Expected: {test['expected']}")
    print(f"Got: {matrix}\n")
