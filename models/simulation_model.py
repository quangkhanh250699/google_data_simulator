# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology

from typing import List

from task import Task
from machine import Machine
from utilities import Noise


class SimulationModel:

    def __init__(self):
        pass 

    def update(self,
               running_tasks: List[Task],
               machines: List[Machine],
               scheduling_table: dict,
               noise: Noise,
               interval_time: float):

        total_time = 420.0
        for task in running_tasks:
            completion = task.completion + interval_time / total_time
            if completion > 1.01:
                gap = 1 - task.completion
                task.completion = 1.01
                task.execution_time = task.execution_time + gap * total_time
            else:
                task.execution_time += interval_time
                task.completion = completion

    def __update_single_machine(self, tasks, machines, noise, interval_time):
        pass
