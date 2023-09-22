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
        vessel.berth(time=env.now, berth=berth)
        env.process(discharge_container(env=env, port=port, berth=berth, vessel=vessel))


def discharge_container(*, env: simpy.Environment, port: Port, berth: str, vessel: Vessel):
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
    yield env.process(truck.move_container_to_yard_block())
    truck.available(time=env.now)
    port.trucks.put(truck)
