# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology

from typing import List

from machine import Machine


class Datacenter:
    """
    This class denote a datacenter with list of virtual machines
    """

    def __init__(self, vm_list=List[Machine]):
        """
        Parameters
        ----------
        vm_list
        """
        self.__vm_list = vm_list
        
    @property
    def vm_list(self):
        return self.__vm_list
    
    @vm_list.setter
    def vm_list(self, vm_list: list):
        self.__vm_list = vm_list


if __name__ == '__main__':
    pass
