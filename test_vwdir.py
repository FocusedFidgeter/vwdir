import argparse
import unittest
from unittest.mock import patch, MagicMock
import sys
from io import StringIO
import vwdir

class TestVWDir(unittest.TestCase):
    def setUp(self):
        # Backup the original stdout
        self.held_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        # Restore the original stdout
        sys.stdout = self.held_stdout

    @patch('os.listdir')
    @patch('argparse.ArgumentParser.parse_args')
    def test_print_directory(self, mock_parse_args, mock_listdir):
        # Mock the arguments
        mock_parse_args.return_value = argparse.Namespace(directory='test_directory')

        # Mock the listdir response
        mock_listdir.return_value = ['file1.txt', 'file2.txt', 'subdir1']

        # Call the function
        vwdir.print_directory('test_directory')

        # Check the output
        output = sys.stdout.getvalue().strip()
        expected_output = 'file1.txt\nfile2.txt\nsubdir1'
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
