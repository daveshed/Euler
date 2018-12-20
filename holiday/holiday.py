import random


class Day:
    def __init__(self, date):
        self.date = date


class Holiday(Day):
    holiday = True


class WorkDay(Day):
    holiday = False


class Calendar:

    def __init__(self, n_days):
        self.n_days = n_days
        self.days = [WorkDay(date) for date in range(n_days)]

    def get_day(self, date):
        return self.days[self._normalise_date(date)]

    def is_holiday(self, date):
        day = self.get_day(date)
        return day.holiday

    def is_single_workday(self, date):
        day = self.get_day(date)
        # look out for index error
        return self.is_holiday(date + 1) and self.is_holiday(date - 1)

    def to_holiday(self, date):
        self.days[self._normalise_date(date)] = Holiday(date)

    def to_workday(self, date):
        self.days[self._normalise_date(date)] = WorkDay(date)

    @property
    def party_on(self):
        return all([self.is_holiday(date) for date in range(self.n_days)])
    
    def _normalise_date(self, date):
        return date % self.n_days


class Emperor:

    def spawn(calendar):
        birthdate = random.randrange(calendar.n_days)
        # print("spawning Emperor with birthdate {}".format(birthdate))
        if calendar.is_holiday(birthdate):
            return
        else:
            calendar.to_holiday(birthdate)
            if calendar.is_single_workday(birthdate + 1):
                calendar.to_holiday(birthdate + 1)
            if calendar.is_single_workday(birthdate - 1):
                calendar.to_holiday(birthdate - 1)


class World:
    def __init__(self, n_days):
        self.calendar = Calendar(n_days)

    def run(self):
        counter = 0
        while not self.calendar.party_on:
            Emperor.spawn(self.calendar)
            counter += 1
        return counter


class God:

    @staticmethod
    def create_world(n_days):
        return World(n_days)

    @staticmethod
    def spawn_emperor(planet):
        Emperor(planet.calendar)


N_RUNS = 100

def how_many_emperors(days):
    results = []
    for i in range(N_RUNS):
        world = God.create_world(days)
        results.append(world.run())
    return sum(results) / N_RUNS