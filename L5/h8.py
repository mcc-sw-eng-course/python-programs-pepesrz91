from math import *
import unittest
import statistics
import numpy

def mean(list):
    sum = 0
    for i in list:
        sum += i
    mean = sum / len(list)

    return mean

def standardDeviation(list):
    sum = 0

    for i in list:
        sum += i
    mean = sum / len(list)

    sum_sd = 0
    for i in list:
        sum_sd += (i - mean)**2

    sum_sd = sum_sd / len(list)
    sd = sqrt(sum_sd)

    return sd

def median(list):
    list.sort()
    i_median = len(list)
    if i_median % 2 == 0:
        i_median = int(i_median/2)
        value = (list[i_median] + list[i_median + 1]) / 2
    else:
        value = list[i_median//2]

    return value


def quartile(list):
    list.sort()
    quartiles = []
    median_list = median(list)
    index = list.index(median_list)
    quartiles.append(median(list))

    first_quartile = median(list[:index])
    quartiles.append(first_quartile)

    third_quartile = median(list[index:])
    quartiles.append(third_quartile)

    counter = 1
    for i in quartiles:
        print("{} quartile: {}".format(counter, i))
        counter += 1

    return quartiles

def percentile(p,list):

    return (p / 100)*(len(list) + 1)


class TestCases(unittest.TestCase):
    """
      Tests to check if the mean  function is working correctly.
      Checking the Right - BICEP
      Boundaries
      """

    def test_mean_ints(self):
        self.assertEqual(mean([1,2,3]),2.0) # Results Right
        self.assertEqual(mean([1,2,3]), 2)
        self.assertEqual(mean([1,2,3]), statistics.mean([1,2,3])) #CROSS CHECK

    def test_mean_type(self):
        with self.assertRaises(TypeError): #Force errors
            mean(["2","2","4"])
        with self.assertRaises(TypeError):
            statistics.mean(["hola","2","4"])
        with self.assertRaises(TypeError):
            mean(1)
        with self.assertRaises(TypeError):
            mean([1,2,3,[1,2,3]])

    def test_mean_value(self):
        with self.assertRaises(Exception): # Boundaries
            mean()

    """
    Tests to check if the standard deviation function is working correctly.
    Checking the Right - BICEP
    Boundaries
    """

    def test_standard_deviation_right(self):
        self.assertEqual(standardDeviation([1,2,3]),0.816496580927726)
        self.assertEqual(standardDeviation([1,2,3]),statistics.pstdev([1,2,3]))

    def test_standard_deviation_type(self):
        with self.assertRaises(Exception):
            standardDeviation("Hello")
        with self.assertRaises(TypeError):
            standardDeviation(1234)

    def test_standard_deviation_boundaries(self):
        with self.assertRaises(TypeError):
            standardDeviation()

    """
    Tests to check if the median function is working correctly.
    Checking the Right - BICEP
    Boundaries
    """

    def test_median_right(self):
        self.assertEqual(median([1,2,3,3,4,5]),statistics.median([1,2,3,4,5,5]))
        self.assertEqual(median([1,2,3,4,5,6,7]),4)

    def test_median_type(self):
        with self.assertRaises(Exception):
            median("12234")
        with self.assertRaises(AttributeError):
            median(12345)

    def test_median_boundaries(self):
        with self.assertRaises(Exception):
            median()

    """
    Tests to check if the median function is working correctly.
    Checking the Right - BICEP
    Boundaries
    """

    def test_quartile_right(self):
        self.assertEqual(quartile([1,2,3,4,5,6,7,8,9])[0],numpy.percentile([1,2,3,4,5,6,7,8,9],50))
        self.assertEqual(quartile([1,2,3,4,5,6,7,8,9])[2],numpy.percentile([1,2,3,4,5,6,7,8,9],75))
        # self.assertEqual(quartile([1,2,3,4,5,6,7,8,9])[1],numpy.percentile([1,2,3,4,5,6,7,8,9],25))

    def test_percentile_right(self):
        self.assertEqual(percentile(50,[1,2,3,4,5,6,7]),numpy.percentile([1,2,3,4,5,6,7],50))
        # self.assertEqual(percentile(25, [1, 2, 3, 4, 5, 6, 7, 8]), numpy.percentile([1, 2, 3, 4, 5, 6, 7,8], 25))

if __name__ == "__main__":
    unittest.main()