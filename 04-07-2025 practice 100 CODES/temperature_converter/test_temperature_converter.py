
# test_temperature_converter.py

import pytest
from temperature_converter import TemperatureConverter

def test_freezing_point():
    converter = TemperatureConverter(0)
    assert converter.to_fahrenheit() == 32.0

def test_boiling_point():
    converter = TemperatureConverter(100)
    assert converter.to_fahrenheit() == 212.0

def test_negative_temperature():
    converter = TemperatureConverter(-40)
    assert converter.to_fahrenheit() == -40.0  # special case: -40°C == -40°F

def test_decimal_input():
    converter = TemperatureConverter(37.5)
    assert round(converter.to_fahrenheit(), 2) == 99.5

def test_large_value():
    converter = TemperatureConverter(1000)
    assert converter.to_fahrenheit() == 1832.0
