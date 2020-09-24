# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology

from typing import List

from machine import Machine
from task import Task


def load_coming_tasks(interval_time: float) -> List[Task]:
    """
    Load coming_tasks to servers, yields list of tasks
    Parameters
    ----------
    interval_time

    Returns
    -------

    """
    n_leap = 10
    n_tasks = 10

    for i in range(n_leap):
        coming_tasks = list()
        for j in range(n_tasks):
            coming_tasks.append(Task(str(i * n_leap + j), 0.1, 0.1, 0.1, i * interval_time))

        yield coming_tasks


def load_machines() -> List[Machine]:
    """
    Load the config to create machines in the datacenter
    Returns
    -------

    """
    n_machines = 10
    vm_list = list()
    for i in range(n_machines):
        vm_list.append(Machine(str(i), 1, 1, 1))
    return vm_list


if __name__ == '__main__':
    i = 0
    coming_tasks = load_coming_tasks(interval_time=60)
    while True:
        try:
            tasks = next(coming_tasks)
            print(tasks.__len__())
            i += 1
            print(tasks[0].task_id)
        except StopIteration:
            print("All tasks have come!")
            break
