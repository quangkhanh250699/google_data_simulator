# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology

class Task:
    """
    Denote a task submitted to servers.
    """

    def __init__(self, task_id, cpu_request, memory_request, disk_request, coming_time):
        """
        Create task with basic information.

        Parameters
        ----------
        task_id: string
        cpu_request: float
        memory_request: float
        disk_request: float
        coming_time: float

        """
        self.task_id = task_id
        self.cpu_request = cpu_request
        self.memory_request = memory_request
        self.disk_request = disk_request
        self.coming_time = coming_time
        self.completion = -1
        self.priority = -1

    @property
    def task_id(self):
        return self.__task_id

    @task_id.setter
    def task_id(self, task_id):
        self.__task_id = task_id

    @property
    def cpu_request(self):
        return self.__cpu_request
    
    @cpu_request.setter
    def cpu_request(self, cpu_request: float):
        if cpu_request < 0:
            raise ValueError("Cpu_request cannot be negative value")
        self.__cpu_request = cpu_request

    @property
    def memory_request(self):
        return self.__memory_request

    @memory_request.setter
    def memory_request(self, memory_request: float):
        if memory_request < 0:
            raise ValueError("memory_request cannot be negative value")
        self.__memory_request = memory_request


    @property
    def disk_request(self):
        return self.__disk_request

    @disk_request.setter
    def disk_request(self, disk_request: float):
        if disk_request < 0:
            raise ValueError("disk_request cannot be negative value")
        self.__disk_request = disk_request

    @property
    def coming_time(self):
        return self.__coming_time

    @coming_time.setter
    def coming_time(self, coming_time: float):
        if coming_time < 0:
            raise ValueError("coming_time cannot be negative value")
        self.__coming_time = coming_time


if __name__ == '__main__':
    pass
