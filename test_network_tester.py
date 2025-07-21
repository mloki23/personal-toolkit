import unittest
from unittest.mock import patch
from personal_toolkit_network_tester import run_speed_test

class TestNetworkTester(unittest.TestCase):

    @patch('speedtest.Speedtest')
    def test_run_speed_test(self, MockSpeedtest):
        mock_instance = MockSpeedtest.return_value
        mock_instance.download.return_value = 100_000_000  # 100 Mbps
        mock_instance.upload.return_value = 50_000_000    # 50 Mbps

        speeds = run_speed_test()
        self.assertAlmostEqual(speeds['download_speed'], 100.0)
        self.assertAlmostEqual(speeds['upload_speed'], 50.0)