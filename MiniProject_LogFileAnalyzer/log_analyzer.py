import re

# Dictionary to store the count of each log level
log_count = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0,
    "DEBUG": 0
}

total_entries = 0
invalid_entries = 0

# Regular expression to identify log entries
pattern = r"^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (INFO|WARNING|ERROR|DEBUG) (.+)$"

try:
    # Open the log file in read mode
    with open("sample.log", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            # Check the line using Regex
            match = re.search(pattern, line)

            if match:
                level = match.group(3)
                log_count[level] += 1
                total_entries += 1
            else:
                invalid_entries += 1

    # Display the analysis results
    print("\n===== LOG FILE ANALYZER =====")
    print("Total valid entries:", total_entries)
    print("Invalid entries:", invalid_entries)

    print("\nLog Level Summary:")
    for level, count in log_count.items():
        print(level, ":", count)

    # Display error messages
    print("\nError Messages:")

    with open("sample.log", "r", encoding="utf-8") as file:
        for line in file:
            match = re.search(pattern, line.strip())

            if match and match.group(3) == "ERROR":
                print("-", match.group(4))

    print("\nAnalysis completed successfully.")

except FileNotFoundError:
    print("Error: sample.log file was not found.")
    print("Please keep the log file in the same folder.")
