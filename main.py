import psutil
import argparse

def check_cpu():
    return psutil.cpu_percent(interval=1)

def check_memory():
    memory = psutil.virtual_memory()
    return memory.percent

def check_disk():
    disk = psutil.disk_usage('/')
    return disk.percent

def main():
    parser = argparse.ArgumentParser(description="System Health Checker")
    parser.add_argument('--cpu', action='store_true', help="Check CPU usage")
    parser.add_argument('--memory', action='store_true', help="Check memory usage")
    parser.add_argument('--disk', action='store_true', help="Check disk usage")
    parser.add_argument('--summary', action='store_true', help="Display summary report")
    args = parser.parse_args()

    results = {}
    if args.cpu:
        results['CPU Usage'] = f"{check_cpu()}%"
    if args.memory:
        results['Memory Usage'] = f"{check_memory()}%"
    if args.disk:
        results['Disk Usage'] = f"{check_disk()}%"

    if args.summary:
        print("Summary Report:")
        for key, value in results.items():
            print(f"{key}: {value}")
    else:
        for key, value in results.items():
            print(f"{key}: {value}")

    if not any(vars(args).values()):
        parser.print_help()

if __name__ == "__main__":
    main()
