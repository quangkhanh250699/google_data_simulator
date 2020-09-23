# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology

from typing import List

from task import Task
from machine import Machine
from utilities import Noise


class SimulationModel:

    def update(self,
               running_tasks: List[Task],
               machines: List[Machine],
               scheduling_table: dict,
               noise: Noise,
               time: float):

        pass
