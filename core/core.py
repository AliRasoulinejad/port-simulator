import random

import simpy

from entities.truck import Truck
from entities.vessel import Vessel
from settings.logs import setup_logger
from .port import Port

logger = setup_logger(__name__)


def vessel_generator(*, env, vessels_queue: simpy.PriorityStore):
    while True:
        yield env.timeout(random.expovariate(1 / 5))  # Exponential distribution for vessel arrivals
        vessel = Vessel()
        vessel.arrive(time=env.now)
        vessels_queue.put(vessel)  # Store the vessel that arrives in the queue


def handle_vessels(*, env, port: Port, vessels_queue: simpy.PriorityStore):
    while True:
        berth = yield port.slots.get()
        vessel = yield vessels_queue.get()
        vessel.berth(time=env.now, berth_name=berth)
        env.process(discharge(env=env, port=port, vessel=vessel))


def discharge(*, env: simpy.Environment, port: Port, vessel: Vessel):
    crane = yield port.cranes.get()
    for c_id in range(vessel.capacity):
        yield crane.discharge(vessel_code=vessel.code, container_id=c_id)
        truck = yield port.trucks.get()
        logger.info(f"container #{c_id} loaded to {truck.name} at {env.now}")
        env.process(move_container(env=env, port=port, truck=truck))

    crane.available_from = env.now
    port.cranes.put(crane)
    vessel.departure(time=env.now)


def move_container(*, env: simpy.Environment, port: Port, truck: Truck):
    yield env.process(port.move_container_to_yard_block(truck=truck))
    logger.info(f"{truck.name} returned back to the port at {env.now}")

    truck.available_from = env.now
    port.trucks.put(truck)
