from statistics import median
from array import array

class Array:
    '''
    This is a single-dimensional numeric
    array for scientific computing.

    This array will compute lots of
    basic statistics.

    Attributes
    ----------
    data: list
        List of numbers

    Methods
    -------
    TODO
    '''


    def __init__(self, data):
        # b - boolean (1 byte integer)
        # q - interger (4 bytes)
        # d - float (8 bytes)
        self.data = array('d', data)

    def sum(self):
        '''
        Sums all the values in the array

        Returns
        -------
        int or float
        '''
        return sum(self.data)

    def max(self):
        '''
        Finds max of all values in the array

        Returns
        -------
        int or float
        '''
        return max(self.data)

    def min(self):
        '''
        Finds min of all values in the array

        Returns
        -------
        int or float
        '''
        return min(self.data)

    def mean(self):
        '''
        Finds mean of all values in the array

        Returns
        -------
        int or float
        '''
        return self.sum() / len(self.data)

    def median(self):
        '''
        Finds median of all values in the array

        Returns
        -------
        int or float
        '''
        return median(self.data)