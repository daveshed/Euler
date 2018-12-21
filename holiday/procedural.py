import random
from statistics import mean
import sys

TOLERANCE = 0.00001

def how_many_emperors(days):
    holidays = [False] * days
    emperors = 0
    while not all(holidays):
        emperors += 1
        _create_emperor(holidays, days)
    return emperors

def expected_emperors(days):
    results = []
    new_result = 1
    n_runs = 0
    while True:
        n_runs += 1
        old_result = new_result
        n_emperors = how_many_emperors(days)
        results.append(n_emperors)
        new_result = mean(results)
        print("year of {} days needs {} emperors. result is {}".format(days, n_emperors, new_result))
        if abs(new_result - old_result) < TOLERANCE:
            break
    return new_result

def _create_emperor(holidays, days):
    birthday = random.randrange(days)
    # emperor is born
    if holidays[birthday]:
        # return early, already a holiday. nothing to do
        return
    holidays[birthday] = True
    # check adjacent days for single workday
    next_day = (birthday + 1) % days
    if _is_single_workday(holidays, next_day, days):
        holidays[next_day] = True
    prev_day = birthday - 1
    if _is_single_workday(holidays, prev_day, days):
        holidays[prev_day] = True

def _is_single_workday(holidays, day, days):
    next_day = (day + 1) % days
    prev_day = day - 1
    if holidays[next_day] and holidays[prev_day]:
        holidays[day] = True

if __name__ == '__main__':
    expected_emperors(int(sys.argv[1]))
