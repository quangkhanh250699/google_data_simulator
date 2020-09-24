# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology

from scheduler import Scheduler


class Broker:
    """
    This class receives task from users and distributes to virtual machines in datacenter.
    
    Attributes
    ----------
    scheduler: the scheduler making strategy to distribute tasks to machines
    vm_list: list of virtual machines managed by the broker
    coming_tasks: list of task submitted by users
    running_tasks: list of task running in the virtual machines
    log: dictionary recording execution time of tasks
    scheduling_table: dictionary map tasks to assigned machines

    """

    def __init__(self, scheduler: Scheduler):
        """
        Create a Broker with default values

        Parameters
        ----------
        scheduler
        """
        self.scheduler = scheduler
        self.vm_list = list()
        self.coming_tasks = list()
        self.running_tasks = list()
        self.log = dict()
        self.scheduling_table = dict()
        
    @property
    def vm_list(self):
        return self.__vm_list
    
    @vm_list.setter
    def vm_list(self, vm_list: list):
        self.__vm_list = vm_list

    @property
    def coming_tasks(self):
        return self.__coming_tasks

    @coming_tasks.setter
    def coming_tasks(self, coming_tasks: list):
        self.__coming_tasks = coming_tasks

    @property
    def running_tasks(self):
        return self.__running_tasks

    @running_tasks.setter
    def running_tasks(self, running_tasks: list):
        self.__running_tasks = running_tasks

    @property
    def log(self):
        return self.__log

    @log.setter
    def log(self, log: dict):
        self.__log = log

    @property
    def scheduling_table(self):
        return self.__scheduling_table

    @scheduling_table.setter
    def scheduling_table(self, scheduling_table: dict):
        self.__scheduling_table = scheduling_table
        
    @property
    def scheduler(self):
        return self.__scheduler
    
    @scheduler.setter
    def scheduler(self, scheduler: Scheduler):
        self.__scheduler = scheduler

    def submit_machines(self, machines: list):
        self.vm_list = machines

    def submit_tasks(self, coming_tasks: list):
        """
        Receive tasks from users and send to appropriate virtual machines.

        Parameters
        ----------
        coming_tasks

        Returns
        -------

        """
        self.coming_tasks.extend(coming_tasks)
        self.__schedule()
        self.running_tasks.extend(self.coming_tasks)
        self.coming_tasks = list()

    def update_log(self):
        completed_tasks = list()
        for task in self.running_tasks:
            if task.completion >= 1:
                self.log[task.task_id] = task.execution_time
                completed_tasks.append(task)

        for task in completed_tasks:
            self.running_tasks.remove(task)

    def __schedule(self):
        new_table = self.scheduler.schedule(self.coming_tasks,
                                            self.running_tasks,
                                            self.scheduling_table,
                                            self.vm_list)

        self.scheduling_table.update(new_table)


if __name__ == '__main__':
    pass
