import unittest
import os
from personal_toolkit_log_analyzer import analyze_log_file, count_log_levels

class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        self.test_log_file = "test.log"
        with open(self.test_log_file, "w") as f:
            f.write("INFO: This is an info message.\n")
            f.write("WARNING: This is a warning.\n")
            f.write("ERROR: This is an error.\n")
            f.write("DEBUG: This is a debug message.\n")
            f.write("Another ERROR: Something went wrong.\n")

    def tearDown(self):
        os.remove(self.test_log_file)

    def test_analyze_log_file(self):
        errors = analyze_log_file(self.test_log_file)
        self.assertEqual(len(errors), 2)
        self.assertIn("ERROR: This is an error.", errors[0])
        self.assertIn("Another ERROR: Something went wrong.", errors[1])

    def test_count_log_levels(self):
        counts = count_log_levels(self.test_log_file)
        self.assertEqual(counts['INFO'], 1)
        self.assertEqual(counts['WARNING'], 1)
        self.assertEqual(counts['ERROR'], 2)
        self.assertEqual(counts['DEBUG'], 1)