Feature: View directory structure
  As a user
  I want to view the structure of a directory
  So that I can see the files and subdirectories it contains

  Scenario: View directory structure
    Given a directory named "./test_directory" containing "file1.txt", "file2.txt", and "subdir1"
    When I run the vwdir script with the directory "test_directory"
    Then I should see "file1.txt", "file2.txt", and "subdir1" in the output
