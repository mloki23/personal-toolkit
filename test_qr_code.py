import os
import unittest
from personal_toolkit_qr_code import generate_qr_code, read_qr_code

class TestQRCode(unittest.TestCase):

    def setUp(self):
        self.test_qr_file = "test_qr.png"
        self.test_data = "Hello, QR Code!"

    def tearDown(self):
        if os.path.exists(self.test_qr_file):
            os.remove(self.test_qr_file)

    def test_generate_and_read_qr_code(self):
        generate_qr_code(self.test_data, self.test_qr_file)
        self.assertTrue(os.path.exists(self.test_qr_file))
        decoded_data = read_qr_code(self.test_qr_file)
        self.assertEqual(decoded_data, self.test_data)