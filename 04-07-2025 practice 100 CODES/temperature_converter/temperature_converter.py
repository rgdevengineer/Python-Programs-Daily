

class TemperatureConverter:
    def __init__(self, celsius: float):
        self.celsius = celsius

    def to_fahrenheit(self) -> float:
        return (9 * self.celsius) / 5 + 32
