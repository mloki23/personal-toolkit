import unittest
from unittest.mock import patch
from personal_toolkit_system_info_checker import get_system_info

class TestSystemInfoChecker(unittest.TestCase):

    @patch('platform.system', return_value='Linux')
    @patch('platform.node', return_value='test-node')
    @patch('platform.release', return_value='5.4.0-100-generic')
    @patch('platform.version', return_value='#113-Ubuntu SMP Thu Feb 11 18:51:53 UTC 2021')
    @patch('platform.machine', return_value='x86_64')
    @patch('platform.processor', return_value='x86_64')
    @patch('psutil.cpu_percent', return_value=50.0)
    @patch('psutil.virtual_memory')
    @patch('psutil.disk_usage')
    def test_get_system_info(self, mock_disk_usage, mock_virtual_memory, mock_cpu_percent, mock_processor, mock_machine, mock_version, mock_release, mock_node, mock_system):
        mock_virtual_memory.return_value.percent = 60.0
        mock_disk_usage.return_value.percent = 70.0
        info = get_system_info()
        self.assertEqual(info['system'], 'Linux')
        self.assertEqual(info['node_name'], 'test-node')
        self.assertEqual(info['release'], '5.4.0-100-generic')
        self.assertEqual(info['version'], '#113-Ubuntu SMP Thu Feb 11 18:51:53 UTC 2021')
        self.assertEqual(info['machine'], 'x86_64')
        self.assertEqual(info['processor'], 'x86_64')
        self.assertEqual(info['cpu_usage'], 50.0)
        self.assertEqual(info['memory_usage'], 60.0)
        self.assertEqual(info['disk_usage'], 70.0)