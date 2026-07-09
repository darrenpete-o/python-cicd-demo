"""
Temperature conversion functions
"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    if kelvin < 0:
        raise ValueError("Kelvin cannot be negative")
    return kelvin - 273.15

def is_boiling(celsius):
    """Check if water is boiling at given temperature"""
    return celsius >= 100

def is_freezing(celsius):
    """Check if water is freezing at given temperature"""
    return celsius <= 0
