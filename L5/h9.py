import unittest


def int_to_roman(i):
    numeral_map = zip(
        (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
        ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    )

    result = []
    for integer, numeral in numeral_map:
        count = int(i / integer)
        result.append(numeral * count)
        i -= integer * count
    return ''.join(result)

# print(int_to_roman(967))

class TestCases(unittest.TestCase):

    def test_roman_right(self):
        self.assertEqual(int_to_roman(100),'C')
        self.assertEqual(int_to_roman(3),'III')

    def test_roman_type(self):
        with self.assertRaises(TypeError):
            int_to_roman()
        with self.assertRaises(TypeError):
            int_to_roman("")


if __name__ == "__main__":
    unittest.main()