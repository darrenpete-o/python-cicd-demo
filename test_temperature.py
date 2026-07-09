"""
Unit tests for temperature converter
"""
import unittest
from temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    is_boiling,
    is_freezing
)


class TestTemperatureConversions(unittest.TestCase):
    """Test temperature conversion functions"""

    def test_celsius_to_fahrenheit(self):
        """Test Celsius to Fahrenheit conversion"""
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertEqual(celsius_to_fahrenheit(-40), -40)
        self.assertEqual(celsius_to_fahrenheit(37), 98.6)

    def test_fahrenheit_to_celsius(self):
        """Test Fahrenheit to Celsius conversion"""
        self.assertEqual(fahrenheit_to_celsius(32), 0)
        self.assertEqual(fahrenheit_to_celsius(212), 100)
        self.assertEqual(fahrenheit_to_celsius(-40), -40)
        self.assertEqual(fahrenheit_to_celsius(98.6), 37)

    def test_celsius_to_kelvin(self):
        """Test Celsius to Kelvin conversion"""
        self.assertEqual(celsius_to_kelvin(0), 273.15)
        self.assertEqual(celsius_to_kelvin(100), 373.15)
        self.assertEqual(celsius_to_kelvin(-273.15), 0)

    def test_kelvin_to_celsius(self):
        """Test Kelvin to Celsius conversion"""
        self.assertEqual(kelvin_to_celsius(273.15), 0)
        self.assertEqual(kelvin_to_celsius(373.15), 100)
        self.assertEqual(kelvin_to_celsius(0), -273.15)

    def test_kelvin_negative_error(self):
        """Test that negative Kelvin raises error"""
        with self.assertRaises(ValueError):
            kelvin_to_celsius(-10)

    def test_is_boiling(self):
        """Test boiling point detection"""
        self.assertTrue(is_boiling(100))
        self.assertTrue(is_boiling(110))
        self.assertFalse(is_boiling(99))
        self.assertFalse(is_boiling(0))

    def test_is_freezing(self):
        """Test freezing point detection"""
        self.assertTrue(is_freezing(0))
        self.assertTrue(is_freezing(-10))
        self.assertFalse(is_freezing(1))
        self.assertFalse(is_freezing(100))


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and invalid inputs"""

    def test_very_large_numbers(self):
        """Test with very large numbers"""
        result = celsius_to_fahrenheit(1e6)
        self.assertAlmostEqual(result, 1800032.0)

    def test_very_small_numbers(self):
        """Test with very small numbers"""
        result = celsius_to_fahrenheit(-1e6)
        self.assertAlmostEqual(result, -1799968.0)

    def test_floating_point_precision(self):
        """Test floating point precision"""
        f = celsius_to_fahrenheit(25)
        c = fahrenheit_to_celsius(f)
        self.assertAlmostEqual(c, 25, places=6)


if __name__ == '__main__':
    unittest.main()
