# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology

from sklearn.base import TransformerMixin, BaseEstimator

from metaclass import MetaTask
from machine import Machine


class StatePredictionModel(BaseEstimator, TransformerMixin):

    def predict(self, metatask: MetaTask, machine: Machine, time: float):
        pass
