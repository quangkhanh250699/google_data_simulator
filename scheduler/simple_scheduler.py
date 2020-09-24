# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology

from typing import List

from machine import Machine
from task import Task
from scheduler.scheduler import Scheduler


class SimpleScheduler(Scheduler):
    def schedule(self,
                 coming_tasks: List[Task],
                 running_tasks: List[Task],
                 mapper: dict,
                 machines: List[Machine]) -> dict:
        i = 0
        j = 0
        for i in range(len(coming_tasks)):
            mapper[coming_tasks[i].task_id] = machines[j].machine_id

        return mapper
