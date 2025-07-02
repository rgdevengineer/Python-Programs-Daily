
# Even and Odd Checking

class Solution:
    def checkNumber(self, x: int) -> str:
        if not isinstance(x, int):
            raise TypeError("Input must be an integer")
        
        if x == 0 or 1:
            return "Neither Even nor Odd"
        elif x % 2 == 0:
            return "Even"
        else:
            return "Odd"