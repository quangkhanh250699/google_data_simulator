# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology

import pandas as pd

from broker import Broker
from scheduler import SimpleScheduler
from utilities import load_machines, load_coming_tasks, get_noise
from datacenter import Datacenter
from models import SimulationModel


class Simulator:
    """
    This class simulate running process in a datacenter
    """

    task_source: str

    def __init__(self, datacenter: Datacenter, broker: Broker, simulation_model: SimulationModel):
        self.clock = 0
        self.broker = broker
        self.datacenter = datacenter
        self.simulation_model = simulation_model
        self.interval_time = 60

    @property
    def clock(self):
        return self.__clock

    @clock.setter
    def clock(self, clock: float):
        self.__clock = clock

    @property
    def broker(self):
        return self.__broker

    @broker.setter
    def broker(self, broker: Broker):
        self.__broker = broker

    @property
    def datacenter(self):
        return self.__datacenter

    @datacenter.setter
    def datacenter(self, datacenter: Datacenter):
        self.__datacenter = datacenter

    @property
    def simulation_model(self):
        return self.__simulation_model

    @simulation_model.setter
    def simulation_model(self, simulation_model: SimulationModel):
        self.__simulation_model = simulation_model

    def run(self):
        """
        Run simulation to calculate execution time of tasks
        Returns
        -------

        """
        self.__update_state()
        self.broker.submit_machines(self.datacenter.vm_list)
        coming_tasks = load_coming_tasks(interval_time=self.interval_time,
                                         task_source=self.task_source)

        while True:
            try:
                tasks = next(coming_tasks)
            except StopIteration:
                pass
            self.broker.submit_tasks(coming_tasks=tasks)
            noise = get_noise()
            self.simulation_model.update(running_tasks=self.broker.running_tasks,
                                         machines=self.broker.vm_list,
                                         scheduling_table=self.broker.scheduling_table,
                                         noise=noise,
                                         interval_time=self.interval_time)
            self.broker.update_log()
            self.clock += self.interval_time
            if self.broker.running_tasks.__len__() == 0:
                break

    def print_log(self):
        log_df = pd.DataFrame(data={'time': pd.Series(self.broker.log)})
        print(log_df)

    def __update_state(self):
        self.clock = 0

    def __update_tasks(self):
        pass


if __name__ == '__main__':
    # Source of data
    machine_source = 'data/machine_attr.csv'
    task_source = 'data/task_info.csv'

    # Create instances
    vm_list = load_machines(machine_source)
    datacenter = Datacenter(vm_list=vm_list)
    scheduler = SimpleScheduler()
    broker = Broker(scheduler=scheduler)
    simulation_model = SimulationModel()
    simulator = Simulator(datacenter=datacenter, broker=broker, simulation_model=simulation_model)
    simulator.task_source = task_source

    # Simulate datacenter
    simulator.run()
    simulator.print_log()
