import unittest
from personal_toolkit_password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password_length(self):
        self.assertEqual(len(generate_password(length=16)), 16)

    def test_generate_password_no_uppercase(self):
        password = generate_password(use_uppercase=False)
        self.assertFalse(any(c.isupper() for c in password))

    def test_generate_password_no_lowercase(self):
        password = generate_password(use_lowercase=False)
        self.assertFalse(any(c.islower() for c in password))

    def test_generate_password_no_digits(self):
        password = generate_password(use_digits=False)
        self.assertFalse(any(c.isdigit() for c in password))

    def test_generate_password_no_symbols(self):
        password = generate_password(use_symbols=False)
        self.assertTrue(all(c.isalnum() for c in password))