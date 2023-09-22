import simpy

from core.core import vessel_generator, handle_vessels
from core.port import Port
from settings.config import Setting

if __name__ == "__main__":
    env = simpy.Environment()
    vessels_queue = simpy.PriorityStore(env)
    env.process(vessel_generator(env=env, vessels_queue=vessels_queue))  # generate vessels

    port = Port(
        env=env,
        slots_count=Setting.port.slots_count,
        cranes_count=Setting.port.cranes_count,
        trucks_count=Setting.port.trucks_count
    )
    env.process(handle_vessels(env=env, port=port, vessels_queue=vessels_queue))

    env.run(until=Setting.basic.duration)
