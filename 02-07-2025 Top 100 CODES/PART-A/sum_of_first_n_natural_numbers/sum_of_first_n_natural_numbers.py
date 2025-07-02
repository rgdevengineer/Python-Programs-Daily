
# Sum of First N natural numbers

class Solution:
    def sum_Natural_Number(self, n: int) -> str:
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        
        if n < 1:
            raise ValueError("Input must be greater than equal to 1")
        
        return n * (n+1) // 2
