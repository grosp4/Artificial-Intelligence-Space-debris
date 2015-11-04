__author__ = 'Pedro'

import gain_dataset

def collectDataset():

    dataset1 = gain_dataset.Dataset()

    if dataset1.extractDataset():
        if dataset1.saveToFile():
            return 0

        else:
            return 2

    return 1

def teach():

    return 1