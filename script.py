try:
    with open("log.txt", "r") as file:
        error_count = 0
        info_count = 0
        warning_count = 0
        total_lines = 0

        for line in file:
            total_lines += 1

            if "ERROR" in line:
                error_count += 1
            elif "INFO" in line:
                info_count += 1
            elif "WARNING" in line:
                warning_count += 1

    if total_lines > 0:
    	error_percentage = (error_count / total_lines) * 100
    else:
    	error_percentage = 0

    print("Total lines:", total_lines)
    print("ERROR:", error_count)
    print("INFO:", info_count)
    print("WARNING:", warning_count)
    print("Error %:", round(error_percentage, 2))

except FileNotFoundError:
    print("Log file not found. Please check the file path.")