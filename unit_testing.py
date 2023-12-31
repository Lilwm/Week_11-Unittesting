# -*- coding: utf-8 -*-
"""Unit testing

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rrd9lr1SBfMeVnEkaASgdh1tjoA0fEnW

Below is the starting code that includes the data pipeline functions. You should focus on writing unit tests for these functions using the unittest framework.
"""

import pandas as pd
import unittest

def data_extraction(file_path):
    data = pd.read_csv(file_path)
    return data

def data_transformation(data):
    data = data.drop_duplicates()
    data['billing_amount'] = data['billing_amount'].str.replace('$', '').astype(float)
    data['total_charges'] = data['billing_amount'] + data['tax_amount']
    return data

def data_loading(data, output_file):
    data.to_csv(output_file, index=False)

class TestDataPipeline(unittest.TestCase):
    def setUp(self):
        # Set up any necessary test data
        self.input_file = 'billing_data.csv'
        self.output_file = 'transformed_data.csv'

    def test_data_extraction(self):
        # Test data_extraction function
        data = data_extraction(self.input_file)

        # Check if the returned object is a DataFrame
        self.assertIsInstance(data, pd.DataFrame)

        # Check if the DataFrame has the expected columns
        expected_columns = ['customer_id', 'billing_amount', 'tax_amount']
        self.assertEqual(list(data.columns), expected_columns)

        # Check if the DataFrame has non-null values in all columns
        self.assertTrue(data.notnull().values.all())

        # Check if the DataFrame has at least one row
        self.assertGreater(len(data), 0)

    def test_data_transformation(self):
        # Test data_transformation function
        input_data = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'billing_amount': ['$100.50', '$200.75', '$300.25'],
            'tax_amount': [10.05, 20.10, 30.15]
        })

        expected_data = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'billing_amount': [100.50, 200.75, 300.25],
            'tax_amount': [10.05, 20.10, 30.15],
            'total_charges': [110.55, 220.85, 330.40]
        })

        # Call the function and get the result
        result = data_transformation(input_data)

        # Check if the result is a DataFrame
        self.assertIsInstance(result, pd.DataFrame)

        # Check if the result matches the expected transformed data
        self.assertTrue(expected_data.equals(result))

    def test_data_loading(self):
        # Test data_loading function
        input_data = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'total_charges': [110.55, 220.85, 330.40]
        })

        # Call the function to save the data
        data_loading(input_data, self.output_file)

        # Read the saved data
        saved_data = pd.read_csv(self.output_file)

        # Check if the saved data is a DataFrame
        self.assertIsInstance(saved_data, pd.DataFrame)

        # Check if the saved data has the same columns as the input data
        self.assertEqual(list(saved_data.columns), list(input_data.columns))

        # Check if the saved data has the same values as the input data
        self.assertTrue(input_data.equals(saved_data))

if __name__ == '__main__':
    unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(TestDataPipeline)
runner = unittest.TextTestRunner()
result = runner.run(suite)