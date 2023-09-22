import random

import simpy

from entities.vessel import Vessel
from settings.logs import setup_logger

logger = setup_logger(__name__)


def vessel_generator(env, vessels_queue: simpy.PriorityStore):
    while True:
        yield env.timeout(random.expovariate(1 / 5))  # Exponential distribution for vessel arrivals
        vessel = Vessel()
        vessels_queue.put(vessel)  # Store the vessel that arrives in the queue
