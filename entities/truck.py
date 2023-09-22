import simpy
import typing

from settings.logs import setup_logger

logger = setup_logger(__name__)


class Truck(object):
    def __init__(self, *, env: simpy.Environment, number: int, operation_time: int):
        """
        :param env: The environment that truck work on
        :param operation_time: The needed time to drop off the container at the yard block and come back again
        """
        self.env = env
        self.name = f"truck_{number}"
        self.operation_time = operation_time
        self.available_from = 0

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.available_from < other.available_from

    def available(self, *, time: float):
        self.available_from = time
        logger.info(f"{self.name} returned back to the port at {time}")

    def load(self, *, time: float, vessel_code: str, container_id: int):
        logger.info(f"container #{container_id} of #{vessel_code} loaded to {self.name} at {time}")

    def move_container_to_yard_block(self) -> typing.Generator:
        yield self.env.timeout(self.operation_time)
