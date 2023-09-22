class Truck(object):
    def __init__(self, *, number: int, operation_time: int):
        """
        :param operation_time: The needed time to drop off the container at the yard block and come back again
        """
        self.name = f"truck_{number}"
        self.operation_time = operation_time
        self.available_from = 0

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.available_from < other.available_from
