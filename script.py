try:
    log_counts = {
        "error": 0,
        "info": 0,
        "warning": 0
    }

    total_lines = 0

    with open("log.txt", "r") as file:
        for line in file:
            total_lines += 1
            line = line.lower()

            for key in log_counts:
                if key in line:
                    log_counts[key] += 1

    if total_lines == 0:
        print("Log file is empty.")
    else:
        error_percentage = (log_counts["error"] / total_lines) * 100
        print("\n--- Log Summary ---")
        for key, value in log_counts.items():
            print(f"{key.upper()}: {value}")

        print("Total lines:", total_lines)
        print("Error %:", round(error_percentage, 2))

        if log_counts["error"] > 5:
            print("ALERT: High error rate detected!")
    

except FileNotFoundError:
    print("Log file not found.")