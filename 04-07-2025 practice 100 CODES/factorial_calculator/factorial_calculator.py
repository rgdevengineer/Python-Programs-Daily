
class FactorialCalculator:
    def __init__(self, number: int):
        self.number = number

    def calculate(self) -> int:
        if self.number < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        fact = 1
        for i in range(1, self.number + 1):
            fact *= i
        return fact
