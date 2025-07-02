
# Check if a Number is Positive and Negative

class Solution:
    def checkNumber(self, x: int) -> str:
        if not isinstance(x, int):
            raise TypeError("Input must be an integer")
        
        if x > 0:
            return "positive"     
        elif x < 0:
            return "negative"
        else:
            return "zero"


