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
    args = parser.parse_args()

    if args.cpu:
        print(f"CPU Usage: {check_cpu()}%")
    if args.memory:
        print(f"Memory Usage: {check_memory()}%")
    if args.disk:
        print(f"Disk Usage: {check_disk()}%")
    if not any(vars(args).values()):
        parser.print_help()

if __name__ == "__main__":
    main()
