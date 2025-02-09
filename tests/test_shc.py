import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
import os
from main import check_cpu, check_memory, check_disk, check_network, check_temperature, display_results, get_system_uptime

class TestSystemHealthChecker(unittest.TestCase):

    @patch('main.psutil.cpu_percent')
    def test_check_cpu(self, mock_cpu_percent):
        mock_cpu_percent.return_value = 50
        self.assertEqual(check_cpu(), 50)


    @patch('main.psutil.virtual_memory')
    def test_check_memory(self, mock_virtual_memory):
        mock_virtual_memory.return_value.percent = 75
        self.assertEqual(check_memory(), 75)


    @patch('main.psutil.disk_usage')
    def test_check_disk(self, mock_disk_usage):
        mock_disk_usage.return_value.percent = 80
        self.assertEqual(check_disk(), 80)


    @patch('main.psutil.net_io_counters')
    def test_check_network(self, mock_net_io_counters):
        mock_net_io_counters.return_value.bytes_sent = 1000
        mock_net_io_counters.return_value.bytes_recv = 2000
        self.assertEqual(check_network(), (1000, 2000))


    @patch('main.psutil.sensors_temperatures')
    def test_check_temperature(self, mock_sensors_temperatures):
        mock_sensors_temperatures.return_value = {'sensor1': [MagicMock(current=55)]}
        self.assertEqual(check_temperature(), {'sensor1': 55})
        mock_sensors_temperatures.return_value = {}
        self.assertIsNone(check_temperature())


    @patch('main.os.system')
    @patch('builtins.print')
    def test_display_results(self, mock_print, mock_os_system):
        results = {
            'CPU Usage': '50%',
            'Memory Usage': '75%',
            'Disk Usage': '80%',
            'Network Sent': '1000 bytes',
            'Network Received': '2000 bytes',
            'Temperature (sensor1)': '55°C'
        }
        display_results(results)

        mock_os_system.assert_called_once_with('cls' if os.name == 'nt' else 'clear')
        calls = [
            unittest.mock.call('CPU Usage: 50%'),
            unittest.mock.call('Memory Usage: 75%'),
            unittest.mock.call('Disk Usage: 80%'),
            unittest.mock.call('Network Sent: 1000 bytes'),
            unittest.mock.call('Network Received: 2000 bytes'),
            unittest.mock.call('Temperature (sensor1): 55°C')
        ]
        mock_print.assert_has_calls(calls, any_order=False)


    @patch('main.psutil.boot_time')
    def test_get_system_uptime(self, mock_boot_time):
        # Mock the boot time to a fixed point in the past
        mock_boot_time.return_value = (datetime.now() - timedelta(hours=5)).timestamp()

        # Calculate expected uptime
        expected_uptime = timedelta(hours=5)

        # Get actual uptime from the function
        actual_uptime_str = get_system_uptime()

        # Convert actual uptime string back to a timedelta object for comparison
        actual_uptime_parts = actual_uptime_str.split(':')
        actual_uptime = timedelta(
            hours=int(actual_uptime_parts[0]),
            minutes=int(actual_uptime_parts[1]),
            seconds=int(actual_uptime_parts[2])
        )

        # Check if the actual uptime matches the expected uptime
        self.assertEqual(expected_uptime, actual_uptime, "Uptime does not match the expected value")


if __name__ == '__main__':
    unittest.main()
