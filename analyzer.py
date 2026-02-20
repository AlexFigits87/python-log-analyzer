import re
from collections import Counter

# This regex matches IP, HTTP method, and status code in common log format
LOG_PATTERN = r'(\d+\.\d+\.\d+\.\d+).*?"(GET|POST).*?" (\d{3})'

def parse_log(file_path):
    ip_counter = Counter()
    status_counter = Counter()

    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(LOG_PATTERN, line)
            if match:
                ip, method, status = match.groups()
                ip_counter[ip] += 1
                status_counter[status] += 1

    return ip_counter, status_counter

def main():
    file_path = "sample.log"  # This is the log file we will analyze
    ip_counts, status_counts = parse_log(file_path)

    print("\nTop IP Addresses:")
    for ip, count in ip_counts.most_common(5):
        print(f"{ip}: {count} requests")

    print("\nHTTP Status Codes:")
    for status, count in status_counts.items():
        print(f"{status}: {count} responses")

if __name__ == "__main__":
    main()
