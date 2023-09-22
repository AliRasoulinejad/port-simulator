from configparser import ConfigParser
from dataclasses import dataclass


@dataclass
class Basic:
    duration: int
    distribution_average_hours: int


@dataclass
class Logging:
    level: str


@dataclass
class Port:
    slots_count: int
    cranes_count: int
    trucks_count: int


@dataclass
class Vessel:
    default_capacity: int


@dataclass
class Crane:
    operation_time: int


@dataclass
class Truck:
    operation_time: int


@dataclass
class Settings:
    basic: Basic
    logging: Logging
    port: Port
    vessel: Vessel
    crane: Crane
    truck: Truck


def load_settings():
    config = ConfigParser()
    config.read('configs.ini')

    basic = Basic(
        duration=int(config["basic"]["duration"]),
        distribution_average_hours=int(config["basic"]["distribution_average_hours"]),
    )
    logging = Logging(level=config["logging"]["level"])
    port = Port(
        slots_count=int(config["port"]["slots"]),
        cranes_count=int(config["port"]["cranes"]),
        trucks_count=int(config["port"]["trucks"])
    )
    vessel = Vessel(default_capacity=int(config["vessel"]["default_capacity"]))
    crane = Crane(operation_time=int(config["crane"]["operation_time"]))
    truck = Truck(operation_time=int(config["truck"]["operation_time"]))

    return Settings(basic=basic, logging=logging, port=port, vessel=vessel, crane=crane, truck=truck)


# TODO: Singleton
Setting = load_settings()
