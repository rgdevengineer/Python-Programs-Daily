
# Sum of numbers in a given range

class Solution:
    def sumInRange(self, left: int, right: int) -> int:
        if left > right:
            raise ValueError("Left value must be lesser than the right value")
        if left < 1:
            raise ValueError("Only Positive integers are allowed")

        total = 0
        for i in range(left, right + 1):
            total += i
        return total