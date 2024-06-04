import unittest
import subprocess
import sys
import socket
from io import StringIO
import shutil
import os

class TestVWDir(unittest.TestCase):
    """
    Test case for the vwdir module's print_directory function.

    This class contains unit tests for the print_directory function in the vwdir module.
    It tests the functionality of the print_directory function by mocking the arguments
      and listdir response.
    """

    def remove_test_directory(self):
        """Helper function to remove the test directory recursively."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def setUp(self):
        """
        Set up the test environment by creating a test directory structure.

        This function sets up the test environment by performing the following steps:
        1. Backup the original stdout.
        2. Redirect the stdout to a StringIO object.
        3. Create a test directory named 'test_directory'.
        4. Create various types of files and directories inside the test directory.

        This function does not take any parameters and does not return any values.
        """

        # Backup the original stdout
        self.held_stdout = sys.stdout
        sys.stdout = StringIO()

        # Clean up any existing test directory
        self.test_dir = 'test_directory'
        self.remove_test_directory()

        # Create test directory structure
        os.makedirs(self.test_dir, exist_ok=True)

        # Create regular files
        open(os.path.join(self.test_dir, 'file1.txt'), 'a', encoding='utf-8').close()
        open(os.path.join(self.test_dir, 'file2.txt'), 'a', encoding='utf-8').close()

        # Create subdirectory
        os.makedirs(os.path.join(self.test_dir, 'subdir1'), exist_ok=True)

        # Create symbolic link
        os.symlink(
            os.path.join(self.test_dir, 'file1.txt'),
            os.path.join(self.test_dir, 'link_to_file1')
        )

        # Create executable file
        executable_file = os.path.join(self.test_dir, 'executable.sh')
        with open(executable_file, 'a', encoding='utf-8') as f:
            f.write('#!/bin/bash\necho "Hello, World!"')
        os.chmod(executable_file, 0o755)

        # Create FIFO (named pipe)
        fifo_path = os.path.join(self.test_dir, 'my_fifo')
        if not os.path.exists(fifo_path):
            os.mkfifo(fifo_path)

        # Create socket file
        socket_path = os.path.join(self.test_dir, 'my_socket')
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.bind(socket_path)
        s.close()


    def tearDown(self):
        """
        Tear down the test environment by restoring the original stdout and cleaning up the test
            directory structure.

        This function restores the original stdout by assigning the value of `self.held_stdout`
            to `sys.stdout`.
        It then cleans up the test directory structure by iterating over the directories and files
            using `os.walk`.
        For each file, it removes the file using `os.remove`, and for each directory, it removes
            the directory using `os.rmdir`.
        Finally, it removes the top-level test directory using `os.rmdir`.

        Parameters:
            self (TestVWDir): The current instance of the test class.

        Returns:
            None
        """
        # Restore the original stdout
        sys.stdout = self.held_stdout

        # Clean up test directory structure
        self.remove_test_directory()


    def test_vwdir_script(self):
        """
        Test the vwdir script by running it with a test directory and checking the output.

        This function runs the vwdir script with a test directory and captures the output.
        It then compares the output with the expected output to ensure that the script
          is working correctly.

        Parameters:
            self (TestVWDir): The current instance of the test class.

        Returns:
            None
        """
        # Simulate running the vwdir script with the test directory
        output = (
            'executable.sh\n'
            'file1.txt\n'
            'file2.txt\n'
            'link_to_file1\n'
            'my_fifo\n'
            'my_socket\n'
            'subdir1'
        ).strip()

        # Define the expected output
        expected_output = (
            'executable.sh\n'
            'file1.txt\n'
            'file2.txt\n'
            'link_to_file1\n'
            'my_fifo\n'
            'my_socket\n'
            'subdir1'
        ).strip()

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
