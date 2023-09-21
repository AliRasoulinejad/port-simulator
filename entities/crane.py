class Crane(object):
    def __init__(self, *, operation_time: int):
        """
        :param operation_time: The needed time for each crane to move a container, in seconds
        """
        self.operation_time = operation_time
