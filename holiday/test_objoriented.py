import unittest
from timeit import timeit

from objoriented import expected_emperors, World

class EveryDayIsAHoliday(unittest.TestCase):

    def test_two_day_year_needs_one_emperor(self):
        self.assertEqual(1, expected_emperors(days=2))

    def test_5_day(self):
        self.assertEqual(31/6, expected_emperors(5))

    def test_365_day_year(self):
        self.assertEqual(1174.3501, expected_emperors(365))

    def test_time_to_compute_no_emperors(self):
        days = 365
        def procedure():
            World(days).run()
        runs = 100
        time_to_compute = \
            timeit(
                "procedure()",
                number=runs,
                globals=locals()) / runs
        print("Time to calculate emperors {:f} ms".format(time_to_compute * 1000))