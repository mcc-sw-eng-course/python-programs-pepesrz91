import unittest

class Powerlist():
    items = []
    list_string = ""
    def add_item(self,item):
        self.items.append(item)

    def delete_item(self,index):
        self.items.pop(index)

    def sort(self): ## Works just for ints by the moment.
        new_list = []
        while self.items:
            minimum = self.items[0]
            for x in self.items:
                if x < minimum:
                    minimum = x
            new_list.append(minimum)
            self.items.remove(minimum)

        self.items = new_list
        return new_list

    def Lmerge(self,list):
        new_list = list + self.items
        return new_list

    def Rmerge(self, list):
        new_list = self.items + list
        return new_list

    def save(self, filename):

        s = str(self.items)
        with open(filename, 'w') as outfile:
            outfile.write(s)

    def restore_list(self, filename):
        with open(filename) as f:
            self.list_string = f.read()

            for s in self.list_string:
                if s == "[" or s == "]" or ",":
                    continue
                else:
                    self.items.append(s)

                return self.list_string

class TestCases(unittest.TestCase):

    def test_add_item(self):
        new = Powerlist()
        new.items = [1, 2, 4, 7, 3, 8, 9]
        self.assertEqual(new.items,[1, 2, 4, 7, 3, 8, 9])
        new.add_item(10)
        self.assertEqual(new.items,[1, 2, 4, 7, 3, 8, 9,10])

    def test_delete(self):
        new = Powerlist()
        new.items = [1, 2, 4, 7, 3, 8, 9]
        new.delete_item(0)
        self.assertEqual(new.items,[2, 4, 7, 3, 8, 9])

    def test_sort(self):
        new = Powerlist()
        new.items = [1,3,2]
        self.assertEqual(new.sort(),[1,2,3])

    def test_left_merge(self):
        new = Powerlist()
        new.items = [1, 2,3]
        self.assertEqual(new.Lmerge([0]),[0,1,2,3])

    def test_righ_merge(self):
        new = Powerlist()
        new.items = [1, 2, 3]
        self.assertEqual(new.Rmerge([0]), [1, 2, 3,0])


if __name__ == "__main__":
    unittest.main()