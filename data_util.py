"""
Filename: data_util.py
Maintainers: x.huang

A data util for Kaggle competition 2019 Summer.

"""

import numpy as np


class DataLoader:
    # TODO
    pass


class DataSampler:

    def __init__(self):
        pass

    def sample(self):
        # TODO
        pass

    @staticmethod
    def reservoir_sample(it, sample_size):
        """
        Input an iterator with len and size to sample.
        Only return sampled data in-order.

        Parameters
        ----------
        it: Iterator of data to sample.
        sample_size: size to keep.

        Returns
        -------
        pool: sampled data. If len(it) < sample_size, return all data.
        """
        pool = [None] * sample_size
        npool = 0

        for i in it:
            if npool < sample_size:
                pool[npool] = i
            else:
                rand = np.random.randint(npool + 1)
                if rand < sample_size:
                    pool[rand] = i
            npool += 1

        if npool < sample_size:
            pool = pool[:npool]
        return pool

    @staticmethod
    def reservoir_split(it, sample_size):
        """
        TODO: (Do we have something in numpy to use directly...?)
        Input an iterator with len and size to sample.
        Data not sampled are returned.

        Parameters
        ----------
        it: Iterator of data to sample. Assume len(it) can be retrieved.
        sample_size: size to keep.

        Returns
        -------
        pool: sampled data. If len(it) < sample_size, return all data.
        unsampled: data not chosen.
        """
        pass


# TEMP: Test Cases
if "__main__" == __name__:
    # data = [1, 2, 3, 'a', 'b', DataSampler(), 'c', 5, DataLoader()]
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    data_sampler = DataSampler()

    # DataSampler.reservoir_sample: functionality
    for i in range(len(data) + 2):
        print(data_sampler.reservoir_sample(data, i))
    # DataSampler.reservoir_sample: distribution
    count = {}
    for i in data:
        count[i] = 0
    nturn = 10000
    for i in range(len(data) * nturn):
        for s in data_sampler.reservoir_sample(data, i % len(data)):
            count[s] += 1
    print(count)
    exp = (len(data) - 1) / 2 * nturn
    stdd = 0
    for k in count.keys():
        stdd += (count[k] - exp) * (count[k] - exp)
        count[k] = int((count[k] - exp) / exp * 10000)
    print(count)
    print(f"Stdd: {np.sqrt(stdd / exp):.4f}")
