import unittest
from unittest.mock import patch
from personal_toolkit_url_shortener import shorten_url

class TestUrlShortener(unittest.TestCase):

    @patch('pyshorteners.Shortener')
    def test_shorten_url(self, mock_shortener):
        mock_instance = mock_shortener.return_value
        mock_instance.tinyurl.short.return_value = 'http://tinyurl.com/123456'
        short_url = shorten_url('http://example.com')
        self.assertEqual(short_url, 'http://tinyurl.com/123456')