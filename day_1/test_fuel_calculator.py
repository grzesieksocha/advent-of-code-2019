from unittest import TestCase
from day_1 import fuel_calculator


class CountFuelNeededTestCase(TestCase):
    def test_count_fuel_needed_without_self_mass(self):
        self.assertEqual(2, fuel_calculator.count_fuel_needed(12))
        self.assertEqual(2, fuel_calculator.count_fuel_needed(14))
        self.assertEqual(654, fuel_calculator.count_fuel_needed(1969))
        self.assertEqual(33583, fuel_calculator.count_fuel_needed(100756))

    def test_count_fuel_needed_with_self_mass(self):
        self.assertEqual(2, fuel_calculator.count_fuel_needed(12, 0, True))
        self.assertEqual(966, fuel_calculator.count_fuel_needed(1969, 0, True))
        self.assertEqual(50346, fuel_calculator.count_fuel_needed(100756, 0, True))
