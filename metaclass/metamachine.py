# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology


class MetaMachine:
    """
    This class is synthesis of virtual machines.

    Attributes
    ----------
    quantity: int
    sum_cpu: float
    sum_memory: float
    sum_disk: float
    """

    def __init__(self):
        self.quantity = 0
        self.sum_cpu = 0
        self.sum_memory = 0
        self.sum_disk = 0
        
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity
        
    @property
    def sum_cpu(self):
        return self.__sum_cpu
    
    @sum_cpu.setter
    def sum_cpu(self, sum_cpu: float):
        self.__sum_cpu = sum_cpu
        
    @property
    def sum_memory(self):
        return self.__sum_memory
    
    @sum_memory.setter
    def sum_memory(self, sum_memory: float):
        self.__sum_memory = sum_memory
        
    @property
    def sum_disk(self):
        return self.__sum_disk
    
    @sum_disk.setter
    def sum_disk(self, sum_disk: float):
        self.__sum_disk = sum_disk
