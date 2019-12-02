from unittest import TestCase
from day_2.intcode_analyzer import analyze


class AnalyzeIntcodeTestCase(TestCase):
    def test_intcode_analysis(self):
        self.assertEqual([2, 0, 0, 0, 99], analyze([1, 0, 0, 0, 99]))
        self.assertEqual([2, 3, 0, 6, 99], analyze([2, 3, 0, 3, 99]))
        self.assertEqual([2, 4, 4, 5, 99, 9801], analyze([2, 4, 4, 5, 99, 0]))
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], analyze([1, 1, 1, 4, 99, 5, 6, 0, 99]))
