class Truck(object):
    def __init__(self, *, operation_time: int):
        """
        :param operation_time: The needed time to drop off the container at the yard block and come back again
        """
        self.operation_time = operation_time
