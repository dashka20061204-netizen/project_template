import unittest
import os
import pandas as pd
from app.io.input import read_from_file_builtin, read_from_file_pandas

class TestInputFunctions(unittest.TestCase):

    def setUp(self):
        """
        Set up a temporary CSV file with sample data before each test.
        """
        self.test_file = "tests/test_data.csv"
        self.content = "col1,col2\nval1,val2\nval3,val4"
        with open(self.test_file, "w") as f:
            f.write(self.content)

    def tearDown(self):
        """
        Remove the temporary test file after each test execution.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    # --- Tests for read_from_file_builtin ---
    def test_builtin_read_content(self):
        """
        Verify that read_from_file_builtin correctly reads the exact string content of a file.
        """
        result = read_from_file_builtin(self.test_file)
        self.assertEqual(result, self.content)

    def test_builtin_file_not_found(self):
        """
        Ensure that read_from_file_builtin raises FileNotFoundError when the file path is invalid.
        """
        with self.assertRaises(FileNotFoundError):
            read_from_file_builtin("non_existent.txt")

    def test_builtin_return_type(self):
        """
        Confirm that the function returns a string object.
        """
        result = read_from_file_builtin(self.test_file)
        self.assertIsInstance(result, str)

    # --- Tests for read_from_file_pandas ---
    def test_pandas_read_not_empty(self):
        """
        Verify that the pandas-based reader does not return an empty result for a valid file.
        """
        result = read_from_file_pandas(self.test_file)
        self.assertTrue(len(result) > 0)

    def test_pandas_return_type(self):
        """
        Confirm that the data read via pandas is correctly converted to a string format.
        """
        result = read_from_file_pandas(self.test_file)
        self.assertIsInstance(result, str)

    def test_pandas_exception_on_missing_file(self):
        """
        Ensure that an exception is raised when trying to read a missing file using pandas.
        """
        with self.assertRaises(Exception):
            read_from_file_pandas("missing_file.csv")

if __name__ == '__main__':
    unittest.main()