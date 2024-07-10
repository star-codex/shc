import unittest
from unittest.mock import patch, MagicMock
from main import check_cpu, check_memory, check_disk, check_network, check_temperature

# Run tests with "python3 -m unittest test_shc.py"

class TestHealthChecker(unittest.TestCase):

    @patch('main.psutil.cpu_percent')
    def test_check_cpu(self, mock_cpu_percent):
        # Arrange
        mock_cpu_percent.return_value = 50.0

        # Act
        result = check_cpu()

        # Assert
        self.assertEqual(result, 50.0)

    @patch('main.psutil.virtual_memory')
    def test_check_memory(self, mock_virtual_memory):
        # Arrange
        mock_virtual_memory.return_value.percent = 60.0

        # Act
        result = check_memory()

        # Assert
        self.assertEqual(result, 60.0)

    @patch('main.psutil.disk_usage')
    def test_check_disk(self, mock_disk_usage):
        # Arrange
        mock_disk_usage.return_value.percent = 70.0

        # Act
        result = check_disk()

        # Assert
        self.assertEqual(result, 70.0)

    @patch('main.psutil.net_io_counters')
    def test_check_network(self, mock_net_io_counters):
        # Arrange
        mock_net_io_counters.return_value.bytes_sent = 1000
        mock_net_io_counters.return_value.bytes_recv = 2000

        # Act
        bytes_sent, bytes_recv = check_network()

        # Assert
        self.assertEqual(bytes_sent, 1000)
        self.assertEqual(bytes_recv, 2000)

    @patch('main.psutil.sensors_temperatures')
    def test_check_temperature(self, mock_sensors_temperatures):
        # Arrange
        mock_temperatures = {
            'coretemp': [MagicMock(current=50.0)],
            'gpu': [MagicMock(current=70.0)]
        }
        mock_sensors_temperatures.return_value = mock_temperatures

        # Act
        result = check_temperature()

        # Assert
        expected_result = {'coretemp': 50.0, 'gpu': 70.0}
        self.assertEqual(result, expected_result)

    @patch('main.psutil.sensors_temperatures')
    def test_check_temperature_no_sensors(self, mock_sensors_temperatures):
        # Arrange
        mock_sensors_temperatures.return_value = {}

        # Act
        result = check_temperature()

        # Assert
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
