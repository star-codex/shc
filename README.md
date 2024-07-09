# System Health Checker (SHC)

## Purpose

The System Health Checker (SHC) is a Python CLI tool designed to monitor and report on various system resource metrics, including CPU usage, memory usage, disk usage, network usage, and system temperature. This tool provides both snapshot and real-time continuous monitoring capabilities.

I created this to develop my skills with Python, employ test-driven-development, and assemble my own tools from scratch for greater understanding.

## Features

- **CPU Usage**: Monitor the current CPU usage percentage.
- **Memory Usage**: Monitor the current memory usage percentage.
- **Disk Usage**: Monitor the current disk usage percentage.
- **Network Usage**: Monitor the number of bytes sent and received.
- **System Temperature**: Monitor the current temperature of various system sensors.
- **Summary Report**: Display and log a summary report of the monitored metrics.
- **Real-Time Monitoring**: Continuously monitor and report system metrics at a specified interval.

## Usage

### Command-Line Arguments

- `--cpu`: Check CPU usage.
- `--memory`: Check memory usage.
- `--disk`: Check disk usage.
- `--network`: Check network usage.
- `--temperature`: Check system temperature.
- `--summary`: Display a summary report and log it to a file.
- `--interval`: Set the interval (in seconds) for continuous monitoring.

### Example Commands

#### Snapshot Mode

To check CPU and memory usage in snapshot mode:

```
python health_checker.py --cpu --memory
```

#### Summary Report

To check CPU, memory, and disk usage and display a summary report that is sent to a log file:

```
python health_checker.py --cpu --memory --disk --summary
```

#### Real-Time Monitoring

To continuously check CPU and memory usage every 5 seconds:

```
python health_checker.py --cpu --memory --interval 5
```

You can exit the real time monitoring with `CTRL+C`.

## Running Tests

### Prerequisites

Make sure you have `unittest` and `unittest.mock` available in your Python environment.

### Test File

`test_shc.py`  can be executed with the following command:

```
python -m unittest test_health_checker.py
```

## Logging

The SHC tool logs summary reports to `shc_report.log` in the current directory. Each log entry includes a timestamp and the report content. This is added to each time `--summary` is run.

## Dependencies

- `psutil`: Used for retrieving system metrics.
- `argparse`: Used for parsing command-line arguments.
- `unittest`: Used for writing and running tests.
- `unittest.mock`: Used for mocking in tests.

## Installation

Install the required dependencies using `pip`:

```
pip install psutil
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
