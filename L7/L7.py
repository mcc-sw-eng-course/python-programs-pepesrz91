import csv
import pandas
import unittest

data_set = {'Name':["Pepe","Jose","Bob","Bill","Jacob"],
            "Age":[26,28,29,30,39],
            "Favorite Foods":[['Pizza',"Sushi"],["Pasta","Cheesecake"],["Fish"],["Potatoes","Pizza"],["Shrimps"]]}

def set_input_data(name):
    if name.endswith('.csv'):
        return pandas.read_csv(name)
    else:
        raise ValueError("File must have .csv extension")

def set_output_data(data_set, file_name):
    df = pandas.DataFrame(data_set)
    if file_name.endswith('.csv'):
        df.to_csv(file_name)
    else:
        raise ValueError("File must have .csv extension")

def merge_merge_sort(column, dataset):
    df = pandas.DataFrame(data_set)
    return  df.sort_values(by=[column])

with open ('data.csv') as data:
    print(data)
    new_table = pandas.read_csv('data.csv')
    print(new_table.head())


class Read_Tests(unittest.TestCase):

    data_set = {'Name': ["Pepe", "Jose", "Bob", "Bill", "Jacob"],
                "Age": [26, 28, 29, 30, 39],
                "Favorite Foods": [['Pizza', "Sushi"], ["Pasta", "Cheesecake"],
                                   ["Fish"], ["Potatoes", "Pizza"],["Shrimps"]]}
    data_set2 = {'Location': ["QTR", "YCT", "MEX", "JAL", "CHP"],
                "phone": [3335675454, 3331896565, 333909087, 3336655, 3331897656],
               }

    """
    All the unit tests cases for the set_input_data function
    """
    def test_read_cvs(self):
        new_table = pandas.read_csv('data.csv')
        another_table = pandas.read_csv('data.csv')
        self.assertEqual(new_table.empty, False)
        self.assertEqual(new_table.equals(another_table), True)

    def test_set_input_data(self):
        first_table = set_input_data('data.csv')
        new_table = pandas.read_csv('data.csv')
        self.assertEqual(first_table.equals(new_table), True)

    def test_file_not_found(self):
        with self.assertRaises(ValueError):
            set_input_data('hola')

    def test_file_type_error(self):
        with self.assertRaises(ValueError):
            set_input_data('hola.txt')
        self.assertRaisesRegex(ValueError,'File must have .csv extension')

    def test_file_type(self):
       with self.assertRaises(AttributeError):
           set_input_data(0)

    """
    All the test cases for the 
    """

    def test_write_data(self):
        set_output_data(self.data_set,'data1.csv')
        new_data = pandas.read_csv('data1.csv')
        self.assertEqual(new_data.empty, False)

    def test_read_data(self):
        set_output_data(self.data_set,'data1.csv')
        id = set_input_data('data1.csv')
        set_output_data(self.data_set,'data2.csv')
        id2 = set_input_data('data2.csv')
        self.assertEqual(id.equals(id2),True)

    def test_arguments_validation(self):
        with self.assertRaises(AttributeError):
            set_input_data(0)
        with self.assertRaises(ValueError):
            set_output_data(self.data_set,"hola")
        with self.assertRaises(TypeError):
            set_output_data()

    """
        Unit tests for the merge of the lists
    """

    def test_sort_right(self):
        df = pandas.DataFrame(data_set)
        self.assertEqual(merge_merge_sort('Name',data_set).equals(df.sort_values(['Name'])), True )
        self.assertEqual(merge_merge_sort('Name',data_set).empty, False)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            merge_merge_sort(0)

    def test_invalid_inputs(self):
        with self.assertRaises(KeyError):
            merge_merge_sort('','hello')
        with self.assertRaises(TypeError):
            merge_merge_sort()
        with self.assertRaises(KeyError):
            merge_merge_sort("",data_set)




if __name__ == "__main__":
    unittest.main()
