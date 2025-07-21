import unittest
import os
import shutil
from personal_toolkit_duplicate_finder import find_duplicate_files, calculate_file_hash

class TestDuplicateFinder(unittest.TestCase):

    def setUp(self):
        self.test_dir = "test_duplicate_dir"
        os.makedirs(self.test_dir, exist_ok=True)

        # Create some test files
        with open(os.path.join(self.test_dir, "file1.txt"), "w") as f:
            f.write("content1")
        with open(os.path.join(self.test_dir, "file2.txt"), "w") as f:
            f.write("content1") # Duplicate of file1.txt
        with open(os.path.join(self.test_dir, "file3.txt"), "w") as f:
            f.write("content2")
        with open(os.path.join(self.test_dir, "file4.txt"), "w") as f:
            f.write("content2") # Duplicate of file3.txt
        
        # Create a subdirectory and a file in it
        os.makedirs(os.path.join(self.test_dir, "subdir"), exist_ok=True)
        with open(os.path.join(self.test_dir, "subdir", "file5.txt"), "w") as f:
            f.write("content1") # Duplicate of file1.txt and file2.txt

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_calculate_file_hash(self):
        file_path = os.path.join(self.test_dir, "file1.txt")
        expected_hash = "e7d9071bce22571875256544199646871315739c527f430f7241917691074104"
        self.assertEqual(calculate_file_hash(file_path), expected_hash)

    def test_find_duplicate_files(self):
        duplicates = find_duplicate_files(self.test_dir)
        self.assertEqual(len(duplicates), 2) # Two sets of duplicates

        content1_hash = calculate_file_hash(os.path.join(self.test_dir, "file1.txt"))
        self.assertIn(content1_hash, duplicates)
        self.assertEqual(len(duplicates[content1_hash]), 3)
        self.assertIn(os.path.join(self.test_dir, "file1.txt"), duplicates[content1_hash])
        self.assertIn(os.path.join(self.test_dir, "file2.txt"), duplicates[content1_hash])
        self.assertIn(os.path.join(self.test_dir, "subdir", "file5.txt"), duplicates[content1_hash])

        content2_hash = calculate_file_hash(os.path.join(self.test_dir, "file3.txt"))
        self.assertIn(content2_hash, duplicates)
        self.assertEqual(len(duplicates[content2_hash]), 2)
        self.assertIn(os.path.join(self.test_dir, "file3.txt"), duplicates[content2_hash])
        self.assertIn(os.path.join(self.test_dir, "file4.txt"), duplicates[content2_hash])

if __name__ == '__main__':
    unittest.main()