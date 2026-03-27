with open("log.txt", "r") as file:
    error_count = 0
    info_count = 0
    total_lines = 0

    for line in file:
        total_lines += 1

        if "ERROR" in line:
            error_count += 1
        elif "INFO" in line:
            info_count += 1

print("Total lines:", total_lines)
print("ERROR:", error_count)
print("INFO:", info_count)