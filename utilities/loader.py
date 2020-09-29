# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology

import pandas as pd

from typing import List

from machine import Machine
from task import Task


def __find_pavot(times, value, head, tail):
    if head > tail:
        return tail
    mid = (head + tail) // 2
    if mid == head:
        return mid
    if times[mid] > value:
        return __find_pavot(times, value, head, mid)
    else:
        return __find_pavot(times, value, mid+1, tail)


def __make_tasks(task_df: pd.DataFrame) -> List[Task] :
    tasks = []
    for _, row in task_df.iterrows():
        task = Task(task_id=row.task_id,
                    cpu_request=row.cpu_request,
                    memory_request=row.memory_request,
                    disk_request=row.disk_space_request,
                    coming_time=row.time)
        tasks.append(task)
    return tasks


def load_coming_tasks(interval_time: float, task_source: str):
    """
    Load coming_tasks to servers, yields list of tasks
    """

    task_df = pd.read_csv(task_source)
    head = task_df.index[0]
    tail = task_df.index[-1]
    next_time = 0

    while head < tail:
        next_time += interval_time
        mid = __find_pavot(task_df.time, next_time, head, tail)
        inter_tasks = task_df.iloc[head:mid+1]
        head = mid+1
        yield __make_tasks(inter_tasks)


def load_machines(machine_source: str) -> List[Machine]:
    """
    Load the config to create machines in the datacenter
    Returns
    -------

    """

    machines = []
    machine_df = pd.read_csv(machine_source)
    for _, row in machine_df.iterrows():
        machine = Machine(row.machine_id, row.cpus, row.memory)
        machines.append(machine)
    return machines


if __name__ == '__main__':
    machines = load_machines('../data/machine_attr.csv')
    print(machines.__len__())

    # coming_tasks = load_coming_tasks(interval_time=600,
    #                                  task_source='../data/task_info.csv')
    # while True:
    #     try:
    #         tasks = next(coming_tasks)
    #         print(len(tasks))
    #     except StopIteration:
    #         print("All tasks have come!")
    #         break
