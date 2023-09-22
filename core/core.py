import random

import simpy

from entities.truck import Truck
from entities.vessel import Vessel
from settings.config import Setting
from settings.logs import setup_logger
from .port import Port

logger = setup_logger(__name__)


def vessel_generator(*, env, vessels_queue: simpy.PriorityStore):
    """
    This function generate random vessels. Its generation follow the exponential distribution.
    :param env: The base environment
    :param vessels_queue: A "FIFO" queue that stores all arrived vessels.
    :return: None
    """
    while True:
        yield env.timeout(random.expovariate(1 / Setting.basic.distribution_average_hours))  # Exponential distribution for vessel arrivals
        vessel = Vessel()
        vessel.arrive(time=env.now)
        vessels_queue.put(vessel)  # Store the vessel that arrives in the queue


def handle_vessels(*, env: simpy.Environment, port: Port, vessels_queue: simpy.PriorityStore):
    """
    :param env: The base environment
    :param port: Current port
    :param vessels_queue: A "FIFO" queue that stores all arrived vessels.
    :return:
    """
    while True:
        berth = yield port.slots.get()
        vessel = yield vessels_queue.get()
        vessel.berth(time=env.now, berth=berth)
        env.process(discharge_container(env=env, port=port, berth=berth, vessel=vessel))


def discharge_container(*, env: simpy.Environment, port: Port, berth: str, vessel: Vessel):
    """
    Main component that manages the containers discharging
    :param env: The base environment
    :param port: Current port
    :param berth: Occupied berth by the vessel
    :param vessel: Berthed vessel
    :return:
    """
    crane = yield port.cranes.get()
    for c_id in range(vessel.capacity):
        yield crane.discharge(vessel_code=vessel.code, container_id=c_id)
        truck = yield port.trucks.get()
        truck.load(time=env.now, vessel_code=vessel.code, container_id=c_id)
        env.process(move_container(env=env, port=port, truck=truck))

    crane.available(time=env.now)
    port.cranes.put(crane)
    port.slots.put(berth)
    vessel.departure(time=env.now, berth=berth)


def move_container(*, env: simpy.Environment, port: Port, truck: Truck):
    """
    This part manage the moving containers to yard-block by trucks and their returning back
    :param env: The base environment
    :param port: Current port
    :param truck: Specified truck to move the container to yard-block
    :return:
    """
    yield env.process(truck.move_container_to_yard_block())
    truck.available(time=env.now)
    port.trucks.put(truck)
