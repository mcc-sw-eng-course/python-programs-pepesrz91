import csv
import pandas
import unittest

def set_input_data(name):
    return pandas.read_csv(name)

with open ('data.csv') as data:
    print(data)
    new_table = pandas.read_csv('data.csv')
    print(new_table.head())


class Read_Tests(unittest.TestCase):

    def test_read_cvs(self):
        new_table = pandas.read_csv('data.csv')
        another_table = pandas.read_csv('data.csv')
        self.assertEqual(new_table.empty, False)
        self.assertEqual(new_table.equals(another_table), True)

    def test_set_input_data(self):
        first_table = set_input_data('data.csv')
        new_table = pandas.read_csv('data.csv')
        self.assertEqual(first_table.equals(new_table), True)



if __name__ == "__main__":
    unittest.main()
