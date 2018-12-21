import unittest

from procedural import expected_emperors

class EveryDayIsAHoliday(unittest.TestCase):

    def test_two_day_year_needs_one_emperor(self):
        self.assertEqual(1, expected_emperors(days=2))

    def test_5_day(self):
        self.assertEqual(31/6, expected_emperors(5))

    def test_365_day_year(self):
        self.assertEqual(1174.3501, expected_emperors(365))
