# Port Simulator

- [Description](#Description)
- [Installation](#Installation)
- [Using](#Using)
  - [Manual](#Manual-Execution)
  - [Docker](#Docker)

## Description
This project simulate all processes that occur in a port.

## Installation
We use the `Python` for development and `Poetry` as the package manager.
To install the required packages and set up the project in your local environment, you can use the following commands:

```shell
pip install poetry
poetry install
```

## Using
Before anything else, you should generate your own config file. You can create it manually from configs.example.ini 
or use the following command:
```shell
make prepare-configs
```
Then you can run  the simulator in two ways:
1. Manual Execution
2. Docker

### Manual-Execution
You can run the project locally using the following "make" command:
```shell
make run
```

### Docker
You can run the simulator in a Docker container using these commands:
```shell
make build-image
make run-image
```
Alternatively, you can use the following command to run it automatically with Docker:
```shell
make run-docker
```
It's worth mentioning that the Docker image uses your `configs.ini` as the configuration file.
