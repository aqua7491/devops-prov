import unittest
from unittest.mock import patch
from io import StringIO
from app import call


class TestMyFunction(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_output_content(self, mock_stdout):
        call()
        self.assertEqual(mock_stdout.getvalue(), "Hello, World!\n")


if __name__ == '__main__':
    unittest.main()
