import os
from behave import given, when, then
from unittest.mock import patch
from io import StringIO
import sys
import vwdir

@given('a directory named "{directory}" containing "{file1}", "{file2}", and "{subdir}"')
def step_given_directory(context, directory, file1, file2, subdir):
    context.directory = directory
    context.files = [file1, file2, subdir]

@when('I run the vwdir script with the directory "{directory}"')
def step_when_run_script(context, directory):
    with patch('os.listdir') as mock_listdir:
        mock_listdir.return_value = context.files
        with patch('argparse.ArgumentParser.parse_args') as mock_parse_args:
            mock_parse_args.return_value = argparse.Namespace(directory=directory)
            # Capture the output
            context.held_stdout = sys.stdout
            sys.stdout = StringIO()
            vwdir.print_directory(directory)
            context.output = sys.stdout.getvalue().strip()
            sys.stdout = context.held_stdout

@then('I should see "{file1}", "{file2}", and "{subdir}" in the output')
def step_then_see_output(context, file1, file2, subdir):
    expected_output = f"{file1}\n{file2}\n{subdir}"
    assert context.output == expected_output, f"Expected output: {expected_output}, but got: {context.output}"
