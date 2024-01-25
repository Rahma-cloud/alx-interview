#!/usr/bin/python3
"""
Log parse 
"""
import sys
from collections import defaultdict


def print_stats(total_size, status_code_count):
    """ This function prints out stats """
    print("File size: {}".format(total_size))
    for code in sorted(status_code_count):
        print("{}: {}".format(code, status_code_count[code]))


def parse_line(line):
    """ This function seperates the line """
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (ValueError, IndexError):
        return None, None, None


def main():
    """ This finction stores the 2 functions above's output """
    total_size = 0
    status_code_count = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            ip_address, status_code, file_size = parse_line(line)

            if ip_address is not None:
                total_size += file_size
                status_code_count[status_code] += 1
                line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_code_count)

    except KeyboardInterrupt:
        pass  # Handle Ctrl+C

    finally:
        print_stats(total_size, status_code_count)


if __name__ == "__main__":
    main()
