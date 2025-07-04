
from typing import List

class Solution:
    def triangleArea(self, a: float, b: float, c: float) -> float:

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")
    
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return area
    