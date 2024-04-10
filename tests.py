import unittest
import json


class MyTest(unittest.TestCase):
    def test_csv_column_count(self):
        with open('./profiles1.csv', 'r') as csv:
            first_line = csv.readline()
            ncol = first_line.count(',') + 1         
        self.assertEqual(12,ncol)

    def test_csv_row_count(self):
        with open('./profiles1.csv', 'r') as csv:
            nrows = len(csv.readlines())            
        self.assertGreater(nrows,90)

    def test_json_row_count(self):
        with open('./data.json', 'r') as f:
            data = json.load(f)      
            nrows =  len(data)
        self.assertGreater(nrows,90)     

    def test_json_columns(self):
        with open('./data.json', 'r') as f:
            data = json.load(f)      
            d1 = data[0]
        self.assertTrue("Givenname" in d1)             
        self.assertTrue("Surname" in d1)             
        self.assertTrue("Streetaddress" in d1)             
        self.assertTrue("StreetAddres2" in d1)             



if __name__ == '__main__':
    unittest.main()     