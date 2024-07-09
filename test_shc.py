import unittest
from unittest.mock import patch
from main import check_cpu

class TestHealthChecker(unittest.TestCase):

    @patch('main.psutil.cpu_percent')
    def test_check_cpu(self, mock_cpu_percent):
        # Arrange
        mock_cpu_percent.return_value = 50.0

        # Act
        result = check_cpu()

        # Assert
        self.assertEqual(result, 50.0)

if __name__ == '__main__':
    unittest.main()
