from configparser import ConfigParser
from dataclasses import dataclass


@dataclass
class Basic:
    Time: int


@dataclass
class Logging:
    Level: str


@dataclass
class Settings:
    Basic: Basic
    Logging: Logging


def load_settings():
    config = ConfigParser()
    config.read('configs.ini')

    basic = Basic(Time=int(config["basic"]["time"]))
    logging = Logging(Level=config["logging"]["level"])

    return Settings(basic, logging)


# TODO: Singleton
Setting = load_settings()
