class NationalPark:
    _all_parks = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise Exception("Name must be a string with at least 3 characters.")
        self._name = name
        NationalPark._all_parks.append(self)

    @property
    def name(self):
        return self._name

    def trips(self):
        return [trip for trip in Trip._all_trips if trip.national_park == self]

    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        if not self.trips():
            return None
        visitor_counts = {}
        for trip in self.trips():
            visitor_counts[trip.visitor] = visitor_counts.get(trip.visitor, 0) + 1
        return max(visitor_counts, key=visitor_counts.get)

    @classmethod
    def most_visited(cls):
        if not Trip._all_trips:
            return None
        return max(cls._all_parks, key=lambda park: park.total_visits())


class Trip:
    _all_trips = []

    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(visitor, Visitor):
            raise Exception("visitor must be a Visitor instance")
        if not isinstance(national_park, NationalPark):
            raise Exception("national_park must be a NationalPark instance")
        if not isinstance(start_date, str) or len(start_date) < 7:
            raise Exception("start_date must be a string of at least 7 characters")
        if not isinstance(end_date, str) or len(end_date) < 7:
            raise Exception("end_date must be a string of at least 7 characters")

        self._visitor = visitor
        self._national_park = national_park
        self._start_date = start_date
        self._end_date = end_date
        Trip._all_trips.append(self)

    @property
    def visitor(self):
        return self._visitor

    @property
    def national_park(self):
        return self._national_park

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise Exception("start_date must be a string of at least 7 characters")
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise Exception("end_date must be a string of at least 7 characters")
        self._end_date = value


class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise Exception("Name must be a string between 1 and 15 characters")
        self._name = value

    def trips(self):
        return [trip for trip in Trip._all_trips if trip.visitor == self]

    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))

    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])
