import unittest

class TestMeasurements(unittest.TestCase):

    def test_convert_from_cm_to_inches(self):
        self.assertEqual(convert_from_cm_to_inches(10), 4)
        self.assertEqual(convert_from_cm_to_inches(100), 39)

    def test_convert_from_cm_to_inches_negative_input(self):
        with self.assertRaises(ValueError):
            convert_from_cm_to_inches(-10)

    def test_convert_from_cm_to_inches_string_input(self):
        with self.assertRaises(TypeError):
            convert_from_cm_to_inches("hello")


    def test_convert_from_inches_to_cm(self):
        self.assertEqual(convert_from_inches_to_cm(10), 25)
        self.assertEqual(convert_from_inches_to_cm(18), 46)

    def test_convert_from_inches_to_cm_negative_input(self):
        with self.assertRaises(ValueError):
            convert_from_inches_to_cm(-10)

    def test_convert_from_inches_to_cm_string_input(self):
        with self.assertRaises(TypeError):
            convert_from_inches_to_cm("hello")

    def test_convert_from_celsius_to_fahrenheit(self):
        self.assertEqual(convert_from_celsius_to_fahrenheit(10), 50)
        self.assertEqual(convert_from_celsius_to_fahrenheit(16), 61)

    def test_convert_from_celsius_to_fahrenheit_temperature_low_limit(self):
        # https://en.wikipedia.org/wiki/Absolute_zero
        with self.assertRaises(ValueError):
            convert_from_celsius_to_fahrenheit(-400)

    def test_convert_from_celsius_to_fahrenheit_string_input(self):
        with self.assertRaises(TypeError):
            convert_from_celsius_to_fahrenheit("zero")
