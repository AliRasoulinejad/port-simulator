import random
import string

from settings.config import Setting


class Vessel(object):
    def __init__(self, *, capacity: int = Setting.vessel.default_capacity):
        """
        :param capacity: The maximum capacity of each vessel
        """
        self.code = "".join(random.choices(string.digits + string.ascii_letters, k=10))
        self.capacity = capacity
        self.arrival_time = None
        self.departure_time = None

    def __str__(self):
        return self.code

    def __lt__(self, other):
        return self.arrival_time < other.arrival_time
