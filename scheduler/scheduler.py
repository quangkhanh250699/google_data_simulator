# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology

import abc


class Scheduler(metaclass=abc.ABCMeta):
    """
    This class implements task scheduling algorithm to assign tasks to machines
    """

    def __init__(self):
        pass

    @abc.abstractmethod
    def schedule(self, coming_tasks: list, running_tasks: list, mapper: dict, machines: list) -> dict:
        """

        Parameters
        ----------
        coming_tasks
        running_tasks
        mapper
        machines

        Returns
        -------

        """

        raise NotImplementedError("Must implement schedule()")