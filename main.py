import psutil
import argparse
import logging
import time
import os

def check_cpu():
    return psutil.cpu_percent(interval=1)

def check_memory():
    memory = psutil.virtual_memory()
    return memory.percent

def check_disk():
    disk = psutil.disk_usage('/')
    return disk.percent

def check_network():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

def check_temperature():
    temperatures = psutil.sensors_temperatures()
    if temperatures:
        return {sensor: temps[0].current for sensor, temps in temperatures.items()}
    return None

def setup_logging():
    logging.basicConfig(
        filename='shc_report.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def log_summary(results):
    summary = "Summary Report:\n"
    for key, value in results.items():
        summary += f"{key}: {value}\n"
    logging.info(summary)

def display_results(results):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    for key, value in results.items():
        print(f"{key}: {value}")

def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="System Health Checker")
    parser.add_argument('--cpu', action='store_true', help="Check CPU usage")
    parser.add_argument('--memory', action='store_true', help="Check memory usage")
    parser.add_argument('--disk', action='store_true', help="Check disk usage")
    parser.add_argument('--network', action='store_true', help="Check network usage")
    parser.add_argument('--temperature', action='store_true', help="Check system temperature")
    parser.add_argument('--summary', action='store_true', help="Display summary report & log to file")
    parser.add_argument('--interval', type=int, help="Set interval in seconds for continuous monitoring")
    args = parser.parse_args()

    try:
        if args.interval:
            while True:
                results = {}
                if args.cpu:
                    results['CPU Usage'] = f"{check_cpu()}%"
                if args.memory:
                    results['Memory Usage'] = f"{check_memory()}%"
                if args.disk:
                    results['Disk Usage'] = f"{check_disk()}%"
                if args.network:
                    bytes_sent, bytes_recv = check_network()
                    results['Network Sent'] = f"{bytes_sent} bytes"
                    results['Network Received'] = f"{bytes_recv} bytes"
                if args.temperature:
                    temperatures = check_temperature()
                    if temperatures:
                        for sensor, temp in temperatures.items():
                            results[f'Temperature ({sensor})'] = f"{temp}°C"
                    else:
                        results['Temperature'] = "Sensors not available."

                display_results(results)
                log_summary(results)
                time.sleep(args.interval)
        else:
            results = {}
            if args.cpu:
                results['CPU Usage'] = f"{check_cpu()}%"
            if args.memory:
                results['Memory Usage'] = f"{check_memory()}%"
            if args.disk:
                results['Disk Usage'] = f"{check_disk()}%"
            if args.network:
                bytes_sent, bytes_recv = check_network()
                results['Network Sent'] = f"{bytes_sent} bytes"
                results['Network Received'] = f"{bytes_recv} bytes"
            if args.temperature:
                temperatures = check_temperature()
                if temperatures:
                    for sensor, temp in temperatures.items():
                        results[f'Temperature ({sensor})'] = f"{temp}°C"
                else:
                    results['Temperature'] = "Sensors not available."

            if args.summary:
                display_results(results)
                log_summary(results)
            else:
                display_results(results)

            if not any(vars(args).values()):
                parser.print_help()
    except KeyboardInterrupt:
        print("\nReal-time monitoring stopped.")
        logging.info("Real-time monitoring stopped by user.")

if __name__ == "__main__":
    main()
