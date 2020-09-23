# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology


class MetaTask:
    """
    The class is synthesis of lists of tasks.

    Attributes
    ----------
    cpu_request: float
    memory_request: float
    disk_request: float
    power: float
    """

    def __init__(self):
        self.cpu_request = -1
        self.memory_request = -1
        self.disk_request = -1
        self.power = -1

    @property
    def cpu_request(self):
        return self.__cpu_request

    @cpu_request.setter
    def cpu_request(self, cpu_request: float):
        self.__cpu_request = cpu_request

    @property
    def memory_request(self):
        return self.__memory_request

    @memory_request.setter
    def memory_request(self, memory_request: float):
        self.__memory_request = memory_request

    @property
    def disk_request(self):
        return self.__disk_request

    @disk_request.setter
    def disk_request(self, disk_request: float):
        self.__disk_request = disk_request

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power: float):
        self.__power = power
