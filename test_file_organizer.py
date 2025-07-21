import os
import shutil
import unittest
from personal_toolkit_file_organizer import organize_files

class TestFileOrganizer(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'test_organizer_dir'
        os.makedirs(self.test_dir, exist_ok=True)
        with open(os.path.join(self.test_dir, 'test1.txt'), 'w') as f:
            f.write('test')
        with open(os.path.join(self.test_dir, 'test2.jpg'), 'w') as f:
            f.write('test')

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_organize_files(self):
        organize_files(self.test_dir)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'txt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'jpg')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'txt', 'test1.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'jpg', 'test2.jpg')))