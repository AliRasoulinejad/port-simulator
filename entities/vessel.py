import random
import string

from settings.config import Setting
from settings.logs import setup_logger

logger = setup_logger(__name__)


class Vessel(object):
    def __init__(self, *, capacity: int = Setting.vessel.default_capacity):
        """
        :param capacity: The maximum capacity of each vessel
        """
        self.code = "".join(random.choices(string.digits + string.ascii_letters, k=10))
        self.capacity = capacity
        self.arrival_time = None
        self.berthed_time = None
        self.departure_time = None

    def __str__(self):
        return self.code

    def __lt__(self, other):
        """To manage vessels in FIFO queue, we should arrange all of them by their availability time."""
        return self.arrival_time < other.arrival_time

    def arrive(self, *, time: float):
        """
        :param time: The time that the vessel arrive to port
        :return:
        """
        self.arrival_time = time
        logger.info(f"#{self.code} arrived at {time}")

    def berth(self, *, time: float, berth: str):
        """
        :param time: The time that the vessel berth at port
        :param berth: The name of slot that vessel berthed at it
        :return:
        """
        self.berthed_time = time
        logger.info(f"#{self.code} berthed in {berth} at {time}")

    def departure(self, *, time: float, berth: str):
        """
        :param time: The time that the vessel depart the port.
        :param berth: The name of slot that vessel berthed at it
        :return:
        """
        self.departure_time = time
        logger.info(f"#{self.code} departed the {berth} at {time}")
