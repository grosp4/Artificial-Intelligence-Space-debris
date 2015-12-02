__author__ = 'Patrick'

from enum import Enum

class DataType(Enum):
    all = 1
    satellites = 2
    errors = 3


if __name__ == "__main__":

    type = DataType
    type.all