import unittest
from timeit import timeit

from procedural import expected_emperors, how_many_emperors

class EveryDayIsAHoliday(unittest.TestCase):

    def test_two_day_year_needs_one_emperor(self):
        self.assertEqual(1, expected_emperors(days=2))

    def test_5_day(self):
        self.assertEqual(31/6, expected_emperors(5))

    def test_365_day_year(self):
        self.assertEqual(1174.3501, expected_emperors(365))

    def test_time_to_compute_no_emperors(self):
        days = 365
        runs = 100
        fn = how_many_emperors
        args = days
        time_to_compute = \
            timeit(
                "fn(args)",
                number=runs,
                globals=locals()) / runs
        print("Time to calculate emperors {:f} ms".format(time_to_compute * 1000))
