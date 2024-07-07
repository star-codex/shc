import psutil
import argparse
import logging
from datetime import datetime

def check_cpu():
    return psutil.cpu_percent(interval=1)

def check_memory():
    memory = psutil.virtual_memory()
    return memory.percent

def check_disk():
    disk = psutil.disk_usage('/')
    return disk.percent

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

def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="System Health Checker")
    parser.add_argument('--cpu', action='store_true', help="Check CPU usage")
    parser.add_argument('--memory', action='store_true', help="Check memory usage")
    parser.add_argument('--disk', action='store_true', help="Check disk usage")
    parser.add_argument('--summary', action='store_true', help="Display summary report")
    args = parser.parse_args()

    results = {}
    if args.cpu:
        cpu_usage = check_cpu()
        results['CPU Usage'] = f"{cpu_usage}%"
        if not args.summary:
            print(f"CPU Usage: {cpu_usage}%")
    if args.memory:
        memory_usage = check_memory()
        results['Memory Usage'] = f"{memory_usage}%"
        if not args.summary:
            print(f"Memory Usage: {memory_usage}%")
    if args.disk:
        disk_usage = check_disk()
        results['Disk Usage'] = f"{disk_usage}%"
        if not args.summary:
            print(f"Disk Usage: {disk_usage}%")

    if args.summary:
        print("Summary Report:")
        for key, value in results.items():
            print(f"{key}: {value}")
        log_summary(results)

    if not any(vars(args).values()):
        parser.print_help()

if __name__ == "__main__":
    main()
