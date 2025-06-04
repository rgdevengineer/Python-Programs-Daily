import unittest
from io import StringIO
import sys

# Function to test
def EvenOdd(number):
    if number % 2 == 0:
        print('Even Number')
    else:
        print('Odd Number')

# Unit test cases
def test_even_number():
    captured_output = StringIO()
    sys.stdout = captured_output
    EvenOdd(12)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "Even Number"

def test_odd_number():
    captured_output = StringIO()
    sys.stdout = captured_output
    EvenOdd(15)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "Odd Number"

# Running the tests
if __name__ == '__main__':
    test_even_number()
    test_odd_number()
    print("All tests passed!")