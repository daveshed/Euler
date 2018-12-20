import unittest

from holiday import how_many_emperors

class HoldayTestGroup(unittest.TestCase):

    def test_two_day_year_needs_one_emperor(self):
        self.assertEqual(1, how_many_emperors(days=2))

    def test_5_day(self):
        self.assertEqual(31/6, how_many_emperors(5))

    def test_365_day_year(self):
        self.assertEqual(1174.3501, how_many_emperors(365))
