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

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        # recursion
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


        return alist

def merge_sort(dataframe,column):
    alist = dataframe[column].values.tolist()
    mergeSort(alist)
    dataframe[column] = alist

def quickSort(alist):

  quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):

  if first<last:
      splitpoint = partition(alist,first,last)
      quickSortHelper(alist,first,splitpoint-1)
      quickSortHelper(alist,splitpoint+1,last)
def quick_sort(dataframe,column):
    alist = dataframe[column].values.tolist()
    quickSort(alist)
    dataframe[column] = alist

def partition(alist,first,last):

  pivotvalue = alist[first]
  leftmark = first+1
  rightmark = last
  done = False

  while not done:
      while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
          leftmark = leftmark + 1

      while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
          rightmark = rightmark -1

      if rightmark < leftmark:
          done = True
      else:
          temp = alist[leftmark]
          alist[leftmark] = alist[rightmark]
          alist[rightmark] = temp

  temp = alist[first]
  alist[first] = alist[rightmark]
  alist[rightmark] = temp

  return rightmark

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

    data_set1 = {1:[2,3,1,4,5,6,7,8,9],
                 2:[1,2,3,4,5]}

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

    "COLUMNS MUST CONTAIN NUMBERS"
    def test_mergeSort(self):
        new_table = pandas.read_csv('data.csv')
        df = pandas.read_csv('data.csv')
        new_array = df.sort_values(['Reviews'],kind="mergesort")
        merge_sort(new_table,'Reviews')
        self.assertEqual(new_table['Reviews'].values.tolist() == new_array['Reviews'].values.tolist(),True)

    """TESTS FOR QUICKSORT"""
    def test_quick_sort(self):
        new_table = pandas.read_csv('data.csv')
        quick_sort(new_table,'Reviews')
        df = pandas.read_csv('data.csv')
        new_array = df.sort_values(['Reviews'],kind='quicksort')
        self.assertEqual(new_table['Reviews'].values.tolist() == new_array['Reviews'].values.tolist(), True)

    def test_type_quick_sort(self):
        new_table = pandas.read_csv('data.csv')
        with self.assertRaises(Exception):
            quick_sort(new_table, '')
        with self.assertRaises(NameError):
            quick_sort(new_table, name)
        with self.assertRaises(KeyError):
            quick_sort(new_table, 0)

    def test_right_sort(self):
        new_table = pandas.read_csv('data.csv')
        quick_sort(new_table, 'Reviews')
        df = pandas.read_csv('data.csv')
        new_array = df.sort_values(['Reviews'], kind='mergesort')
        self.assertEqual(new_table['Reviews'].values.tolist() == new_array['Reviews'].values.tolist(), True)












if __name__ == "__main__":
    unittest.main()
