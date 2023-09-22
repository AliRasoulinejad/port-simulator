import simpy

from settings.logs import setup_logger

logger = setup_logger(__name__)


class Crane(object):
    def __init__(self, *, env: simpy.Environment, number: int, operation_time: int):
        """
        :param env: The environment that crane work on
        :param number: The number of crane
        :param operation_time: The needed time for each crane to move a container, in seconds
        """
        self.env = env
        self.name = f"crane_{number}"
        self.operation_time = operation_time
        self.available_from = 0

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.available_from < other.available_from

    def discharge(self, *, vessel_code: str, container_id: int) -> simpy.Timeout:
        """
        :param vessel_code: The code on vessel thar is discharging
        :param container_id: The number of container which the crane is moving
        """
        logger.info(f"container #{container_id} discharged from vessel #{vessel_code} by {self.name} at {self.env.now}")
        return self.env.timeout(self.operation_time)
