"""
This module is responsible for sampling.

Type of sampling:
1. Simple Random Sampling
2. Stratified Random Sampling
3. Clustered Random Sampling
4. Systematic Random Sampling
5. Non-Random / convinient sampling
"""


class Sample:
    def __init__(self):
        """
        """
        self._df = None

    def _simple_random_sampling(self):
        """
        Calculate simple random sampling
        """
        raise NotImplementedError

    def _stratified_random_sampling(self):
        """
        Calculate Stratified Random Sampling
        """
        raise NotImplementedError

    def _clustered_random_sampling(self):
        """
        Calculate Clustered Random Sampling
        """
        raise NotImplementedError

    def _systematic_random_sampling(self):
        """
        Calculate Systematic Random Sampling
        """
        raise NotImplementedError

    def _convinent_sampling(self):
        """
        Calculate Non-Random / convinient sampling
        """
        raise NotImplementedError

    def get_sampling(self, df, sampling_mechanism, sample_size):
        """
        Apply the sampling mechanism to get the demo sample
        """
        raise NotImplementedError
