import io
import json
import unittest

class User_Manager:

    def __init__(self):
        self.records = {}

    def create_record(self, record):
        new_user = len(self.records) + 1
        new_user = "user{}".format(new_user)
        self.records[new_user] = record

    def get_records(self, dict):
        self.records = dict

    def save_records(self):
        print(type(self.records))
        s = json.dumps(self.records)

        with open('data.json', 'w') as outfile:
            outfile.write(s)

    def restore_records(self):
        with open('data.json') as f:
            self.records = json.load(f)

    def look_record(self, record):
        for r in self.records:
            if r == record:
                print("Record Found!")
                return self.records[r]
            else:
                print("No record was found")

class TestCases(unittest.TestCase):
    def test_create_user_manager(self):
        um = User_Manager()
        self.assertEqual(um, um)
        self.assertEqual(um.records,{})


    def test_create_record(self):
        record = {"name": "Pepe", "address": "Paseo del Valle", "phone": 3332142324, "email": "pepe@p.com"}
        um = User_Manager()
        um.create_record(record)
        self.assertEqual(um.records['user1'],record)

    def test_errors_us(self):
        um = User_Manager()
        with self.assertRaises(Exception):
            um.create_record()
        with self.assertRaises(Exception):
            um.create_record()

    def test_get_records(self):
        record = {"name": "Pepe", "address": "Paseo del Valle", "phone": 3332142324, "email": "pepe@p.com"}
        um = User_Manager()
        um.create_record(record)
        um2 = User_Manager()
        um2.create_record(record)
        self.assertEqual(um.get_records("user1"), um2.get_records("user1"))

    def test_save_record(self):
        record = {"name": "Pepe", "address": "Paseo del Valle", "phone": 3332142324, "email": "pepe@p.com"}
        um = User_Manager()
        um2 = User_Manager()
        um2.create_record(record)
        um2.save_records()
        um.restore_records()
        self.assertEqual(um.records,um2.records)


if __name__ == "__main__":
    unittest.main()