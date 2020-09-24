# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology

class Machine:
    def __init__(self, machine_id, cpu, memory, disk=1):
        """

        Parameters
        ----------
        machine_id: str
        cpu: float
        memory: float
        disk: float

        Returns
        -------
        Machine
        """

        self.__machine_id = machine_id
        self.cpu = cpu
        self.memory = memory
        self.disk = disk

    @property
    def machine_id(self):
        return self.__machine_id

    @machine_id.setter
    def machine_id(self):
        raise Exception("Cannot assign value for machine_id after creating")

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, cpu):
        if cpu < 0:
            raise ValueError("Value should not be negative")
        self.__cpu = cpu

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, memory):
        if memory < 0:
            raise ValueError("Value should not be negative")
        self.__memory = memory

    @property
    def disk(self):
        return self.__disk

    @disk.setter
    def disk(self, disk):
        if disk < 0:
            raise ValueError("Value should not be negative")
        self.__disk = disk
