import random
import sys

TOLERANCE = 0.00001


def how_many_emperors(days):
    holidays = [False] * days
    emperors = 0
    while not all(holidays):
        emperors += 1
        _create_emperor(holidays)
    return emperors

def expected_emperors(days):
    results = []
    new_result = 1
    old_result = new_result + TOLERANCE * 2
    n_runs = 0
    while abs(new_result - old_result) > TOLERANCE:
        n_runs += 1
        old_result = new_result
        n_emperors = how_many_emperors(days)
        results.append(n_emperors)
        new_result = sum(results) / n_runs
        print("year of {} days needs {} emperors. result is {}".format(days, n_emperors, new_result))
    return sum(results) / n_runs

def _create_emperor(holidays):
    birthday = random.randrange(len(holidays))
    # emperor is born
    holidays[birthday] = True
    # check adjacent days for single workday
    next_day = (birthday + 1) % len(holidays)
    if _is_single_workday(holidays, next_day):
        holidays[next_day] = True
    prev_day = birthday - 1
    if _is_single_workday(holidays, prev_day):
        holidays[prev_day] = True


def _is_single_workday(holidays, day):
    next_day = (day + 1) % len(holidays)
    prev_day = day - 1
    if holidays[next_day] and holidays[prev_day]:
        holidays[day] = True

if __name__ == '__main__':
    expected_emperors(int(sys.argv[1]))
