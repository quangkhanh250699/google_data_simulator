# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology

from sklearn.base import BaseEstimator, TransformerMixin
from typing import List

from task import Task


class SynthesisModel(BaseEstimator, TransformerMixin):

    def transform(self, tasks: List[Task]):
        pass
