import simpy

from entities.crane import Crane
from entities.truck import Truck
from settings.config import Setting


class Port(object):
    def __init__(self, *, env: simpy.Environment, slots_count: int, cranes_count: int, trucks_count: int):
        """
        :param env:
        :param slots_count: The number of slots
        :param trucks_count: The number of trucks
        """
        self.env = env
        self.slots = simpy.PriorityStore(env=env, capacity=slots_count)
        self.slots.items = [f"berth_{i + 1}" for i in range(cranes_count)]
        # Crane resources
        self.cranes = simpy.PriorityStore(env=env, capacity=cranes_count)
        self.cranes.items = [
            Crane(env=env, number=i, operation_time=Setting.crane.operation_time) for i in range(cranes_count)
        ]
        # Truck resources
        self.trucks = simpy.PriorityStore(env=env, capacity=trucks_count)
        self.trucks.items = [
            Truck(env=env, number=i, operation_time=Setting.truck.operation_time) for i in range(trucks_count)
        ]
