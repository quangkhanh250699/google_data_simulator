# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology

from sklearn.base import BaseEstimator, RegressorMixin
from typing import List

from machine import Machine
from task import Task


class TimeCalculationModel(BaseEstimator, RegressorMixin):

    def predict(self, tasks: List[Task], machine: Machine):
        pass
