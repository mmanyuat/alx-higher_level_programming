#!/usr/bin/python3
""" something imported here"""
import sys


def print_stats(total_size, status_codes):
    """Prints the total file size and number of lines by status code."""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))


def parse_line(line):
    """Parses a line and extracts the file size and status code."""
    parts = line.split()
    if len(parts) >= 9:
        status_code = parts[-2]
        file_size = parts[-1]
        return int(file_size), status_code
    return None, None


def main():
    total_size = 0
    status_codes = {
            str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            file_size, status_code = parse_line(line)
            if file_size is not None and status_code in status_codes:
                total_size += file_size
                status_codes[status_code] += 1
                line_count += 1
            if line_count == 10:
                print_stats(total_size, status_codes)
                line_count = 0
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
