# Author: Truong Quang Khanh
# Institute: Hanoi University of Science and Technology

from sklearn.base import BaseEstimator, TransformerMixin

from metaclass import MetaTask, MetaMachine


class IntervalTimeModel(BaseEstimator, TransformerMixin):

    def predict(self, matatask: MetaTask, metamachine: MetaMachine):
        pass
