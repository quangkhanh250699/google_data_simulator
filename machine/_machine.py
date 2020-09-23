# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology

class Machine:
    def __init__(self, id, cpu, memory, disk=1):
        """

        Parameters
        ----------
        cpu: the normalized cpu value of the machine
        memory: the normalized memory value of the machine
        disk: the disk space of the machine

        Returns
        -------
        Machine
        """

        self.__id = id
        self.cpu = cpu
        self.memory = memory
        self.disk = disk

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self):
        raise Exception("Cannot assign value for id after creating")

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
